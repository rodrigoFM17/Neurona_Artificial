import tkinter as tk
from random import random
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

global df, matrix_X, matrix_Y, matrix_W, matrix_dW, matrix_error
matrix_X = None

app = tk.Tk()
app.title("Neurona Artificial")

def upload_file():
    global df

    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    
    if file_path:
        df = pd.read_csv(file_path, delimiter=";")
        df.insert(0, "Ones", 1)
        matrix_X = df[["Ones","X1", "X2", "X3"]].values
        matrix_Y = df[["Y"]].values
        matrix_W = []
        for i in range(4):
            matrix_W.append(random())
        print(matrix_X)
        print(matrix_Y)

def get_parameters():
    global df


upload_button = tk.Button(app, text="Cargar archivo", command=upload_file)
upload_button.pack()


app.geometry("1200x600")

app.mainloop()

