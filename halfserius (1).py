purple = 0
green = 0
yellow = 0
hunger = 0
health = 100
day = 1
monstercare = 100
saves = [None] * 11
# purple is enasni, green is lamron, yellow is bmud
def slrmenu():
    print("You somehow had an ending. Now, you get the chance to restart.")
    slr = input("{Restart}\t{Load}\t{Exit}\n")
    if slr == "Restart":
        restart()
    elif slr == "Load":
        load()
    elif slr == "Exit":
        print("Very well.\nENDING: COULDN'T TAKE THE PRESSURE")
        exit()
    else:
        print("I literally gave you easier choices and you're still messing around. I made a save menu for you and you don't care? Fine! I won't stop the program! Sit here in uncomfortable silence.")
def save():
    global purple, green, yellow, hunger, health, day, monstercare, saves
    print("\n")
    saves[day] = [
        green,
        purple,
        yellow,
        monstercare,
        health,
        hunger,
        day
    ]

def load():
    global purple, green, yellow, hunger, health, day, monstercare, saves
    print("Type days 2-10 or I'll be mad.")
    day = int(input("What day are you loading?\n"))
    
    if day < 2 or day > 10:
        print("That is not what I told you.")
        return
    elif saves[day] is None:
        print("You didn't play that day yet.")
        restart()
    else:
        green, purple, yellow, monstercare, health, hunger, day = saves[day]
        print("Loaded.")
def restart():
    global purple, green, yellow, hunger, health, day, monstercare, saves
    saves = [None] * 11
    print("You restarted.")
    day = 1
    purple = 0
    green = 0
    yellow = 0
    hunger = 0
    health = 100
    monstercare = 100

def day6if3():
    global purple, green, yellow, hunger, health, day, monstercare, saves
    print("You wake up the next day. You slept a lot better. You realise your only roommates ate your earlier roommate and realise how bad all this looks. You get a headache.")
    headache = input("{take a pill}\t{sleep it off}\t{ignore it}\n")
    if headache == "take a pill":
        print("You went to your drug cabinet. As you opened it, you saw everything was expired. You have two options... Go to the pharmacy or try these.")
        pharmacy = input("{pharmacy}\t{try these}\n")
        if pharmacy == "pharmacy":
            print("placeholder")
    elif headache == "sleep it off":
        print("You can't sleep. It gets worse because you think even more.")
        return
    elif headache == "ignore it":
        print("It gets impossible to ignore and everything starts spinning.")
    else:
        print("nope")
        exit()
def day6if0():
    global purple, green, yellow, hunger, health, day, monstercare, saves
    print("The monsters are still trying to kill you.")
def day6if1():
    global purple, green, yellow, hunger, health, day, monstercare, saves
    print("The monsters see you but don't really care.")
def day6if2():
    global purple, green, yellow, hunger, health, day, monstercare, saves
    print("The monsters are obsessed!")
def day6ify():
    print("You wake up after an unidentified amount of time. The basement is dimly lit. The cookies had a weird aftertaste and you fell asleep almost instantly after eating them.\nYou decide it's just the sugar teen love thing. The narrator can't take your idiotism and cuts in: Are you such a moron that you don't know what sugar... ugh.\nYou don't really know what that was about. Anyway, you keep on eating the cookies.\nYour brain the size of a peanut that's basically polished to perfection manages to get the 1.5 braincells working and gives you an idea.")
    dumbass1 = input("{drool}\t{quote brainrots}\t{try to run}\t{think}\n")
    if dumbass1 == "drool":
        print("You drool over the chains and your saliva makes them dissolve. Probably from every sleeping pill that's in your body right now. Or the teen love sugar thing. You don't have enough brainpower to care.\nYou see a weird looking chair with a red sign and some white letters on it. It's probably nothing.")
        drooled1 = input("{sit}\t{red bad}\n")
        if drooled1 == "sit":
            print("You sit on the chair and push a button. You feel tickles and your 1 braincell gets electrocuted, leaving you with 0.5.")
        elif drooled1 == "red bad":
            print("Apparently one thing in your mind stayed intact - fear of red. That decision unlocks the next level of evolution and you can read again. Mostly. You see a danger sign.\nIt was a good choice.")
    elif dumbass1 == "quote brainrots":
        for i in range(100):
            print("burn in hell.")
        print("You have personally insulted me, the developer, and every being in this multiverse. You, filthy creature, you do not deserve having an electronic device anymore. Burn in hell.")
        print("You do not have enough dignity to witness the load reset exit menu. You little ipad kid timmy, your mom should never give you her phone. You're not funny, nor cool. I could fry your stinky iphone right now.\nENDING: YOU DO NOT DESERVE TO ROAM THIS WORLD")
        exit()
