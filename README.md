# Criptare XOR ASC 0x00 UB

Programul realizează criptare/decriptare XOR, cheia permutându-se circular de fiecare dată când se termina de xorat toate caracterele acesteia.

Cerința: https://cs.unibuc.ro/~crusu/asc/Arhitectura%20Sistemelor%20de%20Calcul%20(ASC)%20-%20Proiect%200x00.pdf

Textul criptat este luat din "Enigma Otiliei", de George Călinescu.

Am întampinat câteva probleme la decriptarea fișierului binar, nu toate caracterele erau decriptate corect, insa folosind documentația, am reușit să scriem corect fisierul binar, transformând caracterele în bytes.

Comenzile de rulare ale programului sunt:

```
python encrypt.py <cheie> <input file> <output file>
```

si

```
python decrypt.py <cheie> <output> <input_recuperat file>
```

În folderul `hack` se află soluțiile de spargere a parolei.

Proiect realizat de:

[Rosu Vlad-Andrei](github.com/vlandero), 151

[Benescu Ioan](https://github.com/BetJohn), 151

[Gheorghe Radu-Mihai](https://github.com/radugheo), 151
