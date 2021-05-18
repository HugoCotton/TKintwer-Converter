import tkinter
from tkinter import ttk
from tkinter import *

root = tkinter.Tk()
root.title('Conversion')
root.config(bg = 'gray15')
weightans = 'Please enter an answer'

tabControl = ttk.Notebook(root)

mainframe = Frame(tabControl)
mainframe.configure(bg = '#040000')
mainframe.pack(pady = 125, padx = 225)
mainframe.place()

bordercolour = Frame(root, background = 'black')

s = ttk.Style(root)
s.configure('TNotebook', background = 'gray20')
s.configure('TLabel', background = 'gray20', foreground = 'white')
s.configure('TFrame', background = 'gray20', foreground = 'white')
s.configure('TMenubutton', background = 'gray20', foreground = 'white')
s.configure('TEntry', background = 'gray20')

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Weight')
tabControl.add(tab2, text='Distance')
tabControl.add(tab3, text='Denary, Binary and Hex')
tabControl.add(tab4, text='Temperature')
tabControl.add(tab5, text='Volume')
tabControl.pack(expand=1, fill="both")

weightconversionfactors = [
[  1,  0.001,  0.000001,  0.035274,  0.002205, 0.000157],
[  1000,  1,  0.001,  35.274,  2.205,  0.157],
[  1000000,  1000,  1,  35274,  2205,  157],
[  28.35,  0.02835,  0.00002835,  1,  0.0625,  0.004464],
[  454,  0.454,  0.000454,  16,  1,  0.07143],
[  6350,  0.157,  6.369,  224,  14,  1]
]
weightOPTIONS = ['Grams', 'Kilograms', 'Tonnes', 'Ounces', 'Pounds', 'Stones']

distconversionfactors = [
[  1,  0.1,  0.001,  0.000001,  0.0394,  0.00328,  0.0010941,  0.0000006215],
[  10,  1,  0.01, 0.00001, 0.394,  0.0328,  0.010941,  0.000006215],
[  1000,  100,  1,  0.001,  39.37,  3.281,  1.094,  0.0006215],
[  1000000,  100000,  1000,  1,  39370,  3281,  1094,  0.6215],
[  25.4,  2.54,  0.0254,  0.0000254,  1,  0.0833,  0.02778,  0.000015783],
[  305,  30.48,  0.3048,  0.0003048,  12,  1,  0.33333,  0.0001894],
[  914,  91.44,  0.9141,  0.0009141,  36,  3,  1,  0.0005682],
[  1609000,  160934,  1609,  1.609,  63360,  5280,  1760,  1],
]
distOPTIONS = ['Millimetres', 'Centimetres', 'Metres', 'Kilometres', 'Inches', 'Foot', 'Yard', 'Mile']

compOPTIONS = ['Denary', 'Binary', 'Hex']

tempOPTIONS = ['Celcius', 'Farenheit', 'Kelvin']

def weightcalculate():
    weightask = float(weightentry1.get())
    weightfrom = weighttkvar.get()
    weightto = weight2tkvar.get()
    weightfromindex = weightOPTIONS.index(weightfrom)
    weighttoindex = weightOPTIONS.index(weightto)
    weightans = weightask * weightconversionfactors[weightfromindex][weighttoindex]        
    weightans2 = ttk.Label(tab1, text = weightans)
    weightans2.place(relx = 0.5, rely = 0.7, anchor = CENTER)      



def distcalculate():
    distask = float(distentry1.get())
    distfrom = disttkvar.get()
    distto = dist2tkvar.get()
    distfromindex = distOPTIONS.index(distfrom)
    disttoindex = distOPTIONS.index(distto)
    distans = distask * distconversionfactors[distfromindex][disttoindex]    
    distans2 = ttk.Label(tab2, text = distans)
    distans2.place(relx = 0.5, rely = 0.7, anchor = CENTER)    

