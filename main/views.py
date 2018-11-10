# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.log import getLogger
import os
import dict4ini

logger = getLogger("default")


def index(request):
    a = os.path.join("/home/web/", "site.ini")
    obj = dict4ini.DictIni(a)
    b = obj["SERVER"]["A"]
    logger.info("======>1={0}, 2={1}".format(a, b))
    logger.info("url={0}".format(request.get_full_path()))
    return render(request, 'main/index.html')
