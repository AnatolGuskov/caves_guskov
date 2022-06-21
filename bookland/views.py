from django.shortcuts import render

from django.views import generic
from django.db.models import Q

from . models import Bookseites, Register, Text_site, Object_typ




# ================== INDEX  ===========================
def index(request):
    tytle = Text_site.objects.get(theme = "index_tytle")
    text_tytle = tytle.ukr
    annotation = Text_site.objects.get(theme="index_annotation")
    text_annotation = annotation.ukr


    return render(
        request, 'index.html',
        context = {
            'template': "base_generic.html",
            'language': "UKR",
            'eng': "англійська",
            'ukr': "українська",

            'text_tytle': text_tytle,
            'text_annotation': text_annotation,
        }
           )
# ================== SEITES  ===========================
def seites(request, topic):
    if topic == "1":
        seites = Bookseites.objects.all()
        bookcontents = "Зміст книги"
    else:
        seites = Bookseites.objects.all().filter(Q(name_eng1=topic) | Q(name_seites1=topic))
        bookcontents = "Зміст розділу"
        topic_menu = [[]]
        for item in seites:
            t = []
            t.append(0)
            t.append(item.name_seites1)     #1
            t.append(item.name_seites)      #2
            topic_menu.append(t)
        topic = topic_menu[1][1]

    seites_list = [[]]
    for item in seites:
        m = []
        m.append(0)
        m.append(item.name_seites1)  # 1
        m.append(item.name_seites)  # 2
        m.append(item.seites)  # 3
        m.append(item.id)  # 4
        m.append(item.name_step)  # 5
        seites_list.append(m)
    seites_list = seites_list[1:]

    section = Bookseites.objects.all().filter(name_step = "1")

    section_list = [[]]
    for item in section:
        s = []
        s.append(0)
        s.append(item.name_seites1)     #1
        if ": печерне місто" in item.name_seites1:
            s.append("___")               #2
        else:
            s.append("")                 #2
        section_list.append(s)


    return render(
        request, 'seites.html',
        context = {
            'template': "base_generic.html",
            'url_topic': "bookland:seites",
            'url_seiteslist': "bookland:seites-list",
            'language': "UKR",
            'eng': "англійська",
            'ukr': "українська",

            'seittopic': "Перегляд сторінок Книги",
            'bookcontents': bookcontents,
            'seites_list': seites_list,
            'section_list': section_list,
            'topic': topic, 'seites': seites,
            'name': 1,
            'illustration': "Світанок у миса Куле-бурун (місцевість Мангуп)"
                  }
           )

# ================== END seites  ===========================

# ================== SITES_LIST  ===========================
def seites_list(request, topic, pk):
    pk_s = Bookseites.objects.get(pk = pk)
    pk_site = pk_s.image_seites

    if topic == "1":
        seites = Bookseites.objects.all().filter(image_seites__gte=pk_site)[:10]
        menu = Bookseites.objects.all()
        bookcontents = "Зміст книги"
    else:
        seites = Bookseites.objects.all().filter(
            Q(name_eng1=topic, image_seites__gte=pk_site) | Q(name_seites1=topic, image_seites__gte=pk_site))[:10]
        menu = Bookseites.objects.all().filter(Q(name_eng1=topic) | Q(name_seites1=topic))
        bookcontents = "Зміст розділу"

    seites_list = [[]]
    for item in seites:
        m = []
        m.append(0)
        m.append(item.name_seites1)  # 1
        m.append(item.name_seites)  # 2
        m.append(item.seites)  # 3
        m.append(item.id)  # 4
        m.append(item.image_seites)  # 5
        seites_list.append(m)
    seites_list = seites_list[1:]

    seites_menu = [[]]
    for item in menu:
        m = []
        m.append(0)
        m.append(item.name_seites1)  # 1
        m.append(item.name_seites)  # 2
        m.append(item.seites)  # 3
        m.append(item.id)  # 4
        m.append(item.name_step)  # 5
        seites_menu.append(m)
    seites_menu = seites_menu[1:]



    max_seit = len(seites)
    seit_max = seites[max_seit - 1].id
    if max_seit == 1:
        text = "ОСТАННЯ СТОРІНКА виборки"
    else:
        text = "ДАЛІ - наступні сторінки ... "


    return render(
        request, 'seites_list.html',
        context = {
            'template': "base_generic.html",
            'url_seiteslist': "bookland:seites-list",
            'url_zoom': "bookland:zoom",
            'language': "UKR",
            'eng': "англійська", 'ukr': "українська",

            'seites_list': seites_list,
            'seites_menu': seites_menu,
            'seit_max': seit_max,
            'text': text, 'site': "стор.", 'zoom': "Збільшити/Переклад",
            'bookcontents': bookcontents,
            'seit_pk': pk, 'topic': topic,
        }
           )