def compcalculate():
    compask = float(compentry1.get())
    compfrom = comptkvar.get()
    compto = comp2tkvar.get()
    if compfrom == 'Denary':
        if compto == 'Denary':
            compans = compask
        if compto == 'Binary':
            compans = bin(compask)
        if compto == 'Hexadecimal':
            compans = hex(compask)
    if compfrom == 'Binary':
        if compto == 'Denary':
            compans = int(compask, 2)
        if compto =='Binary':
            compans = compans
        if compto == 'Hexadecimal':
            compans = hex(int(compask, 2))
    if compfrom == 'Hexadecimal':
        if compto == 'Denary':
            compans = int(compask, 16)
        if compto == 'Binary':
            compans = bin(int(compask, 16))
        if compto == 'Hexadecimal':
            compans = compask

def tempcalculate():
    tempask = float(tempentry.get())
    tempfrom = temptkvar.get()
    tempto = temp2tkvar.get()
    if tempfrom == 'Celcius':
        if tempto == 'Celcius':
            tempans = tempask
        if tempto == 'Farenheit':
            tempans = (tempask * 9/5) + 32
        if tempto == 'Kelvin':
            compans = tempask + 273.15
    if tempfrom == 'Farenheit':
        if tempto == 'Celcius':
            compans = (tempask - 32) * 5/9

def volcalculate():
    print('ham')

##################################################################

weighttkvar = StringVar(tab1)
weight2tkvar = StringVar(tab1)

weightpopupMenu = OptionMenu(tab1, weighttkvar, *weightOPTIONS)
weightpopupMenu.config(bg = 'gray20', fg = 'white')
weightpopupMenu['menu'].config(bg = 'gray20', fg = 'white')
weightpopupMenu2 = OptionMenu(tab1, weight2tkvar, *weightOPTIONS)
weightpopupMenu2.config(bg = 'gray20', fg = 'white')
weightpopupMenu2['menu'].config(bg = 'gray20', fg = 'white', activebackground = 'gray20', activeforeground = 'white')

weighttkvar.set('Please pick an option')
weight2tkvar.set('Please pick an option')

weightpopupMenu.place(relx = 0.4, rely = 0.2, anchor = E)

to = ttk.Label(tab1, text = 'to')
to.place(relx = 0.5, rely = 0.2, anchor = CENTER)

weightpopupMenu2.place(relx = 0.6, rely = 0.2, anchor = W)

weightentry1 = Entry(tab1, justify = CENTER )
weightentry1.place(relx = 0.5, rely = 0.4, anchor = CENTER)

weightbutton1 = Button(tab1, text = 'Submit', justify = CENTER, command = weightcalculate)
weightbutton1.place(relx = 0.5, rely = 0.6, anchor = CENTER)



##################################################################


disttkvar = StringVar(tab2)
dist2tkvar = StringVar(tab2)

distpopupMenu = OptionMenu(tab2, disttkvar, *distOPTIONS)
distpopupMenu.config(bg = 'gray20', fg = 'white')
distpopupMenu['menu'].config(bg = 'gray20', fg = 'white')
distpopupMenu2 = OptionMenu(tab2, dist2tkvar, *distOPTIONS)
distpopupMenu2.config(bg = 'gray20', fg = 'white')
distpopupMenu2['menu'].config(bg = 'gray20', fg = 'white', activebackground = 'gray20', activeforeground = 'white')

disttkvar.set('Please pick an option')
dist2tkvar.set('Please pick an option')

distpopupMenu.place(relx = 0.4, rely = 0.2, anchor = E)

to = ttk.Label(tab2, text = 'to')
to.place(relx = 0.5, rely = 0.2, anchor = CENTER)

distpopupMenu2.place(relx = 0.6, rely = 0.2, anchor = W)

distentry1 = Entry(tab2, justify = CENTER )
distentry1.place(relx = 0.5, rely = 0.4, anchor = CENTER)


distbutton1 = Button(tab2, text = 'Submit', justify = CENTER, command = distcalculate)
distbutton1.place(relx = 0.5, rely = 0.6, anchor = CENTER)


##################################################################


comptkvar = StringVar(tab3)
comp2tkvar = StringVar(tab3)

