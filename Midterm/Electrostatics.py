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

def pointField(x, y, q, Xq, Yq):
    """Takes in x, y, q, and Xq and Yq to determine the x and y compenents of an E field"""
    k = 8.99e9
    Ex = k * q *(x - Xq)/((x - Xq)**2 + (y - Yq)**2)**.5
    Ey = k * q *(y - Yq)/((x - Xq)**2 + (y - Yq)**2)**.5
    return (Ex, Ey)
