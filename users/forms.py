from django import forms
from django.contrib.auth import get_user_model

from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import SetPasswordForm

class CsRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CsRegisterForm, self).__init__(*args, **kwargs)

        self.fields['user_id'].label = '아이디'
        self.fields['user_id'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': False
        })
        self.fields['password1'].label = '비밀번호'
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = User
        fields = ['user_id', 'password1', 'password2', 'email', 'name']

    def save(self, commit=True):
        user = super(CsRegisterForm, self).save(commit=False)
        user.level = '2'
        user.department = '인증사용자'
        user.is_active = False
        user.save()

        return user


# 로그인 폼
class LoginForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', }),
        error_messages={
            'required': '아이디을 입력해주세요.'
        },
        max_length=32,
        label='아이디'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', }),
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        password = cleaned_data.get('password')

        if user_id and password:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                self.add_error('user_id', '아이디가 존재하지 않습니다.')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')



class RecoveryIdForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput,)
    email = forms.EmailField(widget=forms.EmailInput,)

    class Meta:
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super(RecoveryIdForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '이름'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_name',
        })
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_email'
        })



class RecoveryPwForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput,)
    name = forms.CharField(
        widget=forms.TextInput,)
    email = forms.EmailField(
        widget=forms.EmailInput,)

    class Meta:
        fields = ['user_id', 'name', 'email']

    def __init__(self, *args, **kwargs):
        super(RecoveryPwForm, self).__init__(*args, **kwargs)
        self.fields['user_id'].label = '아이디'
        self.fields['user_id'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_id',
        })
        self.fields['name'].label = '이름'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_name',
        })
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_email',
        })


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })


class CustomCsUserChangeForm(UserChangeForm):
    password = None

    name = forms.CharField(label='이름', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'8',}),
    )


    class Meta:
        model = get_user_model()
        fields = ['name']


# 비밀번호 변경 폼
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = '기존 비밀번호'
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': False,
            'style': 'margin-top:-15px;'
        })
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })

# 회원탈퇴 비밀번호확인 폼
class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control', }),
                               )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')