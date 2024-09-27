import tkinter as tk


class Car:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def display_info(self):
        print(f"Carro: {self.marca}, {self.modelo}")
    
marcaexibe = input("Marca: ")
modeloexibe = input("Modelo: ")

carro1 = Car(marcaexibe, modeloexibe)

carro1.display_info()