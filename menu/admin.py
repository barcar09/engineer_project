# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Links)
admin.site.register(Group_type)
admin.site.register(Person)
admin.site.register(Group_in_time)
admin.site.register(Finance)
admin.site.register(CashValue)

