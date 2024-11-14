from django.views.generic import TemplateView

class BVAISView(TemplateView):
    template_name = "bv_ais_plugin/index.html"