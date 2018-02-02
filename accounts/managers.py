#coding: utf-8
#accounts.managers.py

from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		'''
		Cria e salva um usuário com um e-mail e senha dados
		'''
		if not email:
			raise ValueError(_('The given email must be set'))
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self_create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_('Superuser must have is_superuser=True'))
		user = self._create_user(email, password, **extra_fields) 
		user.is_staff = True
		return user





