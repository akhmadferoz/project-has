import random

def roll():
    return random.randint(1,6)

def properties():
    p = {0:"Start",1:"Mediteranean avenue",2:"Community Chest",3:"Baltic Avenue",4:"Income Tax"
    ,5:"Reading Railboard",6:"Oriental Avenue",7:"Chance",8:"Vermont Avenue",9:"Connectuit Avenue"
    ,10:"Visiting Jail",11:"St.Charles Place",12:"Electric Company",13:"States Avenue",14: "Virginia Avenue"
    ,15:"Pensylvania Railroad",16:"St.James Palace",17:"Community Chest",18:"Tennesse Avenue",19:"New York Avenue"
    ,20:"Free Parking",21:"Kentucky Avenue",22:"Chance",23:"Indiana Avenue",24:"Illinois Avenue",25:"B & O Railroad",
    26:"Atlantic Avenue",27:"Ventor Avenue",28:"Water Works",29:"Marvin Gardens",30:"Go to jail",31:"Pacific Avenue",
    32:"North Carolina Avenue",33:"Community Chest",34:"Pensylvania Avenue",35:"Short line",36:"Chance",
    37:"Park Palace",38:"Income Tax",39:"BoardWalk"}

    return p


def players_():
    m = """
    1. Add Player
    2. Start Game. """
    a = 0
    players = {}
    while True:
        a+=1
        print(m)
        x = input("Chose one option: ").strip()
        if x == '1':
            p = input("Enter Player name: ")
            players[a]= p
            print(p," Successfully added.")
        elif x=='2':
            break
        else:
            print("Please Chose the correct option")
            a-=1

    return players


def money(M,i,add,sub,thing):
    if add:
        M[i]+=thing
    if sub:
        M[i]-=thing

counters = {}
x = players_()
for i in range(1,len(x)+1):
    counters[i] = 0


def add_prop(d,i,proppy):
    d[i].append(proppy)
    return d
    
def second_menu():
    M ={}
    for i in range(1,len(x)+1):
        M[i] = 1500
    d = {}
    for i in range(1,len(x)+1):
        d[i] = []

    while True: 
        for i in range(1,len(x)+1):
            print("""
            1. Roll Dice.
            2. Show my properties.""")   
            b = input("Choose one option: ") 
            if b=="1":
                z = roll()
                print("Player",i,"You rolled",z)
                counters[i]+=z
                for j in range(len(properties())):
                    if counters[i]== j and properties()[j] == "Income Tax":
                        money(M,False,True,100)
                    if counters[i] == j and properties()[j]!="Income Tax" and properties()[j]!="Chance" and properties()[j]!="Community Tax":
                        print("You have landed on",properties()[j])
                        print("""
                        1. Buy Property.
                        2. Pass""")
                        g = input("Please choose one option: ")
                        if g=='1':
                            add_prop(d,i,properties()[j])
                        elif g=='2':
                            pass
                        else:
                            print("Please choose correct the option")

            elif b=="2":
                print(d)
            else:
                print("Please choose correct option.")
                                 
            print(counters)


second_menu()






        
















