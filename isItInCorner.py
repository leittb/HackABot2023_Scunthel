#top right -  top left - corner nums
#1/7 horizontal =
#1/5 vertical =
import math

# return 0 not corner, return 1 - Top left, return 2 - Top right, return 3 - Bottom right, return 3 - Bottom left
def isItInCorner(environmentDict):
    bCoords = environmentDict["B"]
    c0Coords = environmentDict["C0"]
    c1Coords = environmentDict["C1"]

    def euclidean_distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    cornersDist = []
    cornersDist[0] =  euclidean_distance(bCoords[0],bCoords[1],c0Coords[0],c0Coords[1] )
    cornersDist[1] =  euclidean_distance(bCoords[0],bCoords[1],c1Coords[0],c0Coords[1] )
    cornersDist[2] =  euclidean_distance(bCoords[0],bCoords[1],c1Coords[0],c1Coords[1] )
    cornersDist[3] =  euclidean_distance(bCoords[0],bCoords[1],c0Coords[0],c1Coords[1] )

    isCorner = 0
    for x in range(0,4):
        if cornersDist < 170:
            isCorner = x

    return x
