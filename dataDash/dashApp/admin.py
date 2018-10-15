from django.contrib import admin
from .models import Dentrix


class Dentrix_Admin(admin.ModelAdmin):
    model = Dentrix
    list_display = ('Month','Production','Hygienist_Production','Collections_Percentage','Overthe_Counter',
'AR_31_60','AR_61_90','AR_Over_90','AR_Ins_31_60','AR_Ins_61_90','AR_Ins_Over_90','New_Patients',
'Total_Patients_Seen','Broken_Apointments','Broken_Appt_Pct','Hygiene_Pct',
)
# Register your models here.

admin.site.register(Dentrix, Dentrix_Admin)
