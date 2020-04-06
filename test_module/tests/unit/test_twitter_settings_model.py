# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase


class TwitterSettingsModel(TransactionCase):
    def test_settings_model_exists(self):
        self.assertTrue('twitter.settings' in self.env)
