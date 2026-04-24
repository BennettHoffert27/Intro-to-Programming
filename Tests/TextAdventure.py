import time
import random 
def start_adventure():
    print("You are in your rocketship, having just entered the SX-2023 system. Welcome! What do you do next?")
    print("1. Begin travelling toward Intr-a, the First Planet")
    print("2. Begin travelling toward Dunia, the Third Planet")
    
    choice_of_planet = input("> ")

    if choice_of_planet == "1":
        travel_to_intra()
    elif choice_of_planet == "2":
        travel_to_dunia()
    else:
        print("Invalid choice. Try again.")
        start_adventure()


def travel_to_intra():
    print("You chart a course to Intr-a. 31 hours later, you arrive on Intr-a.")
    print("The rocketship door opens, and as the smoke clears, you see a large springtime village in the distance!")
    print("Your rocketship then spontaneously combusts, and YOU ARE STRANDED!")
    print("You:")
    print("1. Walk to the village")
    print("2. Explore the nearby forest")
    
    destination_choice = input("> ")

    if destination_choice == "1":
        walk_to_village()
    elif destination_choice == "2":
        explore_forest()
    else:
        print("Invalid choice. Try again.")
        travel_to_intra()

def explore_forest():
    print("You decide to wander the forest. You enter the forest, and you see a giant spider spinning a giant spider web. The spiderweb is changing shapes and colors, and you end up dancining endlessly because the spiderweb is also playing groovy dance music! The End!")

def walk_to_village():
    print("You walk to the village.")
    print("It takes you thirty  minutes.")
    print("When you arrive, three servant girls approach and ask you politely why you've come to the village.")
    print("You tell them that your ship has crashlanded and disappeared on this planet and that therefore you are a guest from Earth!")
    print("The servants are overjoyed to have a Earth guest on Intr-a! They skip away joyfully, cheering, and you decide to wander the village.")
    print("But as you look overhead, a giant soaring creature with wings speeds overhead! It's a giant predatory bird native to Intr-a!")
    print("What do you do next?")

    village_choice_1 = input("> ")

    if village_choice_1 == "1":
        chase_the_bird()
    elif village_choice_1 == "2":
        wander_the_village()
    else:
        print("Invalid choice. Try again.")
        walk_to_village()  


def wander_the_village():
    print("You decide to wander the village.")
    print("You spend 30 minutes simply walking around, untill suddenly you get bitten by a snake and become a zombie! Your adventure ends here, but know that you ended up destroying 58,000 new civiliations on Intr-a due to this event!")
def chase_the_bird():
    print("You run out of the village, and suddenly, you notice a storm in the distance. But then. a loud rumble occurs...")
    print("...and a long line of lightning surges toward you, and crashes into you, and you are illuminated!")
    time.sleep(3)
    print("After the flash clears, you are coursing with lightning, with the dazzling wings of a phoenix arching strongly from your shoulders! And yes, they are perpetually enflamed!")
    print("Your vision expands to 20/5, your hearing sharpens to the point of a needle, and your voice becomes shrill and thunderous!")
    print("On top of that, your nails sharpen ever so slightly.")
    print("The servant girls, meanwhile, look up and see you in the sky, and being dazzled by your appearance they all faint.")
    print("As they do, you let out an eagle's screech without even opening your mouth to do so!")
    print("After all of this, you turn around and spot the giant bird swooping away into the distance. But your speed is no match for it...")
    print("You launch into the sky, wings spread, and suddenly you fall forward like a flying bird, as you shoot through the air at phoenix speed, never mind how fast that is, flying after the bird!")
    time.sleep(4)
    print("Twenty minutes later, you land in a forest fifty miles outside the village.")
    print("You land, wings folding, and you spot the giant Intra-native bird in its nest... kicking a rock?!")
    print("It notices you, and as it stares at you, you have to make a decision. Do you run or do you stand your ground?")

    run_or_stand = input("> ")
    if run_or_stand == "1":
        you_stay_there()
    elif run_or_stand == "2":
        you_run_away()
    else:
        print("Invalid choice. Try again.")
        chase_the_bird()

    
