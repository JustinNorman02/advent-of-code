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
    
    for region in regions:
        perim = []
        edges = 0
        for plot in region:
              
            for d in direct:
                x, y = plot[0] + d[0], plot[1] + d[1]

                if [x,y] not in region:
                    perim.append([x,y,d])

                   

        for x,y,d in perim: 
            edgeExists = False
            for d1 in [[1,0],[0,1]]:
                
                nx, ny = x + d1[0], y + d1[1]
                
                if [nx,ny,d] in perim:
                    edgeExists = True

            if not edgeExists:
                    edges += 1


        print(edges*len(region), edges, len(region))    

        ans += edges*len(region)

    print(ans)




