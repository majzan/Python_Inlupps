"""
Memory Game

Detta är ett minnesspel där spelaren kan välja att memorera en sekvens av siffror eller bokstäver.
Spelet genererar en slumpmässig sekvens och visar den i 5 sekunder. Spelaren ska sedan försöka
återskapa sekvensen.

Hur man kör koden:
1. Kör scriptet i en Python-miljö. py memory_NumChar.py.py
2. Välj längden på sekvensen eller tryck Enter för default längden (8 siffror/tecken).
3. Välj om du vill spela med siffror eller bokstäver.
4. Memorera den visade sekvensen innan terminalen rensas och sekvensen försvinner.
5. Försök ange sekvensen korrekt ordning, max 15 försök.

Om spelaren gissar rätt avslutas spelet, annars får de en hint om hur många tecken som var rätt.
Om 15 försök görs utan korrekt svar avslutas spelet och den rätta sekvensen visas.
För att avbryta exekvering av spelet, tryck Ctrl+C.

"""
# Importera moduler
import random
import time
import string

# Funktioner

# Funktionen generate_sequence() genererar en slumpmässig sekvens av siffror eller bokstäver
def generate_sequence(length, mode):
    """Genererar en slumpmässig sekvens av siffror eller bokstäver."""
    if mode == "siffror":
        return [str(random.randint(0, 9)) for _ in range(length)]
    elif mode == "bokstäver":
        return [random.choice(string.ascii_uppercase) for _ in range(length)]

# Funktionen clear_screen() rensar skärmen genom att skriva ut många nya rader för att dölja sekvensen.
def clear_screen():
    """Rensar skärmen genom att skriva ut många nya rader för att dölja sekvensen."""
    print("\n" * 50)

# Funktionen count_correct_positions() räknar antalet tecken i gissningen som är på rätt plats.
def count_correct_positions(original, guess):
    """Räknar hur många tecken i gissningen som är på rätt plats."""
    return sum(1 for o, g in zip(original, guess) if o == g)

#   Funktionen count_correct_elements() räknar antalet tecken i gissningen som finns
def count_correct_elements(original, guess):
    """Räknar hur många av tecknen i gissningen som finns i sekvensen men kan vara på fel plats."""
    return sum(1 for g in guess if g in original)

# Funktionen get_user_input() hämtar användarens inmatning och returnerar standardvärde om inmatning inte fungerar.
def get_user_input(prompt, default_value):
    """Hämtar användarens inmatning, returnerar standardvärde om `input()` inte fungerar."""
    try:
        return input(prompt).strip()
    except OSError:
        print("Inmatning fungerar inte i denna miljö. Använder standardvärde.")
        return default_value

# Funktionen play_memory_game() är huvudfunktionen som kör spelet.
def play_memory_game():
    """Huvudfunktionen som kör spelet."""
    try:
        sequence_length = get_user_input("Hur lång ska sekvensen vara? (Tryck Enter för 8): ", "8")
        sequence_length = int(sequence_length) if sequence_length else 8
    except ValueError:
        print("Ogiltig inmatning, standardvärde 8 används.")
        sequence_length = 8
    
    # Fråga spelaren om de vill spela med siffror eller bokstäver
    while True:
        mode = get_user_input("Vill du spela med siffror eller bokstäver? (siffror/bokstäver): ", "siffror").lower()
        if mode in ["siffror", "bokstäver"]:
            break
        print("Ogiltigt val. Vänligen skriv 'siffror' eller 'bokstäver'.")
    
    # Generera en slumpmässig sekvens baserat på spelarens val
    original_sequence = generate_sequence(sequence_length, mode)
    
    print("Memorera denna sekvens:", " ".join(original_sequence))
    time.sleep(5)  # Vänta i 5 sekunder
    clear_screen()
    
    attempts = 0
    max_attempts = 15
    # Spelarens gissning
    while attempts < max_attempts:
        # Spelaren matar in sin gissning
        guess = get_user_input(f"Försök {attempts + 1}/{max_attempts}: Ange sekvensen: ", "").upper()
        guess_list = guess.split()  # Delar upp inmatningen i en lista baserat på mellanslag
        # Kontrollera att gissningen har rätt längd
        if len(guess_list) != sequence_length:
            print(f"Din gissning måste innehålla {sequence_length} tecken separerade med mellanslag.")
            continue
        
        # Kontrollera hur många gissade tecken som är på rätt plats 
        correct_positions = count_correct_positions(original_sequence, guess_list)
        # Kontrollera hur många gissade tecken som finns med i sekvensen
        correct_elements = count_correct_elements(original_sequence, guess_list)
        
        if correct_positions == sequence_length:
            print("Grattis! Du gissade rätt!")
            break
        else:
            print(f"Du hade {correct_positions} tecken på rätt plats och {correct_elements} som fanns med i sekvensen.")
            attempts += 1
    else:
        # Om max antal försök har uppnåtts
        print("Tyvärr, du har gjort 15 försök. Spelet är över.")
        print("Den korrekta sekvensen var:", " ".join(original_sequence))

if __name__ == "__main__":
    play_memory_game()