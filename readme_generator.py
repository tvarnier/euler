import subprocess
import os
 
rootdir = '.'
for file in os.listdir(rootdir):
    d = file
    if os.path.isdir(d):
        if d[:4].isdigit():
            if not os.path.isfile("./" + d + "/README.md"):
                with open("./" + d + "/README.md", 'w') as f:
                    proc = subprocess.Popen(["curl", "https://projecteuler.net/minimal=" + d[:4]], stdout=subprocess.PIPE)
                    (out, err) = proc.communicate()
                    title = d[5:].replace("_", " ")
                    f.write("## " + title[0].upper() + title[1:] + "\n<br>\n" + out.decode("utf-8"))
                    f.close()
