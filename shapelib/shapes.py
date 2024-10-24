import py5
import shapelib.scenelib as sl
import shapelib.animetion.animetionlib as al

# TODO: Rewrite using py5Shape
# I just saw this thing...

class AbsShape:
    def __init__(self, x=0, y=0, w=0, h=0, color="#FFFFFFFF", layer=2, moveChain=None, zoomChain=None, border=None):
        self.x:int = x
        self.y:int = y
        self.w:int = w
        self.h:int = h
        self.color:str = color
        self.border:str = border
        self.moveChain:al.AnimetionChain = moveChain
        self.zoomChain:al.AnimetionChain = zoomChain
        self.tick:int = 0
        self.maxLive:int = -1
        self.update = self.state_saver()
        self.layer = layer

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        self.update = self.state_saver()
        return self

    def setLayer(self, layer:int):
        """ layer: 0-4 """
        self.layer = layer
        return self
    
    def setSize(self, w:int, h:int):
        self.w = w
        self.h = h
        self.update = self.state_saver()
        return self
    
    def setColor(self, color:str):
        self.color = color
        return self
    
    def setMoveChain(self, moveChain):
        self.moveChain = moveChain
        return self
    
    def setZoomChain(self, zoomChain):
        self.zoomChain = zoomChain
        return self
    
    def setBorder(self, border):
        self.border = border
        return self
        
    # def removed(self) -> bool:
    #     outOfBorderRight = self.x < -self.w-200 or self.y < -self.h-200
    #     outOfBorderLeft = self.x > 640+self.w+200 or self.y > 640+self.h+200
    #     outOfBorder = outOfBorderRight or outOfBorderLeft
    #     outOfSize = self.w == 0 or self.h == 0
    #     outTime = self.tick == self.maxLive
    #     return not (outOfBorder or outTime or outOfSize)
    
    def draw(self):
        sl.resetAll()
        if self.border != None: py5.stroke(self.border)
        self.inner_draw()
        sl.resetAll()

    def inner_draw(self):
        raise NotImplementedError("draw() hasn't implement")
        
    def state_saver(self):
        ori_x = self.x
        ori_y = self.y
        ori_w = self.w
        ori_h = self.h
        def update(tick):
            nonlocal ori_x, ori_y, ori_w, ori_h
            self.x, self.y = self.moveChain.animation(ori_x, ori_y, tick)
            self.w, self.h = self.zoomChain.animation(ori_w, ori_h, tick)
        return update
    
    def __str__(self):
        dict = {
            "x": self.x,
            "y": self.y,
            "w": self.w,
            "h": self.h,
            "color": self.color,
            "border": self.border,
            "move": self.moveChain,
            "zoom": self.zoomChain,
            "tick": self.tick,
        }
        return str(self.__class__) + ": " + str(dict)


class Rect(AbsShape):
    def __init__(self, x=0, y=0, w=0, h=0, color="#FFFFFFFF", layer=2, move=None, zoom=None, border=None, rectMode=py5.CORNER):
        super().__init__(x, y, w, h, color, layer, move, zoom, border)
        self.rectMode = rectMode

    def inner_draw(self):
        py5.fill(self.color)
        py5.rect_mode(self.rectMode)
        py5.rect(self.x, self.y, self.w, self.h)

    def setRectMode(self, rectMode):
        self.rectMode = rectMode
        return self


class Ellipse(AbsShape):
    def inner_draw(self):
        py5.fill(self.color)
        py5.ellipse(self.x, self.y, self.w, self.h)


class Star(AbsShape):

    def __init__(self, x=0, y=0, w=0.5, c1="#0000aa", c2="#0000ff", move=None, zoom=None, border=None):
        super().__init__(x, y, w, 0, None, move, zoom, border)
        self.c1 = c1
        self.c2 = c2

    def setColor(self, c1: str, c2: str):
        self.c1 = c1
        self.c2 = c2
        return self
    
    def setSize(self, w: int):
        self.w = w
        self.update = self.state_saver()
        return self
    
    # def removed(self) -> bool:
    #     outOfBorder = self.x == -self.w*10 or self.y == 640+self.w*10
    #     outTime = self.tick == self.maxLive
    #     return not (outOfBorder or outTime)

    def inner_draw(self):
        py5.fill(self.c1)
        py5.stroke(self.c2)

        x = self.x
        y = self.y
        w = self.w
        py5.begin_shape()
        py5.vertex(x, y)
        py5.bezier_vertex(x, y, x, y+10*w, x+10*w, y+10*w)
        py5.bezier_vertex(x+10*w, y+10*w, x, y+10*w, x, y+20*w)
        py5.bezier_vertex(x, y+20*w, x, y+10*w, x-10*w, y+10*w)
        py5.bezier_vertex(x-10*w, y+10*w, x, y+10*w, x, y)
        py5.end_shape()

class Ring(AbsShape):
    def __init__(self, x=0, y=0, w=0, h=0, layer=2, moveChain=None, zoomChain=None, border=255, borderSize=0, innerShape=None):
        super().__init__(x, y, w, h, None, layer, moveChain, zoomChain, border)
        self.borderSize = borderSize
        self.innerShape:AbsShape = innerShape
    
    def setBorder(self, border, borderSize):
        self.border = border
        self.borderSize = borderSize
        return self
    
    def setPosition(self, x, y):
        super().setPosition(x, y)

        if self.innerShape != None:
            self.innerShape.setPosition(x, y)
        
        return self
    
    def setInnerShape(self, innerShape:AbsShape):
        if innerShape == None: return self

        self.innerShape = innerShape
        innerShape.setPosition(innerShape.x+self.x, innerShape.y+self.y)
        return self
    
    def state_saver(self):
        superUpdate = super().state_saver()
        def update(tick):
            superUpdate(tick)
            self.innerShape.update(tick)
        return update
        

    def inner_draw(self):
        x, y, w, h = self.x, self.y, self.w, self.h
        borderSize = self.borderSize
        border = self.border
        innerShape = self.innerShape

        py5.no_fill()
        py5.stroke_weight(borderSize)
        py5.stroke(border)
        py5.arc(x, y, w, h, py5.PI, 2*py5.PI)

        if (innerShape != None):
            innerShape.draw()

        py5.no_fill()
        py5.stroke_weight(borderSize)
        py5.stroke(border)
        py5.arc(x, y, w, h, 0, py5.PI)


class Image(AbsShape):
    def __init__(self, x=0, y=0, w=0, h=0, layer=2, moveChain=None, zoomChain=None, src=None):
        super().__init__(x, y, w, h, None, layer, moveChain, zoomChain, None)
        self.src = src

    def setSrc(self, src:str):
        self.src = src
        return self
    
    def inner_draw(self):
        py5.image(py5.load_image(self.src), self.x, self.y, self.w, self.h)


class Text(AbsShape):
    def __init__(self, x=0, y=0, w=0, color="#FFFFFFFF", layer=2, moveChain=None, zoomChain=None, msg=""):
        super().__init__(x, y, w, None, color, layer, moveChain, zoomChain, None)
        self.msg = msg

    def setMsg(self, msg):
        self.msg = msg
        return self
    
    def setSize(self, w: int):
        return super().setSize(w, 0)

    def inner_draw(self):
        py5.text_align(py5.CENTER)
        py5.fill(self.color)
        py5.text_size(self.w)
        py5.text(self.msg, self.x, self.y)