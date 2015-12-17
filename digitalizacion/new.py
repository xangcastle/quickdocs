# -*- coding: utf-8 -*-
import pyPdf
import os
from .models import *
import string
import random
from django.conf import settings
import math


def only_alfabetics(text):
    for char in text:
        if l not in ['A', 'B', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z,'
        ' ']:
            text = text.replace(l, '')
    return text


def clean_spaces(text):
    text = text.replace(' ', '')
    return text


def only_digits(text):
    for l in text:
        if l not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']:
            text = text.replace(l, '')
    return text


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


def generar_paginas(queryset, by_page=6.0):
    model = type(queryset[0])
    pages = []
    number = 1
    if queryset:
        page = {'objects': []}
        page['number'] = number
        total_pages = int(math.ceil(queryset.count() / by_page))
        for p in range(0, total_paginas):
            for i in range(p, int(total_pages * int(by_page)), total_pages):
                try:
                    page['objects'].append(queryset[i])
                except:
                    page['objects'].append(model())
                if len(page['objects']) == int(by_page):
                    number += 1
                    pages.append(page)
                    page = {'objects': []}
                    page['number'] = number
    return pages


def extract_content(pdf):
    content = ""
    content += pdf.getPage(0).extractText() + "\n"
    content = content.encode("ascii", "ignore")
    content = " ".join(content.replace("\xa0", " ").strip().split())
    return content