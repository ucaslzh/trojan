import os
def run(**arg):
    print "[*]In dirlister module."
    files=os.listedir(".")
    return str(files)

