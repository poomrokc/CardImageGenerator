from PIL import Image, ImageDraw, ImageFont, ImageFile
import time
import datetime
import os
import requests
import json
ImageFile.LOAD_TRUNCATED_IMAGES = True
with open('./globalConfig.json','r',encoding='utf-8') as f:
    globalConfig = json.load(f)

with open('./backgroundConfig.json','r',encoding='utf-8') as f:
    backgroundConfig = json.load(f)

with open('bigData.json','r',encoding='utf-8') as f:
    data = json.load(f)

def logError(iden,message):
    print("Error detected for data id:",iden,"Message:",message)

folderName = str(datetime.datetime.now()).replace(":","_")
os.makedirs(globalConfig["path"]["output"] + folderName)
os.makedirs(globalConfig["path"]["output"] + folderName + "/grouped")
os.makedirs(globalConfig["path"]["output"] + folderName + "/raw")

bField = globalConfig["backgroundSelectorField"]

completedCount=0

for people in data:
    if not ("id" in people) :
        logError("Not Found","No id Provided")
        continue
    if not (bField in people):
        logError(people["id"],"No background selector field")
        continue
    if not (people[bField] in backgroundConfig):
        logError(people["id"],"Provided background does not exist")
        continue
    
    background = backgroundConfig[people[bField]]
    baseImage = Image.open(globalConfig["path"]["background"] + background["fileName"]).convert('RGBA')
    draw = ImageDraw.Draw(baseImage)
    
    for prop in background["props"]:
        if not(prop["field"] in people):
            logError(people["id"],"Field " + prop["field"] + " does not exist")
            break
        if prop["type"] == "text":
            text = " " + str(people[prop["field"]]) + " "
            font = ImageFont.truetype(globalConfig["path"]["font"] + prop["font"], prop["size"])
            size = draw.textsize(text, font=font)
            drawX = prop["xTopLeft"]
            drawY = prop["yTopLeft"]
            if prop["xAlign"] == "right":
                drawX = drawX + prop["xLength"] - size[0]
            elif prop["xAlign"] == "center":
                drawX = drawX + (prop["xLength"] - size[0]) / 2
            if prop["yAlign"] == "bottom":
                drawY = drawY + prop["yLength"] - size[1]
            elif prop["yAlign"] == "center":
                drawY = drawY + (prop["yLength"] - size[1]) / 2
            draw.text((drawX,drawY), text, font=font, fill=eval(prop["fill"]))    
        else:
            if people[prop["field"]]["type"]=="url":
                try:
                    r = requests.get(people[prop["field"]]["path"], stream=True)
                    paste = Image.open(r.raw).convert('RGBA')
                    paste = paste.resize((prop["xLength"],prop["yLength"]),resample=Image.LANCZOS)
                    baseImage.paste(paste,(prop["xTopLeft"],prop["yTopLeft"]))
                except Exception as e:
                    logError(people["id"],"Field [" + prop["field"] + "]'s picture url seems to be broken. e:"+str(e))
                    break
            else:
                try:
                    paste = Image.open(people[prop["field"]]["path"]).convert('RGBA')
                    paste = paste.resize((prop["xLength"],prop["yLength"]),resample=Image.LANCZOS)
                    baseImage.paste(paste,(prop["xTopLeft"],prop["yTopLeft"]))
                except Exception as e:
                    logError(people["id"],"Field [" + prop["field"] + "]'s picture path seems to be broken. e:"+str(e))
                    break
    else:
        currPath = globalConfig["path"]["output"] + folderName + "/grouped"
        for depth in globalConfig["groupBy"]:
            currPath = currPath + "/" + people[depth]
            if not os.path.exists(currPath):
                os.makedirs(currPath)
        baseImage = baseImage.convert('RGB')
        baseImage.save(currPath + "/" + str(people["id"])+".jpg", quality=90)
        baseImage.save(globalConfig["path"]["output"] + folderName + "/raw/" + str(people["id"])+".jpg", quality=90)
    completedCount += 1
    print(str(completedCount)+" / "+str(len(data)))
