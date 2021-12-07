f = open("input.txt", "r")
g = open("output", "rb")

parola = []

text_input = f.read()
text_output = g.read()

f.close()
g.close()

for i in range(len(text_input)):
    print( chr( ord(text_input[i]) ^ ord( chr(text_output[i])) ), end = "" )

