import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result.set(f"Fahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")

        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result.set(f"Celsius: {c:.2f} °C\nKelvin: {k:.2f} K")

        elif unit == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result.set(f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# GUI window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("350x300")
window.resizable(False, False)

# Heading
tk.Label(window, text="Temperature Converter", font=("Arial", 16, "bold")).pack(pady=10)

# Input
tk.Label(window, text="Enter Temperature:").pack()
entry_temp = tk.Entry(window)
entry_temp.pack(pady=5)

# Unit selection
tk.Label(window, text="Select Unit:").pack()
unit_var = tk.StringVar(value="Celsius")
tk.OptionMenu(window, unit_var, "Celsius", "Fahrenheit", "Kelvin").pack(pady=5)

# Convert button
tk.Button(window, text="Convert", command=convert_temperature, bg="blue", fg="white").pack(pady=10)

# Result display
result = tk.StringVar()
tk.Label(window, textvariable=result, font=("Arial", 12)).pack(pady=10)

# Run app
window.mainloop()
