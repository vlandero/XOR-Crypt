fin = open("output", 'rb')
freq = open("frequency.txt", "w")
decrypt = open("decrypted.txt", "w")
myText = open("my_text.txt", "r")
myFreq = open("freq_my_text.txt", "w")
lg_key = 12
d = [{} for _ in range(lg_key)]
letter_freq = {}
total_litere = [0] * lg_key
ch = fin.read(1)
i = 0
while ch != b"":
    if i == lg_key:
        i = 0
    try:
        d[i][ord(ch)] += 1
    except:
        d[i][ord(ch)] = 1
    total_litere[i] += 1
    ch = fin.read(1)
    i += 1
for i in range(lg_key):
    first = 1
    freq.write(f"Litera {i}:\n")
    for key, value in sorted(d[i].items(), key=lambda x: x[1], reverse=True):
        letter_freq[key] = round(value/total_litere[i], 4)
        freq.write(f"{key}: {letter_freq[key]}\n")
        if first == 1:
            decrypt.write(chr(key ^ 32))
            first = 0
    freq.write("\n")
d = {}
total_litere = 0
ch = myText.read(1)
while ch != "":
    try:
        d[ch] += 1
    except:
        d[ch] = 1
    total_litere += 1
    ch = myText.read(1)
letter_freq = {}
for key, value in sorted(d.items(), key=lambda x: x[1], reverse=True):
    letter_freq[key] = round(value/total_litere, 4)
    myFreq.write(f"{key}: {letter_freq[key]}\n")
fin.close()
freq.close()
decrypt.close()
myText.close()
myFreq.close()
