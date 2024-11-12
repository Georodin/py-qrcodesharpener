from PIL import Image, ImageDraw
import svgwrite
import tkinter as tk
from tkinter import filedialog, messagebox, Label, Entry, Checkbutton, BooleanVar
from tkinter.ttk import Combobox, Button

def analyze_qr_code(image_path, qr_code_dimension, output_format='png', output_size=(1024, 1024), transparent=False):
    img = Image.open(image_path).convert('L')
    img_width, img_height = img.size

    cell_width = img_width / qr_code_dimension[1]
    cell_height = img_height / qr_code_dimension[0]

    qr_grid = []
    for row in range(qr_code_dimension[0]):
        row_data = []
        for col in range(qr_code_dimension[1]):
            center_x = int((col + 0.5) * cell_width)
            center_y = int((row + 0.5) * cell_height)
            color = img.getpixel((center_x, center_y))
            is_black = color < 128
            row_data.append(is_black)
        qr_grid.append(row_data)

    if output_format == 'svg':
        output_svg(qr_grid, cell_width, cell_height, output_size, "recreated_qr_code.svg", transparent)
    else:
        output_png(qr_grid, output_size, "recreated_qr_code.png", transparent)

def output_svg(qr_grid, cell_width, cell_height, output_size, output_path, transparent):
    rows, cols = len(qr_grid), len(qr_grid[0])
    svg = svgwrite.Drawing(output_path, size=output_size)
    rect_width = output_size[0] / cols
    rect_height = output_size[1] / rows

    for row in range(rows):
        for col in range(cols):
            if qr_grid[row][col]:  # Black cells only
                svg.add(svg.rect((col * rect_width, row * rect_height), (rect_width, rect_height), fill="black"))
            elif not transparent:  # Add white cells only if not transparent
                svg.add(svg.rect((col * rect_width, row * rect_height), (rect_width, rect_height), fill="white"))
                
    svg.save()
    messagebox.showinfo("SVG Output", f"SVG saved as {output_path}")


def output_png(qr_grid, output_size, output_path, transparent):
    rows, cols = len(qr_grid), len(qr_grid[0])
    mode = "RGBA" if transparent else "L"  # Use RGBA for transparency
    img = Image.new(mode, (cols, rows), (255, 255, 255, 0) if transparent else 255)
    draw = ImageDraw.Draw(img)

    for row in range(rows):
        for col in range(cols):
            if qr_grid[row][col]:  # Black cells
                color = (0, 0, 0, 255) if transparent else 0  # Opaque black for transparent mode
            else:
                color = (255, 255, 255, 0) if transparent else 255  # Transparent white for transparent mode
            draw.point((col, row), fill=color)

    img = img.resize(output_size, Image.NEAREST)
    img.save(output_path)
    messagebox.showinfo("PNG Output", f"PNG saved as {output_path}")

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if filepath:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filepath)

def start_conversion():
    image_path = file_entry.get()
    if not image_path:
        messagebox.showerror("Error", "Please select an input file.")
        return

    try:
        rows = int(rows_entry.get())
        cols = int(cols_entry.get())
        qr_code_dimension = (rows, cols)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid dimensions.")
        return

    output_format = format_combobox.get().lower()
    transparent = transparent_var.get()
    analyze_qr_code(image_path, qr_code_dimension, output_format=output_format, transparent=transparent)

# Create the main GUI window
root = tk.Tk()
root.title("QR Code Analyzer")
root.geometry("400x250")
root.configure(bg="#333333")

# Input File
Label(root, text="Input File:", bg="#333333", fg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, sticky="w")
file_entry = Entry(root, width=30)
file_entry.grid(row=0, column=1, padx=10, pady=10)
Button(root, text="Browse", command=open_file).grid(row=0, column=2, padx=10, pady=10)

# QR Code Dimensions
Label(root, text="QR Code Rows:", bg="#333333", fg="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, sticky="w")
rows_entry = Entry(root, width=10)
rows_entry.insert(0, "33")
rows_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

Label(root, text="QR Code Columns:", bg="#333333", fg="#FFFFFF").grid(row=2, column=0, padx=10, pady=10, sticky="w")
cols_entry = Entry(root, width=10)
cols_entry.insert(0, "33")
cols_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Output Format
Label(root, text="Output Format:", bg="#333333", fg="#FFFFFF").grid(row=3, column=0, padx=10, pady=10, sticky="w")
format_combobox = Combobox(root, values=["PNG", "SVG"], width=8)
format_combobox.current(0)
format_combobox.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Transparent Option
transparent_var = BooleanVar()
transparent_check = Checkbutton(root, text="White is Transparent", variable=transparent_var, bg="#333333", fg="#FFFFFF", activebackground="#333333", activeforeground="#FFFFFF", selectcolor="#333333")
transparent_check.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# Start Button
Button(root, text="Start Conversion", command=start_conversion).grid(row=5, column=0, columnspan=3, padx=10, pady=20)

# Run the GUI
root.mainloop()
