from gridcreation import grid
from tkinter import *
import cv2
import time
import math


class main:
    def __init__(self, root):
        path = 'C:\\Users\\gebruiker\\Desktop\\python\\gamepie\\imagetocheckbox\\images\\Mona_Lisa1.jpg'  # path to image
        if path.split('.')[1] == 'png':  # checks if its a png since png's need special treatment
            image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        else:
            image = cv2.imread(path)
        self.y = image.shape[0]  # gets images x and y values
        self.x = image.shape[1]
        self.maxx, self.maxy = 69, 41  # maximum amount of checkboxes on x and y axis numbers which I found to be the best fit for a 1080p monitor

        self.downscale()

        self.resized = cv2.resize(image, (self.newx, self.newy))  # resizes image to the dimensions formed in downscale
        cv2.imshow("testwin", self.resized)  # shows preview of image

        self.grid1 = grid(root, self.newx - 1, self.newy - 1)  # creates a checkboxgrid, read gridcreation.py for info
        self.grid1.root.title('art')
        self.colorin()

    def downscale(self):
        self.newx, self.newy = self.x, self.y
        while 1:    # loops and changes the y value by 1 and the x value by the relative x/y until it fits in the pre astablished 69x41 area
            if (int(self.newx) <= self.maxx and self.newy <= self.maxy):
                self.newx = int(self.newx)
                break
            self.newy -= 1
            self.newx -= self.x/self.y

    def colorin(self):              # grabs the color of each pixel and modifies the checkboxes to be that color
        x, y = 1, 1
        for i in self.grid1.boxlist:
            mycolor = '#%02x%02x%02x' % (self.resized[y-1][x-1][2], self.resized[y-1][x-1][1], self.resized[y-1][x-1][0])  # converts rgb to hex
            if list(self.resized[y-1][x-1]) == [0, 0, 0, 0]:
                mycolor = 'white'
            self.grid1.boxlist[self.grid1.coords(x, self.grid1.numbery - (y - 1))].configure(bg=mycolor, fg=mycolor)
            self.grid1.boxlist[self.grid1.coords(x, self.grid1.numbery - (y - 1))].configure(state='disabled')  # disables checkboxes to get more color, remove/comment this line to make them checkable
#            self.grid1.boxlist[self.grid1.coords(x, self.grid1.numbery-(y-1))].select() #selects checkboxes to get more color, remove/comment this line to make them checkable
            x += 1
            if x == self.newx:
                y += 1
                x = 1
            if y == self.newy:
                break
if __name__ == "__main__":
    root = Tk()
    gui = main(root)
    gui.grid1.root.mainloop()
