#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def main():
    pipe = subprocess.Popen(['/usr/bin/odoo', '--db_host', 'postgres', '-d', 'postgres', '--db_user', 'odoo', '--db_password', 'odoo', '-i', 'base',
 '--test-enable', '--stop-after-init'], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    with open('stdout.log', 'wb') as stdout:
        for line in iter(pipe.stdout.readline, b''):
            stdout.write(line)
            print(line.strip().decode(
                'UTF-8', errors='backslashreplace'
            ))
    returncode = pipe.wait()
    # Find errors, except from failed mails
    # errors = has_test_errors(
    #     "stdout.log", 'odoo', '12.0', False)
    if returncode != 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    exit(main())
    