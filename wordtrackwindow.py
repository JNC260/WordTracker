import functions
import tkinter as tk

LARGE_FONT = ('Verdana',12)

class WordTrackApp(tk.Tk): #input tk inheritance in parentheses

#baseline code for adding pages...
    def __init__(self, *args, **kwargs): #initialize, when call class, this will always run right away args, pass through variables, kwargs pass through dictionaries
        #add what we want to initialize
        tk.Tk.__init__(self, *args, **kwargs) #run tkinter
        container = tk.Frame(self) #create window

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew") #sticky is like alignment +stretch nsew (north, south, east, west)

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#add a page...
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Don't repeat yourself!", font=LARGE_FONT)
        label.pack(pady=10, padx=10) #add padding

        barButton = tk.Button(self, text="View Bar Graph", command=lamda: 'somefunction(param)')#command runs on load, so we need to get around it using lamda
        barButton.pack()


app = WordTrackApp()
app.mainloop()