# -*- encoding: utf-8 -*-

from osv import osv
from osv import fields


class res_partner(osv.osv):
    _inherit = 'res.partner'

    _columns = {
                'province': fields.related('address', 'province', type='char', string='Prov'),
                'region': fields.related('address', 'region', type='char', string='Regione'),
                }

res_partner()