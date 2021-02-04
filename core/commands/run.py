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

from core.io import io
from core.badges import badges
from core.storage import storage
from core.modules import modules

from core.jobs import jobs

class ZetaSploitCommand:
    def __init__(self):
        self.io = io()
        self.badges = badges()
        self.storage = storage()
        self.modules = modules()
        
        self.jobs = jobs()

        self.details = {
            'Category': "module",
            'Name': "run",
            'Description': "Run current module.",
            'Usage': "run [-j]",
            'ArgsCount': 0,
            'NeedsArgs': True,
            'Args': list()
        }

    def entry_to_module(self, current_module):
        if len(self.details['Args']) > 0:
            if self.details['Args'][0] == "-j":
                self.badges.output_process("Running module as background job...")
                job_id = self.jobs.create_job(current_module.details['Name'], current_module.details['Name'], current_module.run)
                self.badges.output_information("Module started as a background job " + job_id + ".")
                return
        current_module.run()
        
    def run(self):
        if self.modules.check_current_module():
            current_module = self.modules.get_current_module_object()
            count = 0
            if hasattr(current_module, "options"):
                for option in current_module.options.keys():
                    current_option = current_module.options[option]
                    if not current_option['Value'] and current_option['Value'] != 0 and current_option['Required']:
                        count += 1
                if count > 0:
                    self.badges.output_error("Missed some required options!")
                else:
                    try:
                        self.entry_to_module(current_module)
                    except (KeyboardInterrupt, EOFError):
                        self.io.output("")
            else:
                try:
                    self.entry_to_module(current_module)
                except (KeyboardInterrupt, EOFError):
                    self.io.output("")
        else:
            self.badges.output_warning("No module selected.")
