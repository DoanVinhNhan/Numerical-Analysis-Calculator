import customtkinter as ctk

# Initialize the application
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.title("Numerical Analysis Calculator")
root.geometry("800x600")
root.resizable(False, False)

# Function to switch frames
def switch_frame(new_frame):
    for widget in root.winfo_children():
        widget.destroy()
    new_frame()

# Main frame
def main_frame():
    label = ctk.CTkLabel(root, text="Máy tính giải tích số", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    source = ctk.CTkLabel(root, text="Source by ĐVN", font=ctk.CTkFont(size=12))
    source.place(x=10, y=565)
    feedback = ctk.CTkButton(root, text="Feedback")
    feedback.place(x=700, y=560)
    ctk.CTkButton(root, text="Giải phương trình f(x) = 0", command=lambda: switch_frame(equation_frame), width=400, height=60).place(x=200, y=100)
    ctk.CTkButton(root, text="Giải hệ phi tuyến", command=lambda: switch_frame(nonlinear_system_frame), width=400, height=60).place(x=200, y=200)
    ctk.CTkButton(root, text="Giải hệ phương trình AX = B", command=lambda: switch_frame(matrix_frame), width=400, height=60).place(x=200, y=300)

# Problems frame
def equation_frame():
    label = ctk.CTkLabel(root, text="Giải phương trình", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    ctk.CTkButton(root, text="Phương pháp Chia đôi", command=lambda: switch_frame(bisection_frame), width=400, height=60).place(x=200, y=100)
    ctk.CTkButton(root, text="Phương pháp Dây cung", command=lambda: switch_frame(secant_frame), width=400, height=60).place(x=200, y=200)
    ctk.CTkButton(root, text="Phương pháp Tiếp tuyến", command=lambda: switch_frame(newton1_frame), width=400, height=60).place(x=200, y=300)
    ctk.CTkButton(root, text="Phương pháp Lặp đơn", command=lambda: switch_frame(single1_loop_frame), width=400, height=60).place(x=200, y=400)
    ctk.CTkButton(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    ctk.CTkButton(root, text="Quay lại", command=lambda: switch_frame(main_frame)).place(x=600, y=560)

def nonlinear_system_frame():
    label = ctk.CTkLabel(root, text="Giải hệ phi tuyến", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    ctk.CTkButton(root, text="Phương pháp Newton Raphson", command=lambda: switch_frame(newton_frame), width=400, height=60).place(x=200, y=100)
    ctk.CTkButton(root, text="Phương pháp Newton Modified", command=lambda: switch_frame(newton_m_frame), width=400, height=60).place(x=200, y=200)
    ctk.CTkButton(root, text="Phương pháp Lặp đơn", command=lambda: switch_frame(single_loop_frame), width=400, height=60).place(x=200, y=300)
    ctk.CTkButton(root, text="Quay lại", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    ctk.CTkButton(root, text="Quay lại", command=lambda: switch_frame(main_frame)).place(x=600, y=560)

def matrix_frame():
    label = ctk.CTkLabel(root, text="Giải hệ phương trình AX = B", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    ctk.CTkButton(root, text="Phương pháp Gauss", command=lambda: switch_frame(gauss_frame), width=400, height=60).place(x=200, y=100)
    ctk.CTkButton(root, text="Phương pháp Gauss-Jordan", command=lambda: switch_frame(gauss_jordan_frame), width=400, height=60).place(x=200, y=200)
    ctk.CTkButton(root, text="Phương pháp Phân rã LU", command=lambda: switch_frame(lu_frame), width=400, height=60).place(x=200, y=300)
    ctk.CTkButton(root, text="Phương pháp Cholesky", command=lambda: switch_frame(cholesky_frame), width=400, height=60).place(x=200, y=400)
    ctk.CTkButton(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    ctk.CTkButton(root, text="Quay lại", command=lambda: switch_frame(main_frame)).place(x=600, y=560)

# Example method frame
def bisection_frame():
    label = ctk.CTkLabel(root, text="Phương pháp Chia đôi", font=ctk.CTkFont(size=30, weight="bold"))
    label.pack(pady=20)
    ctk.CTkButton(root, text="Home", command=lambda: switch_frame(main_frame)).place(x=700, y=560)
    ctk.CTkButton(root, text="Quay lại", command=lambda: switch_frame(equation_frame)).place(x=600, y=560)
    ctk.CTkButton(root, text="Reset", command=lambda: switch_frame(bisection_frame)).place(x=20, y=560)

# Add more method frames as needed... (similar to bisection_frame)

# Initialize with the main frame
main_frame()

# Start the main event loop
root.mainloop()
