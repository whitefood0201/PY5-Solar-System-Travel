import py5
import functional.FLfunctions as fl
import shapelib.sceneFactory as sf
from shapelib.scenelib import *
from shapelib.shapes import *

SCENES_PATH = ".\\scenes.txt"
DEBUG = True
#DEBUG = False

def initVelocity():
    VELOCITY = [1, 2, 4, 8]
    velocityIndex = 0

    def change(dir:int):
        """ dir: -1 or 1"""
        nonlocal velocityIndex

        if not DEBUG: return

        velocityIndex += dir

        # border check
        if velocityIndex >= len(VELOCITY):
            velocityIndex = 0
        elif velocityIndex < 0:
            velocityIndex = len(VELOCITY)-1

    def getVelocity():
        return VELOCITY[velocityIndex]
    
    return lambda : change(1), lambda : change(-1), getVelocity
vFaster, vSlower, getV = initVelocity()

def initScenes():
    scenes = sf.scenes_processor(SCENES_PATH)
    sceneIndex = 0
    sceneTick = 0
    currScene = scenes[0]

    def updateScene():
        nonlocal sceneIndex, sceneTick, scenes
        
        # reset
        if sceneIndex >= len(scenes): 
            sceneIndex = 0 
            sceneTick = 0
            changeStop()

        scene = scenes[sceneIndex]
        if sceneTick >= scene["duration"]:
            sceneIndex +=1
            sceneTick = 0
        sceneTick += getV()
        return scene
    
    def updateShapes():
        nonlocal currScene
        currScene = updateScene()
        
        # def updLayer(layer):
        #     return fl.filter(lambda shp: not shp.removed(), layer)
        # layers = fl.map(updLayer, currScene["layers"])

        def upd(layer):
            fl.map(shapeUpdate(sceneTick), layer)
        fl.map(upd, currScene["layers"])

        #currScene["layers"] = layers

    def getScene():
        return currScene
    
    return updateShapes, getScene
updateShapes, getScene = initScenes()

def initStop():
    stop:bool = True 
    def getStop() -> bool:
        return stop
    def changeStop():
        nonlocal stop
        stop = not stop
    return changeStop, getStop
changeStop, getStop = initStop()


def debugging():
    drawText("velocity: {}".format(getV()), 580, 25, size=25, color=100, align=py5.CENTER)


# ----------------------PY5--------------------------


def setup():
    py5.size(640, 640)

def draw():
    resetAll()
    scene = getScene()
    layers:list[list[AbsShape]] = scene["layers"]

    py5.background(10, 10, 20)
    
    for shapes in layers:
        fl.map(shapeDraw, shapes)

    title = scene["title"]
    drawText(title["name"], 10, 30, size=title["font-size"], color=title["color"])

    if DEBUG:
        debugging()
    
    if not getStop():
        updateShapes() 
        return
    
    # draw "PAUSE"
    drawText("PAUSE", 320, 320, size=40, color=100, align=py5.CENTER)

def key_pressed(e:py5.Py5KeyEvent):
    key = e.get_key()
    match key:
        case " ":
            changeStop()
        case "p":
            vFaster()
        case "o":
            vSlower()

py5.run_sketch()
