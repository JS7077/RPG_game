import sys
import random
import time


#list of variables

a = '' #answer
b = '' #alternate answer
c = ',nbv' #loop break
m = 100 #money
n = 0 #math variable
player_name = '' #name of player
quest = '' #what quest the player is on
quest1 = '' #other quest
php = 20 #player current health
max_hp = 20 #player max health
pdmg = 1 #player damage
hp_pot = 0 #healing potions owned
str_pot = 0 #strength potions owned
score = 0 #player's score but not
real_score = score + max_hp + pdmg * 5 + hp_pot * 5 + str_pot * 5 + m / 2 #player's displayed score



#functions

def query(question, answers):
    global a
    while True:
        print('', question, '')
        print(' Choose one of:', ', '.join(answers))
        a = input(' > ')
        a = a.lower() # make lowercase
        if a == 'y':
            a = 'yes'
        if a == 'n':
            a = 'no'
        if a in answers:
            return a
        else:
            print('Invalid response')

def heal(amount='0'):
    global php, max_hp
    amount = int(amount)
    php = php + amount
    if php > max_hp:
        amount = php - max_hp
        php = max_hp
    print('You gained', str(amount), 'health. You are now at', str(php), 'health.')

def money(cost='0'):
    global m
    cost = int(cost)
    costt = 0
    if cost > m:
        print('You don\'t have enough money.')
        return
    else:
        costt = m - cost
        print('You have $' + str(costt) + '.')
        m = costt

def say(message='', talker=''):
  global player_name
  if talker == '':
    print(player_name + ':"' + message + '"')
  else:
    print(talker + ':"' + message + '"')

def shop():
    global a, b, c, n, pdmg, max_hp, hp_pot, str_pot
    c = 'sg'
    while c != '':
        c = 'sf'
        a = query('(1)Weapons, (2)Armor, (3)Potions, (4)Food, or (5)Sell.', ['1', '2', '3', '4', '5', ''])        
        money('0')
        if a == '1':
            a = query('What level weapon?', ['1', '2', '3', '4', '5'])
            n = int(a) * 50
            b = 'That will be $' + str(n) + '. Confirm.'
            a = query(b, ['yes', 'no'])
            if a == 'yes':
                money(n)
                print('You got a better weapon.')
                pdmg = pdmg + n / 50
        elif a == '2':
            a = query('What level armor?', ['1', '2', '3', '4', '5'])
            n = int(a) * 40
            a = query('That will be $' + str(n) + '. Confirm.', ['yes', 'no'])
            if a == 'yes':
                money(n)
                print('You got better armor.')
                b = n / 20
                max_hp = max_hp + b
                heal(b)
        elif a == '3':
            a = query('Do you want a (1)Healing, or (2)Strength potion?', ['1', '2'])
            if a == '1':
                a = query('That will be ($15). Confirm.', ['yes', 'no'])
                if a == 'yes':
                    money(15)
                    print('You got a healing potion.')
                    hp_pot = hp_pot + 1
            elif a == '2':
                a = query('That will be ($20). Confirm.', ['yes', 'no'])
                if a == 'yes':
                    money(20)
                    print('You got a strength potion.')
                    str_pot = str_pot + 1
        elif a == '4':
            a = query('Do you want (1)Food or (2)Drinks?', ['1', '2'])
            if a == '1':
                a = query('(1)Stew($10), (2)Bread($5), or (3)Cheese($5)?',
                          ['1', '2', '3'])
                if a == '1':
                    money(10)
                    print('You got stew.')
                elif a == '2':
                    money(5)
                    print('You got bread.')
                else:
                    money(5)
                    print('You got cheese.')
            else:
                a = query('(1)Mead($5), (2)Cider($5), (3)Wine($10), or (4)Beer($10)?', ['1', '2', '3', '4'])
                if a == '1':
                    money(5)
                    print('You got mead.')
                elif a == '2':
                    money(5)
                    print('You got cider.')
                elif a == '3':
                    money(10)
                    print('You got wine.')
                else:
                    money(10)
                    print('You got beer.')
        elif a == '5' or a == '':
            a = query('(1)Potions, (2)Edibles, (3)Other', ['1', '2', '3', ''])
            if a == '1':
                if hp_pot < 1:
                    if str_pot > 0:
                        a = query('Sell strength potion?', ['yes', 'no'])
                        if a == 'yes':
                            money(-15)
                            str_pot = str_pot - 1
                    else:
                        print('You can\'t sell any potions.')
                else:
                    if str_pot > 0:
                        a = query('(1)Healing or (2)Strength.', ['1', '2'])
                        if a == '1':
                            money(-10)
                            hp_pot = hp_pot - 1
                        elif a == '2':
                            str_pot = str_pot - 1
                            money(-15)
                    else:
                        a = query('Sell healing potion?', ['yes', 'no'])
                        if a == 'yes':
                            money(-10)
            elif a == '2':
                print('We don\'t have anything here.')
            elif a == '3':
                print('We don\'t have anything here.')
            elif a == '':
                money(-1000000000)
            if c != 'sf':
                print('You sold', a + '.')
        a = query('Do you want to exit the shop?', ['yes', 'no', ''])
        if a == 'yes':
            c = ''

