def read_file(f):
    #return f.read()
    if not f.name.endswith(".txt"):
        return "NOT TXT"
    else:
        dest = []
        for chunk in f.chunks():
            dest.append(chunk)
        return b''.join(dest).strip()
