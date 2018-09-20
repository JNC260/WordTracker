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

        for F in (StartPage, BarPage, PiePage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew") #sticky is like alignment +stretch nsew (north, south, east, west)

        self.show_frame(StartPage)

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
        label.pack(pady=10, padx=10) #add padding

        def analyze(text):
            words = functions.formatInputText(text)
            counts = functions.findWordCount(words)
            most = functions.findMostUsed(counts)
            tk.Label(self, text = most).pack()

        textInput = ttk.Entry(self)
        textInput.pack()
        self.text = textInput.get()

        analyzeButton =ttk.Button(self, text="Analyze Text", command=lambda: analyze(textInput.get()))
        analyzeButton.pack()

        barButton = ttk.Button(self, text="View Bar Graph", command=lambda: controller.show_frame(BarPage)) #command runs on load, so we need to get around it using lamda
        barButton.pack()

        pieButton = ttk.Button(self, text="View Pie Chart", command=lambda: controller.show_frame(PiePage))
        pieButton.pack()

class BarPage(tk.Frame):

    def __init__(self, parent, controller):

        self.controller = controller

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Word Frequency", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        def getText():
            startPage = self.controller.access_page("StartPage")
            text = startPage.text
            return text
        
        # barText = getText()

        showGraphButton = ttk.Button(self, text="Show Graph", command=lambda: makeBar(getText()))
        showGraphButton.pack()

        backButton = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage)) 
        backButton.pack()
        
        def makeBar(text):
            words = functions.formatInputText(text)
            print(words)
            counts = functions.findWordCount(words)
            print(counts)
            values = functions.wordBarGraph(counts, words)
            print(values)
            x = values["x"]
            y = values["y"]

            f = Figure()
            ax = f.add_subplot(111)
            myBar = ax.bar(x, y)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack()

class PiePage(tk.Frame):

    def __init__(self, parent, controller):

        self.controller = controller

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Word Frequency", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def makePie(text):
            words = functions.formatInputText(text)
            counts = functions.findWordCount(words)
            pie = functions.wordPieChart(counts, words)
            return pie

        data = makePie('She loves me yea yea yea')
        labels = data["labels"]
        values = data["values"]

        f = Figure()
        ax = f.add_subplot(111)
        myPie = ax.pie(values, labels=labels)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        backButton = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage)) 
        backButton.pack()
        
#tkinter code...
app = WordTrackApp()
app.mainloop()