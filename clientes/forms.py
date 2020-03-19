from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['frist_name', 'last_name', 'age', 'salary', 'bio', 'doc', 'photo']

