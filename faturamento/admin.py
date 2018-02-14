#coding: utf-8
# accounts.admin.py
from django.contrib import admin
from .models import Cliente, Leitura

admin.site.register(Cliente)
admin.site.register(Leitura)


