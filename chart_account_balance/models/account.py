# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp

class AccountAccount(models.Model):
    _inherit = "account.account"
    

#    mapping = {
#            'balance': "COALESCE(SUM(l.debit),0) - COALESCE(SUM(l.credit), 0) as balance",
#            'debit': "COALESCE(SUM(l.debit), 0) as debit",
#            'credit': "COALESCE(SUM(l.credit), 0) as credit",
#            }
    
    @api.one
    def compute_values(self):
        for account in self:
            balance = 0.0
            credit = 0.0
            debit = 0.0
            search_domain = [('account_id','in',[self.id])]
            for val in self.env['account.move.line'].search(search_domain):
                if val.move_id.state == 'posted':
                    balance += val.debit - val.credit
                    credit += val.credit
                    debit += val.debit
            account.balance = balance
            account.credit = credit
            account.debit = debit
    
    balance = fields.Float(compute="compute_values", digits=dp.get_precision('Account'), string='Saldo')
    credit = fields.Float(compute="compute_values",digits=dp.get_precision('Account'), string='Credito')
    debit = fields.Float(compute="compute_values",digits=dp.get_precision('Account'), string='Debito')
