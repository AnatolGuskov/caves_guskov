from django.contrib import admin

from .models import Bookseites, Bookseites_eng, Register, Register_eng, \
                    Text_site, Object_typ

# admin.site.register(Bookseites)

class BookseitesAdmin(admin.ModelAdmin):
    list_display = ('id', 'seites', 'name_seites1', 'name_seites', 'image_seites', )
admin.site.register(Bookseites, BookseitesAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'reg_art', 'reg_f_name', 'reg_s_name', 'reg_numbers',  )
admin.site.register(Register, RegisterAdmin)


class Bookseites_engAdmin(admin.ModelAdmin):
    list_display = ('id', 'seites', 'name_seites1', 'name_seites', 'image_seites', )
admin.site.register(Bookseites_eng, Bookseites_engAdmin)

class Register_engAdmin(admin.ModelAdmin):
    list_display = ('id', 'reg_art', 'reg_f_name', 'reg_s_name', 'reg_numbers',  )
admin.site.register(Register_eng, Register_engAdmin)

admin.site.register(Text_site)

class Object_typAdmin(admin.ModelAdmin):
    list_display = ('ukr', 'eng', 'ita', )
admin.site.register(Object_typ, Object_typAdmin)








