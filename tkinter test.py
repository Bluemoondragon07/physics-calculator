import tkinter as tk

# Initialize global tracking variables
current_mass = ""
current_velocity = ""

def confirm_mass_input():
    global current_mass
    current_mass = mass_var.get()
    
    # 1. Update text instructions for the user
    instructionText.config(text="Now, enter the object's velocity in m/s:")
    infoText.config(text="Mass: " + current_mass + " kg")
    
    # 2. Redirect the Entry box to write to the velocity variable instead
    mass_entry.config(textvariable=velocity_var)
    mass_entry.delete(0, tk.END)  # Clear the previous text
    
    # 3. Change the button action to process the velocity next
    confirmButton.config(command=confirm_velocity_input)

def confirm_velocity_input():
    global current_mass, current_velocity
    current_velocity = velocity_var.get()
    
    # 1. Try to calculate the final momentum value safely
    try:
        m = float(current_mass)
        v = float(current_velocity)
        momentum = m * v
        result_text = f"Mass: {m} kg\nVelocity: {v} m/s\n\nMomentum: {momentum:.2f} kg·m/s"
    except ValueError:
        result_text = f"Mass: {current_mass} kg\nVelocity: {current_velocity} m/s\n\n(Error: Please enter numbers only!)"
        
    # 2. Update the final UI display
    instructionText.config(text="Calculation Complete!")
    infoText.config(text=result_text)
    confirmButton.config(state=tk.DISABLED)  # Freeze button when done

# 1. Initialize the main window root
root = tk.Tk()
root.title("Momentum Calculator")
root.geometry("500x350")

# 1.1 UI String variables
mass_var = tk.StringVar(root)
velocity_var = tk.StringVar(root)

# 2. Create standard widgets
instructionText = tk.Label(root, text="Welcome to momentum calculator. \n \n If the object's mass is known, enter it in kg", font=("Consolas", 10))
infoText = tk.Label(root, text="", font=("Consolas", 10))

confirmButton = tk.Button(root, text="Confirm", command=confirm_mass_input)
mass_entry = tk.Entry(root, textvariable=mass_var)

# 3. Geometry management to position widgets
instructionText.pack(pady=10)
infoText.pack(pady=5)
confirmButton.pack(pady=5)
mass_entry.pack(pady=5)

# 4. Run the application main event loop
root.mainloop()