def day5():
    global purple, green, yellow, hunger, health, day, monstercare, saves
    print("Day 5... Congrats on getting through yesterday. I'm guessing it's not your first attempt. It got pretty dark, didn't it? Well. Since no one wanted more days, I'll make them.")
    # This one will make you feel weird because it will be super goofy! So you will feel like something bad's gonna come!") - originally a print, but decided better not to
    print("You are at your house. Or something similiar to it. Anyway, you're in a place very similiar to your house.")
    if yellow >= 7:
        print("The monsters are a little concerned because of all the questionable choices you made. They're wondering if you should be sent to get supervision.\nThe monsters speak to you like to a kid. They are getting more and more worried, since you tried to drink gasoline you found lying around. They try to calm you down.")
        ihnifana1 = input("{GRR}\t{im not that dumb}\t{SQUIRREL}\n")
        # i have no idea for a name anymore. ihnifana1 is staying
        if ihnifana1 == "GRR":
            yellow += 3
            print("YoU snArLeD aT thEm! They decide it's best to send you back to grandma. She welcomed you and had to restrain you in the basement, but still fed you cookies and tea.")
            day6ify()
        elif ihnifana1 == "im not that dumb":
            green += 1
            yellow -= 1
            print("'th@at 1Iis a R3elief.' The monsters calmed down a little, but were still a bit worried about you. And scared of you...\nThey still kick you out. There's no way they are gonna let you stay.")
            day6ify()
        elif ihnifana1 == "SQUIRREL":
            print("the hell you want from me? im not gonna rap if that's what you want. what do you want from the dev? can a person even be ginger without comments like- ah you're here for the rabies.\nok. i uh may have been carried away. heres your rabid ending i guess\nENDING: RABIES")
            slrmenu()
        else:
            print("when you pick a route just stay on it geez. maybe you did an idiot speedrun huh")
            exit()
    elif monstercare == 4 or purple > 7 and yellow < 6:
        print("Your friends care. They will let you go, but won't force you to do anything. You're one of them.")
        day += 1
        save()
    elif monstercare == 3 or (green > 4 and purple <= 4):
        print("'You should go... We want you to feel good.' The monsters look genuinely concerned. It's the first time they spoke like a human. I think they're trying to be as human as they can for you. Do you leave?")
        staygo3 = input("{stay}\t{go}\n")
        if staygo3 == "stay":
            print("Not an option. You get forced out of the paralell universe into your house and you realise your fridge is empty again.")
            print("You noticed the apples you buy often go missing. It's weird. Anyway, you just T-Pose the whole day since i have no idea for this line.")
            day6if3()
            save()
    elif monstercare == 1:
        print("The monsters are neutral. They will let you choose whether you go or stay.")
    elif monstercare == 0:
        print("The monsters want you gone or dead.")
    elif monstercare == 2:
        print("The monsters want you here forever. You're too important to let out! You are funny, cool, and their bestie! The outside is too dangerous.")
    else:
        print("CONGRATULATIONS! YOU GOT THE IMPOSSIBLE BUG ROUTE! for getting here i will reward you with a q&a. oops you clipped into the backrooms bye ending seeker. also youre here because you made the most plain character ever\n3ND1NG: B@CKR00MS")
        restart()
