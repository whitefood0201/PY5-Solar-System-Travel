import math

#https://zh.wikipedia.org/zh-cn/%E5%8F%83%E6%95%B8%E6%96%B9%E7%A8%8B

def line_zoom(dw, dh):
    def line(w, h, t):
        w2 = w + dw*t
        h2 = h + dh*t
        return w2, h2
    return line

def abs_sin_zoom(a):
    def abs_sin(w, h, t):
        w2 = w + a*abs(math.sin(math.radians(t)))
        h2 = h + a*abs(math.sin(math.radians(t)))
        return w2, h2
    return abs_sin

def zoomToZero(timeUse):
    def zoom(w, h, t):
        if t >= timeUse: return 0, 0
        w2 = w - t*w/timeUse
        h2 = h - t*h/timeUse
        return w2, h2
    return zoom

def zoomTo(dw, dh, timeUse):
    ddw:float = dw/timeUse
    ddh:float = dh/timeUse
    def zoom(w, h, t):
        if t >= timeUse: return w+dw, h+dh
        w2 = w + ddw*t
        h2 = h + ddh*t
        return w2, h2
    return zoom

def zoomToThenRecover(dw, dh, timeUse, keepTime, startIn=0):
    ddw:float = dw/timeUse
    ddh:float = dh/timeUse
    def zoom(w, h, t):
        if t <= startIn: return w, h
        t -= startIn
        
        if t <= timeUse:
            w2 = w + ddw*t
            h2 = h + ddh*t
            return w2, h2
        
        if t > timeUse and t <= timeUse+keepTime:
            return w + dw, h + dh
        
        if t > timeUse+keepTime and t <= timeUse*2+keepTime:
            w += dw
            h += dh
            w2 = w - ddw*(t-timeUse-keepTime)
            h2 = h - ddh*(t-timeUse-keepTime)
            return w2, h2
        
        if t > timeUse*2+keepTime: return w, h
    
    return zoom


def defaultZoom(w, h, t):
    return w, h