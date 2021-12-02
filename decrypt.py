import sys
key = sys.argv[1]
cnt_key = 0
n = len(key)
inputFile = sys.argv[2]
outputFile = sys.argv[3]
fin = open(inputFile, "rb")
fout = open(outputFile, 'w')
litera = fin.read(1)
while litera != b"":
    ascii_litera = ord(litera)
    if cnt_key == n:
        cnt_key = 0
        key = key[-1] + key[:n-1]
    ascii_litera_key = ord(key[cnt_key])
    fout.write(chr(ascii_litera ^ ascii_litera_key))
    litera = fin.read(1)
    cnt_key += 1
