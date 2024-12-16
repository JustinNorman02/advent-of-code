def notinregions(target, list):
     
    for sublist in list:
          if target in sublist:
               return False
          
    return True



with open('data.txt') as f:
    farm = f.read().split('\n')

    for i in range(len(farm)):
        farm[i] = list(farm[i])

   
    direct = [[1,0],[-1,0],[0,1],[0,-1]]

    regions = []

    for i in range(len(farm)):
        for j in range(len(farm[1])):
            
            if notinregions([i,j], regions):

                zoneNum = len(regions)

                zone = farm[i][j]

                regions.append([[i,j]])

                toSearch = []

                for d in direct:

                    x, y = i + d[0], j + d[1]

                    if 0 <= x < len(farm) and 0 <= y < len(farm[1]):
                            toSearch.append([x,y])

                
                while toSearch:
                     cx, cy = toSearch.pop(0)

                     if farm[cx][cy] == zone and [cx,cy] not in regions[zoneNum]:
                          regions[zoneNum].append([cx,cy])

                          for d in direct:

                            x, y = cx + d[0], cy + d[1]

                            if 0 <= x < len(farm) and 0 <= y < len(farm[1]):
                                    toSearch.append([x,y])

    ans = 0

    hor = [[0,1],[0,-1]]
    vert = [[1,0],[-1,0]]
    
    for region in regions:
        perim = []
        edges = 0
        for plot in region:
              
            for d in direct:
                x, y = plot[0] + d[0], plot[1] + d[1]

                if [x,y] not in region:
                    perim.append(((plot[0],plot[1]),(x,y)))
                    # perim.append(((x,y),(plot[0],plot[1])))

        per2 = []
        for p1, p2 in perim:
            keep = True
            for dx,dy in [[1,0],[0,1]]:
                p1n = (p1[0] +dx,p1[1]+dy)
                p2n = (p2[0] +dx,p2[1]+dy)
                if (p1n,p2n) in perim:
                    keep = False

            if keep:
                per2.append((p1,p2))
              

        print(per2)        
        ans += len(region)*len(per2)
        print(len(per2)*len(region), len(per2), len(region))
    

    print(ans)




