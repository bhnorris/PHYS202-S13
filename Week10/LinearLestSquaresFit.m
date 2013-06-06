function [ slope,intercept,slerr,interr ] = LinearLestSquaresFit(x,y)
%Take in arrays representing (x,y) values for a set of linearly varying data and 
%perform a linear least squares regression, Return the resulting slope and intercept
%parameter of the best fit line with their uncertainties.
    n = len(x)
    n = float(n)
    X = sum(x) / n
    Y = sum(y) / n
    X2 = sum(x**2) / n
    XY = sum(x*y) / n
    slope = (XY - X*Y) / (X2 - X**2)
    intercept = (X2*Y - X*XY) / (X2 - X**2)
    d = y - (slope*x + intercept)
    D2 = sum(d**2)/n
    slerr = sqrt((1/(n-2))*(D2/(X2 - X**2)))
    interr = sqrt((1/(n-2))*(D2*X2/(X2 - X**2)))
    return slope,intercept,slerr,interr


end

