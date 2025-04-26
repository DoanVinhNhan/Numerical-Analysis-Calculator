import customtkinter as ctk
from sympy import *
from frame_lib import *

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
single_loop1_frame_instance = single_loop1_frame(root, frame_manager)
newton_raphson_frame_instance = newton_raphson_frame(root,frame_manager)
single_loop_frame_instance = single_loop_frame(root, frame_manager)

frame_manager.add_frame("main_frame", main_frame_instance)
frame_manager.add_frame("equation_frame", equation_frame_instance)
frame_manager.add_frame("nonlinear_system_frame",nonlinear_system_frame_instance)
frame_manager.add_frame("matrix_frame",matrix_frame_instance)
frame_manager.add_frame("bisection_frame",bisection_frame_instance)
frame_manager.add_frame("secant_frame",secant_frame_instance)
frame_manager.add_frame("newton1_frame",newton1_frame_instance)
frame_manager.add_frame("single_loop1_frame", single_loop1_frame_instance)
frame_manager.add_frame("single_loop_frame", single_loop_frame_instance)
frame_manager.add_frame("newton_raphson_frame",newton_raphson_frame_instance)

frame_manager.switch_frame("newton_raphson_frame")

root.mainloop()
