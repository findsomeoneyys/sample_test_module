# -*- coding: utf-8 -*-
__import__('os').environ['TZ'] = 'UTC'

import odoo

if __name__ == "__main__":
    odoo.cli.main()