comppopupMenu = OptionMenu(tab3, comptkvar, *compOPTIONS)
comppopupMenu.config(bg = 'gray20', fg = 'white')
comppopupMenu['menu'].config(bg = 'gray20', fg = 'white')
comppopupMenu2 = OptionMenu(tab3, comp2tkvar, *compOPTIONS)
comppopupMenu2.config(bg = 'gray20', fg = 'white')
comppopupMenu2['menu'].config(bg = 'gray20', fg = 'white', activebackground = 'gray20', activeforeground = 'white')

comptkvar.set('Please pick an option')
comp2tkvar.set('Please pick an option')

comppopupMenu.place(relx = 0.4, rely = 0.2, anchor = E)

to = ttk.Label(tab3, text = 'to')
to.place(relx = 0.5, rely = 0.2, anchor = CENTER)

comppopupMenu2.place(relx = 0.6, rely = 0.2, anchor = W)

compentry1 = Entry(tab3, justify = CENTER )
compentry1.place(relx = 0.5, rely = 0.4, anchor = CENTER)


compbutton1 = Button(tab3, text = 'Submit', justify = CENTER, command = compcalculate)
compbutton1.place(relx = 0.5, rely = 0.6, anchor = CENTER)


##################################################################


temptkvar = StringVar(tab4)
temp2tkvar = StringVar(tab4)

temppopupmenu = OptionMenu(tab4, temptkvar, *tempOPTIONS)
temppopupmenu.config(bg = 'gray20', fg = 'white')
temppopupmenu['menu'].config(bg = 'gray20', fg = 'white')
temppopupmenu2 = OptionMenu(tab4, temp2tkvar, *tempOPTIONS)
temppopupmenu2.config(bg = 'gray20', fg = 'white')
temppopupmenu2['menu'].config(bg = 'gray20', fg = 'white', activebackground = 'gray20', activeforeground = 'white')

temptkvar.set('Please pick an option')
temp2tkvar.set('Please pick an option')

temppopupmenu.place(relx = 0.4, rely = 0.2, anchor = E)

to = ttk.Label(tab4, text = 'to')
to.place(relx = 0.5, rely = 0.2, anchor = CENTER)

temppopupmenu2.place(relx = 0.6, rely = 0.2, anchor = W)

tempentry = Entry(tab4, justify = CENTER )
tempentry.place(relx = 0.5, rely = 0.4, anchor = CENTER)


tempbutton = Button(tab4, text = 'Submit', justify = CENTER, command = tempcalculate)
tempbutton.place(relx = 0.5, rely = 0.6, anchor = CENTER)


##################################################################


volOPTIONS = ['Millilitres', 'Litres', 'Centilitres', 'Decilitres', 'Pint', 'Quart', 'Gallon', 'Teaspoon', 'Tablespoon', 'Fluid ounce']
voltkvar = StringVar(tab5)
vol2tkvar = StringVar(tab5)

volpopupMenu = OptionMenu(tab5, voltkvar, *volOPTIONS)
volpopupMenu.config(bg = 'gray20', fg = 'white')
volpopupMenu['menu'].config(bg = 'gray20', fg = 'white')
volpopupMenu2 = OptionMenu(tab5, vol2tkvar, *volOPTIONS)
volpopupMenu2.config(bg = 'gray20', fg = 'white')
volpopupMenu2['menu'].config(bg = 'gray20', fg = 'white', activebackground = 'gray20', activeforeground = 'white')

voltkvar.set('Please pick an option')
vol2tkvar.set('Please pick an option')

volpopupMenu.place(relx = 0.4, rely = 0.2, anchor = E)

to = ttk.Label(tab5, text = 'to')
to.place(relx = 0.5, rely = 0.2, anchor = CENTER)

volpopupMenu2.place(relx = 0.6, rely = 0.2, anchor = W)

volentry = Entry(tab5, justify = CENTER )
volentry.place(relx = 0.5, rely = 0.4, anchor = CENTER)

volbutton = Button(tab5, text = 'Submit', justify = CENTER, command = volcalculate)
volbutton.place(relx = 0.5, rely = 0.6, anchor = CENTER)

##################################################################

root.mainloop()