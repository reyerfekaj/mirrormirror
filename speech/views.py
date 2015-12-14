import subprocess, re
from django.shortcuts import render

form = "hello"

# Create your views here.
def speech_01(request):
    return render(request, 'speech/speech_01.html', {'form': form})

def results (request):
    ref = "We, the people of the United States, in order to form a more perfect Union"
    hyp = "when people in the United States in order to form a more perfect union"

    with open ("ref.ref", 'w') as f:
      f .write (ref + " (a)\n")
    with open ("hyp.hyp", 'w') as f:
      f .write (hyp + " (a)\n")

    subprocess .call (["evaluate/sclite/sclite", "-i", "spu_id", "-o", "pralign", "-r", "ref.ref", "-h", "hyp.hyp", "-n", "test"])

    results = {}

    with open ("test.pra", 'r') as f:
      text = f .readlines ()
      numbers = text [11] [22:] .split (" ")
      results ['num'] = {'correct':       numbers [0],
                         'substitutions': numbers [1],
                         'deletions':     numbers [2],
                         'insertions':    numbers [3]
                         }
      results ['ref'] = text [12] [6:] .strip ()
      results ['hyp'] = text [13] [6:] .strip ()
      results ['accuracy'] = str (100 * float (results ['num'] ['correct']) / \
        (int (results ['num'] ['correct']) + \
        int (results ['num'] ['substitutions']) + \
        int (results ['num'] ['deletions']))) [:4]

    return render (request, 'speech/results.html', {'results': results})