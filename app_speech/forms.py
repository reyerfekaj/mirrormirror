from django import forms

class TranscriptForm(forms.Form):
    transcript = forms.CharField(label='', widget=\
                                 forms.Textarea(attrs={'cols':100, 'rows':10}))

class UploadForm(forms.Form):
    file = forms.FileField(
        label='Click "Choose File" to upload a txt file',
        )
