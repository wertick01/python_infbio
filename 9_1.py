import pickle
import math

# Честно, я хз что поменять в файле, потому что
# в жопайтере всё запускается и работает нормально

class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)

    def __div__(self, other):
        sr, si, orr, oi = self.real, self.imag, other.real, other.imag # short forms
        r = float(orr**2 + oi**2)
        return Complex((sr*orr+si*oi)/r, (si*orr-sr*oi)/r)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __neg__(self):   # defines -c (c is Complex)
        return Complex(-self.real, -self.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result

    def __repr__(self):
        return 'Complex: ' + str(self)

    def __pow__(self, power):
        raise NotImplementedError ('self**power is not yet impl. for Complex')

    def return_dict(self):
        if self.imag == 0:
            result = {"Complex": "%.2f+0.00i" % (self.real)}
        elif self.real == 0:
            if self.imag >= 0:
                result = {"Complex": "0.00+%.2fi" % (self.imag)}
            else:
                result = {"Complex": "0.00-%.2fi" % (abs(self.imag))}
        elif self.imag > 0:
            result = {"Complex": "%.2f+%.2fi" % (self.real, self.imag)}
        else:
            result = {"Complex": "%.2f-%.2fi" % (self.real, abs(self.imag))}
        return result

    def save_number(self):
        with open('9_1.pickle', 'wb') as handle:
            return pickle.dump(self.return_dict(), handle)

    def load_number(self, filename):
        with open(filename, 'rb') as handle:
            return pickle.load(handle)

x = Complex(2,1)
y = Complex(5,6).save_number()
z = Complex(3, 2).load_number('9_1.pickle')