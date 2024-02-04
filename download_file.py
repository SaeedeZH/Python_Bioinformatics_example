import os, urllib

urlbase = 'http://hplgit.github.com/bioinf-py/data/'
file = 'yeast_chr1.txt'
if not os.path.isfile(file):
    url = urlbase + file
    urllib.urlretrieve(url, filename= file)