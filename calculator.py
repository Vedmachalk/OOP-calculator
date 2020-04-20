class Expression:
    def __init__(self):
        pass

    def evaluate(self, switch):
        pass

    def to_string(self):
        pass

    def get_priority(self):
        pass

    def is_commutative(self):
        pass

    def to_mini_string(self):
        pass


class Variable(Expression):
    def __init__(self, var):
        self.var = var

    def evaluate(self, switch):
        return switch[self.var]

    def to_string(self):
        return str(self.var)

    def get_priority(self):
        return 4

    def is_commutative(self):
        return True

    def to_mini_string(self):
        return str(self.var)


class Const(Expression):
    def __init__(self, const):
        self.const = const

    def evaluate(self, switch):
        return int(self.const)

    def to_string(self):
        return str(self.const)

    def get_priority(self):
        return 4

    def is_commutative(self):
        return True

    def to_mini_string(self):
        return str(self.const)


"""____________________ADD________________________________________________________"""


class Add(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def get_priority(self):
        return 1

    def is_commutative(self):
        return True

    def to_string(self):
        return ("({}+{})".format(self.expr1.to_string(), self.expr2.to_string()))

    def to_mini_string(self):
        if self.expr1.get_priority() < Add.get_priority(self) and Add.get_priority(self) > self.expr2.get_priority():
            return "({})+({})".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        elif self.expr1.get_priority() > Add.get_priority(self) or Add.get_priority(self) < self.expr2.get_priority():
            return "{}+{}".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        if self.expr1.get_priority() < Add.get_priority(self):
            return "({})+{}".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        elif Add.get_priority(self) > self.expr2.get_priority():
            return "{}+({})".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        if self.expr1.get_priority() == Add.get_priority(self) and Add.get_priority(self) == self.expr2.get_priority():
            return "{}+{}".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())


"""_______________________________________SUBTRACT________________________________________________________"""


class Subtract(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self, switch):
        return self.expr1.evaluate(switch) - self.expr2.evaluate(switch)

    def to_string(self):
        return ("({}-{})".format(self.expr1.to_string(), self.expr2.to_string()))

    def get_priority(self):
        return 1

    def is_commutative(self):
        return False

    def to_mini_string(self):
        if self.expr1.is_commutative() == Subtract.is_commutative(
                self) and self.expr2.is_commutative() == Subtract.is_commutative(self) \
                and self.expr1.get_priority() == Subtract.get_priority(self) \
                and self.expr2.get_priority() == Subtract.get_priority(self):
            return "{}-({})".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        elif self.expr1.get_priority() == Subtract.get_priority(self) \
                and self.expr2.get_priority() == Subtract.get_priority(self):
            return "{}-({})".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        else:
            return "{}-{}".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())


"""____________________MULTIPLY________________________________________________________"""


class Multiply(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self, switch):
        return self.expr1.evaluate(switch) * self.expr2.evaluate(switch)

    def to_string(self):
        return ("({}*{})".format(self.expr1.to_string(), self.expr2.to_string()))

    def get_priority(self):
        return 3

    def is_commutative(self):
        return True

    def to_mini_string(self):
        if self.expr1.get_priority() < Multiply.get_priority(self) \
                and Multiply.get_priority(self) > self.expr2.get_priority():
            return "({})*({})".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        if self.expr1.get_priority() < Multiply.get_priority(self):
            return "({})*{}".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        elif self.expr1.get_priority() > Multiply.get_priority(self) \
                or Multiply.get_priority(self) < self.expr2.get_priority():
            return "{}*{}".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        elif Multiply.get_priority(self) > self.expr2.get_priority():
            return "{}*({})".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        if self.expr1.get_priority() == Multiply.get_priority(self):
            return "{}*{}".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        elif Multiply.get_priority(self) == self.expr2.get_priority():
            return "{}*{}".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())


"""____________________----DIVIDE----________________________________________________________"""


class Divide(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self, switch):
        return self.expr1.evaluate(switch) / self.expr2.evaluate(switch)

    def to_string(self):
        return ("({}/{})".format(self.expr1.to_string(), self.expr2.to_string()))

    def get_priority(self):
        return 3

    def is_commutative(self):
        return False

    def to_mini_string(self):
        if self.expr1.get_priority() < Divide.get_priority(self) and self.expr2.get_priority() < Divide.get_priority(self):
            return "({})/({})".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        if self.expr1.get_priority() < Divide.get_priority(self) and self.expr2.get_priority() > Divide.get_priority(self):
            return "({})/{}".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        elif self.expr1.get_priority() == Divide.get_priority(self) and self.expr2.get_priority() == Divide.get_priority(self):
            return "{}/({})".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        elif self.expr1.get_priority() != Divide.get_priority(self) and self.expr2.get_priority() == Divide.get_priority(self):
            return "({})/({})".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())
        else:
            return "{}/{}".format(self.expr1.to_mini_string(), self.expr2.to_mini_string())

# ______________________________________________________________________________________________________________________