def day4():
    global purple, green, yellow, hunger, health, day, monstercare, saves
    print("It's day 4. You woke up back at your house. You probably sleepwalked.")
    if purple < 5:
        print("The monsters are upset with you.")
        choice6 = input("{RUN}\t{STAY}\t{COME AT THEM}\n")
        if choice6 == "RUN":
            green += 2
            print("The doors and windows are stuck. The chimney too. Except you don't have a chimney. All of it's covered in something black.")
            if yellow > 3:
                print("It seems sticky. Touch it?")
                touch1 = input("{yes}\t{no}\n")
                if touch1 == "yes":
                    print("You got stuck in it. You managed to get out, but it took the whole day.")
                    yellow += 2
                    day += 1
                    save()
                elif touch1 == "no":
                    print("Probably a good idea... You sit there. Just... sit. You dont get food and eventually dont wanna do anything. You become the next meal.\nENDING: EATEN c")
                    slrmenu()
            else:
                print("You realise it's not your house. It's really weird. It looks like it's trying to mimic it.\nDid the monsters... Kidnap you? They explain it's a parallel universe they made for you. You realise you can't run away. Do you befriend the monsters or deny them?\n")
                denyfriend1 = input("{Befriend}\t{Deny}\n")
                if denyfriend1 == "Befriend":
                    print("The monsters tell you to cut this crap. When they kidnapped you you're suddenly a friend, huh? Not believable. You become their toy.\nENDING: TOYED")
                    slrmenu()
                elif denyfriend1 == "Deny":
                    print("The monsters thought about this, but still were a little surprised. You showed you stand your ground and don't change just to save yourself. They say they will let you go tomorrow.")
                    day += 1
        elif choice6 == "STAY":
            print("The monsters... did not expect this. They don't accept you. You hear whispers everywhere.\nYou find a small opening in the black thing.")
            runstay1 = input("{Run}\t{Stay}\n")
            if runstay1 == "Run":
                print("You try to. You get stuck. You get closed in a cocoon.\nENDING: HYBERNATING a")
                slrmenu()
            elif runstay1 == "Stay":
                print("You fall asleep. You don't wake up, consumed by the black ooze.\nENDING: HYBERNATING b")
                slrmenu()
        elif choice6 == "COME AT THEM":
            yellow += 2
            print("You do a wimpy slap. The monsters look shocked and laugh. They decide you're funny.\nThey like you. So they won't let you leave...")
            day += 1
            monstercare = 2
            save()

    elif purple >= 8:
        print("The monsters greeted you happily. Your house feels... different, though. You try to open the door, but it's blocked by the monsters' ooze.\nThe monsters come up to you and say you're too fun to let out.")
        mtu1 = input("{PANIC}\t{society is worse}\n")
        if mtu1 == "PANIC":
            print("Party pooper. The monsters felt decieved and used you as a prop in their escape room. So tragic, you can't warn anyone anymore...\nENDING: PROPPED")
            exit()
        elif mtu1 == "society is worse":
            print("You decided being here with the monsters is better than living like a normal person.\nDays pass and you fall deeper into insanity. The monsters start getting concerned and let you out to seek help.\nThere you are again, on the street, because your besties kicked you out. How could they?! You did EVERYTHING to be friends, you were cool, you were fun, you killed too... AND NOW THEY KICK YOU OUT?!\n")
            choice8 = input("{Be upset}\t{Understand}\n")
            if choice8 == "Be upset":
                purple += 10
                print("YES! HOW CAN THEY?! YOU FED THEM FOR MONTHS, YOU CARED! AND THEY?! YOU DECIDE THIS DEMANDS BLOOD. THEY LEFT YOU. YOU WILL GET REVENGE. YOU GATHER WEAPONS, KILL TO GET THEM, AND FINALLY GET TO YOUR HOUSE. YOU SHOOT THE GUNS. YOU BREAK EVERYTHING.\nBut... they caught you. They push you to the ground and take your hard earned toys. They tell you to calm down.\nYOU DON'T. YOU CAN'T. YOU STRUGGLE AGAINST THEIR GRIP. FINALLY, THE POLICE COME. YOU SCREAM YOUR HEART OUT. THE POLICE INVESTIGATE YOU AND TAKE YOU AWAY. EVERYTHING AFTER THAT IS LIKE... a fever dream. You don't know whats right or wrong, who cares?\nYou take every opportunity to go crazy. They close you in an asylum.")
                print("One day, you start spiraling. What did you do... You broke everything, no wonder they hate you. ENDING: very dark turn that i need to mark in the trigger warnings")
                exit()
            elif choice8 == "Understand":
                print("No... They care. You're the bad one here. You would go get help, but it's too expensive... You try to think more... normally. And calling them monsters seems bad now. They're friends, but you're not one of them. You are a human that should take killing and cannibalism as a bad thing. But... Does that make your friends bad? They cared about you. But humanity sees them as bad.\nWho should you believe...\n")
                choice9 = input("{humans?}\t{friends?}\n")
                if choice9 == "humans?":
                    print("You're human. You should believe humans. You go to the police station to explain the situation. Turns out there is free help. One day, after going to therapy for a long time, you see one of your friends carrying groceries. The not human friends. You got your life together, they said.\n")
                    #Should i end here, future me?
                    print("\nENDING: THERAPY IS WORTH IT!")
                    slrmenu()
                elif choice9 == "friends?":
                    print("They are the ones that helped you. You go over to your house, and say what you feel. They show you something. They started eating apples! That's partly the reason your groceries went missing a lot, but they were working to become more human. You realise how ironic this is - You became a monster, they became a human. You decide to meet halfway.")
                    monstercare = 4
                    print("They encourage you to go to a human therapist. But... You don't want to yet.")
                    day += 1
                    save()
    else:
        print("How the hell did you get here... The monsters are neutral with you. They let you go or stay.")
        staygo1 = input("{Stay}\t{Go}\n")
        if staygo1 == "Stay":
            print("You decided staying with the monsters is cool. You live like them, with them, and slowly start feeling as one of them.\n")
            if green > 3 and yellow < 6:
                print("You feel weird about it. You fall into anxiety, jumping at every whisper. You don't feel good about this.")
                print("You tell that to the monster therapist and they say you can go away if you feel so bad. They won't chase you.")
                print("They treat you as their equal. That means you deserve freedom.")
                staygo2 = input ("{Stay}\t{Go}\n")
                if staygo2 == "Stay":
                    print("Your anxiety gets bigger and bigger, followed by an existential crisis. Are you human? Monster? Dead? Fake?\nHard to tell. They start noticing. They are worried.")
                    day += 1
                    monstercare = 3
                    save()
                elif staygo2 == "Go":
                    print("a placeholder")
                    day += 1
                    green += 2
                    save()
            else:
                print("You like living like this. You feel at home. You slowly see your body becoming like the monsters'. It's good. After months, you are officialy one of them! You realise your family isn't as bad as humanity says.\nThey don't kill to kill. That's their way to eat. Being scary, psychotic... That's a habit around humans. Humans are actually worse than them. Not just from your perspective.\nYour family isn't toxic. They tolerate every gender, every hobby, don't have the internet.\nENDING: ONE OF THEM (sane)")
                slrmenu()

