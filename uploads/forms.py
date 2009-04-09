from django.forms.models import ModelForm

from uploads.models import File

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('name', 'file', 'download_key')
