def Henris_Spiel():
    print("Es ist Montag morgen")
    print("Du stehst vor der Schule. Möchtest du hineingehen? (ja/nein)")
    
    choice = input("> ").strip().lower()
    
    if choice == "ja":
        print("Du betrittst die Schule und siehst zwei Türen. Eine rote und eine blaue. Welche wählst du? (rot/blau)")
        door = input("> ").strip().lower()
        
        if door == "rot":
            print("Hinter der roten Tür wartet Herr Grazius und starrt dich an. In welches auge schaust du?  (rechts/links)")
            
            auge = input("> ").strip().lower()
        
            if auge == "rechts":
                print("Du hast in sein starkes Auge geschaut und bekommst eine 1 Mündlich und keine Hausaufgaben")
            
            elif auge == "links":
                print("Du schaust in sein schwaches Auge und Grazius nimmt dich nicht wahr. Bleibst du still oder probierst du zu fliehen?  (still/flucht)")
                plan = input("> ").strip().lower()
             
                if plan == "still":
                    print ("Grazius nimmt dich nicht wahr und geht nach kurzer Zeit in einen anderen Raum. Du konntest fliehen aber wurdest als abwesend für seine Stunde eingetragen")
            
                elif plan == "flucht":
                    import random

                    def generate_number():
                        return random.randint(1, 2)

                    zahl = generate_number()


                    if zahl == 1:
                        print("Du wurdest nicht bemerkt und konntest fliehen doch du wurdest für den rest des Tages als fehlend eingetragen.")
   
                    else:
                        print("Du wurdest von Grazius entdeckt und bekommst eine 6 Mündlich und Hausaufgaben. Game over")
    
            
            
        elif door == "blau":
            print("Hinter der Tür befindet sich ein Flur mit zwei Türen auf welchen A und B steht. Welche Wählst du?  (a/b)")
            tür = input("> ").strip().lower()
            
            if tür == "a":
                print ("Hinter der Tür steht Herr Jerx und fragt ob Nico schon wieder fehlt.")
                import random

                def generate_number():
                    return random.randint(1, 2)

                zahl = generate_number()


                if zahl == 1:
                    print("Nico ist heute krank.")
                    print ("Herr Jerx regt sich wieder über Fehlzeiten auf und gibt Nico eine 6. Zusätzlich erzählt er für den Rest des Tages so lange Geschichten, dass du dich zu Tode langweilst. Game over!")
                
   
                else:
                    print("Nico ist heute da")
                    print ("Herr Jerx ist gut gelaunt und Telefoniert für den rest des Tages")
                
                
               
            elif tür == "b":
                print ("Hinter der Tür steht Frau Vollmer mit Kaffe und Kuchen. Du hast gewonnen :D")
       
    elif choice == "nein":
        print("Du drehst dich um und gehst nach Hause. Da du dich nicht bei Niedorf abgemeldet hast bekommst du einen unentschuldigten Fehltag. Ende")


if __name__ == "__main__":
    Henris_Spiel()
    
import sys
import subprocess

def main():
    input("Drücke Enter, um das Spiel neu zu starten...")

    subprocess.call([sys.executable] + sys.argv)

main()

    
