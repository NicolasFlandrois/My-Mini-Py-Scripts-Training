#!/usr/bin/python3.7
# UTF8
# Date:Thu 19 Mar 2020 22:24:29 CET
# Author: Nicolas Flandrois
# Synthax trees to represent math expressions, & visualise a 2D representation


class Expr:
    '''Empty class, to hold the expression'''
    pass


class Times(Expr):
    """Tree structure construction for sign 'times' '*' """

    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return '(' + str(self.l) + '*' + str(self.r) + ')'

    def eval(self, env):
        return self.l.eval(env) * self.r.eval(env)


class Plus(Expr):
    """Tree structure construction for sign 'plus' '+' """

    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return '(' + str(self.l) + '+' + str(self.r) + ')'

    def eval(self, env):
        return self.l.eval(env) + self.r.eval(env)


class Const(Expr):
    """Values of constance in the expression"""

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def eval(self, env):
        return self.val


class Var(Expr):
    """Values of unknown variables in the expression"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def eval(self, env):
        return env[self.name]


# e1 = 3*(y+x)
e1 = Times(Const(3), Plus(Var('y'), Var('x')))
# e2 = 3*y+x
e2 = Plus(Times(Const(3), Var('y')), Var('x'))

print("e1 = ", e1)
print("e1 = ", e2)

env = {"x": 2, "y": 4}

print("e1 = ", e1.eval(env))
print("e1 = ", e2.eval(env))
