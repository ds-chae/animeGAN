import os

with open("tags.txt") as f:
    content = f.readlines()
os.chdir('animepics')
for c in content:
    #print(c)
    cmdstr = '..\\gallery-dl.exe --range 1-1000 "https://danbooru.donmai.us/posts?tags=' + c.split()[0] + '"'
    print(cmdstr)
    os.system(cmdstr)
































































