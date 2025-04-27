import tkinter as tk

def display_gui(state, window):
    board = state.board
    
    for widget in window.winfo_children():
        widget.destroy()

    title = tk.Label(window, text="Game of Nim", font=("Helvetica", 24, "bold"))
    title.pack(pady=10)
    
    frame = tk.Frame(window)
    frame.pack(pady=10)
    
    for ix, group in enumerate(board):
        if group == 0:
            continue
        
        group_row = tk.Frame(frame)
        group_row.pack(pady=5)

        group_label = tk.Label(group_row, text=f"group {ix+1}: ", font=("Helvetica", 16))
        group_label.pack(side="left")

        for ij in range(group):
            item = tk.Label(group_row, text="●", font=("Helvetica", 16), fg="blue")
            item.pack(side="left", padx=2)
    
    window.update()
    