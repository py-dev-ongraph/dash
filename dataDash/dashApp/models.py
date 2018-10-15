from django.db import models

# Create your models here.
from django.db import models

class Dentrix(models.Model):
    Month = models.CharField(
        max_length=20,
        null=False,
        blank=False
        )
    Production = models.DecimalField(
        max_digits = 12,
        decimal_places=2,
        default=0
        )
    Hygienist_Production = models.DecimalField(
        max_digits = 12,
        decimal_places=2,
        default=0
        )
    Collections_Percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
        )
    Overthe_Counter = models.SmallIntegerField(
        default=0
        )
    AR_31_60 = models.DecimalField(
        max_digits = 12,
        decimal_places=2,
        default=0
    )
    AR_61_90 = models.DecimalField(
        max_digits = 12,
        decimal_places=2,
        default=0
    )
    AR_Over_90 = models.DecimalField(
        max_digits = 12,
        decimal_places=2,
        default=0
    )
    AR_Ins_31_60 = models.DecimalField(
        max_digits = 12,
        decimal_places=2,
        default=0
    )
    AR_Ins_61_90 = models.DecimalField(
        max_digits = 12,
        decimal_places=2,
        default=0
    )
    AR_Ins_Over_90 = models.DecimalField(
        max_digits = 12,
        decimal_places=2,
        default=0
    )
    New_Patients = models.SmallIntegerField(
        default=0
        )
    Total_Patients_Seen =models.SmallIntegerField(
        default=0
    )
    Broken_Apointments = models.SmallIntegerField(
        default=0
    )
    Broken_Appt_Pct = models.IntegerField(
        default = 0
    )
    Hygiene_Pct = models.DecimalField(
        max_digits = 5,
        decimal_places=2,
        default=0
    )

    class Meta:
        verbose_name_plural = "Dentrix"


    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s ' % (self.Month,
                                                                    self.Production,self.Hygienist_Production,
                                                                    self.Collections_Percentage,self.Overthe_Counter,
                                                                    self.AR_31_60,self.AR_61_90,self.AR_Over_90,
                                                                    self.AR_Ins_31_60,self.AR_Ins_61_90,self.AR_Ins_Over_90,
                                                                    self.New_Patients,self.Total_Patients_Seen,
                                                                    self.Broken_Apointments,self.Broken_Appt_Pct,
                                                                    self.Hygiene_Pct)

        
