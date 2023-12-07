# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:38:33 2023

@author: user
"""

# import tkinter as tk
# from tkinter import messagebox

# def show_home():
#     canvas.yview_moveto(0)

# def show_about():
#     canvas.yview_moveto(0.25)

# def show_pdf():
#     canvas.yview_moveto(0.5)

# def show_contact():
#     canvas.yview_moveto(0.75)
    
# def home_content():
#     pdf_text = tk.Text(top_section, wrap=tk.WORD, font=("Comic Sans MS", 12), padx=10, pady=10)
#     pdf_text.insert(tk.END, """For a variety of reasons, the PDF (Portable Document Format) file format has grown to be widely used and significant in today's digital world. PDFs offer a level of security for important data by supporting password protection and encryption.""")
#     pdf_text.config(state=tk.DISABLED)
#     pdf_text.pack(expand=True,fill=tk.BOTH)
#     print('Yes')
    
#     # Add an image to the Home section
#     image_path = "Book1.png"  # Replace with the actual path to your image
#     image = tk.PhotoImage(file=image_path)
#     image_label = tk.Label(top_section, image=image)
#     image_label.pack()
    

# # Create a main window
# root = tk.Tk()

# # Set the window state to maximized (works across different resolutions)
# root.wm_state("zoomed")

# # Set a title for the window
# root.title("SimplyPDF")
# root.iconbitmap("logo1.ico")

# # Create a menu bar
# menubar = tk.Menu(root)

# # Add menus to the menu bar without tearoff
# menubar.add_command(label="Home", command=show_home)
# menubar.add_command(label="PDF Process", command=show_pdf)
# menubar.add_command(label="About", command=show_about)
# menubar.add_command(label="Contact", command=show_contact)

# # Configure the root window with the menu
# root.config(menu=menubar)

# # Create a canvas to hold the sections
# canvas = tk.Canvas(root)
# canvas.pack(fill=tk.BOTH, expand=True)

# # Create frames for the sections
# top_section = tk.Frame(canvas, bg="")
# bottom_section = tk.Frame(canvas, bg="")
# middle_section = tk.Frame(canvas, bg="")
# contact_section = tk.Frame(canvas, bg="")

# # Place the frames on the canvas
# top_section.place(relx=0, rely=0, relwidth=1, relheight=0.25)
# bottom_section.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)
# middle_section.place(relx=0, rely=0.25, relwidth=1, relheight=0.25)
# contact_section.place(relx=0, rely=0.5, relwidth=1, relheight=0.25)

# # Add PDF info and GIF in Home section
# home_content()

# # Start the main event loop
# root.mainloop()    

import tkinter as tk
from tkinter import messagebox

def show_home():
    canvas.yview_moveto(0)

def show_about():
    canvas.yview_moveto(0.25)

def show_pdf():
    canvas.yview_moveto(0.5)

def show_contact():
    canvas.yview_moveto(0.75)

def home_content():
    
    # Create a frame for text
    text_frame = tk.Frame(top_section, bg="")
    text_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

    # Add text to the text frame
    pdf_text = tk.Text(text_frame, wrap=tk.WORD, font=("Comic Sans MS", 12))
    pdf_text.insert(tk.END, """For a variety of reasons, the PDF (Portable Document Format) file format has grown to be widely used and significant in today's digital world. PDFs offer a level of security for important data by supporting password protection and encryption.""")
    pdf_text.config(state=tk.DISABLED)
    pdf_text.pack(expand=True, fill=tk.BOTH)
 

    # Create a frame for the image
    image_frame = tk.Frame(top_section, bg="")
    image_frame.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)

    # Add an image to the image frame with reduced size
    image_path = "Book1.png"  # Replace with the actual path to your image
    original_image = tk.PhotoImage(file=image_path)
    # Reduce the size by a factor (e.g., 2 for half the size)
    reduced_image = original_image.subsample(2, 2)
    image_label = tk.Label(image_frame, image=reduced_image)
    image_label.image = reduced_image  # Keep a reference to the image to prevent garbage collection
    image_label.pack(expand=True, fill=tk.BOTH)

    # Adjust column weights to make them expand proportionally
    top_section.columnconfigure(0, weight=300)
    top_section.columnconfigure(1, weight=1)

    # Adjust row weight to make it expand with the window
    top_section.rowconfigure(0, weight=1)

# Rest of your code...

# Create a main window
root = tk.Tk()

# Set the window state to maximized (works across different resolutions)
root.wm_state("zoomed")

# Set a title for the window
root.title("SimplyPDF")
root.iconbitmap("logo1.ico")

# Create a menu bar
menubar = tk.Menu(root)

# Add menus to the menu bar without tearoff
menubar.add_command(label="Home", command=show_home)
menubar.add_command(label="PDF Process", command=show_pdf)
menubar.add_command(label="About", command=show_about)
menubar.add_command(label="Contact", command=show_contact)

# Configure the root window with the menu
root.config(menu=menubar)

# Create a canvas to hold the sections
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Create frames for the sections
top_section = tk.Frame(canvas, bg="")
bottom_section = tk.Frame(canvas, bg="")
middle_section = tk.Frame(canvas, bg="")
contact_section = tk.Frame(canvas, bg="")

# Place the frames on the canvas
top_section.place(relx=0, rely=0, relwidth=1, relheight=0.25)
bottom_section.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)
middle_section.place(relx=0, rely=0.25, relwidth=1, relheight=0.25)
contact_section.place(relx=0, rely=0.5, relwidth=1, relheight=0.25)

# Add text and image to the Home section
home_content()

# Start the main event loop
root.mainloop()
