# CONSTs:
PREFIX = "[>] "
O_RESPONSES = [
    "Wpisz S jeśli chcesz SZYFROWAĆ\n[>] Wpisz D jeśli chcesz DESZYFROWAĆ\n[>] Wpisz Z jeśli chcesz ZAMKNĄĆ program",
    "Huh? nie spodziewałem się tego... Wpisz S by szyfrować lub D by deszyfrować", 
    "Serio? spróbuj jeszcze raz ._.", 
    "Po prostu wpisz S lub D", 
    "Wierzę że dasz radę!!!",
    "Naprawdę w Ciebię wierzę",
    "Rany...",
    "CO JEST W TYM TRUDNEGO?",
    "PO PROSTU WPISZ S LUB D.",
    "AAAAAAAAAAAAAAAAAAAAAAAA",
    "Program przestał działać. Powód: Głupota użytkownika.",
    "Nastąpił problem warstwy 8.",
    "Dumny z siebie jesteś?",
    "Po prostu wpisz Z i daj mi spokój"
]
N_RESPONSES = [
    "Wpisz wartość przesunięcia:",
    "Tak, ale ta wartość musi być LICZBĄ",
    "CAŁKOWITĄ, pozwolę sobie dodać",
    "Czy ty mnie w ogóle słuchasz?",
    "MÓWIĘ CI, RANY. WPISZ TĄ LICZBĘ CAŁKOWITĄ.",
    "MOŻE TO BYĆ NAWET LICZBA UJEMNA IDC.",
    "AHGGGGGHGGHGHHGHG",   
    "Idź sobie.",
]
ALPHABET_LENGTH = 26
CAPITAL = set(range(65, 91))
SMALL = set(range(97, 123))

o = str()
while o != "Z":
# DECLARE & RESET VARs:
    o = str()
    tries = int()
    characterIDs = list()
    tekst1 = str()

# USER INPUT:
    while o not in ["D","S","Z"]:
        o = input(PREFIX + O_RESPONSES[tries] + "\n").upper()
        if tries < len(O_RESPONSES) - 1: tries += 1    
    if o == "Z": break;
    tries = 0

    tekst = input(PREFIX + "Wpisz swój tekst:\n")
    n = int()

    while not n:
        try: 
            n = int(input(PREFIX + N_RESPONSES[tries] + "\n"))
        except ValueError: 
            if tries < len(N_RESPONSES) - 1: tries += 1
    tries = 0

    if n > ALPHABET_LENGTH or n < -ALPHABET_LENGTH: n -= (n // 26)*26
    if o == "D": n *= -1 
    

# ENCRYPTION/DECRYPTION:
    for character in tekst:
        number = ord(character)

        encryptedNumber = int() 
        overflowNumber = int(ALPHABET_LENGTH * n/abs(n))

        if number not in [*CAPITAL,*SMALL]: encryptedNumber = number
        elif {number,number+n}.issubset(CAPITAL) or {number,number+n}.issubset(SMALL): encryptedNumber = number + n
        else: encryptedNumber = number + n - overflowNumber

        tekst1 += chr(encryptedNumber)

    print(PREFIX + "Twój tekst:\n" + tekst1 + "\n=-=-=")
    

