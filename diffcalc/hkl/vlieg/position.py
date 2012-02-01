from diffcalc.utils import AbstractPosition
try:
    from Jama import Matrix
except ImportError:
    from diffcalc.npadaptor import Matrix
from math import pi
TORAD = pi / 180
TODEG = 180 / pi

class VliegPosition(AbstractPosition):
    """The position of all six diffractometer axis"""
    def __init__(self, alpha=None, delta=None, gamma=None, omega=None, chi=None, phi=None):
        self.alpha = alpha
        self.delta = delta
        self.gamma = gamma
        self.omega = omega
        self.chi = chi
        self.phi = phi
    
    def clone(self):
        return VliegPosition(self.alpha, self.delta, self.gamma, self.omega, self.chi, self.phi)
        
    def changeToRadians(self):
        self.alpha *= TORAD
        self.delta *= TORAD
        self.gamma *= TORAD
        self.omega *= TORAD
        self.chi *= TORAD
        self.phi *= TORAD

    def changeToDegrees(self):
        self.alpha *= TODEG
        self.delta *= TODEG
        self.gamma *= TODEG
        self.omega *= TODEG
        self.chi *= TODEG
        self.phi *= TODEG
        
    def inRadians(self):
        pos = self.clone()
        pos.changeToRadians()
        return pos
        
    def inDegrees(self):
        pos = self.clone()
        pos.changeToDegrees()
        return pos

    def nearlyEquals(self, pos2, maxnorm):
        pos1 = Matrix([[self.alpha, self.delta, self.gamma, self.omega, self.chi, self.phi]])
        pos2 = Matrix([[pos2.alpha, pos2.delta, pos2.gamma, pos2.omega, pos2.chi, pos2.phi]])
        return pos1.minus(pos2).normF() <= maxnorm
    
    def totuple(self):
        return (self.alpha, self.delta, self.gamma, self.omega, self.chi, self.phi)
    
    def __str__(self):
        return "VliegPosition(alpha %s delta: %s gamma: %s omega: %s chi: %s  phi: %s)" % \
              (`self.alpha`, `self.delta`, `self.gamma`, `self.omega`, `self.chi`, `self.phi`)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, b):
        return self.nearlyEquals(b, .001)
