import tkinter as tk
from random import random
from tkinter import filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

global df, matrix_X, matrix_Yd, matrix_Yc, matrix_W, matrix_dW, matrix_error, n, input_n
continue_question = True

error_norms = []
weights = []

sum_mode = True

app = tk.Tk()
app.title("Neurona Artificial")

def upload_file():
    global df, matrix_X, matrix_Yd, matrix_W

    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    
    if file_path:
        df = pd.read_csv(file_path)
        df.insert(0, "Ones", 1)
        matrix_X = df[["Ones","X1", "X2", "X3"]].to_numpy()
        matrix_Yd = df[["Y"]].to_numpy()
        matrix_W = []
        for i in range(matrix_X.shape[1]):
            matrix_W.append(random())
        matrix_W = pd.DataFrame(matrix_W).to_numpy()
        weights.append(matrix_W.flatten().tolist())
        print(matrix_X)
        print(matrix_Yd)
        print(matrix_W)

def start():
    global matrix_X, matrix_Yc, matrix_Yd, matrix_W, matrix_error, matrix_dW, continue_question, n, input_n

    while continue_question:
        matrix_Yc = np.dot(matrix_X, matrix_W)
        matrix_error = matrix_Yd - matrix_Yc

        matrix_XT = matrix_X.T

        matrix_dW = np.dot(matrix_XT, matrix_error)

        n = float(input_n.get())
        
        if sum_mode:
            matrix_W = matrix_W + n * matrix_dW
        else: 
            matrix_W = matrix_W - n * matrix_dW
        
        error_norm = np.linalg.norm(matrix_error)

        error_norms.append(error_norm)
        weights.append(matrix_dW.flatten().tolist())
        
        print("Yc: ", matrix_Yc)
        print("error", matrix_error)
        print("|error| : ", error_norm)
        print("dW: ", matrix_dW)
        print("w: ", matrix_W)

        continue_question = messagebox.askyesno("Continuar", "el error es " + str(error_norm))
    
    grafic_errors()
    grafic_weights()


label = tk.Label(app, text="ingresa el valor de n: ")
label.pack(pady=20)
input_n = tk.Entry(app)
input_n.pack()
upload_button = tk.Button(app, text="Cargar archivo", command=upload_file)
upload_button.pack()
start_button = tk.Button(app, text="iniciar Neurona", command=start)
start_button.pack()

def grafic_errors():
    iterations = np.arange(1, len(error_norms) + 1)
    plt.plot(iterations, error_norms, marker='o', linestyle='-', color='b', label="Error")

    plt.xlabel("Iteración")
    plt.ylabel("Error")
    plt.title("Evolución del Error")
    plt.legend()
    plt.grid(True)
    
    plt.show()

def grafic_weights():

    weights_array = np.array(weights)
    plt.subplot(1, 2, 2)
    for i in range(weights_array.shape[1]):
        plt.plot(range(1, len(weights) + 1), weights_array[:, i], marker='o', linestyle='-', label=f"W{i}")

    plt.xlabel("Iteración")
    plt.ylabel("Valor de los Pesos")
    plt.title("Evolución de los Pesos")
    plt.legend()
    plt.grid(True)

    plt.show()

app.geometry("1200x600")

app.mainloop()

