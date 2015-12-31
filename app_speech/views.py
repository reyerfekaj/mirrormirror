from django.shortcuts import render, render_to_response
from .forms import TranscriptForm, UploadForm, SpeechForm
from .misc import read_file
from django.contrib.auth.decorators import login_required
from .nlp import score_sclite
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required
def speech(request):
    #sform = SpeechForm()
    if request.method == 'POST':
        uform = UploadForm(request.POST, request.FILES)
        #context = {'sform': sform}
        context = {}
        if uform.is_valid():
            #context['uform'] = read_file(request.FILES['file'])
            text = read_file(request.FILES['file'])
            if text == "NOT TXT":
                context['fileError'] = "Uploaded %s file is not of a supported\
 format, please use a txt file" % request.FILES['file'].name
            else:
                context['uform'] = text
        else:
            uform = TranscriptForm(request.POST)
            if uform.is_valid():
                transcript = uform.cleaned_data['transcript']
                context['uform'] = transcript
            else:
                context['textError'] = "Please type in or upload file with\
 your speech transcript"
        if 'uform' in context.keys():
            p = request.user.profile
            p.transcript = context['uform']
            p.save()
    else:
        uform = TranscriptForm()
        #context = {'uform': uform, 'sform': sform}
        context = {'uform': uform}
    return render(request, 'speech/speech.html', context)
        
@login_required
def transcript(request):
    tform = TranscriptForm()
    uform = UploadForm()
    context_data = {'tform': tform, 'uform': uform}
    return render(request, 'speech/transcript.html', context_data)

@login_required
def results(request):
    p = request.user.profile
    hyp = p.speech
    ref = p.transcript
    results = score_sclite(hyp, ref)
    if not results:
        return render_to_response('speech/results_none.html')
    p.feedback = results['accuracy']
    p.save()
    return render (request, 'speech/results.html', results)

@csrf_exempt
def get_speech(request):
    speech_text = str()
    if request.method == 'POST':
        if 'speech_text' in request.POST:
            speech_text = request.POST['speech_text']            
            # doSomething with speech_text here...
            #print(speech_text)
            #assign speech content to 'speech' field of the user profile
            print ("TESTTEST")
            print (speech_text)
            p = request.user.profile
            p.speech = speech_text
            p.save()
            return HttpResponse('success') # if everything is OK
    # nothing went well
    return HttpResponse('failure')
