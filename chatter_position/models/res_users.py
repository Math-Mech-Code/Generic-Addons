from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    chatter_position = fields.Selection(
        [("normal", "Normal"), ("sided", "Sided")],
        default="normal",
    )

    @property
    def SELF_READABLE_FIELDS(self):
        """Extend Readable fields"""
        return super().SELF_READABLE_FIELDS + ["chatter_position"]

    @property
    def SELF_WRITEABLE_FIELDS(self):
        """Extend Writable fields"""
        return super().SELF_WRITEABLE_FIELDS + ["chatter_position"]
