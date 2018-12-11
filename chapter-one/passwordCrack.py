import crypt


def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dict.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if cryptWord == cryptPass:
            print'[+] Password Found: ' + word + '\n'
            return

    print '[-] Password Not found \n'
    return


def main():
    passFile = open("password.txt")
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            print user
            cryptPass = line.split(':')[1].strip(' ')
            print"[*] Cracking Password for: " +user
            testPass(cryptPass)

if __name__ == "__main__":
    main()
