from django.db import models

class Talaba(models.Model):
    objects = None
    ism = models.CharField(max_length=50)
    guruh = models.CharField(max_length=20), models.IntegerField
    kurs = models.PositiveSmallIntegerField(default=1)
    kitob_soni = models.IntegerField(default=4)


    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"

    def __str__(self):
        return self.ism


class Muallif(models.Model):
    objects = None
    JINS = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )
    ism = models.CharField(max_length=255)
    jins = models.CharField(choices=JINS, max_length=150)
    b_date = models.DateField(null=True)
    kitob_soni = models.PositiveSmallIntegerField(blank=True)
    tirik = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"


    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=20, default="Romantika")
    sahifa = models.PositiveSmallIntegerField(blank=True,null=True)
    muallif = models.ForeignKey(Muallif, models.CASCADE)


    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"


    def __str__(self):
        return self.nom


class Kutubxonachi(models.Model):
    ISH_VAQTI = (
        ('1', '8:00,13:00'),
        ('2', '13:00,19:00'),
    )
    ism = models.CharField(max_length=20)
    ish_vaqti = models.CharField(max_length=40, choices=ISH_VAQTI, blank=True, null=True)

    class Meta:
        verbose_name = "Kutubxonachi"
        verbose_name_plural = "Kutubxonachilar"


    def __str__(self):
        return self.ism


class Records(models.Model):
    talaba = models.ForeignKey(Talaba, models.CASCADE)
    kitob = models.ForeignKey(Kitob, models.CASCADE)
    kutubxonaci = models.ForeignKey(Kutubxonachi, models.CASCADE)
    olingan_sana = models.DateTimeField(auto_now_add=True)
    qaytardi = models.BooleanField(default=False)
    qaytarish_sana = models.DateTimeField(blank=True, null=True)


    class Meta:
        verbose_name = "Records"
        verbose_name_plural = "Recordlar"
