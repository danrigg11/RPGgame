import atexit

def options():
    #print a main menu and commands
    print("RPG Game")
    print("=========")
    print("Options:")
    print("'options'")
    print("=========")
    print("Status:")
    print("'status'")
    print("=========")
    print("Commands:")
    print("'go [direction]'")

def status():
    #print players status
    print("----------------------")
    print("You are in the " + rooms[currentRoom]["name"])
    print("----------------------")
    

rooms = {
            1 : { "name"  : "Hall",
                  "east"  : 2,
                  "south" : 3}  ,
            
            2 : { "name" : "Bedroom",
                  "west"  : 1,
                  "south" : 4}  ,

            3 : { "name"  : "Kitchen",
                  "north" : 1}  ,
            
            4 : { "name" : "Bathroom",
                  "north" : 2,
                  "south" : 5}  ,

            5 : { "name" : "Escaperoom",
                  "north" : 4,
                  "west" : 6,
                  "east" : 7}  ,
            6 : { "name" : "Exit 1"}  ,
            7 : { "name" : "Exit 2"}  ,
            }
while 1:
    #start possition
    currentRoom = 1

    options()

    #loop
    while True:

        status()

        #get the player's next 'move'
        #.split() breaks it up into a list array
        #eg typing 'go east' would give you the list:
        #['go','east']
        move = input(">>").lower().split()

        #if they type 'go' first
        if move[0] == "go":
            #check that they are allowed to move in the direction
            if move[1] in rooms[currentRoom]:
                #set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
            #there is no door in that direction
            else:
                print("You can't go that way")

        if move[0] == "options":
            options()

        if currentRoom == 6:
            print("----------------------")
            print("You have escaped")
            print("----------------------")
            break

        if currentRoom == 7:
            print("----------------------")
            print("Oh No! it was a trap-door")
            print("Try again")
            print("----------------------")
            break
        

roomName = rooms[1]


