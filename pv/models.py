# -*- coding: utf-8 -*-

from django.db import models

class DayDate(models.Model):
    day_uv = models.IntegerField(verbose_name=u'当日用户量', db_column='dayUv', default=0)
    day_pv = models.IntegerField(verbose_name=u'当日浏览量', db_column='daypv', default=0)
    current_day = models.DateField(verbose_name=u'当日日期', db_column='currentDay', blank=False)

class MonthDate(models.Model):
    month_uv = models.IntegerField(verbose_name=u'当月用户量', db_column='monthUv', default=0)
    month_pv = models.IntegerField(verbose_name=u'当月浏览量', db_column='monthpv', default=0)
    current_month = models.DateField(verbose_name=u'当月日期', db_column='currentMonth', blank=False)

class SourceData(models.Model):
    source = models.CharField(verbose_name=u'来源', db_column='Source', max_length=50, blank=False)
    name = models.CharField(verbose_name=u'用户名', db_column='Name', max_length=20, blank=False)
    add_time = models.DateTimeField(verbose_name=u'访问时间', db_column='addTime', auto_now_add=True)
