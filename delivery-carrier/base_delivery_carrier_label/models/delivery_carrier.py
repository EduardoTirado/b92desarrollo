# Copyright 2012 Akretion <http://www.akretion.com>.
# Copyright 2013-2016 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(oldname='carrier_type')
    code = fields.Char(
        help="Delivery Method Code (according to carrier)",
    )
    description = fields.Text()
    available_option_ids = fields.One2many(
        comodel_name='delivery.carrier.option',
        inverse_name='carrier_id',
        string='Option',
    )

    @api.multi
    def default_options(self):
        """ Returns default and available options for a carrier """
        options = self.env['delivery.carrier.option'].browse()
        for available_option in self.available_option_ids:
            if (available_option.mandatory or available_option.by_default):
                options |= available_option
        return options
