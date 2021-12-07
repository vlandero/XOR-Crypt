# Hack parola

## Subtask 1:

Este o soluție simplă, se xorează fiecare caracter din output cu fiecare caracter din input. Astfel, se obține un text format din cheia de criptare care se repeta.

## Subtask 2:

Soluția noastră se bazează pe presupunerea că cel mai frecvent caracter în text este `space`.

**O descriere intuitivă a soluției ar fi următoarea**: se calculează frecvența caracterelor din fișierul output, iar celui mai frecvent caracter binar îi va corespunde caracterul `space`. Se xorează apoi acestea două și se obține un posibil caracter al parolei. Deci, vrem să facem un dicționar de frecvență. Una din probleme este că nu putem face un singur dicționar de frecvență pentru tot textul din output, pentru că un caracter din output putea fi tradus ca mai multe caractere din textul original, fiind obținut prin xorarea cu caractere diferite din cheie (se poate întâmpla ca a^b=c, dar și d^e=c). De aceea trebuie să creăm mai multe dicționare, „cu caractere din `n` în `n`”, pentru a lua în calcul doar frecvențele caracterelor xorate cu _același caracter_ din cheie. În `d[k]` vom avea dicționarul de frecvență pentru toate caracterele de pe pozițiile `i` din output, pentru care `i % n = k`, unde `n` este numărul de caractere ale cheii.

Pentru o lungime `n` a cheii cu care a fost criptat textul, programul creează un vector `d[]` de `n` dicționare de frecvență ale caracterelor din outputul de decriptat. Pentru fiecare poziție `i` de la `0` la `n-1`, în `d[i][text[key]]` reținem frecvența caracterului `text[key]` din fisierul output, unde `key` merge din `n` în `n` începând de la poziția `i`, iar `text` este textul din fișierul output. Prin presupunerea făcută, intuim că cea mai mare frecvență dintr-un dicționar `d[i]` corespunde caracterului `space` în textul original. Deci, xorând `frecvMax` cu `32`, obținem un posibil caracter de pe poziția `i` a cheii. (`frecvMax` este codul ascii al caracterului pentru care `d[i][frecvMax]` este maximul din dicționarul `d[i]`, iar `32` este codul ascii al caracterului `space`).

Încercăm tehnica descrisă pentru `n` în intervalul `[10,15]`, și verific pentru ce `n` obțin "the most likely password". În caz că nu obțin o astfel de parolă, decriptăm textul din output cu cheile obținute și vedem când textul se apropie cel mai mult de limba română. Dacă sunt doar câteva caractere care nu se potrivesc, știm măcar că am aflat lungimea cheii. În acest caz, pentru unele dicționare, nu a fost `space` cel mai frecvent caracter, așa că ne uităm în dicționar la următoarele frecvențe în ordine descrescătoare pentru a găsi `space` (acest caracter este sigur unul dintre cele mai folosite).

În programul `frequency.py` am creat și dicționarul de frecvență pentru literele dintr-un text în limba română, pentru a ne face o idee despre frecvența caracterelor.

În `freq_my_text.txt` avem frecvența caracterelor dintr-un text în limba română, sub formă de procente.

În `frequency.txt` avem cele `n` dicționare descrise mai sus și este de forma: `cod ascii`: `frecvența în procente`.

Cu `hack.py` am testat să vedem dacă obținem textul decriptat corect cu cheia găsită.

Cheia echipei adverse este **EllaElias151**, se află în `decrypted.txt`.
