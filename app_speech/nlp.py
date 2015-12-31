import subprocess, re
import os, platform

def tokenize(string):
    return ' '.join(list(x.lower() for x in \
                         re.findall(r'[A-Za-z0-9\']+',
                                    string)))

def score_sclite(hyp, ref):
    _ref = tokenize(ref)
    _hyp = tokenize(hyp)
    #print (hyp)
    #print ("poo")
    #print ("Hypothesis" + str (_hyp))

    with open("ref.ref", 'w') as f:
      f .write(_ref + " (a)\n")
    with open("hyp.hyp", 'w') as f:
      f .write(_hyp + " (a)\n")

    # platform-dependent shell command
    #sclite_windows = ["sclitewin/sclite"]
    sclite_windows = ["sclite"]
    sclite_macosx = ["sclitemac/sclite"]
    sclite_linux = ["sclitelin/sclite"]
    cmd_args = ["-i", "spu_id",
                "-o", "pralign",
                "-r", "ref.ref",
                "-h", "hyp.hyp",
                "-n", "test"]
    if platform.system() == "Windows":
        cmd = sclite_windows + cmd_args
    elif platform.system() == "Darwin":
        cmd = sclite_macosx + cmd_args
    elif platform.system() == "Linux":
        cmd = sclite_linux + cmd_args
    else:
        return None

    subprocess.call(cmd)

    results = {}

    with open("test.pra", 'r') as f:
        text = f.readlines ()
    numbers = text[11][22:].split(" ")
    results['num'] = {'correct': numbers[0],
                      'substitutions': numbers[1],
                      'deletions': numbers [2],
                      'insertions': numbers [3]}
    results['ref'] = text[12][6:].strip()
    results['hyp'] = text[13][6:].strip()
    #print(results)
    denominator = int(results['num']['correct']) + \
        int(results['num']['substitutions']) + \
        int(results['num']['deletions'])
    results['accuracy'] = str(100 * float (results['num']['correct'])\
                              / (denominator))[:4]
    os.remove("ref.ref")
    os.remove("hyp.hyp")
    os.remove("test.pra")
    return results
