from django.contrib import admin
from .models import *


class TalabaAdmin(admin.ModelAdmin):
    list_display = ['id', 'ism', 'kurs', 'guruh', 'kitob_soni']
    list_display_links = ['id', 'ism']
    list_filter = ['kurs', ]
    list_per_page = 10
    search_field = ('ism', 'kurs')
    search_help_text = 'Ism yoki gutuhni qidir ukam...'
    list_editable = ['kurs', ]


class RecordAdmin(admin.ModelAdmin):
    list_display = ['talaba', 'kitob', 'kutubxonaci', 'olingan_sana', 'qaytarish_sana', 'qaytardi']
    list_editable = ['qaytardi']
    date_hierarchy = 'qaytarish_sana'


class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1


class KitobAdmin(admin.ModelAdmin):
    list_display = ('nom', 'janr', 'sahifa', 'muallif')


class MuallifAdmin(admin.ModelAdmin):
    inlines = [KitobInline]


class Kutubxonachi(admin.ModelAdmin):
    list_display = ["ism", "ish_vaqti"]
    list_editable = ["ish_vaqti"]
    search_fields=["ism"]
    search_help_text="Ism bo`yicha qidiring: "
    save_as_continue = True


# admin.site.register(Talaba, TalabaAdmin)
# admin.site.register(Muallif, MuallifAdmin)
# admin.site.register(Kitob, KitobAdmin)
# admin.site.register(Kutubxonachi)
# admin.site.register(Records, RecordAdmin)
