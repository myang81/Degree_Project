#!A:\Group15\VeterinaryHospital\Backend\virtualenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyScss==1.3.7','console_scripts','pyscss'
__requires__ = 'pyScss==1.3.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyScss==1.3.7', 'console_scripts', 'pyscss')()
    )
