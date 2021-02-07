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

from core.badges import badges
from core.config import config

from core.storage import local_storage
from core.storage import global_storage

class ZetaSploitCommand:
    def __init__(self):
        self.badges = badges()
        self.config = config()
        
        self.storage_path = self.config.path_config['base_paths']['storage_path']
        
        self.local_storage = local_storage()
        self.global_storage = global_storage(self.storage_path)

        self.details = {
            'Category': "developer",
            'Name': "storage",
            'Description': "Manage storage variables.",
            'Usage': "storage [global|local] [-l|-v <name>|-s <name> <value>|-d <name>]",
            'ArgsCount': 2,
            'NeedsArgs': True,
            'Args': list()
        }

    def run(self, argc, argv):
        type_of_storage = argv[0]
        if type_of_storage == "global":
            choice = argv[1]
            if choice == "-l":
                self.badges.output_information("Global storage variables:")
                for variable in self.global_storage.get_all():
                    if not str.startswith(variable, '__') and not str.endswith(variable, '__'):
                        self.badges.output_empty("    * " + variable)
            elif choice == "-v":
                if argc < 3:
                    self.badges.output_usage(self.details['Usage'])
                else:
                    if argv[2] in self.global_storage.get_all():
                        self.badges.output_information(argv[2] + " = " + str(
                            self.global_storage.get(argv[2])))
            elif choice == "-s":
                if argc < 4:
                    self.badges.output_usage(self.details['Usage'])
                else:
                    self.global_storage.set(argv[2], argv[3])
            elif choice == "-d":
                if argc < 3:
                    self.badges.output_usage(self.details['Usage'])
                else:
                    if argv[2] in self.global_storage.get_all():
                        self.global_storage.delete(argv[2])
                    else:
                        self.badges.output_error("Invalid storage variable name!")
            else:
                self.badges.output_usage(self.details['Usage'])
        elif type_of_storage == "local":
            choice = argv[1]
            if choice == "-l":
                self.badges.output_information("Local storage variables:")
                for variable in self.local_storage.get_all():
                    if not str.startswith(variable, '__') and not str.endswith(variable, '__'):
                        self.badges.output_empty("    * " + variable)
            elif choice == "-v":
                if argc < 3:
                    self.badges.output_usage(self.details['Usage'])
                else:
                    if argv[2] in self.local_storage.get_all():
                        self.badges.output_information(argv[2] + " = " + str(
                            self.local_storage.get(argv[2])))
                    else:
                        self.badges.output_error("Invalid storage variable name!")
            elif choice == "-s":
                if argc < 4:
                    self.badges.output_usage(self.details['Usage'])
                else:
                    self.local_storage.set(argv[2], argv[3])
            elif choice == "-d":
                if argc < 3:
                    self.badges.output_usage(self.details['Usage'])
                else:
                    if argv[2] in self.local_storage.get_all():
                        self.local_storage.delete(argv[2])
                    else:
                        self.badges.output_error("Invalid storage variable name!")
            else:
                self.badges.output_usage(self.details['Usage'])
        else:
            self.badges.output_usage(self.details['Usage'])
