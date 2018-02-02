#coding: utf-8
#accounts.models.py
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .managers import UserManager

'''
	Modelo que extende o perfil do usuário padrão do Django para realizar login no sistema
'''
class User(AbstractBaseUser, PermissionsMixin):

	#User Fields
	email = models.EmailField(_('email adress'), unique=True)
	first_name = models.CharField(_('first name'), max_length=60)
	last_name = models.CharField(_('last name'), max_length=200)
	date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
	avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

	# Django Admin User Fields
	active = models.BooleanField(_('active'), default=True)
	staff= models.BooleanField(_('staff'), default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIEDS = []

	class Meta:
		verbose_name = _('user')
		verbose_name_plural= _('users')

	def get_full_name(self):
		'''
		Retorna o completo do usuário que é dado pelo primeiro nome e o último nome separados por um espaço
		'''
		full_name = '%s %s'(self.first_name, self.last_name)
		return full_name

	def get_short_name(self):
		'''
		Retorna o nome curto do usuário que é dado pelo primeiro nome
		'''
		return self.first_name

	def email_user(self, subject, message, from_email=None, **kwargs):
		'''
		Envia um e-mail para o usuário
		'''
		send_mail(subject, message, from_email, [self.email], **kwargs)

	def is_staff(self):
		'''
		Retorna se o usuário faz parte do staff
		'''
		return self.staff

	def is_active(self):
		'''
		Retorna se o usuário está ativo
		'''
		return self.active

