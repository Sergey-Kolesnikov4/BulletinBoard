from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Responses

class ResponsesFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='date_creation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Responses
        fields = {
            'ads': ['exact'],
            'status': ['exact']
         }

