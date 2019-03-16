from gridcreation_class import grid
import cv2
import time
image=cv2.imread('em.png')
y=image.shape[0] #length in first dimension
x=image.shape[1]
print(x/y)
grid1 = grid(69, 41)
def downscale(x, y):
    newx,newy =x,y
    while 1:
        newy-=1
        newx-=x/y
        if (int(newx) <= grid1.numberx and newy < grid1.numbery):

            return int(newx), newy
        print(newx,newy)
        #time.sleep(0.02)
newx, newy = downscale(x,y)
resized = cv2.resize(image,(newx,newy))


def colorin():
    x, y =1,1
    for i in grid1.mylist:
        mycolor = '#%02x%02x%02x' % (resized[y-1][x-1][0], resized[y-1][x-1][1], resized[y-1][x-1][2])
        #print(mycolor)
        grid1.mylist[grid1.coords(x, grid1.numbery-y)].configure(bg=mycolor,fg=mycolor)
        grid1.mylist[grid1.coords(x, grid1.numbery-y)].configure(state='disabled')
        #grid1.mylist[grid1.coords(x, grid1.numbery-y)].select()
        x+=1
        if x == newx:
            y+=1
            x=1
        if y == newy:
            break
colorin()
grid1.master.mainloop()
