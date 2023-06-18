maplist1 = ["P","-","-","-","-","-","-","-","-","-"]
maplist2 = ["-","-","-","-","-","-","K","-","-","-"]
maplist3 = ["-","-","-","-","-","-","-","-","-","-"]
maplist4 = ["D","-","-","-","-","-","-","-","-","-"]
map = [maplist1,maplist2,maplist3,maplist4]
while True:
    def dichuyen():
        import msvcrt 
        ch = input()
        ch = msvcrt.getch().decode('utf-8')
        def ngang():
            for x in map:
                if "P" in x:
                    ngang = map.index(x) +1
            return ngang
        def doc():
            for x in range(len(map)):
                for y in map[x]:
                    if y == "P":
                        doc = map[x].index("P") +1
            return doc

        if ch == "d":
            map.pop([ngang][doc])
            map.insert("P",[ngang][doc+1])
            map.pop([ngang][doc+1])
            map.insert("-",[ngang][doc])

        if ch == "w":
            map.pop([ngang][doc])
            map.insert("P",[ngang+1][doc])
            map.pop([ngang+1][doc])
            map.insert("-",[ngang][doc])
        if ch == "s":
            map.insert("P",[ngang-1][doc])
            map.pop([ngang-1][doc])
            map.insert("-",[ngang][doc])
        if ch == "a":
            map.pop([ngang][doc])
            map.insert("P",[ngang][doc-1])
            map.pop([ngang][doc-1])
            map.insert("-",[ngang][doc])
        print(*map)
        map.system('cls')

    
        