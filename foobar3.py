#foobar3
#for details on my approach to this challenge, see the notepad document (also pseudocode-like plan)

def solution(hall): #map cant be called map because map is an inbuilt function
    
    #PICK A NEW WALL TO REMOVE
    finished = False
    while not finished:
        
        newhall = hall #newhall is the hall with 0-all walls removed (so that walls dont get repeated)
        for array in range(0,len(newhall)):
            for place in range(0, len(newhall[array])):
                if newhall[array][place] == 1:
                    newhall[array][place] = 0
                    wallposy,wallposx = array,place #remembering which wall was removed
                    found = True
                    break
            if found:
                break
        if found:
            found = False
        else:
            print("all walls smashed")
            finished = True
            break
        print(newhall)

        #REMOVE WALL FROM MAIN LIST
        currenthall = hall #currenthall is the hall with ONLY 1 wall removed.
        currenthall[wallposy][wallposx] == 0

print(solution(([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])))
