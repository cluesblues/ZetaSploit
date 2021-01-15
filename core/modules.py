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

class modules:
    def __init__(self):
        self.io = io()
        self.badges = badges()
        self.storage = storage()
        
    def check_exist(self, category, platform, name):
        modules = self.storage.get("modules")
        if category in modules.keys():
            if platform in modules[category].keys():
                module = self.get_name(module)
                if module in modules[category][platform].keys():
                    return True
        return False

    def check_style(self, name):
        if len(name.split('/')) >= 4:
            return True
        return False
       
    def get_category(self, name):
        return name.split('/')[0]

    def get_platform(self, name):
        return name.split('/')[1]
    
    def get_name(self, name):
        return os.path.join(*(name.split(os.path.sep)[2:]))

    def get_full_name(self, category, platform, name):
        return category + '/' + platform + '/' + name