def town_hall():
    global a, quest1, score, player_name
    print('You enter the town hall.')
    if quest1 == 'Mayor':
        print('The mayor is inside.')
        if score > 45:
            say('I killed those monsters.')
            say('Thank you.', 'Mayor')
            money(-100)
            score = score + 50
            quest1 = 'Complete'
        else:
            say('They attacked again last night.', 'Mayor')
    elif quest1 == 'Complete':
        print('No one is inside the town hall.')
    else:
        print('The mayor is inside.')
        a = query('Do you want to (1)Talk to the mayor or (2)Leave the town hall?', ['1', '2'])
        if a == '1':
            print('Mayor:"Hello there."')
            print('Mayor:"You look like an adventurer."')
            say('What is your name?', 'Mayor')
            time.sleep(.5)
            say(player_name + '.')
            time.sleep(.5)
            print('Mayor:"Hello', player_name + '."')
            print('Mayor:"I have a quest for you."')
            a = query('Do you want to (1)Accept or (2)Reject?', ['1', '2'])
            if a == '1':
                say('I accept.')
                time.sleep(.5)
                quest1 = 'Mayor'
                say('Monsters are terrorizing my town.', 'Mayor')
                say('Kill them for me.', 'Mayor')
            else:
                say('Sorry.')
    time.sleep(.5)
    print('You leave the town hall.')

def tavern():
    global a, quest, pdmg
    print('You enter the tavern.')
    time.sleep(.5)
    print('Bartender:"Hail traveler."')
    money()
    a = query('Do you want to (1)Drink, (2)Eat, (3)Do both, or (4)Do neither?', ['1', '2', '3', '4'])
    if a == '1':
        say("Drink please.")
        a = query('(1)Mead($5), (2)Cider($5), (3)Wine($10), or (4)Beer($10)?', ['1', '2', '3', '4'])
        if a == '1':
            say('Mead please.')
            money(5)
            say('Here\'s your mead.', 'Bartender')
        elif a == '2':
            say('Cider please.')
            money(5)
            say('Here\'s your cider.', 'Bartender')
        elif a == '3':
            say('Wine please.')
            money(10)
            say('Here\'s your wine.', 'Bartender')
        elif a == '4':
            say('Beer please.')
            money(10)
            say('Here\'s your beer.', 'Bartender')
        heal(5)
    elif a == '2':
        say("Food please.")
        a = query('(1)Stew($10), (2)Bread($5), or (3)Cheese($5)?', ['1', '2', '3'])
        if a == '1':
            say('Stew please.')
            money(10)
            say('Here\'s your stew.', 'Bartender')
        elif a == '2':
            say('Bread please.')
            money(5)
            say('Here\'s your bread.', 'Bartender')
        elif a == '3':
            say('Cheese please.')
            money(5)
            say('Here\'s your cheese.', 'Bartender')
        heal(10)
    elif a == '3':
        say("Both please.")
        a = query('(1)Stew($10), (2)Bread($5), or (3)Cheese($5)?',
                  ['1', '2', '3'])
        if a == '1':
            say('Stew please.')
            money(10)
            say('Here\'s your stew.', 'Bartender')
        elif a == '2':
            say('Bread please.')
            money(5)
            say('Here\'s your bread.', 'Bartender')
        elif a == '3':
            say('Cheese please.')
            money(5)
            say('Here\'s your cheese.', 'Bartender')
        a = query('(1)Mead($5), (2)Cider($5), (3)Wine($10), or (4)Beer($10)?', ['1', '2', '3', '4'])
        if a == '1':
            say('Mead please.')
            money(5)
            say('Here\'s your mead.', 'Bartender')
        elif a == '2':
            say('Cider please.')
            money(5)
            say('Here\'s your cider.', 'Bartender')
        elif a == '3':
            say('Wine please.')
            money(10)
            say('Here\'s your wine.', 'Bartender')
        elif a == '4':
            say('Beer please.')
            money(10)
            say('Here\'s your beer.', 'Bartender')
        heal(15)
    else:
        say("Nothing. Thank you.")
    if quest == 'Jerry':
        say('Wow, look at you.', 'Bartender')
        say('I\'ll go get that weapon.', 'Bartender')
        time.sleep(.5)
        pdmg = pdmg + 1
        say('Here you go.', 'Bartender')
        time.sleep(.5)
        say('Thank you!')
        quest = 'Complete'
    elif quest == 'Bartender':
        say('You haven\'t talked to my friend yet.', 'Bartender')
    elif quest == 'Complete':
        say('Never mind.', 'Bartender')
    else:
        a = query('Bartender:"Do you have some time?"', ['yes', 'no'])
        if a == 'yes':
            say('Yes.')
            time.sleep(.5)
            say('Great.', 'Bartender')
            say('I have a friend, Jerry, who lives down the road.', 'Bartender')
            say('Talk to him.', 'Bartender')
            quest = 'Bartender'
        else:
            say('No.')
            time.sleep(.5)
            say('Whatever works for you.', 'Bartender')
    time.sleep(.5)
    print('After a while you leave the tavern.')

