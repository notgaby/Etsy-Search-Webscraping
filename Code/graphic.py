import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import csv
import statistics

# 8 x 8 pictures = displays all 64

class Buttons(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.pack()
        self.grid(row=0, column=0)
        self.create_widgets()

    def get_data(self):
        print("nothing yet")

    def create_widgets(self):
        self.bts = tk.Button(self, text="Back to school signs",command=self.displayBTS) #, command=self.displayImage) #, command=self.displayImage())
        self.bts.grid(row=0, column=2)
        #self.bts.pack(side="left")

        self.babyShower = tk.Button(self, text="Baby Shower invites", command=self.displayBabyShower)
        self.babyShower.grid(row=0,column=3)
        #self.babyShower.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.grid(row=0,column=4)
        #self.quit.pack(side="left")



    def say_hi(self):
        print("hi there, everyone!")

    def displayBabyShower(self):
        print("here")



        image = Image.open('C:/Users/othscs017/Desktop/sampleimage.jpg').resize((280,280))
        self.img = ImageTk.PhotoImage(image)

        for i in range(0,8):
            for a in range(0,8):
                self.img.label = tk.Label(self,image=self.img)
                self.img.label.grid(row=i,column=a)

    def displayBTS(self):

        #self.Sb = tk.Scale(self, orient=tk.VERTICAL, bg="lightblue")
        #self.Sb.grid(row=1, column=0)


        #############

        prices = []

        #with open('C:/Python27/testweight.csv', 'rb') as f:
    #reader = csv.reader(f, delimiter='\t')
    #header = next(reader)
    #rows = [header] + [[row[0], int(row[1])] for row in reader]

        with open('prices.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            writer = csv.writer(csvfile)

            next(reader)
            print("raeder:", reader)
            for row in reader:

                num = row[0]
                print("row",row[0])
                print("num:", num)
                num = num.replace(",","")
                print("num new", num)
                #print("float num", float(num))
                prices.append(float(num))
                #prices.append(float(row[0]))

        """
        with open('prices.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            next(readCSV) #skips header
            for row in readCSV:
                print("prrrint",row[0])
                prices.append(row[0])
        """
        #prices.pop(0) #delete the 'links' title

        print("PRIZ",prices.__getitem__(1))
        mean = statistics.mean(prices)
        median = statistics.median(prices)
        mode = statistics.mode(prices)
        maxNum = max(prices)
        minNum = min(prices)

        #############

        self.canvas = Canvas(self, width=1000, height=1000, bd=0)
        self.canvas.create_text(700,50, fill="black", font=("Times",15), text=("Mean price: "+str(round(mean,2))))
        self.canvas.create_text(705,80, fill="black", font=("Times",15), text= "Median price: "+str(round(median,2)))
        self.canvas.create_text(700,110, fill="black", font=("Times",15), text= "Mode price: "+str(round(mode,2)))
        self.canvas.create_text(700,140, fill="black", font=("Times",15), text= "Max price: "+str(round(maxNum,2)))
        self.canvas.create_text(700,170, fill="black", font=("Times",15), text= "Min price: "+str(round(minNum,2)))

        self.Images = []
        self.yScroll = Scrollbar(self)
        self.yScroll.grid(row=1,column=1,sticky=N+S)

        self.canvas["yscrollcommand"]= self.yScroll.set
        #(yscrollcommand=self.yScroll.set)
        self.canvas.grid(row=1,column=0,sticky=N+S+E+W)



        #image = Image.open('C:/Users/othscs017/Desktop/sampleimage.jpg').resize((280,280))
        #image = Image.open('C:/Users/gabrielle/Desktop/1.jpg').resize((280,280))
        #self.img = ImageTk.PhotoImage(image)

        num = 0
        for i in range(0,63):

            #image = Image.open('C:/Users/gabrielle/Desktop/EtsySearchFin/pictures/'+str(num)+'.jpg').resize((280,280))
            image = Image.open(r'/Users/gabrielleco/Desktop/EtsySearchFin/pictures/'+str(num)+'.jpg').resize((280,280))
            self.img = ImageTk.PhotoImage(image)
            self.Images.append(self.img)
            num+=1

        print("LLL,",self.Images.__getitem__(1))
        print("MMMM",self.Images.__getitem__(0))
        print("LLL",str(self.img))

        #self.canvas.create_image(900,1000,image=self.img)
        #self.canvas.create_image(900,700,image=self.img)

        a = 0
        b = 0
        c = 0

        print(self.Images)
        for i in range (len(self.Images)-1):
            #print(i)

            print(i)
                                    #x #y

            self.canvas.create_image(b,a,image=self.Images.__getitem__(i),anchor=tk.CENTER)
            if b < 500:
                b+=250
            else:
                #c+=250
                #b = c
                b = 0
                a+=250

            #a+=250

        self.yScroll.config(command=self.canvas.yview)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))


        self.pack(fill=BOTH, expand=1)


        """
        self.scroll = Scrollbar(self, orient="vertical", command=(self.displayBTS(self)))
        self.scroll.grid(row=0,column=1, sticky='ns')
        """






def main():
    root = tk.Tk()
    root.geometry("1500x1500")
    app = Buttons(root)
    root.mainloop()

if __name__ == '__main__':
    main()
