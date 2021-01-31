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

class storage:
    def get_all(self):
        return globals()
    
    def add(self, name):
        globals()[name] = None

    def set(self, name, value):
        globals()[name] = value

    def update(self, name, value):
        try:
            globals()[name].update(value)
        except Exception:
            pass

    def add_array(self, name, value):
        try:
            globals()[name].append(value)
        except Exception:
            pass

    def get_array(self, name, value):
        try:
            return globals()[name][value]
        except Exception:
            return None

    def set_array(self, name, value1, value2):
        try:
            globals()[name][value1] = value2
        except Exception:
            pass

    def delete_element(self, name, value):
        try:
            del globals()[name][value]
        except Exception:
            pass

    def delete(self, name):
        try:
            del globals()[name]
        except Exception:
            pass

    def get(self, name):
        try:
            return globals()[name]
        except Exception:
            return None

    def set_module_option(self, name, number, option, value):
        try:
            globals()[name][number].options[option]['Value'] = value
        except Exception:
            pass
