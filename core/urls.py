from django.contrib import admin
from django.urls import path
from Library.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('homepage_view/', home2_view),
    path('talabalar_all/', talabalar),
    path('mualliflar/', muallif_all),
    path('talaba4/', talaba_bitiruvchi),
    path('student_kitob/', kitob_0),
    path('kitob_all/', all_books),
    path('records_all/', all_records),
    path('muallif_tirik/', tirik_muallif),
    path('sahifa_3/', kitob_sahifa),
    path('latest_records/', oxirgi_3_record),
    path('tiriklar_kitoblari/', tirik_muallif_kitoblar),
    path('badiiylar/', badiiy_kitoblar),
    path('author_old/', oldest_authors),
    path('book10/', less10book),
    path('delete/student/<int:id>',del_talaba),

]