def you_stay_there():
    print("You decide to stand your ground. The bird continues to stare at you, and then it leaves its nest and lands before you, completely still.")
    print("The fantastic creature then plucks out a feather and drops it, and the feather, somehow being as heavy as a bulldozer, plummets toward the ground... and a light blazes as you are teleported back to Earth!")
    print("And since this is the end of your adventure, you go and tell your friends. Oh, and you still have those wings on you, as well...")

def you_run_away():
    print("You decide to freak out and run away. Why not fly? Because that would be cheating. Either way, the bird launches from the ground and darts after you, because it knows something you don't...")
    print("You are running toward a decently-sized regiment of the advancing Fifteenth Army!")
    print("Five soldiers storm toward you. What do you do? Fight ot flee?")

    fight_or_flight = input("> ")
    if fight_or_flight == "1":
        fight()
    elif fight_or_flight == "2":
        flee()
    else:
        print("Invalid choice. Try again.")
        you_run_away()


def flee():
    print("You decide you don't want to face an army. You fly away, back to the village. There is no certainty of a mild public shaming from the community.")
    print("When you get back to the village, you are greeted by all of the citizens... currently standing at the gate. They ask you whether you want to be a part of their community...")
    print("... or whether you want to use their Chamber Well to be teleported back to Earth.")
    print("What do you decide?")

    teleport_or_naturalize = input("> ")
    if teleport_or_naturalize == "1":
        teleport_to_earth()
    elif teleport_or_naturalize == "2":
        become_a_village_citizen()
    else:
        print("Invalid choice. Try again.")
        flee()


def teleport_to_earth():
    print("You ask to be teleported back to Earth. Your request is granted.")
    print("They lead you to the only Chamber Well on Intr-a.")
    print("Thirty minutes later. you step inside the lake of blue you see in front of you, and you disintegrate from the world and re-appear... on mars?! Yes. And you wander that planet for 32 years and then vanish.")

def fight():
    print("You advance toward these soldiers. The feather then clones you into 4 people all like you, and these 4 people destroy the 5 soldiers easily.")
    print("You then merge back into 1 whole person. But there are more soldiers ahead! Suddenly, you hear the bird's scream as it flies over you and lands right as you climb on.")
    print("The bird takes off with a screech that shook the trees, and you now have nothing to worry about.")
    print("The bird easily scatters the soldiers with its respiratory-induced flames, and your flaming wings strike fear in their oblivious hearts. They all run away, wailing. You, sir, have defeated the regiment. Congratulations!")
    print("The bird then lands, and it stands still before you once again. What do you do? Do you attempt to fully tame this creature, or do you fight it to neutralization?!")
    tame_or_fight = input("> ")
    if tame_or_fight == "1":
        tame_the_bird()
    elif tame_or_fight == "2":
        fight_the_bird()
    else:
        print("Invalid choice. Try again.")
        fight()

def tame_the_bird():
    print("You decide to fully tame this creature. It seems to be fine with you anyway.")
    print("So now you have to find an animal to neutralize...")
    time.sleep(3)
    food = random.randint(1,4)
    if food == 1:
        print("You succesfully hunted a rabbit!")
    elif food == 2:
        print("You succesfully hunted a deer!")
    elif food == 3:
        print("You sucessfully hunted a badger!")
    elif food == 4:
        print("You successfully hunted a squirrel!")
    print("You bring the animal back to the bird. The bird then scorches it with its flames, and you realize that it has now been tamed.")
    print("Moments later, you feel yourself being lifted up off the ground, but before you do, you suddenly turn into Max Headroom for 3 seconds, then become yourself again, and then teleport all the way to an abandoned church on the other side of Intr-a!")
    print("You stare at the church, and you decide to go inside. When you step inside, you end up being teleported back to your bedroom! The End!")

def fight_the_bird():
    print("You decide to go and fight the bird. But before you even touch it, the bird lowers its head and lifts you onto its back, and you are flown off to its nest!")
    print("Thirty minutes later, you end up in the bird's nest, and you finally discover that she is a mother bird!")
    print("You can either keep your distance or approach the fledgelings. What do you do?")
    stay_or_go = input("> ")
    if stay_or_go == "1":
        keep_your_distance()
    elif stay_or_go == "2":
        approach_the_fledgelings()
    else:
        print("Invalid choice. Try again.")
        fight_the_bird()
    
