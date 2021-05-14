import tkinter
from tkinter import ttk
from tkinter import *

root = tkinter.Tk()
root.title('Conversion')
root.configure(bg = '#000000')
weightans = 'Please enter an answer'

def weightcalculate():
    weightask = float(weightentry1.get())
    weightfrom = weighttkvar.get()
    weightto = weight2tkvar.get()
    if weightfrom == 'Grams':
        if weightto == 'Grams':
            weightans = weightask
        if weightto == 'Kilograms':
            weightans = weightask/1000
        if weightto == 'Tonnes':
            weightans = weightask/1000000
        if weightto == 'Ounces':
            weightans = weightask/28.35
        if weightto == 'Pound':
            weightans = weightask/454
        if weightto == 'Stone':
            weightans = weightask/6350
    if weightfrom == 'Kilograms':
        if weightto == 'Grams':
            weightans = weightask*1000
        if weightto == 'Kilograms':
            weightans = weightask
        if weightto == 'Tonnes':
            weightans = weightask/1000
        if weightto == 'Ounces':
            weightans = weightask*35.274
        if weightto == 'Pound':
            weightans = weightask*2.205
        if weightto == 'Stone':
            weightans = weightask/6.35
    if weightfrom == 'Tonnes':
        if weightto == 'Grams':
            weightans = weightask*1000000
        if weightto == 'Kilograms':
            weightans = weightask*1000
        if weightto == 'Tonnes':
            weightans = weightask
        if weightto == 'Ounces':
            weightans = weightask*35274
        if weightto == 'Pound':
            weightans = weightask*2205
        if weightto == 'Stone':
            weightans = weightask*157
    if weightfrom == 'Ounces':
        if weightto == 'Grams':
            weightans = weightask*28.35
        if weightto == 'Kilograms':
            weightans = weightask/35.274
        if weightto == 'Tonnes':
            weightans = weightask/35274 
        if weightto == 'Ounces':
            weightans = weightask
        if weightto == 'Pound':
            weightans = weightask/16
        if weightto == 'Stone':
            weightans = weightask/224
    if weightfrom == 'Pounds':
        if weightto == 'Grams':
            weightans = weightask*454
        if weightto == 'Kilograms':
            weightans = weightask/2.205
        if weightto == 'Tonnes':
            weightans = weightask/2205
        if weightto == 'Ounces':
            weightans = weightask*16
        if weightto == 'Pound':
            weightans = weightask
        if weightto == 'Stone':
            weightans = weightask*14
    if weightfrom == 'Stone':
        if weightto == 'Grams':
            weightans = weightask*6350
        if weightto == 'Kilograms':
            weightans = weightask/6.35
        if weightto == 'Tonnes':
            weightans = weightask/157
        if weightto == 'Ounces':
            weightans = weightask*224
        if weightto == 'Pound':
            weightans = weightask*14
        if weightto == 'Stone':
            weightans = weightask        
    weightans2 = ttk.Label(tab1, text = weightans)
    weightans2.place(relx = 0.5, rely = 0.7, anchor = CENTER)      


