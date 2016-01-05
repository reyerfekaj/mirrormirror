from django import forms

class TranscriptForm(forms.Form):
    transcript = forms.CharField(label='', widget=\
                                 forms.Textarea(attrs={'cols':72, 'rows':9}))

class UploadForm(forms.Form):
    file = forms.FileField(
        label='Click "Choose File" to upload a txt file',
        )

class SpeechForm(forms.Form):
    reference = forms.CharField(label='', widget=\
                forms.Textarea(attrs={'style':'display: none'}))
    transcript = forms.CharField(label='', widget=\
                                 forms.Textarea(attrs={'cols':70, 'rows':10}))
