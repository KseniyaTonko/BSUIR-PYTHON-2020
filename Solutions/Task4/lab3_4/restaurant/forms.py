from django.forms import ModelForm
from django.urls import reverse

from restaurant.models import Cook, Contact


class CookModelForm(ModelForm):
    class Meta:
        model = Cook
        fields = ['photo', 'first_name', 'last_name', 'position', 'dishes', 'date']
        labels = {'photo': 'Фото', 'first_name': 'Имя', 'last_name': 'Фамилия',
                  'position': 'Должность', 'dishes': 'Блюда, которые умеет готовить', 'data': 'Начало работы'}
        help_texts = {'photo': None, 'first_name': None, 'last_name': None, 'position': None,
                      'dishes': None, 'date': None}
        localized_fields = ['photo', 'first_name', 'last_name', 'position', 'dishes', 'date']

    def get_absolute_url(self):
        return reverse('cook-detail', args=[str(self.id)])  # cook-detail


class ContactModelForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        localized_fields = '__all__'
