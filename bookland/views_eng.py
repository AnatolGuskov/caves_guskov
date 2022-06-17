from django.shortcuts import render

from django.views import generic
from django.db.models import Q

from . models import Register_eng, Bookseites, Text_site, Object_typ




# ================== INDEX ENG  ===========================
def index_eng(request,):
    tytle = Text_site.objects.get(theme = "index_tytle")
    text_tytle = tytle.eng
    annotation = Text_site.objects.get(theme="index_annotation")
    text_annotation = annotation.eng

    return render(
        request, 'index.html',
        context = {
            'template': "base_generic_eng.html",
            'language': "ENG",
            'eng': " english", 'ukr': "ukrainish",

            'text_tytle': text_tytle,
            'text_annotation': text_annotation,
        }
           )
# ================== SITES_ENG  ===========================
def seites_eng(request, topic):
    if topic == "1":
        seites = Bookseites.objects.all()
    else:
        seites = Bookseites.objects.all().filter(Q(name_eng1=topic) | Q(name_seites1=topic))
        topic_menu = [[]]
        for item in seites:
            t = []
            t.append(0)
            t.append(item.name_eng1)
            t.append(item.name_eng)
            topic_menu.append(t)
        topic = topic_menu[1][2]

    seites_list = [[]]
    for item in seites:
        m = []
        m.append(0)
        m.append(item.name_eng1)  # 1
        m.append(item.name_eng)  # 2
        m.append(item.seites)  # 3
        m.append(item.id)  # 4
        m.append(item.name_step)  # 5
        seites_list.append(m)
    seites_list = seites_list[1:]

    section = Bookseites.objects.all().filter(name_step="1")

    section_list = [[]]
    for item in section:
        s = []
        s.append(0)
        s.append(item.name_eng1)
        section_list.append(s)

    return render(
        request, 'seites.html',
        context = {
            'template': "base_generic_eng.html",
            'url_topic': "bookland:seites_eng",
            'url_seiteslist': "bookland:seites-list_eng",
            'language': "ENG",
            'eng': "english", 'ukr': "ukrainish",

            'seittopic': "Browse Book Pages",
            'bookcontents': "Contents of the Book",
            'seites_list': seites_list,
            'section_list': section_list,
            'topic': topic,
            'name': 1,
            'illustration': "Dawn at Cape Kule Burun (Mangup locality)"

                  }
           )

# ================== END seites_eng  ===========================

# ================== SITES_LIST_ENG  ===========================
def seites_list_eng(request, topic, pk):
    if topic == "1":
        seites = Bookseites.objects.all().filter(id__gte=pk)[:10]
        menu = Bookseites.objects.all()
    else:
        seites = Bookseites.objects.all().filter(
            Q(name_eng1=topic, id__gte=pk) | Q(name_seites1=topic, id__gte=pk))[:10]
        menu = Bookseites.objects.all().filter(
            Q(name_eng1=topic) | Q(name_seites1=topic))

    seites_list = [[]]
    for item in seites:
        m = []
        m.append(0)
        m.append(item.name_eng1)  # 1
        m.append(item.name_eng)  # 2
        m.append(item.seites)  # 3
        m.append(item.id)  # 4
        m.append(item.image_seites)  # 5
        seites_list.append(m)
    seites_list = seites_list[1:]

    seites_menu = [[]]
    for item in menu:
        m = []
        m.append(0)
        m.append(item.name_eng1)  # 1
        m.append(item.name_eng)  # 2
        m.append(item.seites)  # 3
        m.append(item.id)  # 4
        m.append(item.name_step)  # 5
        seites_menu.append(m)
    seites_menu = seites_menu[1:]



    max_seit = len(seites)
    seit_max = seites[max_seit - 1].id
    if max_seit == 1:
        text = "LAST PAGE of the page sample"
    else:
        text = "NEXT - the following pages ..."


    return render(
        request, 'seites_list.html',
        context = {
            'template': "base_generic_eng.html",
            'url_seiteslist': "bookland:seites-list_eng",
            'url_zoom': "bookland:zoom_eng",
            'language': "ENG",
            'eng': "english", 'ukr': "ukrainish",

            'seites_list': seites_list,
            'seites_menu': seites_menu,
            'seit_max': seit_max,
            'text': text, 'site': "pages", 'zoom': "Zoom/Translate",
            'bookcontents': "Contents of the Book",
            'seit_pk': pk, 'topic': topic,
        }
           )
# ================== END seites_list  ===========================


# ================== ZOOM_SEITE_ENG  ===========================
def zoom_seite_eng(request, pk, quelle):

    seite = Bookseites.objects.get(pk = pk)

    zoom_seite = []

    zoom_seite.append(0)
    zoom_seite.append(seite.name_eng1)  # 1
    zoom_seite.append(seite.name_eng)  # 2
    zoom_seite.append(seite.content_eng)  # 3
    zoom_seite.append(seite.image_seites)  # 4
    zoom_seite.append(seite.name_seites)  # 5

    topic = seite.name_eng1
    name = seite.name_eng

    return render(
        request, 'zoom_seite.html',
        context = {
            'template': "base_generic_eng.html",
            'url_zoom': "bookland:zoom_eng",
            'url_seiteslist': "bookland:seites-list_eng",
            'url_register': "bookland:register-seites_eng",
            'language': "ENG",
            'eng': "english", 'ukr': "ukrainish",

            'zoom_seite': zoom_seite,  'seite_id': pk,
            'quelle_zoom': quelle,
            'back': "Back", 'topic': topic, 'name': name,

        }
           )

