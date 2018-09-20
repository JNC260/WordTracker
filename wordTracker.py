import functions
import tkinter as tk
from tkinter import ttk #"css" for tkinter
import matplotlib
from matplotlib import style
from matplotlib import pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

SUPER_FONT = ('Verdana', 18)
HEADING_FONT = ('Verdana', 14)
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

#add a page...
class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Don't repeat yourself!", font=SUPER_FONT)
        label.grid(row=0, column=3, pady=10, padx=10) #add padding

        label = tk.Label(self, text="Word Tracker analyzes text to find the words that appear most frequently (excluding the most common words in the English language). Avoid sounding redundant by varying your vocabulary.", font=HEADING_FONT, wraplength=600)
        label.grid(row=1, column=2, columnspan=3, padx=5) #add padding

        scrollbar = tk.Scrollbar(self)
        scrollbar.grid(column=1, row=2, sticky="nse")
        

        def analyze(text):
            words = functions.formatInputText(text)
            counts = functions.findWordCount(words)
            most = functions.findMostUsed(counts)
            tk.Label(self, text = most, font=HEADING_FONT, pady=5).grid(row=3,column=2, columnspan=3)

        textInput = tk.Text(self, height=3, yscrollcommand=scrollbar.set, background="lightgray", font=LARGE_FONT)
        textInput.grid(column=2,row=2, columnspan=3)
        scrollbar.config(command=textInput.yview)

        analyzeButton =ttk.Button(self, text="Analyze Text", command=lambda: analyze(textInput.get(1.0, "end")))
        analyzeButton.grid(column=3,row=4,pady=5, padx=5)

        barButton = ttk.Button(self, text="View Bar Graph", command=lambda: makeBar(textInput.get(1.0, "end"))) #command runs on load, so we need to get around it using lamda
        barButton.grid(column=0,row=5,pady=5, padx=5)

        pieButton = ttk.Button(self, text="View Pie Chart", command=lambda: makePie(textInput.get(1.0, "end")))
        pieButton.grid(column=5,row=5,pady=5, padx=5)
        

        def makeBar(text):
            words = functions.formatInputText(text)
            counts = functions.findWordCount(words)
            values = functions.wordBarGraph(counts, words)
            x = values["x"]
            y = values["y"]

            f = Figure(figsize=(4,4))
            ax = f.add_subplot(111)
            ax.set_xticklabels(x, rotation=45, fontsize="x-small")
            ax.bar(x, y, align="center")

            barCanvas = FigureCanvasTkAgg(f, self)
            barCanvas.draw()
            barCanvas.get_tk_widget().grid(column=3, row=6)

        def makePie(text):
            words = functions.formatInputText(text)
            counts = functions.findWordCount(words)
            data = functions.wordPieChart(counts, words)
            labels = data["labels"]
            values = data["values"]

            f = Figure(figsize=(4,4))
            ax = f.add_subplot(111)
            myPie = ax.pie(values, labels=labels)

            pieCanvas = FigureCanvasTkAgg(f, self)
            pieCanvas.draw()
            pieCanvas.get_tk_widget().grid(column=3,row=6)

#tkinter code...
app = WordTrackApp()
app.geometry('865x1000')
app.mainloop()