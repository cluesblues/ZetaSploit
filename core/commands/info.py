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
from core.modules import modules
from core.storage import storage

class ZetaSploitCommand:
    def __init__(self):
        self.badges = badges()
        self.modules = modules()
        self.storage = storage()
        
        self.details = {
            'Category': "module",
            'Name': "info",
            'Description': "Show module information.",
            'Usage': "info [<module>]",
            'ArgsCount': 0,
            'NeedsArgs': True,
            'Args': list()
        }

    def format_module_information(self, current_module):
        authors = ""
        for author in current_module['Authors']:
            authors += author + ", "
        authors = authors[:-2]

        dependencies = ""
        for dependence in current_module['Dependencies']:
            dependencies += dependence + ", "
        dependencies = dependencies[:-2]

        comments = ""
        for line in current_module['Comments']:
            comments += line + "\n" + (" " * 13)
        comments = comments[:-14]

        self.badges.output_information("Current module information:")
        self.badges.output_empty("")

        if current_module['Name']:
            self.badges.output_empty("         Name: " + current_module['Name'])
        if authors:
            self.badges.output_empty("      Authors: " + authors)
        if current_module['Description']:
            self.badges.output_empty("  Description: " + current_module['Description'])
        if dependencies:
            self.badges.output_emtpy(" Dependencies: " + dependencies)
        if comments:
            self.badges.output_empty("     Comments: ")
            self.badges.output_empty("             ")
        if current_module['Risk']:
            self.badges.output_empty("         Risk: " + current_module['Risk'])

        self.badges.output_empty("")
        
    def get_module_information(self, module):
        if self.modules.check_exist(module):
            category = self.modules.get_category(module)
            platform = self.modules.get_platform(module)
            name = self.modules.get_name(module)
            
            module = self.modules.get_module_object(category, platform, name)
            self.format_module_information(module)
        else:
            self.badges.output_error("Invalid module!")
        
    def run(self):
        if self.modules.check_current_module():
            self.format_module_information(self.modules.get_current_module_object().details)
        else:
            if len(self.details['Args']) > 0:
                print("|" + self.details['Args'][0] + "|" + str(bool(self.details['Args'][0])))
                self.get_module_information(self.details['Args'][0])
            else:
                self.badges.output_usage(self.details['Usage'])
