
import os

def main():
    while True:
        print("Das Spiel beginnt")



        def Henris_Spiel():
            print("Es ist Montag morgen")
            print("Du stehst vor der Schule. Möchtest du hineingehen? (ja/nein)")
            
            choice = input("> ").strip().lower()
            
            if choice == "ja":
                print("Du betrittst die Schule und stehst vor einem Treppenhaus. Gehst du hoch oder runter? (hoch/runter)")
                treppe = input("> ").strip().lower()
                
                if treppe == "hoch":
                    print("Oben stehst du vor zwei Türen mit der Nummer 1 und 2. Durch welche gehst du?  (1/2)")

                    door = input("> ").strip().lower()

                    if door == "1":

     
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

                    elif door == "2":
                        print ("Hinter der Tür steht Herr Niedorf und macht einen Überraschungstest.")
                        print ("Erste Frage: Ist E.Coli Grammnegativ oder Grammpositiv?.  (negativ/positiv)")

                        gramm = input("> ").strip().lower()

                        if gramm == "positiv":
                            print ("Falsch sie sind Doppelsträngig du bekommst eine 6.")
                            print ("Game Over!")

                        elif gramm == "negativ":
                            print ("Richtig!")
                            print ("Zweite Frage: Kann E.Coli Sporen bilden? (ja/nein)")

                            spore = input("> ").strip().lower()

                            if spore == "ja":
                                print ("Falsch sie bilden keine Sporen du bekommst eine 5")
                                print ("Game Over!")

                            elif spore == "nein":
                                print ("Richtig!")
                                print ("Letzte Frage: Sind Plasmide a)Einsträngig oder b)Doppelsträngig (a/b)")

                                plasmid = input("> ").strip().lower()

                                if plasmid == "a":
                                    print ("Falsch sie sind Doppelsträngig du bekommst eine 4.")
                                    print ("Game Over!")

                                elif plasmid == "b":
                                    print ("Richtig!")
                                    print ("Du bekommst eine 1 und einen Ausbildungsplatzt an dem Ort deiner Wahl.")
                                    print ("Du hast gewonnen!")
                            


                
                    
                    
                elif treppe == "runter":
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
    

        
        input("Drücke Enter, um das Spiel neu zu starten")
        os.system('cls' if os.name == 'nt' else 'clear')
if __name__ == "__main__":
    main()



    
