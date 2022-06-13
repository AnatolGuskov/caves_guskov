from django.urls import path
from caveguskov import views
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url

from . import views, views_eng


app_name = 'bookland'


urlpatterns = [
    path('', views.index, name='index'),
    path('eng/', views_eng.index_eng, name='index_eng'),

    path('list/seites/<topic>', views.seites, name='seites'),
    path('eng/list/seites/<topic>', views_eng.seites_eng, name='seites_eng'),

    path('seites/<pk>', views.seites_list, name='seites-list'),
    path('eng/seites/<pk>', views_eng.seites_list_eng, name='seites-list_eng'),

    path('zoom/<pk>/<quelle>', views.zoom_seite, name='zoom'),
    path('eng/zoom/<pk>/<quelle>', views_eng.zoom_seite_eng, name='zoom_eng'),

    path('register/<art>', views.register_art, name='register-art'),
    path('eng/register/<art>', views_eng.register_art_eng, name='register-art_eng'),

    path('register/object/<obj>/<language>', views.register_object, name='register-object'),
    path('eng/register/object/<obj>/<language>', views_eng.register_object_eng, name='register-object_eng'),

    path('register/<pk>/<art>', views.register_seites, name='register-seites'),
    path('eng/register/<pk>/<art>', views_eng.register_seites_eng, name='register-seites_eng'),

]