# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms.models import model_to_dict
from django.db import models
import datetime

# Create your models here.
class Links(models.Model):
    link = models.URLField()

    def __str__(self):
        return self.link


class Group_type(models.Model):
    group_name = models.CharField(max_length=220)

    def __str__(self):

        return self.group_name



class Finance(models.Model):

    Trimester_type = models.CharField(max_length=220)

    def __str__(self):
        return self.Trimester_type


class Group_in_time(models.Model):

    Group = models.ForeignKey(Group_type, on_delete=models.CASCADE)
    Time_hour = models.IntegerField()
    Time_day = models.CharField(max_length=220)
    Time_minutes = models.IntegerField()
    def __str__(self):
        return self.Time_day+' '+str(self.Time_hour) + ':' + str(self.Time_minutes)


class Person(models.Model):
    Phone_number = models.CharField(max_length=220)
    child_name = models.CharField(max_length=220)
    surname = models.CharField(max_length=220)
    Age = models.IntegerField()
    Parent_name = models.CharField(max_length=220)
    Group = models.ForeignKey(Group_in_time, on_delete=models.CASCADE)


    Pay_in_this_month = models.BooleanField(default=False)
    Pay_for_books = models.BooleanField(default=False)

    def __str__(self):
        return str(self.child_name) + str(" "+self.surname)

class CashValue(models.Model):
    Pay_value = models.DecimalField(max_digits=6, decimal_places=2, default=29)
    tan_value = models.DecimalField(max_digits=6, decimal_places=2, default=0.14)
    vat_value = models.DecimalField(max_digits=6, decimal_places=2, default=0.29)
    Count_of_hours = models.IntegerField(null=True)
    Person =models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    Finance = models.ForeignKey(Finance, on_delete=models.CASCADE, null=True)





