from django.forms import ModelForm

from accounts.models import AccountModel


class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AccountForm(BaseForm):
    class Meta:
        model = AccountModel
        ordering = ['-id']
        exclude = ['date_created', 'creator']
