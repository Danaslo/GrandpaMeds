from Medication import Medication
import random
import time
import copy

class Game:

    def __init__(self):
        self.med_box = self.generate_med_box()
        self.pill_box = {
            "Monday": [], 
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": []
        }
        self.med_order = self.medication_order()

    def medication_order(self):
        med_order = copy.deepcopy(self.pill_box)
        for day in med_order.values():
            for i in range(random.randint(1,1)):
                med = self.med_box[random.randint(0, len(self.med_box) - 1)]
                day.append(f"{med.get_name()}")
        return med_order

    def generate_med_box(self):
        med_box = [
            Medication("Parazepazol", 2.5),
            Medication("Parazopazol", 1),
            Medication("Depiferina", 1.5),
            Medication("Dopiferina", 1),
            Medication("Zytrexol", 0.75),
            Medication("Zytrezol", 2),
            Medication("Flosilona", 1.2),
            Medication("Flosiluma", 2.3),
            Medication("Anxirolax", 1.8),
            Medication("Anxirolan", 1.9),
            Medication("Luminexor", 0.5),
            Medication("Luminexal", 1.7),
            Medication("Toxivarol", 2.1),
            Medication("Toxivalon", 0.9),
            Medication("Serafazol", 1.4),
            Medication("Serafalon", 2.2),
            Medication("Calmirex", 0.6),
            Medication("Calmiron", 2.6),
            Medication("Vibrasen", 1.0),
            Medication("Vibralon", 1.3)
        ]
        random.shuffle(med_box)
        return med_box

    def generate_med_report(self):
        report = ("Medical Report for Mr. Gory Oldman\n\n"
            f"Dear Mr. Oldman,\n"
            f"This medical report outlines the prescribed medications you need to take. It is essential that you take the following medications exactly as listed below. Please note that the specific dosage of each pill does not matter as long as you ensure to take the prescribed medication. The important factor is to focus on the name of each medication.\n"
            f"\nPrescribed Medications:"
        )
        
        for day in self.med_order:
            report = report + '\n' + day + ":\n"
            for meds in self.med_order.get(day):
                report = report + f" {meds}"      

        report = report + (f"\n\nPlease ensure that you take the correct medication by its name, and there is no need to worry about the individual dosage. If you have any questions regarding your medications or dosage, do not hesitate to contact your healthcare provider.\n"
            f"Sincerely,\n\n"
            f"Dr. Mario, Chief of Pill insertion at St. Mushroom Hospital"
        )

        with open("Doctor's report","w") as file:
            file.write(report)

    def pill_assigment(self):
        for day in self.med_order:
            print(f"Meds for {day}: \n")
            exit = False
            while not exit:
                print(f"What do you want to do?\n"
                      f"1. Add another pill\n"
                      f"2. Remove a pill\n"
                      f"3º Next day\n"
                )
                selection = input()
                match selection:
                    case "1":
                        pill = input("Which medicine do you want to add?: ")
                        self.pill_adding(day,pill)
                        print(f"{pill} added to {day}")
                    case "2":
                        pill = input("Which pill do you want to remove?: ")
                        done = self.pill_removal(day,pill)
                        if done:
                            print(f"{pill} removed from {day}")
                        else:
                            print(f"There is no {pill} inside {day}'s box")
                    case "3":
                        exit = True

    def pill_adding(self,day,pill): 
        self.pill_box.get(day).append(pill)
              
    def pill_removal(self,day,pill):
        done = True
        exists = pill in self.pill_box.get(day)   
        if exists:
            self.pill_box.get(day).remove(pill)  
        else:
            done= False
        return done
       
    def pill_comparison(self):
        correct = True
        day_failed = ''
        for day in self.pill_box:
            if sorted(self.pill_box[day]) != sorted(self.med_order.get(day, [])):
                day_failed = day
                correct = False
                break
        return (correct, day_failed)

    def game(self):
        print("You arrive at your grandfather's house. The smell of old wood and dusty carpets fills your lungs. As you step into the main hall, you find him sitting in his usual chair, watching a documentary about gazelles on his old TV.\n")
        time.sleep(5)
        print("When he finally notices you, he lets out a big sigh—he knows exactly why you're here.\n")
        time.sleep(5)
        print("'You just can’t let it go, can you?' he says, giving you a tired grin. Then, after a moment, he smirks.\n")
        time.sleep(5)
        print("'Alright, how about this? Let’s make it interesting. You organize my meds for the week, and I’ll take them exactly in the order you set. If nothing goes wrong, I’ll start taking them seriously from now on. But if something *does* go wrong… you’re gonna be hearing from me every day for a whole month!'\n")
        time.sleep(5)
        print("You're definitely not thrilled about gambling with your grandpa’s health, but you came here to make sure he takes his pills anyway. So, with confidence, you nod and accept the challenge.\n")
        time.sleep(5)
        print("'Here’s the list,' he says, handing you his doctor’s report.\n")
        self.generate_med_report()
        time.sleep(3)
        print("You take one look at the list and another at the chaotic box where he keeps all his pills. It’s a total mess! Everything’s mixed together, and some meds have almost the exact same names.\n")
        time.sleep(5)
        print("Fueled by both courage and the hope of avoiding a month of grandpa’s nagging, you grab the pill box and get to work.\n")
        time.sleep(5)
        self.pill_assigment()
        time.sleep(3)
        print("You finish the dreadful task with confidence, even throwing a smile at your grandpa—who doesn’t look too convinced.\n")
        time.sleep(5)
        print("He mumbles something you can’t quite hear, and after a while, you leave, hoping you did everything right.\n")
        time.sleep(5)
        print("Worried that you might’ve messed something up, you call your grandpa every day.\n")
        time.sleep(5)
        winner = self.pill_comparison()[0]
        if winner:
            print("Day after day, you call him, hoping he’s alright. From Monday to Saturday, all you get are the usual grunts.\n"
                "Then, finally, on Sunday, he picks up the phone and sighs.\n")
            time.sleep(5)
            print("'Okay, okay, you win... Honestly, I was kind of hoping something would go wrong just so I could complain, but… I’ve actually enjoyed your calls more than I’d like to admit. So thanks for putting up with me, and sorry for being such a grump.'\n")
            time.sleep(5)
            print("You feel a little weird—your family usually avoids him because of his rough personality, but now it seems like he’s just kind of lonely.\n")
            time.sleep(5)
            print("You tell him he *is* grumpy, but you appreciate his honesty and promise to visit more often. He lets out a sarcastic laugh.\n")
            time.sleep(5)
            print("'Well then, my dear nurse, I’ll be waiting for your next visit—and I’ll make sure to have some treats ready to thank you for your kindness and patience!'\n")
            time.sleep(5)
            print("Good ending: 'Master’s Degree in Sorting'")
        else:
            day_failed = self.pill_comparison()[1]
            print(f"When you call him on {day_failed}, it takes him way too long to answer. Worried, you rush to his house and find the door open—with one of his neighbors waiting outside.\n")
            time.sleep(5)
            print("She tells you your grandfather ran out of the house shouting your name before collapsing. The ambulance came quickly, and she tells you which hospital they took him to.\n"
                "Without a second thought, you rush over and find him in bed, smiling when he sees how worried you look.\n")
            time.sleep(5)
            print("'I guess I win!' he laughs, like this was all some kind of game. He pats your hand and shakes his head.\n"
                "'Don’t blame yourself. If I had taken my meds seriously, this wouldn’t have happened. It shouldn’t be your job to keep me alive.'\n")
            time.sleep(5)
            print("Noticing that his words aren't exactly comforting, he shouts, 'Ah, quit whining! Let’s just forget it, go back home, and eat some snacks!'\n")
            time.sleep(5)
            print("Even though he seems okay, you can’t shake the feeling that you should’ve paid more attention. Still, you go back to his house with him, share some chocolate, and leave with a sigh—knowing you messed up, but also that there’s still time to make it right.\n")
            time.sleep(5)
            print("Bad ending: 'Pilled Up'")
