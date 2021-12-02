import sys
key = sys.argv[1]
cnt_key = 0
n = len(key)
fileName = sys.argv[2]
outputFile = sys.argv[3]
fin = open(fileName, "r")
fout = open(outputFile, 'wb')
x = fin.read(1)
while x != "":
    y = ord(x)  # ascii litera
    if cnt_key == n:
        cnt_key = 0
        key = key[-1] + key[:n-1]
    z = ord(key[cnt_key])  # ascii litera din key
    # transform in bytes inainte sa afisez in fisierul binar
    fout.write(bytes(chr(y ^ z), 'ascii'))
    # fout.write(bytes(x, 'ascii'))
    # t = bytes(chr(y ^ z), 'ascii')
    # pentru debug, daca se bloca criptarea, imi opream afisarea la
    # caracterul care nu avea codul ascii in [0,127]
    x = fin.read(1)
    cnt_key += 1
