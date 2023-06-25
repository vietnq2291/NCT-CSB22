
import os 
import msvcrt

def escape(): 
    mapList = [["P", "-", "-", "-", "-", "-", "-", "-", "-",  "-"],
           ["-", "-", "-", "-", "-", "K", "-", "-", "-",  "-"],
           ["D", "-", "-", "-", "-", "-", "-", "-", "-",  "-"], 
           ["-", "-", "-", "-", "-", "-", "-", "-", "-",  "-"]]
    
    def initMap():
        os.system('cls')
        row = ""
        for x in range(len(mapList)):
            row = ""
            for y in mapList[x]:
                row += f"{y} "
            print(row)
    initMap()

    def updatePos():
        def getRow():
            for x in mapList:
                if "P" in x:
                    row = mapList.index(x)
            return row


        def getPos():
            for x in range(len(mapList)):
                for y in mapList[x]:
                    if y == "P":
                        playerPos = mapList[x].index("P")
            return playerPos
        

        while True:
            ch = msvcrt.getch().decode('utf-8')
            if ch == "q":
                break
            currentRow = getRow()
            currentPos = getPos()
            if ch == "w":
                mapList[currentRow].pop(currentPos)
                mapList[currentRow].append("-")
                if currentRow == 0:
                    newRow = 3
                    mapList[newRow].pop(currentPos)
                    mapList[newRow].insert(currentPos, "P")
                    initMap()
                else:
                    mapList[currentRow-1].pop(currentPos)
                    mapList[currentRow-1].insert(currentPos, "P")
                    initMap()
                
            if ch == "s":
                if currentRow == 3:
                    mapList[currentRow].pop(currentPos)
                    mapList[currentRow].insert(currentPos, "P")
                else:
                    mapList[currentRow].pop(currentPos)
                    mapList[currentRow].insert(currentPos, "-")
                    mapList[currentRow+1].pop(currentPos)
                    mapList[currentRow+1].insert(currentPos, "P")
                    initMap()
            
            if ch == "a":
                if currentPos == 0:
                    mapList[currentRow].pop(currentPos)
                    mapList[currentRow].insert(0, "P")
                else: 
                    mapList[currentRow].pop(currentPos)
                    mapList[currentRow].insert(currentPos-1, "P")
                initMap()
            if ch == "d":
                mapList[currentRow].pop(currentPos)
                mapList[currentRow].insert(currentPos+1, "P")
                initMap()
    updatePos()

        
escape()  