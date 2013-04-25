from numpy import *

def pointPotential(x,y,q,posx,posy):
    """Takes in x y q and posx and posy to determine the potential at posx posy """
    k = 8.99e9
    V = (k * q) / (sqrt(x**2 + (y - sqrt((posx**2 + posy**2)))**2))
    return V

def dipolePotential(x,y,q,d):
    """Takes x, y and the charge and the distance between the points """
    k = 8.99e9
    V = (k * q) / (sqrt(x**2 + (y - d)**2)) - (k * q) / (sqrt(x**2 + (y + d)**2))
    return V
