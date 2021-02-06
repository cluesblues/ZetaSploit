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
from core.storage import storage
from core.config import config

class ZetaSploitCommand:
    def __init__(self):
        self.badges = badges()
        self.storage = storage()
        self.config = config()
        
        self.history = self.config.path_config['base_paths']['history_path']

        self.details = {
            'Category': "developer",
            'Name': "history",
            'Description': "Manage ZetaSploit history.",
            'Usage': "history [-l|on|off]",
            'ArgsCount': 1,
            'NeedsArgs': True,
            'Args': list()
        }

    def run(self):
        option = self.details['Args'][0]
        if option == "on":
            self.storage.set("history", True)
            self.badges.output_information("ZetaSploit history: on")
        elif option == "off":
            self.storage.set("history", False)
            self.badges.output_information("ZetaSploit history: off")
        elif option == "-c":
            if os.path.exists(self.history):
                os.remove(self.history)
        elif option == "-l":
            using_history = self.storage.get("history")
            if using_history:
                self.badges.output_information("ZetaSploit history:")
                history_file = open(self.history, 'r')
                history = [x.strip() for x in history_file.readlines()]
                history_file.close()
                for line in history:
                    self.badges.output_empty("    * " + line)
            else:
                self.badges.output_warning("No history detected.")
        else:
            self.badges.output_usage(self.details['Usage'])
