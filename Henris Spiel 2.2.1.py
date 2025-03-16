import os
import random

def generate_random_choice():
    return random.randint(1, 2)

def handle_grazius_encounter():
    print("Hinter der Tür wartet Herr Grazius und starrt dich an. In welches Auge schaust du? (rechts/links)")
    auge = input("> ").strip().lower()
    
    if auge == "rechts":
        print("Du hast in sein starkes Auge geschaut und bekommst eine 1 Mündlich und keine Hausaufgaben")
    elif auge == "links":
        print("Du schaust in sein schwaches Auge und Grazius nimmt dich nicht wahr. Bleibst du still oder probierst du zu fliehen? (still/flucht)")
        plan = input("> ").strip().lower()
        
        if plan == "still":
            print("Grazius nimmt dich nicht wahr und geht nach kurzer Zeit in einen anderen Raum. Du konntest fliehen aber wurdest als abwesend für seine Stunde eingetragen")
        elif plan == "flucht":
            if generate_random_choice() == 1:
                print("Du wurdest nicht bemerkt und konntest fliehen doch du wurdest für den Rest des Tages als fehlend eingetragen.")
            else:
                print("Du wurdest von Grazius entdeckt und bekommst eine 6 Mündlich und Hausaufgaben. Game over")

def handle_niedorf_test():
    print("Hinter der Tür steht Herr Niedorf und macht einen Überraschungstest.")
    
    fragen = [
        ("Ist E.Coli Grammnegativ oder Grammpositiv? (negativ/positiv)", "negativ"),
        ("Kann E.Coli Sporen bilden? (ja/nein)", "nein"),
        ("Sind Plasmide a)Einsträngig oder b)Doppelsträngig (a/b)", "b")
    ]
    
    for frage, richtige_antwort in fragen:
        print(frage)
        antwort = input("> ").strip().lower()
        
        if antwort != richtige_antwort:
            print("Falsch! Game Over!")
            return
        print("Richtig!")
    
    print("Du bekommst eine 1 und einen Ausbildungsplatz an dem Ort deiner Wahl.")
    print("Du hast gewonnen!")

def handle_basement():
    print("Hinter der Tür befindet sich ein Flur mit zwei Türen auf welchen A und B steht. Welche wählst du? (a/b)")
    tür = input("> ").strip().lower()
    
    if tür == "a":
        print("Hinter der Tür steht Herr Jerx und fragt ob Nico schon wieder fehlt.")
        if generate_random_choice() == 1:
            print("Nico ist heute krank.")
            print("Herr Jerx regt sich wieder über Fehlzeiten auf und gibt Nico eine 6. Zusätzlich erzählt er für den Rest des Tages so lange Geschichten, dass du dich zu Tode langweilst. Game over!")
        else:
            print("Nico ist heute da")
            print("Herr Jerx ist gut gelaunt und telefoniert für den Rest des Tages")
    elif tür == "b":
        print("Hinter der Tür steht Frau Vollmer mit Kaffee und Kuchen. Du hast gewonnen :D")
        
def handle_tuerwahl():
    print("Du drehst dich um und siehst 5 Türen vor dir. Welche Tür wählst du? (1-5)")
    türwahl = input("> ").strip()
    
    match türwahl:
        case "1":
            print("Hinter der Tür ist ein Portal nach Hause. Da du dich nicht bei Niedorf abgemeldet hast bekommst du einen unentschuldigten Fehltag. Ende")
        case "2": 
            print("Hinter der Tür wartet der Hausmeister und schickt dich zurück in den Unterricht. Ende")
        case "3":
            print("Die Tür führt in den Schulhof. Du machst blau und bekommst einen Fehltag. Ende")
        case "4":
            print("Hinter der Tür ist der Schulleiter. Er ruft deine Eltern an. Ende")
        case "5":
            print("Die Tür führt in die Cafeteria. Du bleibst den Rest des Tages dort. Ende")
        case _:
            print("Diese Tür gibt es nicht. Du gehst verwirrt nach Hause. Ende")

def Henris_Spiel():
    print("Es ist Montag morgen")
    print("Du stehst vor der Schule. Möchtest du hineingehen? (ja/nein)")
    
    choice = input("> ").strip().lower()
    
    if choice == "ja":
        print("Du betrittst die Schule und stehst vor einem Treppenhaus. Gehst du hoch oder runter? (hoch/runter)")
        treppe = input("> ").strip().lower()
        
        if treppe == "hoch":
            print("Oben stehst du vor zwei Türen mit der Nummer 1 und 2. Durch welche gehst du? (1/2)")
            door = input("> ").strip().lower()
            
            if door == "1":
                handle_grazius_encounter()
            elif door == "2":
                handle_niedorf_test()
        elif treppe == "runter":
            handle_basement()
    elif choice == "nein":
        handle_tuerwahl()

def main():
    while True:
        print("Das Spiel beginnt")
        Henris_Spiel()
        input("Drücke Enter, um das Spiel neu zu starten")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()



    
