from tkinter import *   # * means everything so here hum tkinter library se sb kuch import kr rhe hain !
from tkinter import ttk
import random           # random numbers generate krne ke liye iska use krte hain !
from bubblesort import bubble_sort # bubble sort vali file upload krne ke liye !

root=Tk()  #isko root widget bolte hain ,to initialize tkinter we have to create this ,it has to be created before any other widget and there can be only one root widget
root.title("Sorting Algorithm visualizer")#jo winow bnegi uska title bar vala name
root.maxsize(900,600) #max size of default window created ye hoga , it is in pixles
root.config(bg="black") #window ka background black set krne ke liye

selected_alg=StringVar()
data=[]
#tkinter mein basically hr baar 2 cheezen hi krte hain root(widget) bnate hain aur usko pack krte krte hain.pack() ya .grid() se
# fuctions used

def drawData(data,colorarray):   #2
    canvas.delete("all")    #hr baar jb generate krein to canvas mein pehle se bne bar graphs ko clear krne ke liye
    c_height=380            #height of graph 600-200-20 rootwindow ka size - frame ka size - canvas ka offset = canvas pr bar graph ki height
    c_width=450             #width of bar graph
    x_width=c_width/(len(data)+1) #bar graph ki width ko number of values ke hisaab se adjust krna 
    offset=30 #border se spacing ke liye
    spacing=10 # 2 bars ke beech ki distancing ke liye
    normalizeddata=[i/max(data) for i in data] #data ko normalize krna yaani highest vale is divide krna taaki uniform ho jaye
    for i, height in enumerate(normalizeddata):#is loop se ek ek bar bnega
        x0=i*x_width + offset + spacing # top left ka x coordinate
        y0=c_height-height*340 # top left ka y coordinate

        x1=(i+1)* x_width + offset # bottom right ka x coordinate
        y1=c_height# bottom right ka y coordinate


        canvas.create_rectangle(x0,y0,x1,y1,fill=colorarray[i])# create rectangle function x0,y0,x1,y1 leta hai rectangle bnane ke liye
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))#hr bar ke upr ke text ke liye
    root.update_idletasks()#user window update kren ke liye bar graphs show krne ke liye canvas pr.

def generate():      #1
    global data
    minval=int(minentry.get())#minentry vale slider se minvalue lega
    maxval=int(maxentry.get())#maxentry vale slider se max value lega
    size=int(sizeentry.get())#size vale slider se size kivalue lega

    data=[]#data naam ka raay bnaya
    for _ in range(size):
        data.append(random.randrange(minval,maxval+1)) #data naam ke array mein minval se lekr maxval tk range mein random values assign hui
        
    drawData(data, ['red' for x in range(len(data))])# red colour ke value vale bar graphs bnane ke liye function call kiya

def startalgorithm():  #3 bubble sort call krne ke liye function
    global data
    bubble_sort(data,drawData,speedscale.get())
    


UI_frame=Frame(root,width=600,height=200,bg="grey") #user interface vala frame bnane ke liye. frame works like a container,it is rectangular and we can group widgets here
UI_frame.grid(row=0,column=0,padx=10,pady=5)#used to organize widget in a table like structure

canvas=Canvas(root,width=600,height=380,bg="white")#canvas pr mein bar graphs bna skta hun drawings bna skta hun frame pr nhin isliye frame rkha UI ke liye aur canvas display ke liye
canvas.grid(row=1,column=0,padx=10,pady=5)

Label(UI_frame, text="Algorithm: ",bg="grey").grid(row=0,column=0,padx=5,pady=5,sticky=W)#frame ko label dene ke liye iska use kiya hai
algMenu= ttk.Combobox(UI_frame,textvariable=selected_alg,values=["bubblesort","Mergesort"])#frame mein drop down menu bnane ke liye
algMenu.grid(row=0,column=1,padx=5,pady=5)#drop down menu ki positioning ke liye
algMenu.current(0)#initially drop down menu mein jo 0th entry hai usk0 rkho by default
speedscale=Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2,resolution=0.2,orient=HORIZONTAL,label="Select Speed[s]")#sliding bar bnane ke liye, from->starting point,to->ending point,length->x dimension of scale,resolution->2 vales ke beech ka difference,orientation of scale,heading of scale
speedscale.grid(row=0,column=2, padx=5,pady=5)#position of scale
Button(UI_frame,text="start",command=startalgorithm,bg="red").grid(row=0,column=3,padx=5,pady=5)#button bnane ke liye,text=button pr kya likha hoga,command=button press hone prkaunsa function chlega, background of button


sizeentry=Scale(UI_frame, from_=3, to=25, resolution=1,orient=HORIZONTAL,label="data size")#array size adjust krne ke liye slider
sizeentry.grid(row=1,column=0,padx=5,pady=5)


minentry=Scale(UI_frame, from_=0, to=10, resolution=1,orient=HORIZONTAL,label="min value")#minimum value adjust krne ke liye slider
minentry.grid(row=1,column=1,padx=5,pady=5)


maxentry=Scale(UI_frame, from_=10, to=100, resolution=1,orient=HORIZONTAL,label="max value")#maximum value adjust krne ke liye slider
maxentry.grid(row=1,column=2,padx=5,pady=5)


Button(UI_frame,text="generate",command=generate,bg="white").grid(row=1,column=3,padx=5,pady=5)#generate button bnane ke liye


root.mainloop()#it is an infinte loop used to run the application
