from django.urls import path
from .views import IndexView, SobreView, ContatoView, DesenvolvimentoView, ManutencaoView, MarketingView, ConsultoriaView


urlpatterns = [
    path('', IndexView.as_view(), name= 'inicio'),
    path('sobre-nos/', SobreView.as_view(), name= 'sobre'),
    path('contato/', ContatoView.as_view(), name= 'contato'),
    path('solucoes/desenvolvimento/', DesenvolvimentoView.as_view(), name= 'desenvolvimento'),
    path('solucoes/manutencao/', ManutencaoView.as_view(), name= 'manutencao'),
    path('solucoes/marketing/', MarketingView.as_view(), name= 'marketing'),
    path('solucoes/consultoria/', ConsultoriaView.as_view(), name= 'consultoria'),

]