# ================== END seites_list  ===========================

# ================== ZOOM_SEITE  ===========================
def zoom_seite(request, pk, quelle):

    seite = Bookseites.objects.get(pk = pk)

    zoom_seite = []

    zoom_seite.append(0)
    zoom_seite.append(seite.name_seites1)   #1
    zoom_seite.append(seite.name_seites)    #2
    zoom_seite.append(seite.content_seite)  #3
    zoom_seite.append(seite.image_seites)   #4
    zoom_seite.append(seite.name_seites)    #5

    topic = seite.name_seites1
    name = seite.name_seites
    return render(
        request, 'zoom_seite.html',
        context = {
            'template': "base_generic.html",
            'url_zoom': "bookland:zoom",
            'url_seiteslist': "bookland:seites-list",
            'url_register': "bookland:register-seites",
            'language': "UKR",
            'eng': "англійська", 'ukr': "українська",

            'zoom_seite': zoom_seite, 'seite_id': pk,
            'quelle_zoom': quelle, 'topic': topic,
            'back': "Назад",  'name': name,

        }
           )

# ================== END zoom_seite  ===========================

# ================== REGISTER ART ===========================
def register_art(request, art):

    if art == "1":
        art_key = "Географічні назви"
        art_name = "Географічні назви"
    if art == "2":
        art_key = "Населені пункти"
        art_name = "Населені пункти"
    if art == "3":
        art_key = "Туристичні об'єкти"
        art_name = "Туристичні об'єкти"

    reg_name_list = Register.objects.all().filter(reg_art=art_key)
    num_name = len(reg_name_list)

    art_object = set(())
    for object in reg_name_list:
        art_object.add(object.reg_s_name)

    art_object_num = [[], ]
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
            'template': "base_generic.html",
            'url_object': "bookland:register-object",
            'url_register': "bookland:register-seites",
            'language': "UKR",
            'eng': "англійська", 'ukr': "українська",

            'art': art, 'art_name': art_name,
            'reg_name_list': reg_name_list,
            'num_name': num_name,

            'art_object': art_object,
            'art_object_num': art_object_num,
            'illustration': "Світанок у миса Куле-бурун (місцевість Мангуп)",


        }
           )
# ================== END register_art ===========================

# ================== REGISTER OBJECT ===========================
def register_object(request, obj,):

    typ_list = Object_typ.objects.get(Q(ukr=obj) | Q(eng=obj))
    object_name = typ_list.ukr

    # object_name = obj  # обраний тип об'єкту
    reg_name_list = Register.objects.all().filter(reg_s_name = object_name)  # список об'ектів обраного типу
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
            'template': "base_generic.html",
            'url_object': "bookland:register-object",
            'url_register': "bookland:register-seites",
            'language': "UKR",
            'eng': "англійська", 'ukr': "українська",

            'object_name': object_name,
            'reg_name_list': reg_name_list,
            'num_name': num_name,
            'art': art,
            'num_name_art': num_name_art,
            'art_object': art_object,
            'art_object_num': art_object_num,
            'illustration': "Світанок у миса Куле-бурун (місцевість Мангуп)",

        }
           )
