from laptoGamer import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import random
class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.laptos=[]
        self.imagenes=["C:\\Users\\Magaly Chulde\\Desktop\\M6 ANÁLISIS DE DATOS CON PYTHON\\Ejercicios\\CLASES\img\\1.jpg","C:\\Users\\Magaly Chulde\\Desktop\\M6 ANÁLISIS DE DATOS CON PYTHON\\Ejercicios\\CLASES\img\\2.jpg","C:\\Users\\Magaly Chulde\\Desktop\\M6 ANÁLISIS DE DATOS CON PYTHON\\Ejercicios\\CLASES\img\\3.jpg","C:\\Users\\Magaly Chulde\\Desktop\\M6 ANÁLISIS DE DATOS CON PYTHON\\Ejercicios\\CLASES\img\\4.jpg","C:\\Users\\Magaly Chulde\\Desktop\\M6 ANÁLISIS DE DATOS CON PYTHON\\Ejercicios\\CLASES\img\\5.jpg"]
        ventana.title("Ingresar datos")
        self.setup_ui()
    def setup_ui(self):
        ttk.Label(self.ventana, text="Marca").grid(row=0,column=0)
        self.marca=tk.StringVar()
        ttk.Entry(self.ventana, textvariable=self.marca).grid(row=0,column=1)

        ttk.Label(self.ventana, text="Procesador").grid(row=1,column=0)
        self.procesador=tk.StringVar()
        ttk.Entry(self.ventana, textvariable=self.procesador).grid(row=1,column=1)
        
        ttk.Label(self.ventana, text="Memoria").grid(row=2,column=0)
        self.memoria=tk.StringVar()
        ttk.Entry(self.ventana, textvariable=self.memoria).grid(row=2,column=1)

        ttk.Label(self.ventana, text="Tarjeta Grafica").grid(row=3,column=0)
        self.tarjetaGrafica=tk.StringVar()
        ttk.Entry(self.ventana, textvariable=self.tarjetaGrafica).grid(row=3,column=1)
  
        ttk.Label(self.ventana, text="Precio").grid(row=4,column=0)
        self.precio=tk.StringVar()
        ttk.Entry(self.ventana, textvariable=self.precio).grid(row=4,column=1)
        
        ttk.Button(self.ventana,text="Agregar lapto",command=self.agregarLapto).grid(row=5,column=0)
    
        self.mostrarLaptos=tk.Text(self.ventana,height=10,width=50)
        self.mostrarLaptos.grid(row=6,column=0,columnspan=2)

        self.canva=tk.Canvas(self.ventana, width=200,height=200)
        self.canva.grid(row=1,column=3,rowspan=6)

    def agregarLapto(self):
        nuevaLapto=LaptoGamer(self.marca.get(),self.procesador.get(),self.memoria.get(),self.tarjetaGrafica.get(),self.precio.get())
        self.laptos.append(nuevaLapto)
        self.mostrarLaptos.insert(tk.END,f"{nuevaLapto}")
        self.mostrarImagenesAleatorias()
    def mostrarImagenesAleatorias(self):
        imagenPath=random.choice(self.imagenes)
        imagen=Image.open(imagenPath)
        imagen=imagen.resize((200,200),Image.Resampling.LANCZOS)
        photo=ImageTk.PhotoImage(imagen)
        self.canva.create_image(0,0, ancho=tk.NW,image=photo)
        self.canva.image=photo


    
        pass


ventana=tk.Tk()
app=App(ventana)
ventana.mainloop()