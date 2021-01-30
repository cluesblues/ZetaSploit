#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2021 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from core.io import io
from core.badges import badges
from core.storage import storage
from core.formatter import formatter

class ZetaSploitCommand:
    def __init__(self):
        self.io = io()
        self.badges = badges()
        self.storage = storage()
        self.formatter = formatter()
        
        self.details = {
            'Category': "database",
            'Name': "modules_db",
            'Description': "Manage modules databases.",
            'Usage': "modules_db [-l|-r <name>|-a <name> <path>]",
            'ArgsCount': 1,
            'NeedsArgs': True,
            'Args': list()
        }

    def run(self):
        args = self.details['Args']
        option = args[0]
        
        if option == "-l":
            dbs_data = list()
            number = 0
            headers = ("Number", "Name", "Path")
            dbs = self.storage.get("connected_databases")
            for name in dbs.keys():
                if dbs[name]['type'] == "module":
                    dbs_data.append((number, name, dbs[name]['path']))
                    number += 1
            self.io.output("")
            self.formatter.format_table("Connected Databases", headers, *dbs_data)
            self.io.output("")
        elif option == '-r':
            if len(args) < 2:
                self.badges.output_usage(self.details['Usage'])
            else:
                self.storage.delete_element("connected_databases", args[1])
        else:
            self.badges.output_usage(self.details['Usage'])
