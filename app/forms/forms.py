from django.forms import ModelForm
from app.models.models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['id', 'Name', 'Email']