expr1 = Divide(
    Subtract(
        Variable("x"), Const(4)
    ), Add(Const(4),Const(5))

)
print(expr1.to_mini_string())

expr2 = Subtract(
    Subtract(
        Variable("x"), Const(4)
    ),
    Subtract(
        Const(2), Const(3))
)
print(expr2.to_mini_string())

expr3 = Subtract(
    Subtract(
        Variable("x"), Const(4)
    ),
    Divide(Add(
        Const(2), Const(3)),Variable("x"))
)
print(expr3.to_mini_string())

expr4 = Divide(
    Divide(
        Variable("x"), Const(4)
    ) , Divide(Const(4),Const(4))

)
print(expr4.to_mini_string())



expr5 = Divide(
    Subtract(
        Variable("x"), Const(4)
    ), Const(4)

)
print(expr5.to_mini_string())



expr6 = Multiply(
    Subtract(
        Variable("x"), Const(4)
    ),

        Const(2))

print(expr6.to_mini_string())

expr7 = Divide(
    Add(
        Variable("x"), Const(4)
    ), Const(4)

)
print(expr7.to_mini_string())



expr8 = Subtract(
    Add(
        Variable("x"), Const(4)
    ),
    Add(
        Const(2), Const(3))
)
print(expr8.to_mini_string())

expr9 = Subtract(
    Add(
        Variable("x"), Const(4)
    ),
    Subtract(
        Const(2), Const(3))
)
print(expr9.to_mini_string())

expr10 = Subtract(
    Subtract(
        Variable("x"), Const(4)
    ),
    Add(
        Const(2), Const(3))
)
print(expr10.to_mini_string())

expr11 = Subtract(
    Subtract(
        Variable("x"), Const(4)
    ) , Const(4)

)
print(expr11.to_mini_string())

expr12 = Multiply(
    Subtract(
        Variable("x"), Const(4)
    ) , Subtract(Const(4),Const(4))

)
print(expr12.to_mini_string())


expr13 = Subtract(
    Add(Subtract(
        Variable("x"), Const(4)),Const(87)
    ), Subtract(Subtract(Const(4),Divide(Const(4),Const(88))),Subtract(Variable("z"),Multiply(Variable("y"),Const(87))))

)
print(expr13.to_mini_string())

expr14 = Subtract(
    Subtract(Subtract(
        Variable("x"), Const(4)),Add(Const(87),Variable('U'))
    ), Subtract(Subtract(Const(4),Divide(Const(4),Const(88))),Subtract(Variable("z"),Multiply(Variable("y"),Const(87))))

)
print(expr14.to_mini_string())

expr15 = Divide(
    Subtract(
        Variable("x"), Const(4)
    ) , Multiply(Const(4),Const(4))

)
print(expr15.to_mini_string())

expr16 = Divide(
    Subtract(
        Variable("x"), Const(4)
    ) , Divide(Const(3),Const(4))

)
print(expr16.to_mini_string())
# ______________________________________________________________________________________________________________________
a = Multiply(Multiply(Const(2), Variable("b")), Multiply(Const(2), Const(3)))
b = Multiply(Multiply(Const(2), Variable("b")), Add(Const(2), Const(3)))
c = Add(Multiply(Const(2), Variable("b")), Multiply(Const(2), Const(3)))
d = Add(Multiply(Const(2), Variable("b")), Add(Const(2), Const(3)))
e = Multiply(Add(Const(2), Variable("b")), Multiply(Const(2), Const(3)))
f = Multiply(Add(Const(2), Variable("b")), Add(Const(2), Const(3)))
g = Add(Add(Const(2), Variable("b")), Multiply(Const(2), Const(3)))
h = Add(Add(Const(2), Variable("b")), Add(Const(2), Const(3)))

if a.to_mini_string() != "2*b*2*3":
    print ("1 Error: expected 2*b*2*3")
else:
    print( "1 Оки-доки" )

if b.to_mini_string() != "2*b*(2+3)":
    print ("2 Error: expected 2*b*(2+3)")
else:
    print( "2 Оки-доки" )
if c.to_mini_string() != "2*b+2*3":
    print ("3 Error: expected 2*b+2*3")
else:
    print( "3 Оки-доки" )
if d.to_mini_string() != "2*b+2+3":
    print ("4 Error: expected 2*b+2+3")
    print (d.to_mini_string())
else:
    print( "4 Оки-доки" )
if e.to_mini_string() != "(2+b)*2*3":
    print ("5 Error: expected (2+b)*2*3")
else:
    print( "5 Оки-доки" )
if f.to_mini_string() != "(2+b)*(2+3)":
    print ("6 Error: expected (2+b)*(2+3)")
else:
    print( "6 Оки-доки" )
if g.to_mini_string() != "2+b+2*3":
    print ("7 Error: expected 2+b+2*3")
    print (g.to_mini_string())
else:
    print( "7 Оки-доки" )
if h.to_mini_string() != "2+b+2+3":
    print ("8 Error: expected 2+b+2+3")
    print (h.to_mini_string() )
else:
    print( "8 Оки-доки" )


