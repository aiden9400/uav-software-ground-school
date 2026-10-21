
# -*- coding: utf-8 -*-
import re
import sys

from vcs2l.commands.custom import git_main

if __name__ == '__main__':
	sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
	sys.exit(git_main())
