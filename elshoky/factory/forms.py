from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import *
from django.core.exceptions import NON_FIELD_ERRORS


class MakersForm(ModelForm):
    headline = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text='Use puns liberally',
    )
    content = models.TextField()

    class Meta:
        model = Maker
        fields = '__all__'

        labels = {
            'name_maker': _('Writer'),
        }
        help_texts = {
            'name_maker': _('Enter Your name')
        }
        error_messages = {
            'name': {
                'name_maker': _("This writer's name is too long ")
            }
        }

class ModelsForm(ModelForm):
    class Meta:
        model = Model
        exclude = ['machine']

        labels = {
            'name' : _('Model')
        }
        help_texts ={
            'name' : _('enter the name of Model')
        }

        error_masseges ={
            'name' :{
                'name' : _('this is too long')
            }
        }
