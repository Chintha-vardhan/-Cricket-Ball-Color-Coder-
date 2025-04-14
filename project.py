import tkinter as tk

def display_runs():
    try:
        balls = int(entryballs.get())
        dot = int(dotballs.get())
        Runs = int(Runs.get())
        Boundary = int(Sixes.get())
        perball = 360 / balls
        canvas.delete("all")
        radius = 100
        x = 150
        y = 150
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="black")

        counter = 0
        for _ in range(dot):
            angle = counter * perball
            canvas.create_arc(x - radius, y - radius, x + radius, y + radius,
                               start=angle, extent=perball, fill="red", outline="red")
            counter += 1
        for _ in range(Runs):
            angle = counter * perball
            canvas.create_arc(x - radius, y - radius, x + radius, y + radius,
                               start=angle, extent=perball, fill="blue", outline="blue")
            counter += 1
        for _ in range(Boundary):
            angle = counter * perball
            canvas.create_arc(x - radius, y - radius, x + radius, y + y,
                               start=angle, extent=perball, fill="green", outline="green")
            counter += 1

    except ValueError:
        canvas.create_text(150, 250, text="Invalid input. Please enter valid numbers.", fill="red")
root = tk.Tk()
root.title("Cricket Run Color Coding")
tk.Label(root, text="Total number of balls:").grid(row=0, column=0)
entryballs = tk.Entry(root)
entryballs.grid(row=0, column=1)
tk.Label(root, text="Number of dot balls:").grid(row=1, column=0)
dotballs = tk.Entry(root)
dotballs.grid(row=1, column=1)
tk.Label(root, text="Number of 1, 2, 3 run balls:").grid(row=2, column=0)
Runs = tk.Entry(root)
Runs.grid(row=2, column=1)
tk.Label(root, text="Number of 4 or 6 run balls:").grid(row=3, column=0)
Sixes = tk.Entry(root)
Sixes.grid(row=3, column=1)
button = tk.Button(root, text="Show Run Distribution", command=display_runs)
button.grid(row=4, column=0, columnspan=2)
canvas = tk.Canvas(root, width=300, height=300)
canvas.grid(row=5, column=0, columnspan=2)
root.mainloop()
