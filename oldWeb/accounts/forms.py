from django import forms
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from captcha.fields import CaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML
from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import filter_users_by_email
from allauth.account.models import EmailAddress
from allauth.account.forms import LoginForm

from .utils import benchmark
from .models import User
from . import settings


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomSignupForm(forms.ModelForm):
    CHOICES = [
        ('y', 'Yes'),
    ]
    i_agree = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=CHOICES
    )

    class Meta:
        model = User
        fields = [
            'fname',
            'lname',
            'email',
            'birthday',

        ]
        widgets = {
            'birthday': DateInput(),
        }
        required_css_class = 'required'
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            HTML(
                '<h2>Profile</h2>'
            ),
            Field('fname', placeholder="First name", autocomplete='given-name'),
            Field('lname', placeholder="Last name", autocomplete='family-name'),
            Field('birthday', autocomplete='bday'),
            HTML(
                '<br><br><h2>Account</h2>'
            ),
            Field('email', placeholder='Email address', autocomplete='email'),
            Field('password1', placeholder='Password', autocomplete='new-password'),
            Field('password2', placeholder='Password', autocomplete='new-password'),
            HTML(
                "{% if redirect_field_value %}"
                "<input type='hidden' name='{{ redirect_field_name }}'"
                " value='{{ redirect_field_value }}' />"
                "{% endif %}"
            ),
            HTML(
                '<br><br><h2>Preferences</h2>'
           
            HTML(
                "<h2>Terms and Privacy</h2><p>I agree to the <a href='{% url 'main:legal' %}'>Terms and Conditions</a> "
                "and <a href='{% url \'dashboard_data:home\' %}'>Privacy Policy</a>.</p>"
            ),
            'i_agree',
            'captcha',
            HTML(
                '<button class="btn btn-primary btn-block" type="submit">'
                '%s</button>' % _('Register')
            )
        )

    def signup(self, request, user):
        user.birthday = self.cleaned_data['birthday']
        user.fname = self.cleaned_data['fname']
        user.lname = self.cleaned_data['lname']


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            HTML(
                "{% if redirect_field_value %}"
                "<input type='hidden' name='{{ redirect_field_name }}'"
                " value='{{ redirect_field_value }}' />"
                "{% endif %}"
            )
        )
        self.helper.layout.append(
            HTML(
                '<button class="btn btn-primary btn-block" type="submit">'
                '%s</button>' % _('Sign In')
            )
        )
        self.helper.layout.append(
            HTML(
                "<div class='row'><a class='button secondaryAction btn btn-secondary btn-md col m-3' href={url1}>{text1}"
                "</a><a class='col button secondaryAction btn btn-secondary btn-md m-3' href={url2}>{text2}"
                "</a></div>".format(
                    url1=reverse('account_reset_password'),
                    text1=_('Forgot Password?'),
                    url2=reverse('account_signup'),
                    text2=_('Register'),
                )
            )
        )
        self.helper.form_class = 'blob bg-white w-75 mx-auto'

    def save(self):
        super().save()
        self.last_login = timezone.now()


class UserForm(forms.Form):

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)


