import py5

class AbsShape:
    def __init__(self, x=0, y=0, w=0, h=0, color="#FFFFFFFF", move=None, zoom=None, border=None):
        self.x:int = x
        self.y:int = y
        self.w:int = w
        self.h:int = h
        self.color:str = color
        self.border:str = border
        self.move:callable = move
        self.zoom:callable = zoom
        self.tick:int = 0
        self.maxLive:int = -1
        self.update = self.state_saver()

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        self.update = self.state_saver()
        return self
    
    def setSize(self, w:int, h:int):
        self.w = w
        self.h = h
        self.update = self.state_saver()
        return self
    
    def setColor(self, color:str):
        self.color = color
        return self
    
    def setMove(self, move):
        self.move = move
        return self
    
    def setZoom(self, zoom):
        self.zoom = zoom
        return self
    
    def setBorder(self, border):
        self.border = border
        return self
        
    def removed(self) -> bool:
        outOfBorder = self.x == -self.w or self.y == 640+self.h
        outTime = self.tick == self.maxLive
        return not (outOfBorder or outTime)
    
    def draw(self):
        py5.fill(self.color)
        if self.border != None: py5.stroke(self.border)
        self.inner_draw()
        py5.no_stroke()

    def inner_draw(self):
        raise NotImplementedError("draw() hasn't implement")
        
    def state_saver(self):
        ori_x = self.x
        ori_y = self.y
        ori_w = self.w
        ori_h = self.h
        def update():
            nonlocal ori_x, ori_y, ori_w, ori_h
            self.x, self.y = self.move(ori_x, ori_y, self.tick)
            self.w, self.h = self.zoom(ori_w, ori_h, self.tick)
            self.tick+=1
        return update
    
    def __str__(self):
        dict = {
            "x": self.x,
            "y": self.y,
            "w": self.w,
            "h": self.h,
            "color": self.color,
            "border": self.border,
            "move": self.move,
            "zoom": self.zoom,
            "tick": self.tick,
        }
        return str(self.__class__) + ": " + str(dict)


class Rect(AbsShape):
    def inner_draw(self):
        py5.rect(self.x, self.y, self.w, self.h)


class Ellipse(AbsShape):
    def inner_draw(self):
        py5.ellipse(self.x, self.y, self.w, self.h)