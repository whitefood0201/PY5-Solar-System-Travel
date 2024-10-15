import functional.FLfunctions as fl

class AnimetionChain:
    def __init__(self, func=None, next=None, endTime=0, isHead=False):
        self.next: AnimetionChain = next
        self.endTime: int = endTime
        self.isHead = isHead
        self.func = lambda a, b, t: (a, b) if func == None else func

    def setHead(self, isHead):
        self.isHead = isHead
        return self

    def setNext(self, next):
        self.next = next
        return self

    def setFunc(self, func):
        self.func = func
        return self
    
    def setEndTime(self, endTime):
        self.endTime = endTime
        return self

    def animation(self, a:float, b:float, t:int) -> tuple[float, float]:
        endT = self.endTime
        next = self.next
        if t < endT or next == None:
            return self.func(a, b, t)
            
        x1, y1 = self.func(a, b, endT)
        return self.next.animation(x1, y1, t-endT)

    def __str__(self):
        obj = {
            "isHead": self.isHead,
            "function": str(self.func),
            "endTime": self.endTime,
            "next": str(self.next)
        }
        return str(obj)
    
def AnimationBuilder(animationList:list[tuple[callable, int]]):
    """
        Build a animation chain from the giving list.   
        The list should be the list of animation functions, like `zoom`, `move`, `color`.   
        return the head of the chain.   
    """
    def factory(chain:AnimetionChain, animationTuple:tuple[callable, int], index:int):
        c = AnimetionChain()
        func, t = animationTuple
        c.setEndTime(t)
        c.setFunc(func)

        chain.setNext(c)
        return chain.next
    head = AnimetionChain(isHead=True)
    fl.reduce(factory, animationList, head)
    return head


def move(func_name:str) -> callable:
    """ load a move function from the function name"""
    dd = __import__("shapelib.animetion.move")
    f = getattr(dd.animetion.move, func_name, None)
    return f

def zoom(func_name:str) -> callable:
    """ load a zoom function from the function name"""
    dd = __import__("shapelib.animetion.zoom")
    f = getattr(dd.animetion.zoom, func_name, None)
    return f