def inn():
    global a
    print('You enter the inn.')
    say('Hello.', 'Innkeeper')
    a = query('Innkeeper:"Is there anything I can help you with?"', ['yes', 'no'])
    if a == 'yes':
        say('Yes.')
        say('What, may I ask, is that.', 'Innkeeper')
        a = query('(1)I want a room, (2)Idk what to do, (3)You may not', ['1', '2', '3'])
        if a == '1':
            say('I want a place to stay.')
            time.sleep(.5)
            say('You\'ve come to the right place.', 'Innkeeper')
            say('I can get you a Room and food($30) or just a Room($20).', 'Innkeeper')
            a = query('(1)Room and food or (2)Just a room?', ['1', '2'])
            if a == '1':
                say('Room and food please.')
                print('You eat and sleep in the inn and wake up feeling refreshed.')
                money(30)
                heal(999)
            else:
                say('Just a room.')
                print('You sleep in the inn and wake up feeling refreshed but hungry.')
                money(20)
                heal(99)
            say('Come again if you need a place to sleep again.', 'Innkeeper')
        elif a == '2':
            say('Idk what to do.')
            say('Go to the town hall and ask the mayor.', 'Innkeeper')
        else:
            say('You may not.')
            say('So rude.', 'Innkeeper')
    else:
        say('No.')
        say('Ok then.', 'Innkeeper')
    time.sleep(.5)
    print('You leave the inn.')

def jerry():
    global a, c, player_name, quest, max_hp
    if a == 'yes':
        print('You go down the road and find him.')
        print('Stranger:"Hello there,', player_name + '."')
        print('Stranger:"You must be the one the bartender was talking about."')
        a = query('(1)Are you Jerry, (2)How do you know my name?', ['1', '2'])
        if a == '1':
            say('Are you Jerry?')
            say('Yes I am.', 'Jerry')
            say('The bartender told me to give you some armor.', 'Jerry')
            say('Here you go.', 'Jerry')
            max_hp = max_hp + 3
            heal(3)
            print('You go back to town.')
            quest = 'Jerry'
            c = ''
        else:
            say('How do you know my name?')
            say('I have my ways.', 'Stranger')
            print('You walk away from the creep.')

