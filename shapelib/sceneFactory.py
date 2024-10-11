import xml.etree.cElementTree as ET
import functional.FLfunctions as fl
import functional.lambdas as la
import shapelib.move as mv
import shapelib.zoom as zm
import shapelib.shapes as sp

def scenes_processor(path:str) -> list[tuple[list, str, int]]:
    tree = ET.ElementTree(file=path)
    root = tree.getroot()
    xmlScenes = root.findall(path="scene")
    scenes = fl.map(genScene, xmlScenes)
    return scenes

def genScene(xmlScene:ET.Element) -> dict[str, any]:
    dic = {}
    xmlShapes = xmlScene.find("shapes")
    xmlTitle = xmlScene.find("title")

    dic["duration"] = int(xmlScene.get("duration", default=0))
    dic["title"] = genTitle(xmlTitle)
    dic["shapes"] = genShapes(xmlShapes)
    return dic

def genTitle(xmlTitle:ET.Element) -> dict[str, any]:
    title = {}
    title["name"] = xmlTitle.text if xmlTitle.text != None else "scene"  
    title["color"] = xmlTitle.get("color", default="#FFFFFF")
    title["font-size"] = int(xmlTitle.get("font-size", default=32))
    return title


def genShapes(shapes:ET.Element) -> list[sp.AbsShape]:
    ellipse = fl.map(genEllip, shapes.findall(path="ellipse"))
    rects = fl.map(genRect, shapes.findall(path="rect"))
    return rects + ellipse

def genRect(rectTag:ET.Element):
    x = int(rectTag.get("x", default=0))
    y = int(rectTag.get("y", default=0))
    w = int(rectTag.get("w", default=0))
    h = int(rectTag.get("h", default=0))
    color = rectTag.get("color", default="#FFFFFF")
    border = rectTag.get("border", default=None)
    move = getMove(rectTag.find(path="move"))
    zoom = getZoom(rectTag.find(path="zoom"))

    rect = sp.Rect().setPosition(x, y).setSize(w, h).setColor(color).setBorder(border).setMove(move).setZoom(zoom)
    return rect

def genEllip(ellipTag:ET.Element):
    x = int(ellipTag.get("x", default=0))
    y = int(ellipTag.get("y", default=0))
    w = int(ellipTag.get("w", default=0))
    h = int(ellipTag.get("h", default=0))
    color = ellipTag.get("color", default="#FFFFFF")
    border = ellipTag.get("border", default=None)
    move = getMove(ellipTag.find(path="move"))
    zoom = getZoom(ellipTag.find(path="zoom"))

    ellip = sp.Ellipse().setPosition(x, y).setSize(w, h).setColor(color).setBorder(border).setMove(move).setZoom(zoom)
    return ellip

def getZoom(zoomTag:ET.Element):
    if zoomTag == None: return zm.defaultZoom
    name = zoomTag.text
    keys = fl.dict_map(la.intDict, zoomTag.attrib)
    return zm.zoom(name)(**keys)

def getMove(moveTag:ET.Element):
    if moveTag == None: return mv.defaultMove
    name = moveTag.text
    keys = fl.dict_map(la.intDict, moveTag.attrib)
    return mv.move(name)(**keys)
