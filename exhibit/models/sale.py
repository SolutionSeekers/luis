# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import timedelta

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    assembly_date    = fields.Datetime(string = "Fecha de montaje", required = True)
    disassembly_date = fields.Datetime(string = "Fecha de desmontaje", required = True)
    
    @api.one
    def action_confirm(self):
        for sale in self:
            super(SaleOrder, sale).action_confirm()
            sale.env['calendar.event'].create({
                'name': 'Evento {}'.format(sale.partner_id.name),
                'start': sale.assembly_date,
                'stop': sale.disassembly_date,
                'sale_id': sale.id,
            })