# ================== END zoom_seite  ===========================

# ================== REGISTER ART ENG ===========================
def register_art_eng(request, art):

    if art == "1":
        art_key = "Geographical names"
        art_name = "Geographical names"
    if art == "2":
        art_key = "Settlements"
        art_name = "Settlements"
    if art == "3":
        art_key = "Tourist object"
        art_name = "Tourist Facilities"

    reg_name_list = Register_eng.objects.all().filter(reg_art = art_key)
    num_name = len(reg_name_list)

    art_object = set(())
    for object in reg_name_list:
        art_object.add (object.reg_s_name)

    art_object_num = [[],]
    for item in art_object:
        l = []
        l.append(0)
        l.append(item)
        l.append(len(Register_eng.objects.all().filter(reg_s_name=item)))

        art_object_num.append(l)

    art_object_num.sort()


    return render(
        request, 'register_art.html',
        context = {
            'template': "base_generic_eng.html",
            'url_object': "bookland:register-object_eng",
            'url_register': "bookland:register-seites_eng",
            'language': "ENG",
            'eng': "english", 'ukr': "ukrainish",

            'art': art,
            'reg_name_list': reg_name_list,
            'num_name': num_name, 'art_name': art_name,

            'art_object': art_object,
            'art_object_num': art_object_num,
            'illustration': "Dawn at Cape Kule Burun (Mangup locality)",

        }
           )
# ================== END register_art_eng ===========================

# ================== REGISTER OBJECT ENG ===========================
def register_object_eng(request, obj,):

    typ_list = Object_typ.objects.get(Q(ukr=obj) | Q(eng=obj))
    object_name = typ_list.eng


    # object_name = obj
    reg_name_list = Register_eng.objects.all().filter(reg_s_name = object_name)  # список об'ектів обраного типу
    num_name = len(reg_name_list)   # кількість об'ектів обраного типу

    art = reg_name_list [0].reg_art    # вид показчика (географія, міста, туроб'єкти)
    reg_name_list_all = Register_eng.objects.all().filter(reg_art=art)   # список найменувань виду показчика
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
        l.append(len(Register_eng.objects.all().filter(reg_s_name=item)))
        art_object_num.append(l)
    art_object_num = art_object_num[1:]
    art_object_num.sort()

    return render(
        request, 'register_object.html',
        context = {
            'template': "base_generic_eng.html",
            'url_object': "bookland:register-object_eng",
            'url_register': "bookland:register-seites_eng",
            'language': "ENG",
            'eng': "english", 'ukr': "ukrainish",

            'object_name': object_name,
            'reg_name_list': reg_name_list,
            'num_name': num_name,
            'art': art,
            'num_name_art': num_name_art,
            'art_object': art_object,
            'art_object_num': art_object_num,
            'illustration': "Dawn at Cape Kule Burun (Mangup locality)",

        }
           )
# ================== END register_object_eng ===========================

# ================== REGISTER SEITES_eng ===========================
def register_seites_eng(request, pk,):

    reg_seites = Register_eng.objects.get(pk = pk) # сторінки з вказаним об'єктом
    reg_name = reg_seites.reg_f_name           # найменування об'єкту
    reg_numbers =  reg_seites.reg_numbers          # нумера сторінок з вказаним об'єктом
    reg_art =  reg_seites.reg_art              # вид показчика об'єкта
    reg_pk = pk                                # код об'єкта
    reg_object = reg_seites.reg_s_name         # тип об'єкта

    reg_object_list = Register_eng.objects.all().filter(reg_s_name = reg_object) # список об'єктів заданого типу
    num_name = len(reg_object_list)
    reg_name_list = Register_eng.objects.all().filter(reg_art=reg_art) # список всіх об'єктів виду показчика

    seites = reg_seites.reg_seites.all()
    seites_list = [[], ]
    for item in seites:
        l = []
        l.append(0)
        l.append(item.name_eng1)  # 1
        l.append(item.name_eng)  # 2
        l.append(item.seites)  # 3
        l.append(item.id)  # 4
        l.append(item.image_seites)  # 5
        seites_list.append(l)
    seites_list = seites_list[1:]

    return render(
        request, 'register_seites.html',
        context = {
            'template': "base_generic_eng.html",
            'url_zoom': "bookland:zoom_eng",
            'url_register': "bookland:register-seites_eng",
            'language': "ENG",
            'eng': "english", 'ukr': "ukrainish",

            'reg_seites': reg_seites,
            'object_name': reg_object,
            'reg_object_list': reg_object_list,
            'num_name': num_name,
            'reg_name_list': reg_name_list,
            'reg_art': reg_art, 'reg_name': reg_name,
            'reg_numbers': reg_numbers,
            'reg_pk': reg_pk,
            'seites_list': seites_list,
            'site': "pages", 'zoom': "Zoom/Translate",


        }
           )
# ================== END register_seites_eng ===========================
