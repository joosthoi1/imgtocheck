from gridcreation_class import grid
import cv2
import time
image=cv2.imread('gamepie/imagetocheckbox/unknown.png')
y=image.shape[0] #length in first dimension
x=image.shape[1]
maxx, maxy = 69, 41
def downscale(x, y):
    newx,newy =x,y
    while 1:
        if (int(newx) <= maxx and newy < maxy):

            return int(newx), newy
        newy-=1
        newx-=x/y
newx, newy = downscale(x,y)
resized = cv2.resize(image,(newx,newy))
grid1 = grid(newx-1, newy-1)
grid1.master.title('art')

def colorin():
    x, y =1,1
    for i in grid1.mylist:
        mycolor = '#%02x%02x%02x' % (resized[y-1][x-1][2], resized[y-1][x-1][1], resized[y-1][x-1][0])
        grid1.mylist[grid1.coords(x, grid1.numbery-(y-1))].configure(bg=mycolor,fg=mycolor)
        grid1.mylist[grid1.coords(x, grid1.numbery-(y-1))].configure(state='disabled')
        #grid1.mylist[grid1.coords(x, grid1.numbery-y)].select()
        x+=1
        if x == newx:
            y+=1
            x=1
        if y == newy:
            break
grid1.master.after(2, colorin)
grid1.master.mainloop()
