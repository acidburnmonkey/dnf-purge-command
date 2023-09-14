'''
plugins go into /lib/python3.11/site-packages/dnf-plugins
https://github.com/acidburnmonkey/dnf-purge-command
'''

from dnfpluginscore import _, logger
from dnf.cli.option_parser import OptionParser
import dnf
import os
import shutil
import sys
import subprocess
import dnf.cli

# Registering the Command
@dnf.plugin.register_command
class Purge(dnf.cli.Command):

    aliases = ['purge']
    summary = _('removes dangling files in home directory')

    def __init__(self, cli):
        super(Purge, self).__init__(cli)
        self.opts = None
        self.parser = None

    # Aruments for dnf (package)
    @staticmethod
    def set_argparser(parser):
        parser.add_argument('packages', nargs='+',help=_('packages to check'))

    def run(self):
        """Execute the util action here."""
        pacages = list(self.opts.packages)      
        user = os.getenv("SUDO_USER")
        if user is None:
            print ("This program needs 'sudo'")
            exit()

        home = os.path.join('/home', os.getlogin())

        show_user =[]
        string_pack = []
        exclude = set([])

        inxex1 = pacages[0]

        string_pack.append(inxex1)
        string_pack.append(inxex1.capitalize())
        string_pack.append(inxex1.upper())
        string_pack.append('.' + inxex1)
        string_pack.append('.' + inxex1.upper())
        string_pack.append('.' + inxex1.capitalize())

        #call DNF for unistall 
        subprocess.run(f'dnf remove {inxex1}', shell=True)

        # walk for directories
        for root , directoryes , files in os.walk(home):
            for directory in directoryes:
                #packages loop
                for pack in string_pack:
                    if pack == directory :
                        show_user.append(os.path.join(root,directory))
                        exclude.add(directory)

        # walk for lose files
        for root, dirs, files in os.walk(home, topdown=True):
            [dirs.remove(d) for d in list(dirs) if d in exclude]
            for file in files:
                for pack in string_pack:
                    if pack == file:
                        show_user.append(os.path.join(root,file))

        if len(show_user) < 1:
            print("No remaining files found for purging")
            sys.exit()
        print(f"The following directories and files will be deleted \n {show_user}")


        while True:
            ask = str(input("Delete thse files y/n :"))
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
            else:
                ask = str(input("Delete thse files y/n :"))




