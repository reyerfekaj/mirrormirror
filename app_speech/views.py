from django.shortcuts import render
from .forms import TranscriptForm, UploadForm, SpeechForm
from .misc import read_file
from django.contrib.auth.decorators import login_required
import subprocess, re

# Create your views here.

@login_required
def speech(request):
    sform = SpeechForm()
    if request.method == 'POST':
        uform = UploadForm(request.POST, request.FILES)
        context = {'sform': sform}
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
    else:
        uform = TranscriptForm()
        context = {'uform': uform, 'sform': sform}
    return render(request, 'speech/speech.html', context)
        
@login_required
def transcript(request):
    tform = TranscriptForm()
    uform = UploadForm()
    context_data = {'tform': tform, 'uform': uform}
    return render(request, 'speech/transcript.html', context_data)

@login_required
def results(request):
    def tokenize (string):
        return ' ' .join (list (x .lower () for x in re .findall (r'[A-Za-z0-9\']+', string)))

    if request.method == 'POST':
        sform = SpeechForm(request.POST)
        if sform .is_valid ():
            hyp = sform.cleaned_data['transcript']
            ref = sform.cleaned_data['reference']
        else:
            hyp = ''
            ref = ''
    else:
        hyp = ''
        ref = ''

    _ref = tokenize (ref)
    _hyp = tokenize (hyp)

    with open ("ref.ref", 'w') as f:
      f .write (_ref + " (a)\n")
    with open ("hyp.hyp", 'w') as f:
      f .write (_hyp + " (a)\n")

    subprocess .call (["./sclite", "-i", "spu_id", "-o", "pralign", "-r", "ref.ref", "-h", "hyp.hyp", "-n", "test"])

    results = {}

    with open ("test.pra", 'r') as f:
        text = f .readlines ()
    numbers = text [11] [22:] .split (" ")
    results ['num'] = {'correct': numbers [0],
        'substitutions': numbers [1],
        'deletions':     numbers [2],
        'insertions':    numbers [3]
        }
    results ['ref'] = text [12] [6:] .strip ()
    results ['hyp'] = text [13] [6:] .strip ()
    print (results)
    denominator = int (results ['num'] ['correct']) + \
        int (results ['num'] ['substitutions']) + \
        int (results ['num'] ['deletions'])
    results ['accuracy'] = str (100 * float (results ['num'] ['correct'])\
        / (denominator)) [:4]
    subprocess .call (["rm", "ref.ref"])
    subprocess .call (["rm", "hyp.hyp"])
    subprocess .call (["rm", "test.pra"])

    return render (request, 'speech/results.html', results)
