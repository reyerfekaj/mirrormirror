from django.shortcuts import render

# Create your views here.
def speech_01(request):
    return render(request, 'speech/speech_01.html', {})