def distcalculate():
    distask = float(distentry1.get())
    distfrom = disttkvar.get()
    distto = dist2tkvar.get()
    if distfrom == 'Millimetres':
        if distto == 'Millimetres':
            distans = distask
        if distto == 'Centimetres':
            distans = distask/10
        if distto == 'Metres':
            distans = distask/1000
        if distto == 'Kilometres':
            distans = distask/1000000
        if distto == 'Inches':
            distans = distask/25.4
        if distto == 'Foot':
            distans = distask/305
        if distto == 'Yard':
            distans = distask/914
        if distto == 'Mile':
            distans = distask/1609000  
    if distfrom == 'Centimetres':
        if distto == 'Millimetres':
            distans = distask*10
        if distto == 'Centimetres':
            distans = distask
        if distto == 'Metres':
            distans = distask/100
        if distto == 'Kilometres':
            distans = distask/100000
        if distto == 'Inches':
            distans = distask/2.54
        if distto == 'Foot':
            distans = distask/30.48
        if distto == 'Yard':
            distans = distask/91.44
        if distto == 'Mile':
            distans = distask/160934
    if distfrom == 'Metres':
        if distto == 'Millimetres':
            distans = distask*1000
        if distto == 'Centimetres':
            distans = distask*100
        if distto == 'Metres':
            distans = distask
        if distto == 'Kilometres':
            distans = distask/1000
        if distto == 'Inches':
            distans = distask*39.37
        if distto == 'Foot':
            distans = distask*3.281
        if distto == 'Yard':
            distans = distask*1.094
        if distto == 'Mile':
            distans = distask/1609
    if distfrom == 'Kilometres':
        if distto == 'Millimetres':
            distans = distask*1000000
        if distto == 'Centimetres':
            distans = distask*100000
        if distto == 'Metres':
            distans = distask*1000
        if distto == 'Kilometres':
            distans = distask
        if distto == 'Inches':
            distans = distask*39370
        if distto == 'Foot':
            distans = distask*3281
        if distto == 'Yard':
            distans = distask*1094
        if distto == 'Mile':
            distans = distask/1.609
    if distfrom == 'Inch':
        if distto == 'Millimetres':
            distans = distask*25.4
        if distto == 'Centimetres':
            distans = distask*2.54
        if distto == 'Metres':
            distans = distask/39.37
        if distto == 'Kilometres':
            distans = distask/39370
        if distto == 'Inches':
            distans = distask
        if distto == 'Foot':
            distans = distask/12
        if distto == 'Yard':
            distans = distask/36
        if distto == 'Mile':
            distans = distask/63360
    if distfrom == 'Foot':
        if distto == 'Millimetres':
            distans = distask*305
        if distto == 'Centimetres':
            distans = distask*30.48
        if distto == 'Metres':
            distans = distask/3.281
        if distto == 'Kilometres':
            distans = distask/3281
        if distto == 'Inches':
            distans = distask*12
        if distto == 'Foot':
            distans = distask
        if distto == 'Yard':
            distans = distask/3
        if distto == 'Mile':
            distans = distask/5280
    if distfrom == 'Yard':
        if distto == 'Millimetres':
            distans = distask*914
        if distto == 'Centimetres':
            distans = distask*91.44
        if distto == 'Metres':
            distans = distask/1.094
        if distto == 'Kilometres':
            distans = distask/1094
        if distto == 'Inches':
            distans = distask*36
        if distto == 'Foot':
            distans = distask*3
        if distto == 'Yard':
            distans = distask
        if distto == 'Mile':
            distans = distask/1760
    if distfrom == 'Miles':
        if distto == 'Millimetres':
            distans = distask*1609000
        if distto == 'Centimetres':
            distans = distask*160934
        if distto == 'Metres':
            distans = distask*1609
        if distto == 'Kilometres':
            distans = distask*1.609
        if distto == 'Inches':
            distans = distask*63360
        if distto == 'Foot':
            distans = distask*5280
        if distto == 'Yard':
            distans = distask/1760
        if distto == 'Mile':
            distans = distask
    distans2 = ttk.Label(tab2, text = distans)
    distans2.place(relx = 0.5, rely = 0.7, anchor = CENTER)    

def compcalculate():
    print('ham')

def tempcalculate():
    print('ham')

def volcalculate():
    print('ham')

tabControl = ttk.Notebook(root)

mainframe = Frame(tabControl)
mainframe.configure(bg = '#040000')
mainframe.pack(pady = 125, padx = 225)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Weight',)
tabControl.add(tab2, text='Distance')
tabControl.add(tab3, text='Denary, Binary and Hex')
tabControl.add(tab4, text='Temperature')
tabControl.add(tab5, text='Volume')
tabControl.pack(expand=1, fill="both")

##################################################################

weightOPTIONS = ['Grams', 'Kilograms', 'Tonnes', 'Ounces', 'Pounds', 'Stones']
weighttkvar = StringVar(tab1)
weight2tkvar = StringVar(tab1)

weightpopupMenu = OptionMenu(tab1, weighttkvar, *weightOPTIONS)
weightpopupMenu2 = OptionMenu(tab1, weight2tkvar, *weightOPTIONS)

weighttkvar.set('Please pick an option')
weight2tkvar.set('Please pick an option')

weightpopupMenu.place(relx = 0.4, rely = 0.2, anchor = E)

to = ttk.Label(tab1, text = 'to')
to.place(relx = 0.5, rely = 0.2, anchor = CENTER)

weightpopupMenu2.place(relx = 0.6, rely = 0.2, anchor = W)

weightentry1 = Entry(tab1, justify = CENTER )
weightentry1.place(relx = 0.5, rely = 0.4, anchor = CENTER)

weightbutton1 = Button(tab1, text = 'Submit', justify = CENTER, command = weightcalculate)
weightbutton1.place(relx = 0.5, rely = 0.5, anchor = CENTER)



##################################################################