def keep_your_distance():
    print("You decide to keep your distance. When the birds see that you do not approach, they all lower their heads, as if they really do want interaction. What do you do now? Do you change your mind or do you refuse still?")
    change_your_mind = input("> ")
    if change_your_mind == "1":
        approach_the_fledgelings()
    else:
        keep_your_distance()




def approach_the_fledgelings():
    print("You decide to approach the fledgelings. The fledgelings stay still until you approach them... and when you are inches away, you recieve a soft prick of their beaks on your hands. Of course they wanted interaction! They're just fledgelings! It's not like they could actually deal damage.")
    print("But that flock of hawks in the sky swooping toward you certainly looks like it could!")
    print("But the mother bird hears their wingbeats before you do, and she blasts them out of the sky! You are saved!")
    print("The mother bird then walks toward you, sets you on her back again, and flies you back to the village.")
    print("When she drops you off at the village, she turns to leave, but you see her turn her head, and a tear is forming in her eye...")
    print("You then realize that she was banned from this village after her children accidently ruined a window! So you whistle back, and she turns around.")
    print("She then becomes joyful again, as she realizes that you are the Citizen of the Village and that you have invited her back to the village!")
    print("She runs toward you, and gives you a kiss on the face, and then you both run into the village joyfully!")
    print("TWO HOURS LATER")
    print("The bird begins to rebuild its nest as you tell your superior (yes, you do have a superior in this village) the whole story. He grins and laughs, and you live happily ever after. (And so does that mother bird - and her fledgelings!)")





def become_a_village_citizen():
    print("You elect to become a permanent naturalized citizen of this village!")
    print("All the people in your presence cheer, and they lead you to the election room, where another person they have previously considered - a prisoner from Nunze, the Fifth Planet - is waiting...")
    print("Twenty minutes later, you arrive at the election room at their town hall.")
    print("Then, everyone including you takes their seats in the church pews, and their signature citizenship process begins!")
    print("JUDGE: 'We are here today to vote on which citizen shall become naturalized today!'")
    print("Then, the judge rolls a die.")
    print("The die lands on an odd number, and you are instantly naturalized as a citizen in the village!")
    print("3 HOURS LATER")
    print("You are meeting in the town hall with the mayor of the village.")
    print("He asks you what you want to do. Do you want to name the village or do you want to simply demolish the old Town Hall building?")
    name_or_demolish = input("> ")
    if name_or_demolish == "1":
        name_the_village()
    elif name_or_demolish == "2":
        demolish_town_hall()
    else:
        print("Invalid choice. Try again.")
        become_a_village_citizen()
    
    def name_the_village():
        print("You decide to name the village. What do you name it?")
        village_name = input(" ")
        print("You name the village" + village_name + ".")
        print("The whole village cheers at your success, and your adventure ends here as you are now a permanent citizen of" + " " + village_name + "!")
    
    def demolish_town_hall():
        print("You decide to demolish town hall. The construction workers come in and...")
        print("3 DAYS LATER")
        print("The town hall is destroyed.")
        print("The people then rage and throw you into prison. Your adventure ends here!")




        
    



def travel_to_dunia():
    print("You chart a course to Dunia. It takes a day for you to get there.")
    print("Once you land, you see a clock shop with antique Dunian time pieces of all kinds! You like clocks so much. So you decide to enter.")
    print()
    print("Your first order of buisness is to talk to the owner of the shop. Do you ask for a clock or simply take a look around?")
    ask_or_not = input("> ")
    if ask_or_not == "1":
        ask_for_clock()
    elif ask_or_not == "2":
        take_look_around()
    else:
        print("Invalid choice. Try again.")
        travel_to_dunia()


def ask_for_clock():
    print("You decide to ask for a clock. He ends up giving you a Yttia and Daughers Co. clock straight from the polar regions of Dunia.")
    print("You take it and go. Meanwhile, a house magically appears, and you take it to your house and live happily ever after. That is, untill you become a third-person camera! And then you say: 'I AM A VIDEO CAMERA!'")
    print("The End!")


def take_look_around():
    print("You decide to take a look around. You end up standing in front of a grandfather clock... and it looks so creepy the floor opens and turns you into %^@&*(%^@(&%^&@%*^@#%(*^(@*$^%&@^$%&@^%(&)))))!")
    print("The End!")



start_adventure()