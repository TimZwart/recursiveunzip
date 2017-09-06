import os;
import subprocess;

print 'unzipping all .src.zip files'

for (dirpath, dirnames, filenames) in os.walk(folder):
    for filename in filenames:
        if filename.endswith(".src.zip"):
            filename_minuszip = filename[:-4]
            os.chdir(dirpath)
            if not os.path.isfile(filename_minuszip):
                subprocess.call('unzip '+filename+' -d '+filename_minuszip)
