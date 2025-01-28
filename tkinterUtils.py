import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def show_grafic(a, b, geneticAlgorithm):
    def func(x):
        return 0.1 * x * np.log(1 + np.abs(x)) * np.cos(x) * np.cos(x)
    
    x = np.linspace(a, b, 1000)
    y = func(x)

    i_min = np.argmin(y)
    i_max = np.argmax(y)

    x_min, y_min = x[i_min], y[i_min]
    x_max, y_max = x[i_max], y[i_max]

    figure, ax = plt.subplots()

    ax.plot(x, y, label="grafica de la funcion", color="blue")


    points = geneticAlgorithm.get_last_generation_points()
    ax.scatter(points["general"]["x"], points["general"]["y"], color="black", label="individuos",zorder=5, s=50)

    ax.scatter([points["best"]["x"]], [points["best"]["y"]], color="green", label="mejor", zorder=10, s=50)
    ax.scatter([points["worst"]["x"]], [points["worst"]["y"]], color="red", label="peor", zorder=10, s=50)
    ax.axhline(y=points["average_point"]["y"], color='blue', linestyle='--', linewidth=1)

    

    # Detalles del gráfico
    ax.set_title("Grafica de la funcion")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axvline(0, color="black", linewidth=0.5) 
    ax.axhline(0, color="black", linewidth=0.5)  
    ax.grid(color="gray", linestyle="--", linewidth=0.5)
    ax.legend()

    canvas = FigureCanvasTkAgg(figure, master=results) 
    canvas.draw()

    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)