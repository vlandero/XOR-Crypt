fin = open("output", "rb")
fout = open("decrypted.txt", "w")
ch = fin.read(1)
key = "EllaElias151"
cnt = 0
while ch != b"":
    if cnt == len(key):
        cnt = 0
    fout.write(chr(ord(ch) ^ ord(key[cnt])))
    cnt += 1
    ch = fin.read(1)
