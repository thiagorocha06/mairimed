from django.conf.urls import url
from .views import ChatterBotView, ChatterBotAppView


urlpatterns = [
    url(
        r'chatterbot/',
        ChatterBotView.as_view(),
        name='chatterbot',
    ),
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
]
