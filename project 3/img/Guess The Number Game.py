import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
root = Tk()
root.title('Guess The Number Game')

Truestyle = ttk.Style()
Truestyle.theme_use('classic')
Truestyle.configure('T.TButton', padding=(10, 10, 10, 5), font=('Comic Sans MS',12), background = 'green')
Truestyle.map('T.TButton', foreground=[('pressed', 'black'), ('active', 'yellow')],
                background=[('pressed', '!disabled', 'green'), ('active', 'green')])

Farstyle = ttk.Style()
Farstyle.theme_use('classic')
Farstyle.configure('F.TButton', padding=(10, 10, 10, 5), font=('Comic Sans MS',12), background = 'red')
Farstyle.map('F.TButton', foreground=[('pressed', 'black'), ('active', 'blue')],
                background=[('pressed', '!disabled', 'red'), ('active', 'red')])

Buttonstyle = ttk.Style()
Buttonstyle.theme_use('classic')
Buttonstyle.configure('B.TButton', padding=(10, 10, 10, 5), font=('Comic Sans MS',12), background = 'yellow')
Buttonstyle.map('B.TButton', foreground=[('pressed', 'blue'), ('active', 'green')],
                background=[('pressed', '!disabled', 'black'), ('active', 'pink')])

def info():
    info = mb.showinfo(title = 'Information', message = 'Game created by: Olexiy Nizitskiy. Released: 28. 08. 2018')

def rules():
    info = mb.showinfo(title = 'Rules', message = 'There is only one rule: Guess my number')

def exit_game():
    root.destroy()
    
def yes(n):
    l1.destroy()
    bY.destroy()
    bN.destroy()
    start(n)

l1 = Label(text = 'Do You want to play in\n Guess The Number Game?', font=('Comic Sans MS',20))

bY = ttk.Button(text = 'Yes', command = lambda n=(random.randint(1,30)): yes(n), style='B.TButton')
bN = ttk.Button(text = 'No', command = exit_game, style='B.TButton')

l1.grid(row = 1, column = 1, columnspan = 2)
bY.grid(row = 3, column = 1)
bN.grid(row = 3, column = 2)

mainmenu = Menu(root)
root.config(menu=mainmenu)
helpmenu = Menu(mainmenu, tearoff = 0)
helpmenu.add_command(label='Rules', command=rules)
helpmenu.add_command(label='Info', command=info)
mainmenu.add_cascade(label='Menu', menu=helpmenu)

