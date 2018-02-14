#coding: utf-8
#faturamento.models.py
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Cliente(models.Model):
	id_cliente = models.AutoField(
		primary_key = True,
		unique = True,
		verbose_name = _("número identificador do cliente")
		)
	nome = models.CharField(
		max_length = 30,
		help_text = _("nome"),
		verbose_name=_("nome do cliente"),
		null = True,
		blank = True,
		)
	sobrenome = models.CharField(
		max_length = 30,
		help_text = _("nome"),
		verbose_name=_("sobrenome do cliente"),
		null = True,
		blank = True,
		)
	tarifa = models.FloatField(
		help_text = _("tarifa cobrada para o usuário"),
		verbose_name = _("tarifa R$"),
		null = False,
		blank = False,
		)
	class Meta:
		ordering = ["nome", "sobrenome"]
		verbose_name = "cliente"
		verbose_name_plural = "clientes"

	def __str__(self):
		return "(" + self.id_cliente.__str__() + ") " + self.nome + " " + self.sobrenome


class Leitura(models.Model):
	cliente = models.ForeignKey(
		Cliente, 
		on_delete=models.CASCADE,
		verbose_name = _("cliente responsável"),
		)
	data = models.DateField(
		verbose_name = _("data de referência"),
		blank = False,
		null = False,
		)
	leitura = models.FloatField(
		help_text = _("leitura para a data"),
		verbose_name = _("leitura"),
		null = False,
		blank = False,
		)
	class Meta:
		ordering = ["cliente", "data"]
		verbose_name = "leitura"
		verbose_name_plural = "leituras"
	def __str__(self):
		return self.data.__str__() + " - " + self.cliente.nome + " " + self.cliente.sobrenome
