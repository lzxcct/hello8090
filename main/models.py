# -*- coding: utf-8 -*-

from django.db import models

from main.choices import *


class Reply(models.Model):
    floor = models.IntegerField(verbose_name=u'楼层', db_column='Floor', blank=False)
    theme_id = models.IntegerField(verbose_name=u'对应主题', db_column='themeId', blank=False)
    name = models.CharField(verbose_name=u'用户名', db_column='Name', max_length=20, blank=False)
    reply_content = models.CharField(verbose_name=u'回复内容', db_column='replyContent', max_length=3000, blank=False)
    img_url = models.CharField(verbose_name=u'图片路径', db_column='imgUrl', max_length=200, null=True)
    add_time = models.DateTimeField(verbose_name=u'回复时间', db_column='addTime', auto_now_add=True)
    reply_id = models.ForeignKey('self', verbose_name=u'回复内容2', db_column='replyId', null=True)
    status = models.SmallIntegerField(verbose_name=u'是否有效', default=1, choices=STATUS)

class Theme(models.Model):
    title = models.CharField(verbose_name=u'标题', db_column='Title', max_length=50, blank=False)
    name = models.CharField(verbose_name=u'用户名', db_column='Name', max_length=20, blank=False)
    img_url = models.CharField(verbose_name=u'内容图片', db_column='imgUrl', max_length=200, blank=False)
    content_explain = models.CharField(verbose_name=u'内容说明', db_column='contentExplain', max_length=3000, blank=False)
    add_time = models.DateTimeField(verbose_name=u'创建时间', db_column='addTime', auto_now_add=True)
    up_time = models.DateTimeField(verbose_name=u'更新时间', db_column='upTime', auto_now=True)
    reply_id = models.ForeignKey(Reply, verbose_name=u'回复内容', db_column='replyId', null=True)
    good = models.IntegerField(verbose_name=u'赞', db_column='Good', default=0)
    difference = models.IntegerField(verbose_name=u'踩', db_column='Difference', default=0)
    pv_sum = models.IntegerField(verbose_name=u'访问量', db_column='pvSum', default=0)
    reply_sum = models.IntegerField(verbose_name=u'回复量', db_column='replySum', default=0)
    status = models.SmallIntegerField(verbose_name=u'是否有效', default=1, choices=STATUS)