def start(n):
    
    def number(m, n):
        listButtons=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30]
        button = listButtons[m-1]
        if n==m and button['text'] == str(m):
            t = ('HOORAY!!! You guessed!!!')
            button['style'] = 'T.TButton'
            restart()
            
        else:
            button['style'] = 'F.TButton'
            t = 'The difference of our numbers is equal:', n-m, 'The sum of our numbers is equal:', n+m
        l2['text']= t
        
    def restart():
        l3 = Label(width=80, font=('Comic Sans MS',15))
        l3['text']='Do You want to play again?'
        bY = ttk.Button(text = 'Yes', command = lambda n=(random.randint(1,30)): yes(n), style='B.TButton')
        bN = ttk.Button(text = 'No', command = exit_game, style='B.TButton')
        l3.grid(row = 2, column = 1, columnspan = 5)
        bY.grid(row = 3, column = 1, columnspan = 4)
        bN.grid(row = 3, column = 2, columnspan = 4)
        bE.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
        b7.destroy()
        b8.destroy()
        b9.destroy()
        b10.destroy()
        b11.destroy()
        b12.destroy()
        b13.destroy()
        b14.destroy()
        b15.destroy()
        b16.destroy()
        b17.destroy()
        b18.destroy()
        b19.destroy()
        b20.destroy()
        b21.destroy()
        b22.destroy()
        b23.destroy()
        b24.destroy()
        b25.destroy()
        b26.destroy()
        b27.destroy()
        b28.destroy()
        b29.destroy()
        b30.destroy()

    l2 = Label(width = 80, font=('Comic Sans MS',15))
    l2['text']='I made a number from 1 to 30'
    l2.grid(row = 1, column = 1, columnspan = 5)
    l3 = Label(font=('Comic Sans MS',15), width = 80)
    l3['text']='Try to guess'
    l3.grid(row = 2, column = 1, columnspan = 5)
    b1 = ttk.Button(text = '1', style='B.TButton')
    b2 = ttk.Button(style='B.TButton', text = '2')
    b3 = ttk.Button(style='B.TButton', text = '3')
    b4 = ttk.Button(style='B.TButton', text = '4')
    b5 = ttk.Button(style='B.TButton', text = '5')
    b6 = ttk.Button(style='B.TButton', text = '6')
    b7 = ttk.Button(style='B.TButton', text = '7')
    b8 = ttk.Button(style='B.TButton', text = '8')
    b9 = ttk.Button(style='B.TButton', text = '9')
    b10 = ttk.Button(style='B.TButton', text = '10')
    b11 = ttk.Button(style='B.TButton', text = '11')
    b12 = ttk.Button(style='B.TButton', text = '12')
    b13 = ttk.Button(style='B.TButton', text = '13')
    b14 = ttk.Button(style='B.TButton', text = '14')
    b15 = ttk.Button(style='B.TButton', text = '15')
    b16 = ttk.Button(style='B.TButton', text = '16')
    b17 = ttk.Button(style='B.TButton', text = '17')
    b18 = ttk.Button(style='B.TButton', text = '18')
    b19 = ttk.Button(style='B.TButton', text = '19')
    b20 = ttk.Button(style='B.TButton', text = '20')
    b21 = ttk.Button(style='B.TButton', text = '21')
    b22 = ttk.Button(style='B.TButton', text = '22')
    b23 = ttk.Button(style='B.TButton', text = '23')
    b24 = ttk.Button(style='B.TButton', text = '24')
    b25 = ttk.Button(style='B.TButton', text = '25')
    b26 = ttk.Button(style='B.TButton', text = '26')
    b27 = ttk.Button(style='B.TButton', text = '27')
    b28 = ttk.Button(style='B.TButton', text = '28')
    b29 = ttk.Button(style='B.TButton', text = '29')
    b30 = ttk.Button(style='B.TButton', text = '30')
    bE = ttk.Button(text = 'Exit', command = exit_game, style='B.TButton')

    b1.grid(row = 3, column = 1)
    b2.grid(row = 3, column = 2)
    b3.grid(row = 3, column = 3)
    b4.grid(row = 3, column = 4)
    b5.grid(row = 3, column = 5)
    b6.grid(row = 4, column = 1)
    b7.grid(row = 4, column = 2)
    b8.grid(row = 4, column = 3)
    b9.grid(row = 4, column = 4)
    b10.grid(row = 4, column = 5)
    b11.grid(row = 5, column = 1)
    b12.grid(row = 5, column = 2)
    b13.grid(row = 5, column = 3)
    b14.grid(row = 5, column = 4)
    b15.grid(row = 5, column = 5)
    b16.grid(row = 6, column = 1)
    b17.grid(row = 6, column = 2)
    b18.grid(row = 6, column = 3)
    b19.grid(row = 6, column = 4)
    b20.grid(row = 6, column = 5)
    b21.grid(row = 7, column = 1)
    b22.grid(row = 7, column = 2)
    b23.grid(row = 7, column = 3)
    b24.grid(row = 7, column = 4)
    b25.grid(row = 7, column = 5)
    b26.grid(row = 8, column = 1)
    b27.grid(row = 8, column = 2)
    b28.grid(row = 8, column = 3)
    b29.grid(row = 8, column = 4)
    b30.grid(row = 8, column = 5)
    bE.grid(row = 9, column = 3)

    b1.config(command = lambda m = 1: number(m, n))
    b2.config(command = lambda m = 2: number(m, n))
    b3.config(command = lambda m = 3: number(m, n))
    b4.config(command = lambda m = 4: number(m, n))
    b5.config(command = lambda m = 5: number(m, n))
    b6.config(command = lambda m = 6: number(m, n))
    b7.config(command = lambda m = 7: number(m, n))
    b8.config(command = lambda m = 8: number(m, n))
    b9.config(command = lambda m = 9: number(m, n))
    b10.config(command = lambda m = 10: number(m, n))
    b11.config(command = lambda m = 11: number(m, n))
    b12.config(command = lambda m = 12: number(m, n))
    b13.config(command = lambda m = 13: number(m, n))
    b14.config(command = lambda m = 14: number(m, n))
    b15.config(command = lambda m = 15: number(m, n))
    b16.config(command = lambda m = 16: number(m, n))
    b17.config(command = lambda m = 17: number(m, n))
    b18.config(command = lambda m = 18: number(m, n))
    b19.config(command = lambda m = 19: number(m, n))
    b20.config(command = lambda m = 20: number(m, n))
    b21.config(command = lambda m = 21: number(m, n))
    b22.config(command = lambda m = 22: number(m, n))
    b23.config(command = lambda m = 23: number(m, n))
    b24.config(command = lambda m = 24: number(m, n))
    b25.config(command = lambda m = 25: number(m, n))
    b26.config(command = lambda m = 26: number(m, n))
    b27.config(command = lambda m = 27: number(m, n))
    b28.config(command = lambda m = 28: number(m, n))
    b29.config(command = lambda m = 29: number(m, n))
    b30.config(command = lambda m = 30: number(m, n))

root.mainloop()
