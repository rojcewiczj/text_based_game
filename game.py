import random

class Fighter:
    def __init__(self):
        self.strike = False
        self.deflection = False
        self.push = False
        self.pull = False
        self.throw = False
        self.health = 10
        self.balance = 10
        self.resting = False
        self.fallen = False
       
    def attack(self):
        self.strike = True
        self.deflection = False
        self.push = False
        self.pull = False
        self.throw = False
        self.resting = False
       
    def deflectAttack(self):
        self.strike = False
        self.deflection = True
        self.push = False
        self.pull = False
        self.throw = False
        self.resting = False
        
    def pushAttack(self):
        self.deflection = False
        self.strike = False
        self.push = True
        self.pull = False
        self.throw = False
        self.resting = False
       
    def pullAttack(self):
        self.strike = False
        self.deflecion = False
        self.push = False
        self.throw = False
        self.resting = False
        self.pull = True
      
    
    def throwAttack(self):
        self.strike = False
        self.deflection = False
        self.push = False
        self.throw = True
        self.resting = False
        self.pull = False
    def standup(self):
        self.strike = False
        self.deflection = False
        self.push = False
        self.throw = False
        self.resting = False
        self.pull = False
        self.fallen = False

    
   
        
IpMan = Fighter()
BadGuy = Fighter()
def makeAChoice(firstOption = None, secondOption = None, thirdOption = None, fourthOption = None, fifthOption = None):
    if fifthOption is None and fourthOption is not None and thirdOption is not None:
        choice = random.choice([firstOption, secondOption, thirdOption, fourthOption])
    if fifthOption is None and fourthOption is None and thirdOption is not None:
        choice = random.choice([firstOption, secondOption, thirdOption])
    if thirdOption is None:
        choice = random.choice([firstOption, secondOption])
    return choice


