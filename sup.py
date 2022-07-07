import re
def manipilationOfFiles():
    lp = open(r'info.txt')
    for line in lp:
        f = open("info.txt","r+")
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != f"{line}":
                f.write(i)
        f.truncate()
        f.close()
        r = open("done.txt", 'a')
        r.write(f"{line}")
        break
