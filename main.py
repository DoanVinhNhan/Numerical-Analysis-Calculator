import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from sympy import *
import pandas as pd
from frame_lib import *
from equationMethods import bisection_oop, secant_oop, newton1_oop

root = ctk.CTk()
root.title("Numerical Analysis Calculator")
root.geometry("800x600")
root.resizable(False, False)

frame_manager = frameManager(root)

main_frame_instance = main_frame(root, frame_manager)
equation_frame_instance = equation_frame(root, frame_manager)
nonlinear_system_frame_instance = nonlinear_system_frame(root, frame_manager)
matrix_frame_instance = matrix_frame(root, frame_manager)
bisection_frame_instance = bisection_frame(root, frame_manager)
secant_frame_instance = secant_frame(root, frame_manager)
newton1_frame_instance = newton1_frame(root, frame_manager)

frame_manager.add_frame("main_frame", main_frame_instance)
frame_manager.add_frame("equation_frame", equation_frame_instance)
frame_manager.add_frame("nonlinear_system_frame",nonlinear_system_frame_instance)
frame_manager.add_frame("matrix_frame",matrix_frame_instance)
frame_manager.add_frame("bisection_frame",bisection_frame_instance)
frame_manager.add_frame("secant_frame",secant_frame_instance)
frame_manager.add_frame("newton1_frame",newton1_frame_instance)

frame_manager.switch_frame("newton1_frame")

root.mainloop()
