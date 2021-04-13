class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('ran really fast')


# 134. Multiple Inferitance

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb1 = HybridBorg('borg1', 50, 100)
hb1.run()
hb1.check_arrows()
hb1.attack()
hb1.sign_in()

# MRO - Method Resolution Order


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)
print(D.mro())


class X:
    pass


class Y:
    pass


class Z:
    pass


class A2(X, Y):
    pass


class B2(Y, Z):
    pass


class M(B2, A2, Z):
    pass


# Guess: M, Z, B2, A2, Y, X, object -> Correct: M, B2, A2, X, Y, Z, object
print(M.mro())
