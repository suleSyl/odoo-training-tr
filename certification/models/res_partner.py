from odoo.exceptions import ValidationError

from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'


    certification_ids = fields.One2many(comodel_name='certification', inverse_name='owner_id')
    is_certification_body = fields.Boolean(string='It is an entity', default='True',
                                           help='Check this box if the contact is a certification entity')

    @api.constrains('entity_id')
    def _check_entity_id(self):
        if self.entity_id and self.entity_id.is_certification_body == False:
            raise ValidationError('It is not a certification entity' )
