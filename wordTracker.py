import functions
import tkinter as tk
from tkinter import ttk #"css" for tkinter
import matplotlib
from matplotlib import style
from matplotlib import pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

LARGE_FONT = ('Verdana',12)

class WordTrackApp(tk.Tk): #input tk inheritance in parentheses

#baseline code for adding pages...
    def __init__(self, *args, **kwargs): #initialize, when call class, this will always run right away args, pass through variables, kwargs pass through dictionaries
        #add what we want to initialize
        tk.Tk.__init__(self, *args, **kwargs) #run tkinter
        
        tk.Tk.wm_title(self, "Word Tracker")

        container = tk.Frame(self) #create window
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def access_page(self, classname):
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
            return None

#add a page...
class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        self.controller = controller

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Don't repeat yourself!", font=LARGE_FONT)
        label.grid(row=0, column=3, pady=10, padx=10) #add padding

        def analyze(text):
            words = functions.formatInputText(text)
            counts = functions.findWordCount(words)
            most = functions.findMostUsed(counts)
            tk.Label(self, text = most).grid(row=2,column=2, columnspan=3)

        textInput = ttk.Entry(self)
        textInput.grid(column=2,row=1, columnspan=3)
        self.text = textInput.get()

        analyzeButton =ttk.Button(self, text="Analyze Text", command=lambda: analyze(textInput.get()))
        analyzeButton.grid(column=3,row=3)

        barButton = ttk.Button(self, text="View Bar Graph", command=lambda: makeBar(textInput.get())) #command runs on load, so we need to get around it using lamda
        barButton.grid(column=0,row=4)

        pieButton = ttk.Button(self, text="View Pie Chart", command=lambda: makePie(textInput.get()))
        pieButton.grid(column=5,row=4)
        

        def makeBar(text):
            words = functions.formatInputText(text)
            counts = functions.findWordCount(words)
            values = functions.wordBarGraph(counts, words)
            x = values["x"]
            y = values["y"]

            f = Figure()
            ax = f.add_subplot(111)
            myBar = ax.bar(x, y)

            barCanvas = FigureCanvasTkAgg(f, self)
            barCanvas.draw()
            barCanvas.get_tk_widget().grid(column=3, row=5)

        def makePie(text):
            words = functions.formatInputText(text)
            counts = functions.findWordCount(words)
            data = functions.wordPieChart(counts, words)
            labels = data["labels"]
            values = data["values"]

            f = Figure()
            ax = f.add_subplot(111)
            myPie = ax.pie(values, labels=labels)

            pieCanvas = FigureCanvasTkAgg(f, self)
            pieCanvas.draw()
            pieCanvas.get_tk_widget().grid(column=3,row=5)

#tkinter code...
app = WordTrackApp()
app.mainloop()