import sys
#!/usr/bin/env python3
import string
"""wcount.py: count words from an Internet file.

__author__ = "WuJinze"
__pkuid__  = "1700010643"
__email__  = "1700010643@pku.edu.cn"
"""
import sys
from urllib.request import urlopen
def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    '''a=[]
    for line in lines:
        word = line.strip()
        a.append(word)
    def histogram(s):
        d = dict()
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return d'''
    def process_line(lines,diction):
        lines = lines.replace('-',' ')
        for word in lines.split():
            word=word.strip(string.punctuation+string.whitespace)
            word.lower()
            diction[word]=diction.get(word,0)+1

    def process_file(lines):
        diction = {}
        process_line(lines,diction)
        return diction
    diction=process_file(lines)
    x=list(diction.values())
    x.sort()
    x.reverse()
    count = 0
    for i in range(topn):
        for key in list(diction.keys()):
            if diction[key]==x[i] and count<topn:
                print("%s %d"%(key,diction[key]))
                count +=1
                del diction[key]
    pass
'''fin = open('emma.txt')
wcount(fin,10)'''
#if __name__ == '__main__':
'''try:
    with urlopen('http://www.gutenberg.org/cache/epub/19033/pg19033.txt') as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, 10)
except Exception as err:
        print(err)
        sys.exit(1)'''
if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

try:
    with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
except Exception as err:
        print(err)
        sys.exit(1)

