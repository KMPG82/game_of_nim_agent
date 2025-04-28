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

        for ij in range(group):
            item = tk.Label(group_row, text="●", font=("Helvetica", 30), fg="blue")
            item.pack(side="left", padx=7)
    
    window.update()
    