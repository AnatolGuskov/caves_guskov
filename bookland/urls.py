from django.urls import path
from caveguskov import views
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url

from . import views


app_name = 'bookland'


urlpatterns = [
    path('', views.index, name='index'),
    path('seites/<pk>', views.seites, name='seites'),
    path('zoom/<pk>', views.zoom_seite, name='zoom'),

    path('register/<art>', views.register_art, name='register-art'),
    path('register/<pk>/<art>', views.register_seites, name='register-seites'),

]