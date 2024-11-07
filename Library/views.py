import datetime
from urllib import request

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def homepage(request):
    return HttpResponse(
        "<h1> Salom akalar</h1>"
    )


def home2_view(request):
    import datetime
    now = datetime.datetime.now()
    context = {
        'now': now
    }
    return render(request, "home.html", context)


def talabalar(request):
    param=request.GET.get('search')
    talabalar = Talaba.objects.all()
    if param:
        talabalar=talabalar.filter(ism__icontains=param)
    context = {
        'talabalar': talabalar
    }
    return render(request, "talabalar_all.html", context)


def muallif_all(request):
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar
    }
    return render(request, "mualliflar.html", context)


def talaba_bitiruvchi(request):
    talaba4 = Talaba.objects.filter(kurs=4)
    context = {
        'talaba4': talaba4
    }
    return render(request, "talaba_4kurs.html", context)


def kitob_0(request):
    student_kitob = Talaba.objects.filter(kitob_soni__gt=0)
    context = {
        'student_kitob': student_kitob
    }
    return render(request, "kitob_soni_student.html", context)


def all_books(request):
    kitob_all = Kitob.objects.all()
    context = {
        'kitob_all': kitob_all
    }
    return render(request, "kitoblar_all.html", context)


def all_records(request):
    records_all = Records.objects.all()
    context = {
        'records_all': records_all
    }
    return render(request, "recordlar.html", context)


def tirik_muallif(request):
    muallif_tirik = Muallif.objects.filter(tirik=True)
    context = {
        'muallif_tirik': muallif_tirik
    }
    return render(request, "tiriklar_muallif.html", context)


def kitob_sahifa(request):
    sahifa_3 = Kitob.objects.order_by('-sahifa')[:3]
    context = {
        'sahifa_3': sahifa_3
    }
    return render(request, "sahifa_max3.html", context)


def oxirgi_3_record(request):
    latest_records=Records.objects.order_by('-olingan_sana')[:3]
    context={
        'latest_records':latest_records
    }
    return render(request, "latest3_recieved.html", context)


def tirik_muallif_kitoblar(request):
    tiriklar_kitoblari=Kitob.objects.filter(muallif__tirik=True)
    context={
        'tiriklar_kitoblar':tiriklar_kitoblari
    }
    return render(request, "tirik_mualliflar_kitobi.html", context)


def badiiy_kitoblar(request):
    badiiylar=Kitob.objects.filter(janr='badiiy')
    context={
        'badiiylar': badiiylar
    }
    return render(request,"badiiy_books.html", context)


def oldest_authors(request):
    author_old=Muallif.objects.order_by('b_date')[:3]
    context={
        'author_old': author_old
    }
    return render(request, "3old_authors.html", context)


def less10book(request):
    book10=Kitob.objects.filter(muallif__kitob_soni__lt=10)
    context={
        'book10':book10
    }
    return render(request,"book10less.html", context)


def bitiruvchilar_record(request):
    kurs_4_record = Records.objects.filter(talaba__kurs=4)
    context={
        'kurs_4_record':kurs_4_record
    }
    return render(request,"record_4kurs.html", context)

def del_talaba(request, id):
    student=Talaba.objects.get(id=id)
    student.delete()
    return redirect('/talabalar_all/')
