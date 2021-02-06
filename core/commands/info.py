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

class ZetaSploitCommand:
    def __init__(self):
        self.badges = badges()
        self.modules = modules()
        
        self.details = {
            'Category': "module",
            'Name': "info",
            'Description': "Show current module information.",
            'Usage': "info",
            'ArgsCount': 0,
            'NeedsArgs': False,
            'Args': list()
        }

    def run(self):
        if self.modules.check_current_module():
            current_module = self.modules.get_current_module_object()
            
            authors = ""
            for author in current_module.details['Authors']:
                authors += author + ", "
            authors = authors[:-2]
            
            comments = ""
            for line in current_module.details['Comments']:
                comments += line + "\n" + (" " * 13)
            comments = comments[:-14]
            
            self.badges.output_information("Current module information:")
            self.badges.output_empty("")
            self.badges.output_empty("        Name: " + current_module.details['Name'])
            self.badges.output_empty("     Authors: " + authors)
            self.badges.output_empty(" Description: " + current_module.details['Description'])
            self.badges.output_empty("    Comments: ")
            self.badges.output_empty("             ")
            self.badges.output_empty("        Risk: " + current_module.details['Risk'])
            self.badges.output_empty("")
        else:
            self.badges.output_warning("No module selected.")
