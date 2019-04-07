from gridcreation import grid
import tkinter as tk
import cv2
import argparse


class main:
    def __init__(self, root, path, enable_checkboxes):
        self._enable_checkboxes = enable_checkboxes

        if path.endswith('png'):
            image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        else:
            image = cv2.imread(path)
        self.y = image.shape[0]
        self.x = image.shape[1]
        # maximum amount of checkboxes on x and y axis numbers which I found to be the best fit for a 1080p monitor
        self.maxx, self.maxy = 69, 41

        self.downscale()

        self.resized = cv2.resize(image, (self.newx, self.newy))  # resizes image to the dimensions formed in downscale
        cv2.imshow("testwin", self.resized)  # shows preview of image

        self.grid1 = grid(root, self.newx - 1, self.newy - 1)  # creates a checkboxgrid, read gridcreation.py for info
        self.grid1.root.title('art')
        self.colorin()

    def downscale(self):
        self.newx, self.newy = self.x, self.y
        # Changes the y value by 1 and the x value by the relative x/y until it fits in the pre-established 69x41 area
        while 1:
            if (int(self.newx) <= self.maxx and self.newy <= self.maxy):
                self.newx = int(self.newx)
                break
            self.newy -= 1
            self.newx -= self.x/self.y

    def colorin(self):              # grabs the color of each pixel and modifies the checkboxes to be that color
        x, y = 1, 1
        for i in self.grid1.boxlist:
            # convert rgb to hex
            mycolor = '#%02x%02x%02x' % (self.resized[y-1][x-1][2], self.resized[y-1][x-1][1], self.resized[y-1][x-1][0])
            if list(self.resized[y-1][x-1]) == [0, 0, 0, 0]:
                mycolor = 'white'
            self.grid1.boxlist[self.grid1.coords(x, self.grid1.numbery - (y - 1))].configure(bg=mycolor, fg=mycolor)

            # Disabled checkboxes allow more color through but are less fun to click.
            if self._enable_checkboxes:
                self.grid1.boxlist[self.grid1.coords(x, self.grid1.numbery-(y-1))].select()
            else:
                self.grid1.boxlist[self.grid1.coords(x, self.grid1.numbery - (y - 1))].configure(state='disabled')
            x += 1
            if x == self.newx:
                y += 1
                x = 1
            if y == self.newy:
                break


def get_args():
    parser = argparse.ArgumentParser(description='imgtocheck yo')
    parser.add_argument('-i', '--image', type=str, default='em.png', help='Image to Checkify')
    parser.add_argument('-e', '--enable_checkboxes', action='store_true', default=False, help='Enable checkboxes or not.')
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = get_args()
    root = tk.Tk()
    gui = main(root, path=args.image, enable_checkboxes=args.enable_checkboxes)
    gui.grid1.root.mainloop()
