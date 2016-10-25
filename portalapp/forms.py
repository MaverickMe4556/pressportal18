from django import forms
#from django.contrib.admin.widgets import AdminDateTimeWidget
from django.contrib.admin import widgets
from .models import Register
from django.forms import DateTimeField
# from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
from datetime import datetime
from django.forms.fields import DateTimeField
from django.forms.extras.widgets import SelectDateWidget
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from datetimewidget.widgets import DateTimeWidget

class TalkForm(forms.ModelForm):
          #on_date=forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'],default=datetime.now)
          coordinator = forms.CharField(label='Faculty Coordinator')
          bio = forms.CharField(label='Bio of the speaker', widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
          #on_date = forms.DateTimeField(label='Date And Time')

          #on_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"))
          class Meta:
              model = Register
              dateTimeOptions = {'format': 'dd/mm/yyyy HH:ii P','autoclose': 'true','showMeridian' : 'true'}
              widgets = {'date_and_time': DateTimeWidget(options = dateTimeOptions, bootstrap_version=3)}
              fields = ('topic', 'speaker','date_and_time','venue','abstract','bio','coordinator','image',)

