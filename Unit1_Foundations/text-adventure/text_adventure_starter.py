start = '''
You signed up to enroll in the Girls Who Code summer immersion program and got in! You were lucky enough to get
your first location in Emeryville. You will be spending the summer at Pixar!!!
Today is finally your first day at the program. You wake up, eat breakfast, and need to make the decision of how you're
going to get to the site. Will you take the BART or will you drive yourself?
'''

print(start)


print("Type 'bart' to take the BART or 'car' to drive yourself.")
user_input = input()
if user_input == "bart":
    print('''YOU DECIDE TO BART TO EMERVILLE! you wake up early and get dressed for your first day at Pixar. You head out the door on time and walk towards the bus station.
    You end up waiting for the bus for 30 minuetes! you finally get on the bus going towards the BART station. You look at your watch and realize you are running late. You
    rush down to the train and hop on! After the train gets to the first stop, you realize you got on the wrong train! you hop off the BART train as quickly as possible
    and look around. You have no idea which train to get on! Do you ask someone for help? or figure it out by yourself?''')
    print("Type 'ask someone for help' to ask someone for help or 'figure it out by yourself' to figure it out by yourself.")
    user_input = input()
    if user_input == "ask someone for help":
        print('''You decide to ask someone for help. You approach an old lady and ask her for directions. She gladly points you towards the train you should have boarded.
        Lucky for you, the train gets here in 2 min! you look at your watch and calculate that you will get to Pixar with 10 minuetes to spare. When you finally arrive at
        Pixar you have no idea where to go! You see the security guard sitting in the booth and a Pixar worker walking towards the gated entrance. Do you ask the security
        guard for help or follow the worker in?''')
        print("type 'ask the security guard' to ask the security guard for help or 'follow the worker in' to follow the worker into Pixar.")
        user_input= input()
    if user_input == "ask the security guard":
        print('''YOU ASK THE SECURITY GUARD FOR HELP! He asks you what your first & last name and for your ID. After you show him your ID, he finds you in the system
        and welcomes you to Pixar. He directs you to the Brooklyn building and buzzes open the door for you. CONGRATULATIONS YOU MADE IT TO Pixar!''')
    elif user_input == "follow the worker in":
        print('''YOU CREEP OUT THE Pixar WORKER! They stop at the gated door and turn around to ask who you are. Before you can even get a word out, the worker calls over
        the Pixar security guard and he asks you to leave. You FAILED at getting to your host site! GAME OVER!''')
    elif user_input == "figure it out by yourself":
        print('''You choose to figure it out by yourself and can't find the train map! you frantically run around trying to figure out which train to board.
        After 20  you finally find a map to direct you to the train you are supposed to board. Luckily the train gets there in 2 minuetes!
        However,you look at your watch and calculate that you will get to Pixar 10 minuetes late!When you finally arrive at Pixar you have no idea where to go!
        You see the security guard sitting in the booth and a Pixar worker walking towards the gated entrance. Do you ask the security guard for help or follow the worker in?''') # finished the story by writing what happens
        print("type 'ask the security guard' to ask the security guard for help or 'follow the worker in' to follow the worker into none.")
        user_input= input()
        if user_input == "ask the security guard":
            print('''YOU ASK THE SECURITY GUARD FOR HELP! He asks you what your first & last name and for your ID. After you show him your ID, he finds you in the system
            and welcomes you to Pixar. He directs you to the Brooklyn building and buzzes open the door for you. CONGRATULATIONS YOU MADE IT TO Pixar!''')
        elif user_input == "follow the worker in":
            print('''YOU CREEP OUT THE Pixar WORKER! They stop at the gated door and turn around to ask who you are. Before you can even get a word out, the worker calls over
            the Pixar security guard and he asks you to leave.You FAILED at getting to your host site! GAME OVER!''')

elif user_input == "car":
    print ('''You choose to DRIVE YOURSELF and get to the site early.
    However, all of the parking spaces are filled and you can't find any parking in the neighborhood either!
    You have two options here: You could either drive in and talk to the security guard about
    finding parking, or else park outside in any space that you can find.''')

print("Type 'drive in' to talk to the security guard or 'park outside' to look for a parking space outside.")
user_input = input()
if user_input == "drive in":
    print('''You choose to DRIVE IN and talk to the security guard.
    Uh oh! He's super mean and grouchy and obviously hasn't had his morning coffee yet.
    He tells you to buzz off and begins to chase you out of the gate. Do you run or fight him? ''')
    print("Type 'fight' to fight him or 'run' to run away or 'bribe' to bribe him with a cookie.")
    user_input = input()
    if user_input == "fight":
            print('''YOU LOST THE FIGHT! You couldn’t match the security guard’s strength!
            He throws you on the ground and puts you in a choke hold!
            After restraining you, he pages the police to have you arrested.''')
    if user_input == "run":
            print('''You FAILED at getting to your host site!
            YOU RUN AWAY! You start heading towards San Pablo Avenue and hop on the first bus out of here!''')
    if user_input == "bribe":
            print('''You bribe the security guard with a cookie and he lets you into Pixar in return!
            CONGRATULATIONS, YOU MADE IT TO YOUR HOST SITE!''')

    elif user_input == "park outside":
        print('''You choose to park outside.
        You find a parking space and take it, but it's designated for handicapped people.
        Oh no! A cop drives by and gives you a ticket.''')
        print('''You FAILED at getting to your host site!
        YOU GOT A TICKET! Oh no! Your parents are going to kill you!
        The Police officer also decides to impound your car.
        You call your mom and she begins yelling at you about your irresponsible tendencies.
        She rushes over to Pixar and picks you up to ground you!''')
 
