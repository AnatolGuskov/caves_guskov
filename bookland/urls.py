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
    path('seites/', views.seites, name='seites'),
    path('seites/<pk>', views.seites_list, name='seites-list'),
    path('zoom/<pk>/<quelle>', views.zoom_seite, name='zoom'),

    path('register/<art>', views.register_art, name='register-art'),
    path('register/object/<obj>', views.register_object, name='register-object'),
    path('register/<pk>/<art>', views.register_seites, name='register-seites'),

]