def day3():
    global purple, green, yellow, hunger, health, day, monstercare, saves
    print("You had a dream today. You don't remember it though.\nYour room stinks of a dead body. You decide to check...")
    choice4 = input("{the wardrobe}\t{under the bed}\t{HELL NAH}\n")
    if choice4 == "the wardrobe":
        print("You opened the wardrobe and an anime girl knocked you out. You didn't wake up.")
        print("ENDING: WAIFU'D")
        slrmenu()
    elif choice4 == "under the bed":
        print("Ah. You forgot to feed the monsters, and they took a snack themselves. You deducted the person is dead. You may be next.")
        print("Will you feed the monsters?")
        purple += 2
        feedmonsters1 = input("{yes}\t{no}\n")
        purple += 1
        if feedmonsters1 == "yes":
            print("With what?")
            feedingmon1 = input("{normal food}\t{a human}\n")
            if feedingmon1 == "normal food":
                print("The monsters didn't like it and they ate you.")
                print("ENDING: EATEN BY MONSTERS b")
                slrmenu()
            elif feedingmon1 == "a human":
                print("You fed them someone and they're happy.")
                day += 1
                if purple > 4:
                    print("You ate a little of that person too. The aftertaste was interesting. You talked with the monsters for a while and then went to their party. It lasted the whole night.")
                    save()
                else:
                    print("You hid under the blanket for a long time.")
                    save()
        elif feedmonsters1 == "no":
            print("They ate you.")
            print("ENDING: MONSTER EATEN a")
            slrmenu()
    elif choice4 == "HELL NAH":
        print("You ran away from home. You went...")
        green += 2
        runaway1 = input("{to the police station}\t{to a friend's house}\t{to grandma}\t{screw it.}\n")
        if runaway1 == "to grandma":
            print("Grandma welcomed you with opened arms to stay the night. She fed you too many cookies though.")
            hunger -= 20
            health -= 15
            day += 1
            save()
        elif runaway1 == "to the police station":
            print("You told the cops you smelled blood in your room. They reluctantly went to check it and they found nothing.\nThe monsters will probably be upset...")
            day += 1
            green += 4
            save()
        elif runaway1 == "to a friend's house":
            print("Very funny. Maybe the imaginary one. You lay on the street.")
            yellow += 2
            day += 1
            save()
            hunger += 10
            if yellow > 2:
                print("You could always sleep in a store like in those cool videos...")
                choice5 = input("{yes}\t{no}\n")
                if choice5 == "yes":
                    print("You managed to hide in an IKEA. The employees saw you but decided your life is sad enough.")
                    save()
                elif choice5 == "no":
                    print("You sleep on the street. For 2 minutes. You go there anyway.")
                    print("You managed to hide in an IKEA. The employees saw you but decided your life is sad enough.")
                    save()

        elif runaway1 == "screw it.":
            print("You become homeless but your begging is very ineffective. You starve.")
            print("ENDING: HOMELESS                                                                                                                                                                                                                                                                                                                                                                                ")
            exit()
        

