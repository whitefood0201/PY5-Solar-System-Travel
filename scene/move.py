import math

#https://zh.wikipedia.org/zh-cn/%E5%8F%83%E6%95%B8%E6%96%B9%E7%A8%8B

def m(x, y, t):
    #x = ori_x + 50 * math.cos(math.radians(t))
    x2 = x + t
    y2 = y + 100 * math.sin(math.radians(t))
    return x2, y2

def m1(x, y, t):
    #x = ori_x + 50 * math.cos(math.radians(t))
    x2 = x + t
    y2 = y + 100 * math.cos(math.radians(t))
    #y = ori_y + t
    #w2 = ori_w + t
    #h = ori_h + t
    return x2, y2

def circle_move():
    None