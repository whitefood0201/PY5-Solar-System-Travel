import py5
import functional.FLfunctions as fl
import shapelib.sceneFactory as sf
from shapelib.scenelib import *
from shapelib.shapes import *

SCENE_PATH = ".\\shape.xml"

def initScenes():
    scenes = sf.scenes_processor(SCENE_PATH)
    sceneIndex = 0
    sceneTick = 0
    currScene = scenes[0]

    def updateScene():
        nonlocal sceneIndex, sceneTick, scenes
        scene = scenes[sceneIndex]
        #print(sceneTick)
        if sceneTick >= scene["duration"]:
            sceneIndex +=1
            sceneTick = 0
        sceneTick += 1
        return scene
    
    def updateShapes():
        nonlocal currScene
        currScene = updateScene()
        
        def updLayer(layer):
            return fl.filter(lambda shp: not shp.removed(), layer)
        layers = fl.map(updLayer, currScene["layers"])

        def upd(layer):
            fl.map(shapeUpdate, layer)
        fl.map(upd, layers)

        currScene["layers"] = layers

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


# ----------------------PY5--------------------------


def setup():
    py5.size(640, 640)

def draw():
    resetAll()
    scene = getScene()
    layers:list[list[sp.AbsShape]] = scene["layers"]

    py5.background(10, 10, 20)
    
    for shapes in layers:
        fl.map(shapeDraw, shapes)

    title = scene["title"]
    drawText(title["name"], 10, 30, size=title["font-size"], color=title["color"])

    if not getStop():
        updateShapes() 
        return
    
    # draw "PAUSE"
    drawText("PAUSE", 320, 320, size=40, color=100, align=py5.CENTER)

def key_pressed(e:py5.Py5KeyEvent):
    if e.get_key() == " ":
        changeStop()

py5.run_sketch()