# ================== END register_object ===========================

# ================== REGISTER SEITES ===========================
def register_seites(request, pk_top, pk_site):
    # pk_top - id об'єкта Регистру!
    # pk_site - id сторінки з ЦУМу!

    reg_seites = Register.objects.get(pk = pk_top) # записи сторінок з вказаним об'єктом pk
    reg_name = reg_seites.reg_f_name           # найменування об'єкту
    reg_numbers =  reg_seites.reg_numbers      # нумера сторінок з вказаним об'єктом
    reg_art =  reg_seites.reg_art              # вид показчика об'єкта
    reg_pk = pk_top                            # id об'єкта Регистру
    reg_object = reg_seites.reg_s_name         # тип об'єкта

    reg_object_list = Register.objects.all().filter(reg_s_name = reg_object) # список об'єктів заданого типу
    num_name = len(reg_object_list)
    reg_name_list = Register.objects.all().filter(reg_art=reg_art) # список всіх об'єктів виду показчика

    seites = reg_seites.reg_seites.all()
    seites_list = [[], ]
    seites_first = 1
    seites_trans = 0
    i = 0
    for item in seites:
        i = i + 1
        if i == 1:
            seites_trans = item.id
        if item.id == int(pk_site):
            seites_first = i
        l = []
        l.append(0)
        l.append(item.name_seites1)  # 1
        l.append(item.name_seites)   # 2
        l.append(item.seites)        # 3
        l.append(item.id)            # 4
        l.append(item.image_seites)  # 5
        seites_list.append(l)
    seites_list = seites_list[seites_first:]

    return render(
        request, 'register_seites.html',
        context = {
            'template': "base_generic.html",
            'url_zoom': "bookland:zoom",
            'url_register': "bookland:register-seites",
            'language': "UKR",
            'eng': "англійська", 'ukr': "українська",

            'reg_seites': reg_seites,
            'object_name': reg_object,
            'reg_object_list': reg_object_list,
            'num_name': num_name,
            'reg_name_list': reg_name_list,
            'reg_art': reg_art, 'reg_name': reg_name,
            'reg_numbers': reg_numbers,
            'reg_pk': reg_pk,
            'seites_list': seites_list,
            'site': "стор.", 'zoom': "Збільшити/Переклад",
            'seites_first': seites_first, 'i': i,  # ??????
            'seites_trans': seites_trans,
        }
           )
# ================== END register_seites ===========================


# ================== DICTIONARY ===================================
def dictionary (request, dict_lang):
    wort_list = Register.objects.all()

    wort_dict =[[]]
    dict_tytle = ""

    if dict_lang == "1":   # ukrainish
        for wort in wort_list:
            w = []
            w.append(0)
            w.append (wort.reg_f_name)
            w.append (wort.reg_f_eng.reg_f_name)   #2 english
            wort_dict.append(w)
        wort_dict = wort_dict[1:]
        wort_dict.sort()
        dict_tytle = "Топонімічний та термінологічний Словник"
        template = "base_generic.html"

    if dict_lang == "2":     # english
        for wort in wort_list:
            w = []
            w.append(0)
            w.append(wort.reg_f_eng.reg_f_name)  #1 english
            w.append (wort.reg_f_name)
            wort_dict.append(w)
        wort_dict = wort_dict[1:]
        wort_dict.sort()
        dict_tytle = "Toponymic and terminological Dictionary"
        template = "base_generic_eng.html"


    return render(
        request, 'dictionary.html',
        context={
            'template': template,
            'language': "UKR",
            'eng': "англійська", 'ukr': "українська",

            'lang': dict_lang,
            'wort_dict': wort_dict,
            'dict_tytle': dict_tytle,

        }
    )