# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.core import serializers
import simplejson



def main_menu(request):
    queryset_list = Links.objects.all()
    button_list = Group_type.objects.all()
    person_list = Person.objects.values()
    times = Group_in_time.objects.all()
    time_vales = Group_in_time.objects.values()
    per_0 = Person.objects.values('child_name', 'surname', 'Pay_in_this_month', 'Pay_for_books')

    Trim_Val = Finance.objects.values()


    context = {
        "list": queryset_list,
        "Group": button_list,
        "Person": person_list,
        "Time": times,
        "Time_2": time_vales,

        "But_trim": Trim_Val,
        "Per_all" : per_0,
    }
    return render(request, "welcome.html", context)


def site_features(request):
    person_list = Person.objects.all()
    per_2 = Person.objects.values('child_name', 'Parent_name', 'Group__Time_hour','Phone_number', 'surname', 'Age').filter(
                                    Group__Group__group_name='EFAC').order_by('Group__Time_day')
    per_3 = Person.objects.values('child_name', 'Parent_name', 'Phone_number',
                                  'surname', 'Age', 'Group__Time_hour', 'Group__Time_day').filter(
        Group__Group__group_name='LEFAC').order_by('Group__Time_day')

    context = {
        "Person": person_list,
        "Person_2": per_2,
        "Person_3": per_3,
    }
    return render(request, "Js_table.html", context)

    # Create your views here.
def get_groups(request):


    #persons = Person.objects.values('child_name', 'Parent_name', 'Phone_number',
     #                            'surname', 'Age', 'Group__Time_hour', 'Group__Time_day').filter(
      #  Group__Group__group_name='EFAC').order_by('Group__Time_day')

    persons = Person.objects.order_by('Group__Time_day').all().filter(Group__Group__group_name=request.GET['group'])

    json = []

    for person in persons:
        person_json = {
            'child_name': person.child_name,
            'parent_name': person.Parent_name,
            'Phone_number': person.Phone_number,
            'Group_Time_day': person.Group.Time_day,
            'Surname': person.surname,
            'Age': person.Age,
            "Group__Time_hour": person.Group.Time_hour,
            "Group__Time_minutes": person.Group.Time_minutes,
        }
        json.append(person_json)



    return JsonResponse(json, safe=False)
def get_finance(request):
    Count_of_pay = CashValue.objects.all().filter(Finance__pk=request.GET['tri']).aggregate(total_price=Sum('Count_of_hours'))['total_price']
    count_of_person = Person.objects.count()
    Fin_value = CashValue.objects.first().Pay_value
    Fin_val_2 = CashValue.objects.first().tan_value
    Vat_val = CashValue.objects.first().vat_value
    Prof_value = round((Fin_value * count_of_person * Count_of_pay), 2)
    Final_value = round((Fin_val_2 * Fin_value * count_of_person * Count_of_pay), 2)
    netto_value = round(Prof_value - ((Prof_value - Final_value) * Vat_val), 2)
    json = []
    Fin_Json = {
        "Pe_count": count_of_person,
        "Pay": Count_of_pay,
        "Fin_pay": Final_value,
        "Prof_own": Prof_value,
        "Netto": netto_value,
    }
    json.append(Fin_Json)

    return JsonResponse(json, safe=False)

def get_time_of_lesson(request):
    data_json = Group_in_time.objects.all()
    json = []
    for data in data_json :
            dic_dat = {
                'Time_hour':data.Time_hour,
                'Time_minutes':data.Time_minutes,
                'Time_days':data.Time_day,
                'Group__group_name': data.Group.group_name,
            }
            json.append(dic_dat)

    return JsonResponse(json, safe=False)