while True:

    cmds = input("-> ")
    if cmds[0] == 's':
        IpMan.attack()
        print('you strike')
    if cmds[0] == 'd':
        IpMan.deflectAttack()
        print('you deflect')
    if cmds[0] == 'e':
        IpMan.pushAttack()
        print('you push')
    if cmds[0] == 'w':
        IpMan.pullAttack()
        print("you pull")
    if cmds[0] == 'f':
        IpMan.throwAttack() 
        print('you attempt a take-down')
    if cmds[0] == "m":
        possibility = makeAChoice("standup", "fall", "fall", "fall")
        if possibility == "standup":
            IpMan.standup()
            print("you stand up!")
        else:
            IpMan.standup()
            IpMan.fallen is True
            IpMan.health -= 2
            print("you try to stand up but they stop you!")

    if IpMan.strike == True:
        response = makeAChoice(BadGuy.attack, BadGuy.deflectAttack)
        if BadGuy.fallen is True:
            BadGuy.health -= 5
            print("you strike them on the ground!")
        if response == BadGuy.attack:
            print("they respond by trying to strike back!")
        else:
            print("they respond by going for a deflection!")
        if response == BadGuy.attack and IpMan.balance > BadGuy.balance:
            BadGuy.attack()
            IpMan.health -=1
            IpMan.balance -= 1
            BadGuy.health -=4
            BadGuy.balance -=4
            

        if response == BadGuy.attack and IpMan.balance < BadGuy.balance:
            BadGuy.attack()
            IpMan.health -=2
            IpMan.balance -=2
           
            BadGuy.health -=2
            BadGuy.balance -=2
        
        if response == BadGuy.attack and IpMan.balance == BadGuy.balance:
            BadGuy.attack()
            IpMan.health -=1
            IpMan.balance -=1
         
            BadGuy.health -=2
            BadGuy.balance -=2
   
        if response == BadGuy.deflectAttack and IpMan.balance < BadGuy.balance:
            BadGuy.deflectAttack()
            IpMan.balance -= 8
         
                   
        if response == BadGuy.deflectAttack and IpMan.balance > BadGuy.balance:
            BadGuy.deflectAttack()
            IpMan.balance -= 2
        

        if response == BadGuy.deflectAttack and IpMan.balance == BadGuy.balance:
            BadGuy.deflectAttack()
            IpMan.balance -= 4
        print(f'your health is now: {IpMan.health} and your balance is now: {IpMan.balance} ')
        print(f"the bagua masters health is now: {BadGuy.health} and their balance is now: {BadGuy.balance} ")
        opponentsMove = makeAChoice(BadGuy.attack, BadGuy.pushAttack, BadGuy.pullAttack)
        if opponentsMove == BadGuy.attack:
            BadGuy.attack()
            print(f"after responding, they try to strike you!")
            if IpMan.fallen is True:
                print("they strike you on the ground!")
                IpMan.health -= 5
        if opponentsMove == BadGuy.pushAttack:
            BadGuy.pushAttack()
            print(f"after responding, they try to push you!")
        if opponentsMove == BadGuy.pullAttack:
            BadGuy.pullAttack()
            print(f"after responding, they try to pull you!")
            
        if IpMan.strike is True and BadGuy.pull is True:
            if IpMan.balance < BadGuy.balance:
                IpMan.balance -= 4
                BadGuy.balance += 1
                print(f'your opponent grabs your arm and pulls you WAY off balance! your balance is: {IpMan.balance}, your opponents balance is: {BadGuy.balance}')
            if IpMan.balance > BadGuy.balance:
                IpMan.balance -= 2
                BadGuy.balance += 1
                print(f'your opponent grabs your arm and pulls you slightly off balance! your balance is: {IpMan.balance}, your opponents balance is: {BadGuy.balance}')
            if IpMan.balance == BadGuy.balance:
                IpMan.balance -= 3
                BadGuy.balance += 1
                print(f'your opponent grabs your arm and pulls you off balance! your balance is: {IpMan.balance}, your opponents balance is: {BadGuy.balance}')
    if IpMan.push == True:
        if  BadGuy.pull is True:
            IpMan.balance += 2
            BadGuy.balance -= 2
            print("you countered their pull with your push!")
            
        response = makeAChoice("pull", "push")
        if response == "push":
            print("they respond by trying to push you back!")
        else:
            print("they respond by pulling!")

        if response == "pull" :
            BadGuy.pullAttack()
            IpMan.balance -= 2
            BadGuy.balance += 2
            print(f'your health is now: {IpMan.health} and your balance is now: {IpMan.balance} ')
            print(f"the bagua masters health is now: {BadGuy.health} and their balance is now: {BadGuy.balance} ")
        

        if response == "push": 
            BadGuy.pushAttack()
            IpMan.balance -=1
            print(f'your health is now: {IpMan.health} and your balance is now: {IpMan.balance} ')
            BadGuy.balance -=1 
            print(f"the bagua masters health is now: {BadGuy.health} and their balance is now: {BadGuy.balance} ")
      
        opponentsMove = makeAChoice(BadGuy.attack, BadGuy.pushAttack, BadGuy.pullAttack, BadGuy.deflectAttack)
        if opponentsMove == BadGuy.attack:
            BadGuy.attack()
            print(f"after responding, they try to strike you!")
        if opponentsMove == BadGuy.pushAttack:
            BadGuy.pushAttack()
            print(f"after responding, they try to push you!")
        if opponentsMove == BadGuy.pullAttack:
            BadGuy.pullAttack()
            print(f"after responding, they try to pull you!")
        if opponentsMove == BadGuy.deflectAttack:
            BadGuy.deflectAttack()
            print(f"after responding they lock up with you!")
            
        if IpMan.push is True and BadGuy.deflection is True:
            if IpMan.balance < BadGuy.balance:
                IpMan.balance -= 4
                BadGuy.balance += 1
                print(f'your opponent deflect you to the side and sends you WAY off balance! your balance is: {IpMan.balance}, your opponents balance is: {BadGuy.balance}')
            if IpMan.balance > BadGuy.balance:
                IpMan.balance -= 2
                BadGuy.balance += 1
                print(f'your opponent deflect you to the side and sends you slightly off balance! your balance is: {IpMan.balance}, your opponents balance is: {BadGuy.balance}')
            if IpMan.balance == BadGuy.balance:
                IpMan.balance -= 3
                BadGuy.balance += 1
                print(f'your opponent deflect you to the side and sends you off balance! your balance is: {IpMan.balance}, your opponents balance is: {BadGuy.balance}')
    if IpMan.pull is True:
        if BadGuy.push is True:
            IpMan.balance += 2
            BadGuy.balance -= 4
            print("you countered their push with your pull!")
            response = makeAChoice("pull", "push")
        if response == "push":
            print("they respond by trying to push you back!")
        else:
            print("they respond by pulling!")

        if response == "pull" :
            BadGuy.pullAttack()
            IpMan.balance -= 1
            BadGuy.balance += 1
            print(f'your health is now: {IpMan.health} and your balance is now: {IpMan.balance} ')
            print(f"the bagua masters health is now: {BadGuy.health} and their balance is now: {BadGuy.balance} ")
        

        if response == "push": 
            BadGuy.pushAttack()
            IpMan.balance -=2
            print(f'your health is now: {IpMan.health} and your balance is now: {IpMan.balance} ')
            BadGuy.balance -=2
            print(f"the bagua masters health is now: {BadGuy.health} and their balance is now: {BadGuy.balance} ")
      
        opponentsMove = makeAChoice(BadGuy.attack, BadGuy.pushAttack, BadGuy.pullAttack, BadGuy.deflectAttack)
        if opponentsMove == BadGuy.attack:
            BadGuy.attack()
            print(f"after responding, they try to strike you!")
        if opponentsMove == BadGuy.pushAttack:
            BadGuy.pushAttack()
            print(f"after responding, they try to push you!")
        if opponentsMove == BadGuy.pullAttack:
            BadGuy.pullAttack()
            print(f"after responding, they try to pull you!")
        if opponentsMove == BadGuy.deflectAttack:
            BadGuy.deflectAttack()
            print(f"after responding they lock up with you!")
            
        if IpMan.pull is True and BadGuy.deflection is True:
            if IpMan.balance < BadGuy.balance:
                IpMan.balance -= 4
                BadGuy.balance += 1
                print(f'your opponent deflect you to the side and sends you WAY off balance! your balance is: {IpMan.balance}, your opponents balance is: {BadGuy.balance}')
            if IpMan.balance > BadGuy.balance:
                IpMan.balance -= 2
                BadGuy.balance += 1
                print(f'your opponent deflect you to the side and sends you slightly off balance! your balance is: {IpMan.balance}, your opponents balance is: {BadGuy.balance}')
            if IpMan.balance == BadGuy.balance:
                IpMan.balance -= 3
                BadGuy.balance += 1
                print(f'your opponent deflect you to the side and sends you off balance! your balance is: {IpMan.balance}, your opponents balance is: {BadGuy.balance}')
    if IpMan.deflection is True:
            if BadGuy.strike is True:
                IpMan.balance += 4
                BadGuy.balance -= 4
                print("you counter their strike with a deflection!")
            response  = makeAChoice("strike", "push", "pull")
            if response == "strike" and BadGuy.balance < IpMan.balance:
                BadGuy.attack()
                response = "done"
                IpMan.health -= 1
                print("they respond by striking back!")
            if response == "strike" and BadGuy.balance == IpMan.balance:
                BadGuy.attack()
                response = "done"
                IpMan.health -= 1
                IpMan.balance -= 1
                print("they respond by striking back!")
            if response == "strike" and BadGuy.balance > IpMan.balance:
                BadGuy.attack()
                response = "done"
                IpMan.health -= 2
                IpMan.balance -= 1
                print("they respond by striking back!")
            if response == "push" and BadGuy.balance < IpMan.balance:
                BadGuy.attack()
                response = "done"
                IpMan.balance -= 1
                print("they respond by pushing!")
            if response == "push" and BadGuy.balance == IpMan.balance:
                BadGuy.attack()
                response = "done"
                IpMan.balance -= 2
                print("they respond by pushing!")
            if response == "push" and BadGuy.balance > IpMan.balance:
                BadGuy.attack()
                response = "done"
                IpMan.balance -= 3
                print("they respond by pushing!")
            if response == "pull" and BadGuy.balance < IpMan.balance:
                BadGuy.attack()
                response = "done"
                IpMan.balance -= 1
                print("they respond by pulling!")
            if response == "pull" and BadGuy.balance == IpMan.balance:
                BadGuy.attack()
                response = "done"
                IpMan.balance -= 2
                print("they respond by pulling!")
            if response == "pull" and BadGuy.balance > IpMan.balance:
                BadGuy.attack()
                response = "done"
                IpMan.balance -= 3
                print("they respond by pulling!")
            print(f'your health is now: {IpMan.health} and your balance is now: {IpMan.balance} ')
            print(f"the bagua masters health is now: {BadGuy.health} and their balance is now: {BadGuy.balance} ")

    if IpMan.throw is True:
        if BadGuy.balance <= 0:
            BadGuy.fallen = True
            print("you throw your opponent to the ground!")
        response = makeAChoice("deflect", "strike", "pull")
        if response == "deflect" and BadGuy.fallen is True:
            BadGuy.deflectAttack()
            IpMan.balance -= 2
            print("they manage to deflect your attack from their fallen position!")
        if response == "strike" and BadGuy.fallen is True:
            BadGuy.attack()
            IpMan.health -= 2
            print("they manage to strike at you from their fallen position")
        if response == "pull" and BadGuy.fallen is True:
            BadGuy.pullAttack()
            IpMan.balance -= 3
            print("although fallen on the ground, they grab hold on you and pull!")
        opponentsMove = makeAChoice("strike", "push", "pull","standup")
        if opponentsMove == "strike":
            BadGuy.attack()
            print(f"after responding, they try to strike you!")
        if opponentsMove == "push":
            BadGuy.pushAttack()
            print(f"after responding, they try to push you!")
        if opponentsMove == "pull":
            BadGuy.pullAttack()
            print(f"after responding, they try to pull you!")
        if opponentsMove == "standup":
            BadGuy.fallen = False
            print(f"after responding they scramble to their feet!")
    if IpMan.balance < 0 and IpMan.fallen is False and BadGuy.fallen is False:
        BadGuy.throwAttack()
        IpMan.fallen = True
        print("they threw you to the ground!")
        print(f'your health is now: {IpMan.health} and your balance is now: {IpMan.balance} ')
        print(f"the bagua masters health is now: {BadGuy.health} and their balance is now: {BadGuy.balance} ")
    if IpMan.health <= 0:
        print("you have been defeated!")
    if BadGuy.health <= 0:
        print("your opponent has been defeated!")
    
    if IpMan.balance < 0 and IpMan.health > 0 and IpMan.fallen is True:
        BadGuy.attack()
        IpMan.health -= 5
        print("they strike you on the ground!")
        
    if BadGuy.balance > 0 and BadGuy.fallen is True and BadGuy.health > 0:
        BadGuy.standup()
        print("they got back to their feet!")



    if BadGuy.balance > 10:
        BadGuy.balance = 10
    if IpMan.balance > 10:
        IpMan.balance = 10
    if BadGuy.balance < 0:
        BadGuy.balance = 0
    if IpMan.balance < 0:
        IpMan.balance = 0
                
                


                
      

        
     
        
    if cmds[0] == "q":
    
        break
