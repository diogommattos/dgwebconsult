from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"

class ContatoView(TemplateView):
    template_name = "paginas/contato.html"

class DesenvolvimentoView(TemplateView):
    template_name = "paginas/desenvolvimento.html"

class ManutencaoView(TemplateView):
    template_name = "paginas/manutencao.html"

class MarketingView(TemplateView):
    template_name = "paginas/marketing.html"

class ConsultoriaView(TemplateView):
    template_name = "paginas/consultoria.html"
    
