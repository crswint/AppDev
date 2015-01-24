import time

# time.sleep(1) will pause for 1 sec


class BaseGameEntity():
    """Docstring Base"""
    id = 0

    def __init__(self):
        self.id = BaseGameEntity.id
        BaseGameEntity.id += 1

    def Update(self):
        pass


class Miner(BaseGameEntity):
    """Docstring Miner"""
    def __init__(self, current_state, location='Home', gold_carried=0, money_in_bank=2, thirst=0, fatigue=0):
        BaseGameEntity.__init__(self)
        self.current_state = current_state
        self.location = location
        self.gold_carried = int(gold_carried)
        self.money_in_bank = int(money_in_bank)
        self.thirst = int(thirst)
        self.fatigue = int(fatigue)

    def Update(self):
        self.thirst += 1
        self.current_state.execute(self)

    def ChangeState(self, New_state):
        self.current_state.exit(self)
        self.current_state = New_state
        self.current_state.enter(self)


class State():
    """Docstring State"""

    def enter(self):
        pass

    def execute(self):
        pass

    def exit(self):
        pass


class EnterMineAndDigForNugget(State):

    def enter(self, miner):
        if miner.location != 'Mine':
            miner.location = 'Mine'
            print ("Walking to the Gold Mine")

    def execute(self, miner):
        miner.gold_carried += 1
        miner.fatigue += 1
        print ("Picking up a nugget")

        if miner.thirst == 4:
            miner.ChangeState(Saloon)
        elif miner.gold_carried == 2:
            miner.ChangeState(Bank)

    def exit(self, miner):
        print("Ah'm Leavin' the gold mine with mah pockets full o' sweet gold")


class VisitBankAndDepositGold(State):

    def enter(self, miner):
        if miner.location != 'Bank':
            miner.location = 'Bank'
            print ("Going to the bank. yes siree")

    def execute(self, miner):
        miner.gold_carried -= 1
        miner.money_in_bank += 1
        print ("Depositin gold.  Total savings now {0}").format(miner.money_in_bank)
        if miner.thirst == 4:
            miner.ChangeState(Saloon)
        elif miner.money_in_bank % 5 == 0:
            print("Woohoo! Rich enough for now. Back home to mah li'l lady")
            miner.ChangeState(Home)
        else:
            miner.ChangeState(Mine)

    def exit(self, miner):
        print("Leavin' the bank")


class GoHomeAndSleepTilRested(State):

    def enter(self, miner):
        if miner.location != "Home":
            miner.location = "Home"
            print("Walkin home")

    def execute(self, miner):
        while miner.fatigue != 0:
            miner.fatigue -= 1
            print("ZZZzzz...")
        else:
            miner.thirst = 0
            miner.ChangeState(Mine)

    def exit(self, miner):
        print("Headin' to the mine")


class QuenchThirst(State):

    def enter(self, miner):
        if miner.location != 'Saloon':
            miner.location = 'Saloon'
            print("Boy, ah sure is thusty! Walkin' to the saloon")

    def execute(self, miner):
        miner.gold_carried -= 1
        miner.thirst = 0
        print ("That's mighty fine sippin liquor")
        miner.ChangeState(Mine)

    def exit(self, miner):
        print("Leavin' the saloon, feelin' good")


if __name__ == '__main__':
    Mine = EnterMineAndDigForNugget()
    Home = GoHomeAndSleepTilRested()
    Saloon = QuenchThirst()
    Bank = VisitBankAndDepositGold()
    a = Miner(Mine)
    b = Miner(Home)
    game_objects = [a]
    turns = 0
    while turns < 10:
        for object in game_objects:
            object.Update()
        time.sleep(1)
        turns += 1