def day2():
    global purple, green, yellow, hunger, health, day, monstercare, saves
    print("The first day passes.\nYou wake up to the familiar feeling of being broke.\nYou should go shopping today.\n")
    choice2 = input("{go shopping}\t{starve}\t{steal food}\n")
    if choice2 == "go shopping":
        print("You went shopping. You bought some normal things for the money you had.")
        green += 1
        print("You bought 2 apples, some ramen and a bun.")
        day += 1
        if hunger > 10:
            print("You need to eat something. What will you eat?")
            choice3 = input("{the apples}\t{ramen}\t{the bun}\n")
            if choice3 == "the apples":
                hunger -= 4
                print("It was good, but you're still a little hungry.")
                save()
            elif choice3 == "ramen":
                hunger -= 8
                print("That hit the spot.")
                save()
            elif choice3 == "the bun":
                hunger -= 5
                print("Tasted decent.")
                save()
    elif choice2 == "starve":
        print("You are starving.\n")
        starving1 = input("{eat}\t{don't eat}\n")
        if starving1 == "eat":
            print("You ate something. You spent the whole day lying in your bed, exhausted.")
            day += 1
            purple += 1
            save()
        elif starving1 == "don't eat":
            print("You starved.")
            print("ENDING: STARVED")
            hunger += 100
            slrmenu()
        else:
            print("stop trolling/being a dumbass")
            exit()
    elif choice2 == "steal food":
        print("From where?")
        yellow += 1
        stealing1 = input("{neighbour}\t{grandma}\t{cat}\n")
        if stealing1 == "cat":
            print("You stole a cat's food bowl. It striked you with lightning. Never mess with cats.")
            print("ENDING: CAT STRIKED")
            #you dare to mess with God? no restart 4 u
            yellow += 100000000000000000000000000000000000000000
            exit()
        elif stealing1 == "neighbour":
            print("The neighbour caught you. You went to prison.")
            print("ENDING: PRISON a")
            slrmenu()
        elif stealing1 == "grandma":
            print("You are evil. Grandma fed you anyway and insisted you stay for tea.")
            day += 1
            hunger -= 2
            save()
        else:
            print("pfft. you shouldve stolen")
            exit()
    else:
        print("no cheating today")
        exit()

def start():
    global purple, green, yellow, hunger, health, day, monstercare, saves
    print("You wake up to the smell of the trash next to your bed. You haven't cleaned your room since 1885.")
    print("As per usual, you ignore this to go downstairs and check your fridge for food.")
    print("Inside, you find a note from your mom that's been sitting there for 2 years. It's a block of ice.")
    print("The only other thing you have there is ice cream that was frozen and unfrozen 14 times already.")
    print("You decide to eat...")
    choice = input("{the ice cream}\t{the note}\t{none}\n")
    if choice == "the ice cream":
        print("You ate the ice cream.")
        print("You got diarrhoea. The first day flies by on the toilet.")
        yellow += 1
        day += 1
        hunger -= 3
        save()
    elif choice == "the note":
        print("You ate the note")
        print("It tasted like a freezer. The paper was ok though.\nYou spent the whole day trying to eat it.")
        purple += 1
        hunger -= 1
        day += 1
        save()
    elif choice == "none":
        print("You decide it's best if you don't eat.")
        print("You're hungry.")
        green += 1
        hunger += 10
        greenhunger1 = input("{eat something from the fridge}\t{wait until tomorrow}\n")
        if greenhunger1 == "eat something from the fridge":
            print("The day passed normally.")
            day += 1
            hunger -= 2
            save()
        elif greenhunger1 == "wait until tomorrow":
            print("You didn't eat anything and decided to buy food tomorrow. You lie on the couch the whole day.")
            day += 1
            hunger += 5
            save()
        else:
            print("no")
            exit()
    elif choice == "chair":
        print("yum. It took a long time to eat though.")
        day += 1
        purple += 4
        hunger -= 1
        save()
    elif choice == "qwertyuiop":
        print("congrats a skip. you ate your keyboard and the shift button fell off thats why im typing in lowercase. h3v n0vv j can7 sL3ak! 0kav jm g3771ng vs3d 2 7h1s. 1dj07! J vv0n7 g1v3 v m3nv!\n3NDJNG: C0M3 0N! DVMBASS")
        day = 5
        exit()
    else:
        print("either youre trolling or stupid")
        exit()

while True:
    if day == 1:
        start()
    elif day == 2:
        day2()
    elif day == 3:
        day3()
    elif day == 4:
        day4()
    elif day == 5:
        day5()
    else:
        print("not yet")
        break
# easier to copy: slrmenu()
#save()
#this is illegal. i mean you.
