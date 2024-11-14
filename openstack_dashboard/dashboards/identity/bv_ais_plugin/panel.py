import horizon
class BVAISPanel(horizon.Dashboard):
    name = _("BVAIS")
    slug = "bv_ais"

horizon.register(BVAISPanel)