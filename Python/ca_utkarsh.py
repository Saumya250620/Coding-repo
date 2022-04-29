class Sports(object):
    def __init__(boy,why):
        boy.why = "Sports 2020:"

    def Identify(boy):
        return boy.why

    def isBoy(boy):
        return False

class Check(Sports):
    def isBoy(boy):
        return True

x = Sports("Alice")
print(x.Identify(),x.isBoy())

x = Check("Bob")
print(x.Identify(),x.isBoy())


Sports 2020: False
Sports 2020: True
