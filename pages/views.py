from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class SobreView(TemplateView):
    template_name = "sobre.html"

class ContatoView(TemplateView):
    template_name = "contato.html"

class DesenvolvimentoView(TemplateView):
    template_name = "desenvolvimento.html"

class ManutencaoView(TemplateView):
    template_name = "manutencao.html"

class MarketingView(TemplateView):
    template_name = "marketing.html"

class ConsultoriaView(TemplateView):
    template_name = "consultoria.html"
    
