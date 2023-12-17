import tkinter as tk
import csv
import datetime

# Global variables

# Input values
carbs = float(0)
fats = float(0)
proteins = float(0)
grams = float(0)

# Return values
boluscarbs = float(0)
bolusfats = float(0)
bolustotal = float(0)

# Constant values
SENSITIVITY = float(12)

# Define exit program
def exit_program():
    root.destroy()

# Save all given values
def save_values():
    global carbs, fats, proteins, grams, bolustotal, bolusfats, boluscarbs
    carbs = float(entry_carbs.get())
    fats = float(entry_fats.get())
    proteins = float(entry_proteins.get())
    grams = float(entry_grams.get())
    calculate()

# Update return text
def update_display_value():
    global carbs, fats, proteins, grams, bolustotal, bolusfats, boluscarbs
    display_value1.config(text=f"Total bolus: {bolustotal}")
    display_value2.config(text=f"Bolus for carbs: {boluscarbs}")
    display_value3.config(text=f"Bolus for fats: {bolusfats}")

# Calculate values and update return text
def calculate():
    global carbs, fats, proteins, grams, bolustotal, bolusfats, boluscarbs
    boluscarbs = ((carbs / SENSITIVITY) / 100) * grams
    boluscarbs = round(boluscarbs, 1)
    bolusfats = (((fats * 9) + (proteins * 4)) / 10000) * grams
    bolusfats = round(bolusfats, 1)
    bolustotal = boluscarbs + bolusfats
    bolustotal = round(bolustotal, 1)
    update_display_value()

# Log and reset entry values to prevent duplicate presses
def log():
    global carbs, fats, proteins, grams, bolustotal, bolusfats, boluscarbs
    if (bolustotal == 0):
        return 0
    else:
        current = datetime.datetime.now()
        time = current.strftime("%Y-%m-%d %H:%M:%S")
        with open('bolus.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Time", "Carbs", "Fats", "Proteins", "Bolus Total"])
        with open('bolus.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([time, carbs, fats, proteins, bolustotal])
        reset()

# Reset everything
def reset():
    global carbs, fats, proteins, grams, bolustotal, bolusfats, boluscarbs
    carbs = float(0)
    fats = float(0)
    proteins = float(0)
    boluscarbs = float(0)
    bolusfats = float(0)
    bolustotal = float(0)
    grams = float(0)
    sensitivity = float(12)
    entry_carbs.delete(0, tk.END)
    entry_proteins.delete(0, tk.END)
    entry_fats.delete(0, tk.END)
    entry_grams.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Bolus Calculator")
root.geometry("350x200")
root.resizable(width=False, height=False)

# Entry fields

# Carbs
label_carbs = tk.Label(root, text="Carbs:")
label_carbs.place(x=0, y=50)
entry_carbs = tk.Entry(root)
entry_carbs.place(x=60, y=50)
entry_carbs.bind("<Return>", lambda event, :save_values())

# Fats
label_fats = tk.Label(root, text="Fats:")
label_fats.place(x=0, y=80)
entry_fats = tk.Entry(root)
entry_fats.place(x=60, y=80)
entry_fats.bind("<Return>", lambda event, :save_values())

# Proteins
label_proteins = tk.Label(root, text="Proteins:")
label_proteins.place(x=0, y=110)
entry_proteins = tk.Entry(root)
entry_proteins.place(x=60, y=110)
entry_proteins.bind("<Return>", lambda event, :save_values())

# Grams
label_grams = tk.Label(root, text="Grams:")
label_grams.place(x=0, y=140)
entry_grams = tk.Entry(root)
entry_grams.place(x=60, y=140)
entry_grams.bind("<Return>", lambda event, :save_values())

# Text

#label title
label = tk.Label(root, text="Bolus calculator")
label.place(x=50, y=20)
#label total bolus
display_value1 = tk.Label(root, text="Total bolus: ")
display_value1.place(x=200, y=20)
#label bolus for carbs
display_value2 = tk.Label(root, text="Bolus for carbs: ")
display_value2.place(x=200, y=40)
#label bolus for fats
display_value3 = tk.Label(root, text="Bolus for fats:")
display_value3.place(x=200, y=60)


#BUTTONS#

#exit button
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.place(x=200, y=120)
#calc button
calculate_button = tk.Button(root, text="Calculate", command=save_values)
calculate_button.place(x=200, y=90)
#log button
calculate_button = tk.Button(root, text="Log", command=log)
calculate_button.place(x=260, y=90)

root.mainloop()
