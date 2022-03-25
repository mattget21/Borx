'''
Created on Apr 19, 2021
'''
# Learned code for .lower() and .strip() from https://www.programiz.com/python-programming/methods/string/strip
# Code for the skull and cross-bones text art is from http://www.asciiworld.com/-Death-Co-.html
# Code for the sword text art is from https://www.asciiart.eu/weapons/swords
# Code for the crown text art is from https://www.asciiart.eu/clothing-and-accessories/crowns 
# Code for the dragon text art is from https://www.asciiart.eu/mythology/dragons
# Code for the small village text art is from https://www.asciiart.eu/buildings-and-places/cities

def adventureGame():
    def skull(a):
        if a== 1:
            print()
            print('                           uuuuuuu') 
            print('                      uu$$$$$$$$$$$uu')    
            print('                    uu$$$$$$$$$$$$$$$$$uu')
            print('                   u$$$$$$$$$$$$$$$$$$$$$u')
            print('                  u$$$$$$$$$$$$$$$$$$$$$$$u')
            print('                 u$$$$$$$$$$$$$$$$$$$$$$$$$u')
            print('                 u$$$$$$$$$$$$$$$$$$$$$$$$$u')
            print('                 u$$$$$$"   "$$$"   "$$$$$$u')
            print('                 "$$$$"      u$u       $$$$"')
            print('                  $$$u       u$u       u$$$')
            print('                  $$$u      u$$$u      u$$$')
            print('                   "$$$$uu$$$   $$$uu$$$$"')
            print('                    "$$$$$$$"   "$$$$$$$"')
            print('                      u$$$$$$$u$$$$$$$u')
            print('                       u$"$"$"$"$"$"$u')
            print('            uuu        $$u$ $ $ $ $u$$       uuu')
            print('           u$$$$        $$$$$u$u$u$$$       u$$$$')
            print('            $$$$$uu      "$$$$$$$$$"     uu$$$$$$')
            print('          u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$')
            print('          $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"')
            print('           """      ""$$$$$$$$$$$uu ""$"""')
            print('                     uuuu ""$$$$$$$$$$uuu')
            print('           u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$')
            print('          $$$$$$$$$$""""           ""$$$$$$$$$$$"')
            print('           "$$$$$"                      ""$$$$""')
            print('            $$$"                         $$$$"')
            print()
            print("          LETTUCE MOURN. ALL IS LOST. YOU ARE BEET. ")
            print()
            retry= input("Do you want to play again? (yes/no): ")
            if retry.lower().strip()== "yes":
                print()
                adventureGame()
            else:
                print("Game Over")
        elif a==2:
            print()
            print('                           uuuuuuu') 
            print('                      uu$$$$$$$$$$$uu')    
            print('                    uu$$$$$$$$$$$$$$$$$uu')
            print('                   u$$$$$$$$$$$$$$$$$$$$$u')
            print('                  u$$$$$$$$$$$$$$$$$$$$$$$u')
            print('                 u$$$$$$$$$$$$$$$$$$$$$$$$$u')
            print('                 u$$$$$$$$$$$$$$$$$$$$$$$$$u')
            print('                 u$$$$$$"   "$$$"   "$$$$$$u')
            print('                 "$$$$"      u$u       $$$$"')
            print('                  $$$u       u$u       u$$$')
            print('                  $$$u      u$$$u      u$$$')
            print('                   "$$$$uu$$$   $$$uu$$$$"')
            print('                    "$$$$$$$"   "$$$$$$$"')
            print('                      u$$$$$$$u$$$$$$$u')
            print('                       u$"$"$"$"$"$"$u')
            print('            uuu        $$u$ $ $ $ $u$$       uuu')
            print('           u$$$$        $$$$$u$u$u$$$       u$$$$')
            print('            $$$$$uu      "$$$$$$$$$"     uu$$$$$$')
            print('          u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$')
            print('          $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"')
            print('           """      ""$$$$$$$$$$$uu ""$"""')
            print('                     uuuu ""$$$$$$$$$$uuu')
            print('           u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$')
            print('          $$$$$$$$$$""""           ""$$$$$$$$$$$"')
            print('           "$$$$$"                      ""$$$$""')
            print('            $$$"                         $$$$"')
            print()
            print(" VERY WELL THEN, THIS QUEST IS NOT FOR THE FAINT OF HEARTICHOKES.")
            print()
            retry= input("Do you want to play now? (yes/no): ")
            if retry.lower().strip()== "yes":
                print()
                adventureGame()
            else:
                print("Game Over")
    print('Hello hero, your country has been cursed by the self-proclaimed "Evil Wizard of Borx" turning everyone living')
    print('within its borders into talking produce, 72 hours before they turn into complete vegtables. Luckily for you, you')
    print('were exiled years ago, making you exempt from its impact. The king has summoned you requesting that you find the')
    print('wizard and rid your homeland of its plague before its too late...') 
    a = input("Do you accept? (yes/no): ")
    if a.lower().strip()== "yes":
        print()
        print ("Very noble, you have chosen your people... May the odds fall in your favor.")
        print()
        options= ["a) Pickup a mushroom and keep moving", "b) Eat the mushrooms", "a) Stay", "b) Flee",
                  "a) Eat the radish","b) Take him to his lair", "c) Threaten to eat him, then take him to his lair",
                  "a) Throw the wizard at the Alpaca", "b) Flee", "c) Feed the mushroom you picked up to the Alpaca", 
                  "a) Return to your country where you will be hailed as a hero", "b) Accept the Wizard’s offer",
                  "c) Continue traveling helping all those who need a hero along the way","d) Disappear and start a new life in a different country"]
    #Level 1
        print('Onward! You must make it to Borx in two days to reverse the spell and you begin your quest walking through the woods')
        print('with a map and your sword. Eventually, you come across a field of mushrooms, you are very hungry and the nearest town')
        print('isn’t for miles… What do you do?')
        for i in range (0,2):
            print()
            print(options[i])
            print()
        choice= input("Your answer (a/b): ")
        if choice.lower().strip()== "a":
    #Level 2
            print()
            print("Good choice! You continue walking and find a cottage with an old couple who take you in for the night and feed you.")
            print()
            print('Later that night, you wake up and hear a conversation between the old couple and someone else. You find out that they')
            print('are working for the wizard, but they are not yet aware of your mission. Do you stay and listen or run off into the night?')
            for i in range (2,4):
                print()
                print(options[i])
                print()
            choice= input("Your answer (a/b): ")
            if choice.lower().strip()== "a":
        #Level 3
                print()
                print('They discuss how destructive the giant Alpaca (that your king set free last month) has been to their land and now to Borx.')
                print('The next day arrives and the still unsuspecting elderly couple sends you off with a Full Stomach. After a few miles of walking,')
                print('you open the “Full Stomach™” bag and find the Wizard! He has accidentally turned himself into a radish and fell into the bag')
                print('in his sleep! He offers to give you whatever you want if you take him back to his evil lair, he even pinky promises.')
                print('What do you do?')
                for i in range (4,7):
                    print()
                    print(options[i])
                    print()
                choice= input("Your answer (a/b/c): ")
                if choice.lower().strip() == "b" or choice.lower().strip()== "c":
        #Level 4
                    print()
                    print("You are on route to the Wizard's lair when you run into the giant Alpaca! You remember learning that the Alpaca")
                    print('has two weaknesses; Both radishes and mushrooms will cause it to shrink to normal Alpaca size if either is fed')
                    print('to the animal. What do you do?')
                    for i in range (7,10):
                        print()
                        print(options[i])
                        print()
                    choice= input("Your answer (a/b/c): ")
                    if choice.lower().strip()== "c":
        #Level 5
                        print()
                        print('Hurrah! The formerly giant Alpaca is now normal size and the Wizard is both impressed and grateful. After a few')
                        print('more miles, you reach his lair where the people of Borx have heard of your heroic act. The Wizard turns himself')
                        print('back into a person and you convince him to turn your people back into people. He then invites you to stay with him')
                        print('as the new “Duke of Borx” because of your bravery. What is your next move?')
                        for i in range (10,len(options)):
                            print()
                            print(options[i])
                            print()
                        choice= input("Your answer (a/b/c/d): ")
                        if choice.lower().strip()== "a":
                            print ("                           ___")
                            print ("                          ( ((")
                            print ("                           ) ))")
                            print ("  .::.                    / /(")
                            print (" 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._")
                            print ("(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>")
                            print (" `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''")
                            print ("  `::'                    \ \(")
                            print ("                           ) ))")
                            print ("                          (_((")
                            print()
                            print ("                         WELCOME HOME HERO, MISSION ACCOMPLISHED                    ")
                        elif choice.lower().strip()== "b":
                            print ('                                   $""$o')
                            print ('                                  $"  $$')
                            print ('                                   $$$$')
                            print ('                                   o "$o')
                            print ('                                  o"  "$')
                            print ('             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o')
                            print ('o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o')
                            print ('"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$')
                            print ('  ""o       o  $          $"       $$$$$       o          $  ooo     o""')
                            print ('     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"')
                            print ('      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $')
                            print ('        "" "$"     """""            ""$"            """      """ "')
                            print ('         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$')
                            print ('          "$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$')
                            print ('           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"')
                            print ('           $"""""""""""""""""""""""""""""""""""""""""""""""""""$')
                            print ('           $"                                                 "$')
                            print ('           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$')
                            print()
                            print ('              WELCOME TO BORX YOUR HIGHNESS, MISSION SUCCESS')
                        elif choice.lower().strip()== "c":
                            print ("              __ ")
                            print ("          _.-'.-'-.__")
                            print ("       .-'.       '-.'-._ __.--._")
                            print ("-..'\,-,/..-  _         .'   \   '----._")
                            print (" ). /_ _\. (  '.         '-  '/'-----._'-.__")
                            print ("'..'     '-r   _      .-.       '-._ \)")
                            print (" '.\. Y .).'       ( .'  .      .\          '\.")
                            print (" .-')'|'/'-.        \)    )      '',_      _.c_.\ ")
                            print ("   .<, ,>.          |   _/\        . ',   :   : \ ")
                            print ("  .' \_/ '.        /  .'   |          '.     .'  \)")
                            print ("                  / .-'    '-.        : \   _;   ||")
                            print ("                 / /    _     \_      '.'\ ' /   ||")
                            print ("                /.'   .'        \_      .|   \   \|")
                            print ("               / /   /      __.---'      '._  ;  ||")
                            print ("              /.'  _:-.____< ,_           '.\ \  ||")
                            print ("             // .-'     '-.__  '-'-\_      '.\/_ \|")
                            print ("            ( };====.===-==='        '.    .  \ : \ ")
                            print ("             \  '._        /          :   ,'   )\_ \ ")
                            print ("              \    '------/            \ .    /   )/")
                            print ("               \         _|             )Y    |   /")
                            print ("                \       \             .','   /  ,/")
                            print ("                 \     _/            /     _/")
                            print ("                  \    \           .'    .'")
                            print ("                   '| '1          /    .'")
                            print ("                     '. \        |:    /")
                            print ("                       \ |       /', .'")
                            print ("                        \(      ( ;z'")
                            print ("                         \:      \ '(_")
                            print ("                          \_,     '._ '-.___")
                            print ("                                      '-' -.\ ")
                            print()
                            print("    YOU'VE WON, BUT GET SOME REST.... A HERO'S WORK IS NEVER DONE")
                        elif choice.lower().strip()== "d":
                            print ("      ~         ~~          __")
                            print ("            _T      .,,.    ~--~ ^^")
                            print ("      ^^   // \                    ~")
                            print ("           ][O]    ^^      ,-~ ~")
                            print ("        /''-I_I         _II____")
                            print ("     __/_  /   \ ______/ ''   /'\_,__")
                            print ("       | II--'''' \,--:--..,_/,.-{ },")
                            print ("     ; '/__\,.--';|   |[] .-.| O{ _ }")
                            print ("     :' |  | []  -|   ''--:.;[,.'\,/")
                            print ("     '  |[]|,.--'' '',   ''-,.    |")
                            print ("       ..    ..-''    ;       ''. '")
                            print()
                            print ("  CONGRATULATIONS HERO, A NEW LIFE AWAITS")
                        else:
                            skull(1)
                    else:
                        skull(1)
                else:
                    skull(1)  
            else:
                skull(1)
            
        else:
            skull(1)
    else:
        skull(2)
        
adventureGame()
        