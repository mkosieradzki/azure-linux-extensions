#!/usr/bin/env python
#
# DSC Extension For Linux
#
# Copyright 2014 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import env
import dsc
import os
from Utils.WAAgentUtil import waagent
from MockUtil import MockUtil

waagent.LoggerInit('/tmp/test.log','/dev/null')

class TestRegister(unittest.TestCase):
    def test_register_without_registration_info(self):
        print "Register test case with invalid Registration url and Registration key"
        dsc.distro_category = dsc.get_distro_category()
        dsc.hutil = MockUtil(self)
        dsc.install_dsc_packages()
        dsc.start_omiservice()
        exit_code, output = dsc.register_automation('','','','','','')
        self.assertEqual(exit_code, 51)
		
    def test_register_invalid_configuration_mode(self):
        print "Register test case with invalid configuration mode"
        dsc.distro_category = dsc.get_distro_category()
        dsc.hutil = MockUtil(self)
        dsc.install_dsc_packages()
        dsc.start_omiservice()
        exit_code, output = dsc.register_automation('somekey','http://dummy','','','','some')	
        self.assertEqual(exit_code, 51)
	
    def test_register(self):
        print "Register test case with valid parameters"
        dsc.distro_category = dsc.get_distro_category()
        dsc.hutil = MockUtil(self)
        dsc.install_dsc_packages()
        dsc.start_omiservice()
        exit_code, output = dsc.register_automation('somekey','http://dummy','test.localhost.mof','15','30','applyandmonitor')
        self.assertEqual(exit_code, 0)
        
if __name__ == '__main__':
    unittest.main()
