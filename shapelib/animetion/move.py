import math

#https://zh.wikipedia.org/zh-cn/%E5%8F%83%E6%95%B8%E6%96%B9%E7%A8%8B

def no_move():
    def inner(x, y, t):
        return x, y
    return inner

def sin_move(v, a):
    def s(x, y, t):
        x2 = x + v*t
        y2 = y + a * math.sin(math.radians(t))
        return x2, y2
    return s

def cos_move(v, a):
    def c(x, y, t):
        x2 = x + v*t
        y2 = y + a * math.cos(math.radians(t))
        return x2, y2
    return c

def tan_move(v, a):
    def t(x, y, t):
        x2 = x + v*t
        y2 = y - a * math.tan(math.radians(t))
        return x2, y2
    return t

def circle_move(r, x0=0, y0=0, phi=90, rate=30):
    def circle(x, y, t):
        t /= rate
        x2 = x + r*math.cos(t+phi) + x0
        y2 = y + r*math.sin(t+phi) + y0
        return x2, y2
    return circle

def ellipse_move(a, b, x0=0, y0=0, phi=180, rate=30):
    def ellipse(x, y, t):
        t /= rate
        x2 = x + a*math.cos(t+phi) + x0
        y2 = y + b*math.sin(t+phi) + y0
        return x2, y2
    return ellipse

def line_move(x0, y0, dx, dy):
    def line(x, y, t):
        x2 = x + x0 + dx*t
        y2 = y + y0 + dy*t
        return x2, y2
    return line

def keepATime(startTime, keepTime):
    def move(x, y, t):
        if t < startTime:
            return defaultMove(x, y, t)
        if t > startTime and t < startTime+keepTime:
            return x-startTime, y
        return defaultMove(x, y, t-startTime-keepTime)
    return move

def moveTo(dx, dy, timeUse):
    ddx:float = dx/timeUse
    ddy:float = dy/timeUse
    def move(x, y, t):
        if t >= timeUse: return x+dx, y+dy
        x2 = x + ddx*t
        y2 = y + ddy*t
        return x2, y2
    return move

def moveToThenRecover(dx, dy, timeUse, keepTime, startIn=0):
    ddx:float = dx/timeUse
    ddy:float = dy/timeUse
    def move(x, y, t):
        if t <= startIn: return x, y
        t -= startIn

        if t <= timeUse:
            x2 = x + ddx*t
            y2 = y + ddy*t
            return x2, y2
        
        if t > timeUse and t <= timeUse+keepTime:
            return x + dx, y + dy
        
        if t > timeUse+keepTime and t <= timeUse*2+keepTime:
            x += dx
            y += dy
            x2 = x - ddx*(t-timeUse-keepTime)
            y2 = y - ddy*(t-timeUse-keepTime)
            return x2, y2
        
        if t > timeUse*2+keepTime: return x, y
    
    return move

def parabola_move(p, x0=0, y0=0):
    def parabola(x, y ,t):
        t /= 30 
        x2 = x + 2*p*(t + x0)
        y2 = y - 2*p*(t + y0)*(t + y0)
        return x2, y2
    return parabola

def defaultMove():
    def default(x, y, t):
        x2 = x-t
        return x2, y
    return default
