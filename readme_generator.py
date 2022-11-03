import subprocess
import os
 
rootdir = '.'
for file in os.listdir(rootdir):
    d = file
    if os.path.isdir(d):
        if d[:4].isdigit():
            with open("./" + d + "/README.md", 'w') as f:
                proc = subprocess.Popen(["curl", "https://projecteuler.net/minimal=" + d[:4]], stdout=subprocess.PIPE)
                (out, err) = proc.communicate()
                print(out.decode("utf-8"))
                f.write(out.decode("utf-8"))
                f.close()
