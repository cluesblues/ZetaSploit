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

import yaml
import json

from core.badges import badges
from core.storage import storage

class config:
    def __init__(self):
        self.badges = badges()
        self.storage = storage()
        
        self.base_path = '/opt/zsf/'
        self.config_path = self.base_path + 'config/'
        
        self.db_config_file = self.config_path + 'db_config.yml'
        self.path_config_file = self.config_path + 'path_config.yml'
        self.core_config_file = self.config_path + 'core_config.yml'
        
        self.db_config = self.storage.get("db_config")
        self.path_config = self.storage.get("path_config")
        self.core_config = self.storage.get("core_config")

    def get_config_file(self, content):
        return yaml.safe_load(content)
    
    def set_storage_variables(self):
        storage_variables = json.load(open(self.path_config['base_paths']['storage_path']))
        for variable in storage_variables.keys():
            if storage_variables[variable] == "True":
                variable_value = True
            elif storage_variables[variable] == "False":
                variable_value = False
            else:
                variable_value = storage_variables[variable]
            self.storage.set(variable, variable_value)
        
    def set_storage_variable(self, variable, value):
        storage_variables = json.load(open(self.path_config['base_paths']['storage_path']))
        old_storage = storage_variables
        new_storage = open(self.path_config['base_paths']['storage_path'], 'w')
        
        old_storage[variable] = str(value)
        new_storage.write(str(old_storage).replace("'", '"'))
        new_storage.close()
        
    def configure(self):
        db_config = self.get_config_file(open(self.db_config_file))
        path_config = self.get_config_file(open(self.path_config_file))
        core_config = self.get_config_file(open(self.core_config_file))

        self.db_config = db_config
        self.path_config = path_config
        self.core_config = core_config
        
        self.storage.set("db_config", self.db_config)
        self.storage.set("path_config", self.path_config)
        self.storage.set("core_config", self.core_config)
        
        self.set_storage_variables()
