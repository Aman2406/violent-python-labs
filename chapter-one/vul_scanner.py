import socket
import os
import sys

def ret_banner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def chck_vulnb(banner,filename):
    f = open('vul_banner.txt','r')
    for line in f.readline():
        if line.strip('\n') in banner:
            print '[+] Server is Vulnerable:' +\
                banner.strip('\n')

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print '[-]' + filename +\
             'Doesnot Excist'
            exit(0)
        if not os.access(filename,os.R_OK):
            print '[+]' + filename +\
             'Access Denied'
            exit(0)
    else:
        print "[-] Ussage " + str(sys.argv[0]) +\
            ' <Vuln filename>'
        exit(0)
        p_list = [21,22,25,80,110,443]
        for i in range(120,130):
            ip = '192.168.255' + str(i)
            for port in p_list:
                banner = ret_banner(ip,port)
                if banner:
                    print "[+]" + ip + ':' + banner
                    chck_vulnb(banner,filename)

if __name__ == '__main__':
    main()
