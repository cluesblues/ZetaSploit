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

import os

from core.badges import badges
from core.storage import local_storage
from core.modules import modules

class ZetaSploitCommand:
    def __init__(self):
        self.badges = badges()
        self.local_storage = local_storage()
        self.modules = modules()

        self.details = {
            'Category': "module",
            'Name': "set",
            'Description': "Set an option value.",
            'Usage': "set <option> <value>",
            'ArgsCount': 2,
            'NeedsArgs': True,
            'Args': list()
        }

    def run(self, argc, argv):
        option = argv[0].upper()
        value = argv[1]
        
        if self.modules.check_current_module():
            current_module = self.modules.get_current_module_object()
            if option in current_module.options.keys():
                self.badges.output_information(option + " ==> " + value)
                self.local_storage.set_module_option("current_module", self.local_storage.get("current_module_number"), option, value)
            else:
                self.badges.output_error("Unrecognized option!")
        else:
            self.badges.output_warning("No module selected.")
