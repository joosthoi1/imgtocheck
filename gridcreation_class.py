from tkinter import *
class grid:
    def __init__(self, numberx, numbery):
        self.master = Tk()
        self.mylist, self.varlist = [], []
        self.numberx, self.numbery = numberx, numbery
        self.xgrid, self.ygrid = 0, 0
        self.master.title('gridcreation')

        self.coordrost = [[i for i in range(self.numberx*x,self.numberx+self.numberx*x)] for x in range(numbery)]

        for i in range(10000):
            self.varlist.append(IntVar())
            self.mylist.append(Checkbutton(self.master, text="", variable=self.varlist[i]))
            self.mylist[i].grid(row=self.ygrid, sticky=W, column=self.xgrid)
            self.mylist[i].configure(bg='light gray')
            self.xgrid += 1
            if self.xgrid == self.numberx:
                self.ygrid += 1
                self.xgrid = 0

            if self.ygrid == self.numbery:
                break


    def coords(self, x, y):
        return self.coordrost[self.numbery-y][x-1]
    def uncoords(self, coord):
        for i in range(len(self.coordrost)):
            if coord in self.coordrost[i]:
                x1 = self.coordrost[i].index(coord) + 1
                y1 = self.numbery - i
                return [x1, y1]
