#python zipCrack.py -f evil.zip -d dict.txt
import zipfile
from threading import Thread
import optparse

def extractFile(zFile,password):
    try:
        zFile.extractall(pwd = password)
        print "[+] Password is " + password + '\n'
    except Exception, e:
        pass

def main():
    parser = optparse.OptionParser("usage %prog " +\
    "-f <ZipFile> -d <Dictionary file>")

    parser.add_option('-f', dest='zname',type='string',\
    help='Specify ZipFile')

    parser.add_option('-d', dest='dname',type='string',\
    help='Specify Dictionary file')

    (option,args)=parser.parse_args()
    if (option.zname == None) | (option.dname == None):
        print parser.usage
    else:
        zname = option.zname
        dname = option.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target = extractFile, args = (zFile,password))
        t.start()

if __name__ == "__main__":
    main()
