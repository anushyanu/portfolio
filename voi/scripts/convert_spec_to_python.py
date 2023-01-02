#!/usr/bin/python

################################################################################
#
#  File:
#        convert_spec_to_python.py
#
#  Project:
#        
#
#  Module:
#        
#
#  Author:
#        Anushya Balakrishnan
#
#  Description:
#        This is used to convert a spec file .txt to a skeleton file .py
#
#  Copyright notice:
#        Copyright (C) 2023 Anushya Balakrishnan
#
#  Licence:
#
#        This file is free code: you can redistribute it and/or modify it under
#        the terms of the GNU Lesser General Public License version 2.1 as
#        published by the Free Software Foundation.
#
#        This package is distributed in the hope that it will be useful, but
#        WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#        Lesser General Public License for more details.
#
#
import re

input_file = open("../requirements/voi_spec.txt", "r")
output_file = open("voi_spec.py", "w")
output_file.write("#!/usr/bin/python")
for line in input_file:
    match_defines = re.match(r'\s*([a-zA-Z_a-zA-Z]+) (.*)', line)
    match_comments = re.match(r'\s*[/\*][\s*\*](.*)', line)
 	
    if match_defines:
        newline1= "\ndef %s():\n \t # %s" % (match_defines.group(1), match_defines.group(2))
        output_file.write(newline1)

    elif match_comments:
        newline2= "\n# %s" % (match_comments.group(1))
        output_file.write(newline2)

    else:
        output_file.write(line)



