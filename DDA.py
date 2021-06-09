def DDA(x1, y1, x2, y2):   
    li = []
    xr =0
    yr =0
   # plt.xlim([0, 10])
   # plt.ylim([0, 10])
   # plt.title('METODO DDA')
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    if dx > dy:
        steps     = dx
    else: 
        steps = dy

    xInc = round((dx/steps), 2)
    yInc = round((dy/steps), 2)
    
    if x1<=x2 and y1>y2:
        bandera = 1
    elif x1<x2 and y1<=y2: 
        bandera = 2
    elif x1>x2 and y1>y2:
        bandera = 3
    else: 
        bandera = 4
    for i in range(0, steps+1):
       # rect1 = matplotlib.patches.Rectangle((round(x1), round(y1)),1, 1,linewidth=1, edgecolor='b', facecolor='none')
        li.append([])
        li[i].append(round(x1))
        li[i].append(round(y1))
        #ax.add_patch(rect1)
        if bandera==1:
            x1 += xInc 
            y1 -= yInc 
        elif bandera==2:
            x1 += xInc 
            y1 += yInc 
        elif bandera==3:
            x1 -= xInc 
            y1 -= yInc 
        else: 
            x1 -= xInc 
            y1 += yInc 

    return li
