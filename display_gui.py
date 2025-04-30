import tkinter as tk

def display_gui(state, window):
    board = state.board
    
    for widget in window.winfo_children():
        widget.destroy()

    title = tk.Label(window, text="Game of Nim", font=("Helvetica", 24, "bold"))
    title.pack(pady=10)
    
    frame = tk.Frame(window)
    frame.pack(pady=10)
    
    for ix, row in enumerate(board):
        if row == 0:
            continue
        
        row_frame = tk.Frame(frame)
        row_frame.pack(pady=5)

        for ij in range(row):
            item = tk.Label(row_frame, text="●", font=("Helvetica", 30), fg="blue")
            item.pack(side="left", padx=7)
    
    window.update()
    