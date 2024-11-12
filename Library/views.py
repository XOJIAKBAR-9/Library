import datetime
from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import *
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
    form = TalabaForm()
    param = request.GET.get('search')
    if request.method == "POST":
        form_data = TalabaForm(request.POST)
        if form_data.is_valid():
            data = form_data.cleaned_data
            Talaba.objects.create(
                ism=data.get('ism'),
                guruh=data.get('guruh'),
                kurs=data.get('kurs'),
                kitob_soni=data.get('kitob_soni')
            )
        return redirect('talabalar')
    talabalar = Talaba.objects.all()
    if param:
        talabalar = talabalar.filter(ism__icontains=param)
    context = {
        'talabalar': talabalar,
        'form': form
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
    if request.method=="POST":
        form=KitobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('kitob_all')
    form = KitobForm()

    context = {
        'kitob_all': kitob_all,
        'form':form
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
    latest_records = Records.objects.order_by('-olingan_sana')[:3]
    context = {
        'latest_records': latest_records
    }
    return render(request, "latest3_recieved.html", context)


def tirik_muallif_kitoblar(request):
    tiriklar_kitoblari = Kitob.objects.filter(muallif__tirik=True)
    context = {
        'tiriklar_kitoblar': tiriklar_kitoblari
    }
    return render(request, "tirik_mualliflar_kitobi.html", context)


def badiiy_kitoblar(request):
    badiiylar = Kitob.objects.filter(janr='badiiy')
    context = {
        'badiiylar': badiiylar
    }
    return render(request, "badiiy_books.html", context)


def oldest_authors(request):
    author_old = Muallif.objects.order_by('b_date')[:3]
    context = {
        'author_old': author_old
    }
    return render(request, "3old_authors.html", context)


def less10book(request):
    book10 = Kitob.objects.filter(muallif__kitob_soni__lt=10)
    context = {
        'book10': book10
    }
    return render(request, "book10less.html", context)


def bitiruvchilar_record(request):
    kurs_4_record = Records.objects.filter(talaba__kurs=4)
    context = {
        'kurs_4_record': kurs_4_record
    }
    return render(request, "record_4kurs.html", context)


def del_talaba(request, id):
    student = Talaba.objects.get(id=id)
    student.delete()
    return redirect('/talabalar_all/')


def record_students(request):
    param = request.GET.get('search')
    records = Records.objects.all()
    if param:
        records = records.filter(talaba__ism__icontains=param)
        context = {
            'records': records
        }
        return render(request, "search_student_records.html", context)


def add_new_student(request):
    if request.method == "GET":
        return render(request, "newStudent.html")
    elif request.method == "POST":
        ism = request.POST.get('ism')
        guruh = request.POST.get('guruh')
        kurs = request.POST.get('kurs')
        kitob_soni = request.POST.get('kitob_soni')
        Talaba(ism=ism, guruh=guruh, kurs=kurs, kitob_soni=kitob_soni).save()
        return redirect('/talabalar_all/')


def talaba_update(request, student_id):
    talaba = get_object_or_404(Talaba, id=student_id)
    if request.method == "POST":
        talaba.ism = request.POST.get('ism')
        talaba.guruh = request.POST.get('guruh')
        talaba.kurs = request.POST.get('kurs')
        talaba.kitob_soni = request.POST.get('kitob_soni')
        talaba.save()
        return redirect('talabalar')
    context = {
        'talaba': talaba
    }
    return render(request, "talaba_update.html", context)

def kitobupdateview(request, book_id):
    kitob=get_object_or_404(Kitob,id=book_id)
    if request.method=="POST":
        kitob.nom=request.POST.get('nom')
        kitob.janr=request.POST.get('janr')
        kitob.sahifa=request.POST.get('sahifa')
        muallif_id=request.POST.get('muallif_id')
        kitob=get_object_or_404(Muallif, id=muallif_id)
        kitob.save()
        return redirect('kitoblar')
    context={
        'kitob':kitob,
        'mualliflar': Muallif.objects.all()
    }
    return render(request, "kitob_update.html", context)


def kitob_delete(request,book_id):
    kitob=get_object_or_404(Kitob, id=book_id)
    kitob.delete()
    return redirect('kitob_all')