from django import forms
from dashboard import models


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = models.Files
        fields = ('file_link', 'id_issue',)


