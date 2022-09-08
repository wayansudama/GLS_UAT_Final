from odoo import _, api, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    project_code = fields.Char('Project Code')

    def button_confirm(self):
        res = super(PurchaseOrder,self).button_confirm()
        self.order_line.write({'po_confirm_date': fields.Date.context_today(self) })
        return res        

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    project_code = fields.Char('Project Code',compute="_get_project_codepr")
    item_id = fields.Many2one('item.item')
    po_confirm_date = fields.Date('Po Confirm Date')    

    def _get_project_codepr(self):
        code = ''
        for i in self:  
            get_code = i.purchase_request_lines.mapped('project_code')
            if get_code:
                for gc in get_code:
                    code += '('+str(gc)+')' 
            else:
                code = '' 
            i.project_code = code  
