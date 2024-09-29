import py5

class my_shape_class:
    def __init__(self, shape_func, x, y, w, h, color=0xFFFFFFFF, move_func=None, zoom_func=None):
        self.shape_func = shape_func
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

        def defaultMove(x, y, t):
            x2 = x-t
            return x2, y
        def defaultZoom(w, h, t):
            return w, h
        self.move_func = defaultMove if move_func == None else move_func
        self.zoom_func = defaultZoom if zoom_func == None else zoom_func
        self.getPosition, self.getSize, self.update = self.state_saver()

    def draw(self):
        py5.fill(self.color)
        x, y = self.getPosition()
        w, h = self.getSize()
        self.shape_func(x, y, w, h)
    
    def state_saver(self):
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        time = 0
        def getPosition():
            return x, y
        def getSize():
            return w, h
        def update():
            nonlocal x, y, w, h, time
            x, y = self.move_func(self.x, self.y, time)
            w, h = self.zoom_func(self.w, self.h, time)
            time+=1
        return getPosition, getSize, update