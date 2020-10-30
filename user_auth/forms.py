from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm, ChangePasswordForm, ResetPasswordKeyForm
from django import forms
from django.core.validators import MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User
from django.core.exceptions import ValidationError
import re


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'form-control'
        #     if visible.name == 'is_executor':
        #         visible.field.widget.attrs['style'] = 'display: none'
        #         visible.label = None


# class CustomLoginForm(LoginForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomLoginForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'
#             if visible.name == 'remember':
#                 visible.field.widget.attrs['class'] = 'custom-control-input'
#             # visible.label = None
#
#
# class CustomChangePasswordForm(ChangePasswordForm):
#     def __init__(self, *args, **kwargs):
#         super(ChangePasswordForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'
#             visible.label = None
#
#
# class CustomResetPasswordForm(ResetPasswordForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomResetPasswordForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'
#             visible.label = None
#
#
# class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomResetPasswordKeyForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'
#             visible.label = None