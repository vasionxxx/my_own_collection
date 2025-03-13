#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: create_file

short_description: Creates a file with specified content

version_added: "1.0.0"

description: This module creates a file at a specified path with given content.

options:
    path:
        description: The path where the file should be created.
        required: true
        type: str
    content:
        description: The content to write to the file.
        required: true
        type: str

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a file with content
  my_namespace.my_collection.create_file:
    path: /tmp/testfile.txt
    content: "Hello, World!"
'''

RETURN = r'''
path:
    description: The path of the file created.
    type: str
    returned: always
    sample: '/tmp/testfile.txt'
content:
    description: The content written to the file.
    type: str
    returned: always
    sample: 'Hello, World!'
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    path = module.params['path']
    content = module.params['content']

    if os.path.exists(path):
        with open(path, 'r') as file:
            existing_content = file.read()
        if existing_content == content:
            result['changed'] = False
        else:
            with open(path, 'w') as file:
                file.write(content)
            result['changed'] = True
    else:
        with open(path, 'w') as file:
            file.write(content)
        result['changed'] = True

    result['path'] = path
    result['content'] = content

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()