def combat(enemy='', hp='5', dmg='1', bvus='-1'):
    #variables
    enemy_list = ['goblin', 'bandit', 'slime', 'orc', 'slime', 'slime', 'goblin', 'bandit', ]
    enemy_hp = int(hp)
    enemy_dmg = int(dmg)
    global a, b, c, m, php, pdmg, max_hp, hp_pot, str_pot, score, real_score
    #start
    if enemy == '':
        enemy = random.choice(enemy_list)
        if enemy == 'goblin':
            enemy_dmg = 2
        elif enemy == 'bandit':
            enemy_hp = 10
        elif enemy == 'orc':
            enemy_hp = 10
            enemy_dmg = 2
    else:
        enemy = enemy
    print('You enter combat with', enemy + '.')
    #always
    b = pdmg
    while c != '':
        a = query('(1)Attack, (2)Use item, (3)Run.', ['1', '2', '3'])
        if a == '1':
            enemy_hp = enemy_hp - pdmg
            if enemy_hp <= 0:
                print('You killed the', enemy + '.')
                score = score + 25
                #loot
                if bvus == '-1':
                    bvus = random.randint(1, 100)
                    if bvus < 50:
                        loot = '1 healing potion'
                        hp_pot = hp_pot + 1
                    elif bvus < 61 and bvus >= 50:
                        loot = 'a better weapon'
                        b = pdmg + 1
                    elif bvus < 72 and bvus >= 61:
                        loot = 'better armor'
                        max_hp = max_hp + 2
                    elif bvus < 97 and bvus >= 72:
                        loot = '1 strength potion'
                        str_pot = str_pot + 1
                    else:
                        combat('Dragon', '30', '3', bvus='4')
                        break
                else:
                    loot = 'happiness'
                print('You got', loot + '.')
                c = ''
                if loot == 'happiness':
                    print('You won.')
                    score = score + 100
                    real_score = score + max_hp + pdmg * 5 + hp_pot * 5 + str_pot * 5 + m / 2
                    print('Your score is:', str(real_score) + '.')
                    sys.exit()
                break
            else:
                print('You did', pdmg, 'damage. The', enemy, 'is now at', enemy_hp, 'health.')
        elif a == '2':
            if hp_pot < 1:
                if str_pot > 0:
                    a = query('Use strength potion?', ['yes', 'no'])
                    if a == 'yes':
                        print('You feel stronger!')
                        str_pot = str_pot - 1
                        b = pdmg
                        pdmg = pdmg + 2
                    else:
                        print('You didn\'t use anything.')
                        print('But you spent so much time looking you lost your turn.')
                else:
                    print('You can\'t use anything.')
                    print('But you spent so much time looking you lost your turn.')
            else:
                if str_pot > 0:
                    a = query('(1)Healing or (2)Damage.', ['1', '2'])
                    if a == '1':
                        heal(5)
                        hp_pot = hp_pot - 1
                    elif a == '2':
                        print('You feel stronger!')
                        str_pot = str_pot - 1
                        b = pdmg
                        pdmg = pdmg + 2
                else:
                    a = query('Use healing potion?', ['yes', 'no'])
                    if a == 'yes':
                        heal(5)
                        hp_pot = hp_pot - 1
                    else:
                        print('You didn\'t use anything.')
                        print('But you spent so much time looking you lost your turn.')
        else:
            php = php - enemy_dmg
            print('You took', enemy_dmg, 'damage from', enemy + '. You are now at', php, 'health.')
            if php <= 0:
                print('You died.')
                score = score - 100
                if score < 0:
                    score = 0
                real_score = score + max_hp + pdmg * 5 + hp_pot * 5 + str_pot * 5 + m / 2
                print('Your score is:', str(real_score))
                c = ''
                sys.exit()
            print('You ran away from', enemy + '.')
            c = ''
            break
        php = php - enemy_dmg
        print('You took', enemy_dmg, 'damage from', enemy + '. You are now at', php, 'health.')
        if php <= 0:
            print('You died.')
            score = score - 100
            if score < 0:
                score = 0
            real_score = score + max_hp + pdmg * 5 + hp_pot * 5 + str_pot * 5 + m / 2
            print('Your score is:', str(real_score))
            c = ''
            sys.exit()
    pdmg = b


#start of program
print('Ready player n.')
print()
time.sleep(1)
#start of game
#intro
player_name = input(' What is your name?:')
say('Welcome traveler.', 'Dangalf')
a = query('Dangalf:"Do you want to go on an adventure?"', ['yes', 'no'])
if a == 'yes':
    say('Yes.')
    say('Good.', 'Gandalf')
else:
    say('No.')
    say('Well too bad.', 'Gandalf')
print()
time.sleep(1)
#town
print('You come to a town.')
a = query('Do you want to go in?', ['yes', 'no'])
if a == 'no':
    c = 'Yes'
    a = 'sgsbr'
while True:
    if a != 'sgsbr':
        print('You enter the town')
    while c != 'yes':
        a = query('Enter the (1)Town hall, (2)Tavern, (3)Inn, or (4)Shop.', ['1', '2', '3', '4'])
        if a == '1':
            town_hall()
        elif a == '2':
            tavern()
        elif a == '3':
            inn()
        elif a == '4':
            print('You enter the shop.')
            shop()
        time.sleep(.5)
        a = query('Do you want to leave the town?', ['yes', 'no'])
        c = a

    if a != 'sgsbr':
        print('You leave the town.')

    if quest == 'Bartender':
        a = query('Do you want to go to the Bartender\'s friend?', ['yes', 'no'])
        jerry()

    while c != '':
        combat()
        a = query('Do you want to return to the town?', ['yes', 'no'])
        if a == 'yes':
            c = ''
        else:
            c = 'sgs'
