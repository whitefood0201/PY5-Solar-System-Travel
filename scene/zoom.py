import math

#https://zh.wikipedia.org/zh-cn/%E5%8F%83%E6%95%B8%E6%96%B9%E7%A8%8B

def line_zoom(u, v):
    def line(w, h, t):
        w2 = w + u*t
        h2 = h + v*t
        return w2, h2
    return line

def abs_sin_zoom(a):
    def abs_sin(w, h, t):
        w2 = w + a*abs(math.sin(math.radians(t)))
        h2 = h + a*abs(math.sin(math.radians(t)))
        return w2, h2
    return abs_sin