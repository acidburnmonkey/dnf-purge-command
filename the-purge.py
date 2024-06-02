'''
plugins go into /lib/python3.12/site-packages/dnf-plugins
or check your current version : python --version
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

    # Arguments for dnf (package)
    @staticmethod
    def set_argparser(parser):
        parser.add_argument('packages', nargs='+',help=_('packages to check'))
        parser.add_argument('--nuke', dest='nuke', action='store_true' ,help=_('Nuke option do not use , this will try to manually remove binaries and servises, Only takes 1 argument'))

    def run(self):

        """Execute the util action here."""
        
        user = os.getenv("SUDO_USER")
        if user is None:
            print("This program needs 'sudo'")
            exit()

        pacages = list(self.opts.packages)      
        home = os.path.join('/home', os.getlogin())

        show_user =[]
        string_pack = []
        exclude = set([])

        string_pack.extend(pacages)
        for index in pacages:
            string_pack.append(index.capitalize())
            string_pack.append(index.upper())
            string_pack.append('.' + index)
            string_pack.append('.' + index.upper())
            string_pack.append('.' + index.capitalize())

        #--nuke switch here
        if self.opts.nuke == True:
            binary_locations=['/usr/local/bin','/usr/bin','/bin']
            for binaries in binary_locations:
                check = os.listdir(binaries)
                if pacages[0] in check:
                    show_user.append(os.path.join(binaries,pacages[0]))
            if os.path.exists(f'/etc/systemd/system/{pacages[0]}.service'):
                show_user.append(f'/etc/systemd/system/{pacages[0]}.service')

        #call DNF for uninstal 
        string_of_programs = ' '.join(pacages)
        subprocess.run(f'dnf remove {string_of_programs}', shell=True)

        # walk for directories
        for root , directories , files in os.walk(home):
            for directory in directories:
                #packages loop
                for pack in string_pack:
                    if pack == directory :
                        show_user.append(os.path.join(root,directory))
                        exclude.add(directory)

        # walk for loose files
        for root, dirs, files in os.walk(home, topdown=True):
            [dirs.remove(d) for d in list(dirs) if d in exclude]
            for file in files:
                for pack in string_pack:
                    if pack == file:
                        show_user.append(os.path.join(root,file))

        # time to see what deletes
        if len(show_user) < 1:
            print("No remaining files found for purging")
            sys.exit()
        print('The following directories and files will be deleted')
        print('🮶  ',*show_user ,sep='\n' )
        print('🮵  ')

        while True:
            ask = str(input("Delete these files y/n :"))
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
                ask = str(input("Delete these files y/n :"))




