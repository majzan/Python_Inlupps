import random
import os
import time

#   clear_screen() är en funktion som rensar terminalen 
def clear_screen():
    """Rensar terminalen."""
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()


#   generate_sequence() är en funktion som genererar en slumpmässig sekvens av siffror
def generate_sequence(length):
    """Genererar en slumpmässig sekvens av siffror."""
    sequence = []  # Skapa en tom lista för sekvensen
    for i in range(length):
        digit = random.randint(0, 9)  # Generera en slumpmässig siffra
        sequence.append(str(digit))   # Lägg till siffran i listan
    return sequence


#   count_correct_positions() är en funktion som räknar antal siffror på rätt plats
def count_correct_positions(random_sequence, guess):
    """Räknar antal siffror på rätt plats."""
    count = 0  # Räknare för rätt placerade siffror
    pos = 0  # Index för att gå igenom båda listorna
    while pos < len(random_sequence) and pos < len(guess):
        if random_sequence[pos] == guess[pos]:  # Jämför siffrorna på samma position
            count += 1  # Öka räknaren om siffrorna är lika
        pos += 1  # Gå till nästa position
    return count


# count_correct_numbers() är en funktion som räknar antal siffror som finns med i
def count_correct_numbers(random_sequence, guess):
    """Räknar antal siffror som finns med i sekvensen men kan vara på fel plats."""
    count = 0  # Räknare för siffror som finns i random_sequence
    for guess_digit in guess:
        if guess_digit in random_sequence:
            count += 1  # Öka räknaren om siffran finns i random_sequence
    return count


# play_memory_game() är en funktion som kör spelet där spelaren försöker memorera och återskapa en sekvens.
# Funktionen innehåller en loop som körs tills spelet är över. I loopen får spelaren först ange längden på sekvensen   
def play_memory_game():
    """Kör spelet där spelaren försöker memorera och återskapa en sekvens."""
    while True:
        try:
            sequence_length = input("Hur många siffror ska sekvensen ha? (Tryck Enter för 8): ").strip()
            if sequence_length:
                sequence_length = int(sequence_length)
            else:
                sequence_length = 8

            if sequence_length <= 0 or sequence_length > 8:
                print("Längden på sekvensen måste vara större än 0 och mindre än 9. Försök igen.")
                continue  # Återgå till inmatning om längden inte är korrekt
            break  # Avbryt loopen om en giltig längd har matats in

        except ValueError:
            print("Ogiltig inmatning, försök igen.")
    #   random_sequence är en lista som innehåller en slumpmässig sekvens av siffror
    random_sequence = generate_sequence(sequence_length)
    
    print("Memorera denna sekvens:", " ".join(random_sequence))
    time.sleep(5)  # Vänta i 5 sekunder
    clear_screen()
    
    attempts = 0
    max_attempts = 15
    
    # Loop för att låta spelaren gissa sekvensen
    while attempts < max_attempts:
        guess = input(f"Försök {attempts + 1}/{max_attempts}: Ange sekvensen: ").strip()
        guess_list = guess.split()  # Delar upp inmatningen i en lista baserat på mellanslag
        
        # Kontrollera att inmatningen är korrekt
        if len(guess_list) != sequence_length:
            print(f"Din gissning måste innehålla {sequence_length} siffror separerade med mellanslag.")
            continue
        
        correct_positions = count_correct_positions(random_sequence, guess_list)
        correct_numbers = count_correct_numbers(random_sequence, guess_list)
        
        # Om spelaren gissar rätt avslutas spelet
        if correct_positions == sequence_length:
            print("Grattis! Du gissade rätt!")
            break
        else:
            print(f"Du hade {correct_positions} siffror på rätt plats och {correct_numbers} som fanns med i sekvensen.")
            attempts += 1
    else:
        print("Tyvärr, du har gjort 15 försök. Spelet är över.")
        print("Den korrekta sekvensen var:", " ".join(random_sequence))


if __name__ == "__main__":
    play_memory_game()