# -*- coding: utf-8 -*-

from django.db import models

from main.choices import *


class Persona(models.Model):
    name = models.CharField(verbose_name=u'用户名', db_column='Name', max_length=20, blank=False)
    nickname = models.CharField(verbose_name=u'昵称', db_column='Nickname', max_length=20, blank=False)
    gender = models.SmallIntegerField(verbose_name=u'性别', default=0, choices=GENDER)
    age = models.SmallIntegerField(verbose_name=u'年龄', null=True)
    occupation = models.CharField(verbose_name=u'职业', db_column='Occupation', max_length=30, null=True)
    hobby = models.CharField(verbose_name=u'兴趣爱好', db_column='Hobby', max_length=50, null=True)
    location = models.CharField(verbose_name=u'所在地', db_column='Location', max_length=50, null=True)
    email = models.CharField(verbose_name=u'邮箱', db_column='Email', max_length=20, null=True)
    wisdom = models.CharField(verbose_name=u'个人签名', db_column='wisdom', max_length=50, null=True)
    up_time = models.DateTimeField(verbose_name=u'修改时间', db_column='upTime', auto_now=True)
    status = models.SmallIntegerField(verbose_name=u'是否有效', default=1, choices=STATUS)

class User(models.Model):
    name = models.CharField(verbose_name=u'用户名', db_column='Name', max_length=20, blank=False)
    password = models.CharField(verbose_name=u'密码', db_column='Password', max_length=60, blank=False)
    registr_time = models.DateTimeField(verbose_name=u'注册时间', db_column='registrTime', auto_now_add=True)
    login_time = models.DateTimeField(verbose_name=u'登录时间', db_column='loginTime', auto_now=True)
    persona_id = models.ForeignKey(Persona, verbose_name=u'个人信息', db_column='personaId', null=True)
    status = models.SmallIntegerField(verbose_name=u'是否有效', default=1, choices=STATUS)
    u_type = models.SmallIntegerField(verbose_name=u'用户权限', default=1, choices=U_TYPE)
