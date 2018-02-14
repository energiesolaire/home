#coding: utf-8
#accounts.forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

class UserAdminCreationForm(forms.ModelForm):
	'''
	Formulário para criar um novo usuário no site Admin
	'''
	password1 = forms.CharField(label=_('Senha'), widget=forms.PasswordInput)
	password2 = forms.CharField(label=_('Confirmação da senha'), widget=forms.PasswordInput)

	class Meta:
		model = User
		exclude = ['password']

	def clean_password2(self):
		# Checa se as senhas são iguais
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(_("Passwords don't match"))

		return password2

	def save(self, commit=True):
		# Salva a senha em hash
		user = super(UserAdminCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])

		if commit:
			user.save()

		return user

class UserAdminChangeForm(forms.ModelForm):
	'''
	Formulário habilita a mudança de todos os campos do usuário, inclusive a senha com confirmação
	'''
	password = ReadOnlyPasswordHashField(label=_('Password'), help_text=("Raw passwords are not stored, so there is no way to see "
                    														"this user's password, but you can change the password "
                    														"using <a href=\"../password/\">this form</a>."))

	class Meta:
		model = User
		fields = '__all__'

	def clean_password(self):
		'''
		Retorna o password original gravado, pois o campo original não possui esse valor
		'''
		return self.initial['password']

class UserAdmin(BaseUserAdmin):
	# The forms to add and change user instances
	form = UserAdminChangeForm
	add_form = UserAdminCreationForm

	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('email',)

	list_filter = ('staff',)

	fieldsets = (
		('Login info', {'fields': ('email', 'password',)}),
		('Personal info', {'fields': ('avatar',)}),
		('Permissions', {'fields': ('staff','is_superuser',)}),
	)
	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2')}
		),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()




