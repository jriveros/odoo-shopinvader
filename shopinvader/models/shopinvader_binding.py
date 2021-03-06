# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ShopinvaderBinding(models.AbstractModel):
    _name = 'shopinvader.binding'

    backend_id = fields.Many2one(
        'shopinvader.backend',
        string='Backend',
        required=True)
    external_id = fields.Char()
    sync_date = fields.Datetime(
        string='Last synchronization date'
    )
