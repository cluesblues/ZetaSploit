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

import platform

from core.io import io
from core.badges import badges

class ZetaSploitCommand:
    def __init__(self):
        self.io = io()
        self.badges = badges()
        
        self.prompt = self.badges.BOLD + ">>> " + self.badges.END
        
        self.details = {
            'Category': "developer",
            'Name': "pyshell",
            'Description': "Open Python shell.",
            'Usage': "pyshell",
            'ArgsCount': 0,
            'NeedsArgs': False,
            'Args': list()
        }

    def run(self):
        self.badges.output_information(f"Python {platform.python_version()} console")
        self.io.output("")
        while True:
            output = self.badges.input_empty(self.prompt)
            try:
                exec(output.strip())
            except SystemExit:
                return
            except (EOFError, KeyboardInterrupt):
                return
            except Exception as e:
                self.badges.output_error(str(e))
