from django.db import models

# ========================= OBJECT =======
class Object_typ(models.Model):
    class Meta:
        ordering = ["ukr", ]

    ukr = models.CharField(max_length=50, null=True, blank=True)
    eng = models.CharField(max_length=50, null=True, blank=True)
    ita = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.ukr + ' ' + self.eng)

# ========================= BOOKSEITES =======
class Bookseites(models.Model):
    class Meta:
        ordering = ["image_seites"]
    seites = models.CharField(max_length=10,)
    name_seites1 = models.CharField(max_length=100, null = True, blank = True)
    name_seites = models.CharField(max_length=100, null = True, blank = True)
    name_step = models.CharField(max_length=1, null = True, blank = True)
    image_seites = models.CharField(max_length=30, null = True, blank = True)
    content_seite = models.TextField(null = True, blank = True)

    def __str__(self):
        return str(self.seites + ' ' + self.name_seites)

    # def get_absolute_url(self):
    #     return reverse('poems:genre-detail', args=[str(self.id)])

# ========================= REGISTER =======
class Register(models.Model):
    class Meta:
        ordering = ["reg_art", "reg_f_name"]
    reg_art = models.CharField(max_length=30,)
    reg_f_name = models.CharField(max_length=100, null = True, blank = True)
    reg_s_name = models.CharField(max_length=100, null=True, blank=True)
    object_typ = models.ManyToManyField(Object_typ, )
    reg_numbers = models.CharField(max_length=100, null=True, blank=True)
    reg_seites = models.ManyToManyField(Bookseites,)

    def __str__(self):
        return str(self.reg_f_name)

    # def get_absolute_url(self):
    #     return reverse('poems:genre-detail', args=[str(self.id)])

# ========================= BOOKSEITES =======
class Bookseites_eng(models.Model):
    class Meta:
        ordering = ["image_seites"]
    seites = models.CharField(max_length=10,)
    name_seites1 = models.CharField(max_length=100, null = True, blank = True)
    name_seites = models.CharField(max_length=100, null = True, blank = True)
    name_step = models.CharField(max_length=1, null = True, blank = True)
    image_seites = models.CharField(max_length=30, null = True, blank = True)
    content_seite = models.TextField(null = True, blank = True)

    def __str__(self):
        return str(self.seites + ' ' + self.name_seites)

    # def get_absolute_url(self):
    #     return reverse('poems:genre-detail', args=[str(self.id)])

# ========================= REGISTER =======
class Register_eng(models.Model):
    class Meta:
        ordering = ["reg_art", "reg_f_name"]

    reg_art = models.CharField(max_length=30, )
    reg_f_name = models.CharField(max_length=100, null=True, blank=True)
    reg_s_name = models.CharField(max_length=100, null=True, blank=True)
    object_typ = models.ManyToManyField(Object_typ, )
    reg_numbers = models.CharField(max_length=100, null=True, blank=True)
    reg_seites = models.ManyToManyField(Bookseites, )

    def __str__(self):
        return str(self.reg_f_name)

# ========================= TEXT =======
class Text_site(models.Model):

    theme = models.CharField(max_length=100, null=True, blank=True)
    ukr = models.TextField(null = True, blank = True)
    eng = models.TextField(null=True, blank=True)
    ita = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.theme)







