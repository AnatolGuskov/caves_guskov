from django.shortcuts import render

from django.views import generic
from django.db.models import Q

from . models import Bookseites, Register, Bookseites_eng, Text_site




# ================== INDEX  ===========================
def index(request):
    tytle = Text_site.objects.get(theme = "index_tytle")
    text_tytle = tytle.ukr
    annotation = Text_site.objects.get(theme="index_annotation")
    text_annotation = annotation.ukr

    return render(
        request, 'index.html',
        context = {
            'name': "Anatoly",
            'text_tytle': text_tytle,
            'text_annotation': text_annotation,
        }
           )
# ================== SITES  ===========================
def seites(request):
    seites_menu = Bookseites.objects.all()

    return render(
        request, 'seites.html',
        context = {
              'seites_menu': seites_menu,
                  }
           )

# ================== END seites  ===========================

# ================== SITES_LIST  ===========================
def seites_list(request, pk):
    seites_list = Bookseites.objects.all().filter(id__gte = pk)[:10]
    seites_menu = Bookseites.objects.all()
    max_seit = len(seites_list)
    seit_max = seites_list[max_seit - 1].id
    if max_seit == 1:
        text = "ОСТАННЯ СТОРІНКА виборки"
    else:
        text = "ДАЛІ - наступні сторінки ... "
    if max_seit == 72:
        text = "ОСТАННЯ СТОРІНКА книги"

    return render(
        request, 'seites_list.html',
        context = {
            'seites_list': seites_list,
            'seites_menu': seites_menu,
            'seit_max': seit_max,
            'text': text,
        }
           )
# ================== END seites_list  ===========================

# ================== ZOOM_SEITE  ===========================
def zoom_seite(request, pk, quelle):

    zoom_seite = Bookseites.objects.get(pk = pk)
    quelle_zoom = quelle

    return render(
        request, 'zoom_seite.html',
        context = {
            'zoom_seite': zoom_seite,
            'quelle_zoom': quelle_zoom

        }
           )

# ================== END zoom_seite  ===========================

# ================== REGISTER ART ===========================
def register_art(request, art):

    if art == "1":
        art = "Географічні назви"
    if art == "2":
        art = "Населені пункти"
    if art == "3":
        art = "Туристичні об'єкти"
    reg_name_list = Register.objects.all().filter(reg_art = art)
    num_name = len(reg_name_list)

    art_object = set(())
    for object in reg_name_list:
        art_object.add (object.reg_s_name)

    art_object_num = [[],]
    for item in art_object:
        l = []
        l.append(0)
        l.append(item)
        l.append(len(Register.objects.all().filter(reg_s_name=item)))

        art_object_num.append(l)

    art_object_num.sort()


    return render(
        request, 'register_art.html',
        context = {
            'art': art,
            'reg_name_list': reg_name_list,
            'num_name': num_name,

            'art_object': art_object,
            'art_object_num': art_object_num,


        }
           )
# ================== END register_art ===========================

# ================== REGISTER OBJECT ===========================
def register_object(request, obj):

    object_name = obj  # обраний тип об'єкту
    reg_name_list = Register.objects.all().filter(reg_s_name = obj)  # список об'ектів обраного типу
    num_name = len(reg_name_list)   # кількість об'ектів обраного типу

    art = reg_name_list [0].reg_art    # вид показчика (географія, міста, туроб'єкти)
    reg_name_list_all = Register.objects.all().filter(reg_art=art)   # список найменувань виду показчика
    num_name_art = len(reg_name_list_all)  # кількість найменувань виду показчика

# формування списку типів об'єктів показчика з вичисленням кількості об'єктів у списку
    art_object = set(())
    for object in reg_name_list_all:
        art_object.add (object.reg_s_name)

    art_object_num = [[],]
    for item in art_object:
        l = []
        l.append(0)
        l.append(item)
        l.append(len(Register.objects.all().filter(reg_s_name=item)))
        art_object_num.append(l)
    art_object_num.sort()

    return render(
        request, 'register_object.html',
        context = {
            'object_name': object_name,
            'reg_name_list': reg_name_list,
            'num_name': num_name,
            'art': art,
            'num_name_art': num_name_art,
            'art_object': art_object,
            'art_object_num': art_object_num,

        }
           )
# ================== END register_object ===========================



# ================== REGISTER SEITES ===========================
def register_seites(request, pk, art):

    reg_seites = Register.objects.get(pk = pk) # сторінки з вказаним об'єктом
    reg_name = reg_seites.reg_f_name           # найменування об'єкту
    reg_num =  reg_seites.reg_numbers          # нумера сторінок з вказаним об'єктом
    reg_art =  reg_seites.reg_art              # вид показчика об'єкта
    reg_pk = pk                                # код об'єкта
    reg_object = reg_seites.reg_s_name         # тип об'єкта

    reg_object_list = Register.objects.all().filter(reg_s_name = reg_object) # список об'єктів заданого типу
    num_name = len(reg_object_list)
    reg_name_list = Register.objects.all().filter(reg_art=reg_art) # список всіх об'єктів виду показчика

    return render(
        request, 'register_seites.html',
        context = {
            'reg_seites': reg_seites,
            'object_name': reg_object,
            'reg_object_list': reg_object_list,
            'num_name': num_name,
            'reg_name_list': reg_name_list,
            'reg_art': reg_art, 'reg_name': reg_name,
            'reg_num': reg_num,
            'reg_pk': reg_pk,

        }
           )
# ================== END register_seites ===========================
