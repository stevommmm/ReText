#!/usr/bin/env python3

# ReText webpages generator
# Copyright 2011-2012 Dmitry Shachnev

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import os.path
import sys
from ReText.webpages import *

def main(argv):
	if len(argv) > 1:
		if argv[1] == "updateall":
			wpUpdateAll()
		elif argv[1] == "update" and len(argv) > 2:
			wpUpdate(argv[2:])
		elif argv[1] == "init":
			wpInit()
		elif argv[1] == "usestyle" and len(argv) == 3:
			wpUseStyle(argv[2])
		else:
			printUsage()
	else:
		printUsage()

def printUsage():
	print(app_name + ", version " + app_version)
	print("Usage: wpgen COMMAND <ARGUMENTS>")
	print("")
	print("Available commands:")
	print("  init - create new web library")
	print("  updateall - generate html pages from all files")
	print("  update [filename1] [filename2] ... - generate html pages from given files")
	print("  usestyle [stylename] - use the given style (example: Default, Simple)")

if __name__ == '__main__':
	main(sys.argv)
