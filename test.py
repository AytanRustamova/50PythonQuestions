flist = []
for i in range(3):
    flist.append(lambda: i)

[f() for f in flist]

print(flist)

