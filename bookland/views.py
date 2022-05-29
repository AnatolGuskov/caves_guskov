from django.shortcuts import render

from django.views import generic
from django.db.models import Q

from . models import Bookseites, Register




# ================== INDEX  ===========================
def index(request):

    return render(
        request, 'index.html',
        context = {
            'name': "Anatoly",
        }
           )

# ================== SITES  ===========================
def seites(request, pk):
    seites_list = Bookseites.objects.all().filter(id__gte = pk)
    seites_menu = Bookseites.objects.all()



    return render(
        request, 'seites.html',
        context = {
            'seites_list': seites_list,
            'seites_menu': seites_menu,
        }
           )

# ================== REGISTER ART ===========================
def register_art(request, art):

    if art == "1":
        reg_art = "Географічні назви"
    if art == "2":
        reg_art = "Населені пункти"
    if art == "3":
        reg_art = "Туристичні об'єкти"
    reg_name_list = Register.objects.all().filter(reg_art = reg_art)

    seites_menu = Bookseites.objects.all()
    # seites_list = []


    return render(
        request, 'register_art.html',
        context = {
            'reg_name_list': reg_name_list,
            'art': art, 'reg_art': reg_art,

        }
           )
# ================== END register_art ===========================

# ================== REGISTER SEITES ===========================
def register_seites(request, pk, art):

    reg_seites = Register.objects.get(pk = pk)
    reg_name = reg_seites.reg_f_name +", "+ reg_seites.reg_s_name
    reg_num =  reg_seites.reg_numbers
    reg_art =  reg_seites.reg_art

    reg_name_list = Register.objects.all().filter(reg_art=art)

    return render(
        request, 'register_seites.html',
        context = {
            'reg_seites': reg_seites,
            'reg_name_list': reg_name_list,
            'reg_art': reg_art, 'reg_name': reg_name,
            'reg_num': reg_num,

        }
           )
# ================== END register_seites ===========================
