from odoo import models, fields, api


class PracticeModel(models.Model):
    _name = 'practice.test'
    _description = 'First practice model'

    name = fields.Char(string='Name')
    info = fields.Char(string='Information')
    index = fields.Integer(string='Index')

    # parent_path = fields.Char(index=True)
    # depth = fields.Integer(compute="_compute_depth")
    # root_categ = fields.Many2one(_name, compute='_compute_root_categ')
    # display_name = fields.Char(compute='_compute_display_name', recursive=True,
    #                            inverse='_inverse_display_name')
    # dummy = fields.Char(store=False)
    # discussions = fields.Many2many('test_new_api.discussion', 'test_new_api_discussion_category',
    #                                'category', 'discussion')
    #
    # _sql_constraints = [
    #     ('positive_color', 'CHECK(color >= 0)', 'The color code must be positive !')
    # ]
