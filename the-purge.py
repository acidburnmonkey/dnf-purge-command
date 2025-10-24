#!/bin/python3

'''
https://github.com/acidburnmonkey/dnf-purge-command
'''

import stat
import time
import threading
import os
import shutil
import sys
import subprocess
import argparse
from functools import lru_cache

# the spinner thread
flag = threading.Event()


def spinner():
    symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    i = 0
    while not flag.is_set():
        i = (i + 1) % len(symbols)
        print('\r\033[K%s Searching...' % symbols[i], flush=True, end='\r')
        time.sleep(0.1)
    # Clear the spinner line after the thread finishes
    print(' ' * 20, end='\r')


t1 = threading.Thread(target=spinner)

def is_executable(path):
    try:
        file_info = os.stat(path)
        # Check if it's a regular file
        is_regular_file = stat.S_ISREG(file_info.st_mode)

        has_exec_permission = bool(
            file_info.st_mode & (
                stat.S_IXUSR |
                stat.S_IXGRP |
                stat.S_IXOTH
            )
        )
        return is_regular_file and has_exec_permission

    except FileNotFoundError:
        return False

@lru_cache(maxsize=1)
def list_path_cmds():
    seen = set()
    cmds = []

    for d in filter(None, os.environ.get("PATH","").split(os.pathsep)):
        try:
            for name in os.listdir(d):
                if name in seen:
                    continue
                full = os.path.join(d, name)
                if is_executable(full):
                    seen.add(name)
                    cmds.append(name)
        except FileNotFoundError:
            pass
    return sorted(cmds)

def program_candidates() -> list[str]:
    return sorted(set(list_path_cmds()))

def _complete_programs(prefix: str) -> None:
    # print one candidate per line
    for c in program_candidates():
        if c.startswith(prefix):
            print(c)


parser = argparse.ArgumentParser(
    prog='Purge command',
    description='Uninstalls programs via dnf , then searches and removes files and directories created by set programs in your Home directory',
    epilog='End',
)


def set_argparser(parser):
    parser.add_argument('packages', nargs='+', help=('packages to check'))
    parser.add_argument(
        '--nuke',
        dest='nuke',
        action='store_true',
        help=('Nuke option do not use , this will try to manually remove binaries and services, Only takes 1 argument'),
    )
    # parser.add_argument('-v', '--verbose')


# set_argparser(parser)
# args = parser.parse_args()


def main():
    """Execute the util action here."""

    user = os.getenv("SUDO_USER")
    if user is None:
        print("This program needs 'sudo'")
        exit()

    # Packsges arsgs here
    packages = args.packages

    home = os.path.join('/home', os.getlogin())
    show_user = []
    string_pack = []
    exclude = set([])

    string_pack.extend(packages)
    for index in packages:
        string_pack.append(index.capitalize())
        string_pack.append(index.upper())
        string_pack.append('.' + index)
        string_pack.append('.' + index.upper())
        string_pack.append('.' + index.capitalize())

    # --nuke switch here
    if args.nuke:
        binary_locations = ['/usr/local/bin', '/usr/bin', '/bin']
        for binaries in binary_locations:
            check = os.listdir(binaries)
            if packages[0] in check:
                show_user.append(os.path.join(binaries, packages[0]))
        if os.path.exists(f'/etc/systemd/system/{packages[0]}.service'):
            show_user.append(f'/etc/systemd/system/{packages[0]}.service')

    # call DNF for uninstal
    string_of_programs = ' '.join(packages)
    subprocess.run(f'dnf remove {string_of_programs}', shell=True)

    t1.start()
    # walk for directories
    for root, directories, files in os.walk(home):
        for directory in directories:
            # packages loop
            for pack in string_pack:
                if pack == directory:
                    show_user.append(os.path.join(root, directory))
                    exclude.add(directory)

    # walk for loose files
    for root, dirs, files in os.walk(home, topdown=True):
        [dirs.remove(d) for d in list(dirs) if d in exclude]
        for file in files:
            for pack in string_pack:
                if pack == file:
                    show_user.append(os.path.join(root, file))

    # stop spinner
    flag.set()
    t1.join()
    print('\n', 60 * '=')
    # time to see what deletes
    if len(show_user) < 1:
        print("No remaining files found for purging")
        sys.exit()

    print_list(show_user)

    while True:
        ask = input("Delete these files [y/n] [e] to select & exclude:")
        if ask.lower() == 'y':
            for root in show_user:
                try:
                    shutil.rmtree(root)
                except NotADirectoryError:
                    os.remove(root)
                except OSError as e:
                    print("Error: %s - %s." % (e.filename, e.strerror))
            print("Files purged")
            break
        elif ask.lower() == 'n':
            sys.exit()
        elif ask.lower() == 'e':
            try:
                ask = input("Enter the indexes to exclude separated by comas: ")
                remove = set(int(x.strip()) for x in ask.split(','))
                show_user = [item for n, item in enumerate(show_user) if n not in remove]
                print_list(show_user)

            except ValueError:
                print("Invalid selection use indexes separated by comas")

        else:
            print("Delete [y/n] [e] to select & exclude:")


def print_list(show_user):
    print('The following directories and files will be deleted \n🮶 ')
    for n, item in enumerate(show_user):
        print(f'({n}): {item}')
    print('🮵  ')


if __name__ == '__main__':


    # Early helper hooks for auto completion
    if len(sys.argv) >= 2 and sys.argv[1] == "__complete-programs":
        prefix = sys.argv[2] if len(sys.argv) > 2 else ""
        _complete_programs(prefix)
        sys.exit(0)

    if len(sys.argv) >= 3 and sys.argv[1] == "--generate-shell-completion":
        sys.exit(0)

    set_argparser(parser)
    args = parser.parse_args()

    main()
