from django.contrib import admin

from .models import Bookseites, Register, Bookseites_eng, Register_eng

# admin.site.register(Bookseites)

class BookseitesAdmin(admin.ModelAdmin):
    list_display = ('id', 'seites', 'name_seites1', 'name_seites', 'image_seites', )
admin.site.register(Bookseites, BookseitesAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'reg_art', 'reg_f_name', 'reg_s_name', 'reg_numbers',  )
admin.site.register(Register, RegisterAdmin)


class Bookseites_engAdmin(admin.ModelAdmin):
    list_display = ('id', 'seites', 'name_seites1', 'name_seites', 'image_seites', )
admin.site.register(Bookseites_eng, BookseitesAdmin)

class Register_engAdmin(admin.ModelAdmin):
    list_display = ('id', 'reg_art', 'reg_f_name', 'reg_s_name', 'reg_numbers',  )
admin.site.register(Register_eng, RegisterAdmin)

