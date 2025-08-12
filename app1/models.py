from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    def __str__(self):
        return f'Dr.{self.name} - {self.specialization}'
    
class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=10)
    contact=models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField(blank=True, null=True)
    class Meta:
        unique_together=('doctor','date','time')        