distOPTIONS = ['Millimetres', 'Centimetres', 'Metres', 'Kilometres', 'Inches', 'Foot', 'Yard', 'Mile']
disttkvar = StringVar(tab2)
dist2tkvar = StringVar(tab2)

distpopupMenu = OptionMenu(tab2, disttkvar, *distOPTIONS)
distpopupMenu2 = OptionMenu(tab2, dist2tkvar, *distOPTIONS)

disttkvar.set('Please pick an option')
dist2tkvar.set('Please pick an option')

distpopupMenu.place(relx = 0.4, rely = 0.2, anchor = E)

to = ttk.Label(tab2, text = 'to')
to.place(relx = 0.5, rely = 0.2, anchor = CENTER)

distpopupMenu2.place(relx = 0.6, rely = 0.2, anchor = W)

distentry1 = Entry(tab2, justify = CENTER )
distentry1.place(relx = 0.5, rely = 0.4, anchor = CENTER)


distbutton1 = Button(tab2, text = 'Submit', justify = CENTER, command = distcalculate)
distbutton1.place(relx = 0.5, rely = 0.5, anchor = CENTER)


##################################################################


compOPTIONS = ['Denary', 'Binary', 'Hex']
comptkvar = StringVar(tab3)
comp2tkvar = StringVar(tab3)

comppopupMenu = OptionMenu(tab3, comptkvar, *compOPTIONS)
comppopupMenu2 = OptionMenu(tab3, comp2tkvar, *compOPTIONS)

comptkvar.set('Please pick an option')
comp2tkvar.set('Please pick an option')

comppopupMenu.place(relx = 0.4, rely = 0.2, anchor = E)

to = ttk.Label(tab3, text = 'to')
to.place(relx = 0.5, rely = 0.2, anchor = CENTER)

comppopupMenu2.place(relx = 0.6, rely = 0.2, anchor = W)

compentry1 = Entry(tab3, justify = CENTER )
compentry1.place(relx = 0.5, rely = 0.4, anchor = CENTER)


compbutton1 = Button(tab3, text = 'Submit', justify = CENTER, command = compcalculate)
compbutton1.place(relx = 0.5, rely = 0.5, anchor = CENTER)


##################################################################


tempOPTIONS = ['Celcius', 'Farenheit', 'Kelvin']
temptkvar = StringVar(tab4)
temp2tkvar = StringVar(tab4)

temppopupmenu = OptionMenu(tab4, temptkvar, *tempOPTIONS)
temppopupmenu2 = OptionMenu(tab4, temp2tkvar, *tempOPTIONS)

temptkvar.set('Please pick an option')
temp2tkvar.set('Please pick an option')

temppopupmenu.place(relx = 0.4, rely = 0.2, anchor = E)

to = ttk.Label(tab4, text = 'to')
to.place(relx = 0.5, rely = 0.2, anchor = CENTER)

temppopupmenu2.place(relx = 0.6, rely = 0.2, anchor = W)

tempentry = Entry(tab4, justify = CENTER )
tempentry.place(relx = 0.5, rely = 0.4, anchor = CENTER)


tempbutton = Button(tab4, text = 'Submit', justify = CENTER, command = tempcalculate)
tempbutton.place(relx = 0.5, rely = 0.5, anchor = CENTER)


##################################################################


volOPTIONS = ['Millilitres', 'Litres', 'Centilitres', 'Decilitres', 'Pint', 'Quart', 'Gallon', 'Teaspoon', 'Tablespoon', 'Fluid ounce']
voltkvar = StringVar(tab5)
vol2tkvar = StringVar(tab5)

volpopupmenu = OptionMenu(tab5, voltkvar, *volOPTIONS)
volpopupmenu2 = OptionMenu(tab5, vol2tkvar, *volOPTIONS)

voltkvar.set('Please pick an option')
vol2tkvar.set('Please pick an option')

volpopupmenu.place(relx = 0.4, rely = 0.2, anchor = E)

to = ttk.Label(tab5, text = 'to')
to.place(relx = 0.5, rely = 0.2, anchor = CENTER)

volpopupmenu2.place(relx = 0.6, rely = 0.2, anchor = W)

volentry = Entry(tab5, justify = CENTER )
volentry.place(relx = 0.5, rely = 0.4, anchor = CENTER)

volbutton = Button(tab5, text = 'Submit', justify = CENTER, command = volcalculate)
volbutton.place(relx = 0.5, rely = 0.5, anchor = CENTER)


##################################################################




root.mainloop()