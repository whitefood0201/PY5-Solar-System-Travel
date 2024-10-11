import py5
import functional.FLfunctions as fl
import shapelib.sceneFactory as sf
import shapelib.shapes as sp
from shapelib.shapes import *

SCENE_PATH = ".\\shape.xml"
        
def shapeDraw(shape:sp.AbsShape):
    shape.draw()
def shapeUpdate(shape:sp.AbsShape):
    shape.update()


def initScenes():
    scenes = sf.scenes_processor(SCENE_PATH)
    sceneIndex = 0
    sceneTick = 0

    currScene = None
    def updateScene():
        nonlocal sceneIndex, sceneTick, scenes
        scene = scenes[sceneIndex]
        print(sceneTick)
        if sceneTick == scene["duration"]:
            sceneIndex +=1
        sceneTick += 1
        return scene
    
    def updateShapes():
        nonlocal currScene
        currScene = updateScene()
        
        currScene["shapes"] = fl.filter(lambda shp: not shp.removed(), currScene["shapes"])
        fl.map(shapeUpdate, currScene["shapes"])
        currScene["shapes"] = currScene["shapes"]

    def getScene():
        return currScene
    
    return updateShapes, getScene
updateShapes, getScene = initScenes()

def setup():
    py5.size(640, 640)

def draw():
    updateShapes()
    scene = getScene()
    sps = scene["shapes"]
    
    py5.background(10, 10, 20)
    fl.map(shapeDraw, sps)

    title = scene["title"]
    py5.fill(title["color"])
    py5.text_size(title["font-size"])
    py5.text(title["name"], 10, 30)

py5.run_sketch()