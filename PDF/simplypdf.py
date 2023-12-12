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
from tkinter import filedialog

def show_home():
    canvas.yview_moveto(0)

def show_about():
    canvas.yview_moveto(0.25)

def show_pdf():
    canvas.yview_moveto(0.5)

def show_contact():
    canvas.yview_moveto(0.75)


def image_render(section, image, aligment):  
    
    # Create a frame for the image
     image_frame_pdf = tk.Frame(section, bg="")
     image_frame_pdf.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

     # Add an image to the image frame with reduced size
     original_image_pdf = tk.PhotoImage(file=image)

     # Resize the image
     resized_image_pdf = original_image_pdf.subsample(3, 3)

     image_label_pdf = tk.Label(image_frame_pdf, image=resized_image_pdf)
     image_label_pdf.image = resized_image_pdf  # Keep a reference to the image to prevent garbage collection
     
     if aligment == 'LEFT':
         # Place the image to the left of the frame
         image_label_pdf.pack(side=tk.LEFT)
     elif aligment == 'RIGHT':
         image_label_pdf.pack(side=tk.RIGHT)

     # Adjust column weights to make them expand proportionally
     section.columnconfigure(0, weight=1)

     # Adjust row weight to make it expand with the window
     section.rowconfigure(0, weight=1)
     
def upload_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        messagebox.showinfo("File Uploaded", f"Selected PDF file: {file_path}")


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

def pdf_content():  
    image_render(middle_section,"Book2.png",aligment='LEFT')
    
    # Add Upload PDF button
    upload_button = tk.Button(middle_section, text="Upload PDF", command=upload_pdf)
    upload_button.grid(row=0, column=0, pady=10)
    
    # image_render(middle_section,"Book3.png",aligment='RIGHT')
    

def about_content():
    image_render(about_section, "girl1.png",aligment='LEFT')
    
    # Create a frame for text
    text_frame_ab = tk.Frame(about_section, bg="")
    text_frame_ab.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)

    # Add text to the text frame
    pdf_text_ab = tk.Text(text_frame_ab, wrap=tk.WORD, font=("Comic Sans MS", 12))
    pdf_text_ab.insert(tk.END, """Welcome to our innovative and efficient PDF extraction project! Our PDF Extraction Project takes center stage in an era where information is crucial by providing state-of-the-art 
solutions that expedite the extraction of insightful data from PDF documents. Our top priority is creating user-friendly interfaces so that our clients may extract PDFs with ease and convenience.""")
    pdf_text_ab.config(state=tk.DISABLED)
    pdf_text_ab.pack(expand=True, fill=tk.BOTH)

    # Adjust column weights to make them expand proportionally
    about_section.columnconfigure(0, weight=1)
    about_section.columnconfigure(1, weight=300)


def contact_content():
    # Create a frame for image
    image_render(bottom_section, "girl2.png", aligment='LEFT')

    # Create a frame for text
    text_frame_con = tk.Frame(bottom_section, bg="")
    text_frame_con.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)

    # Add text to the text frame
    pdf_text_con = tk.Text(text_frame_con, wrap=tk.WORD, font=("Comic Sans MS", 12))
    pdf_text_con.insert(tk.END, """We appreciate your interest in our PDF extraction project. Your feedback and inquiries are important to us. Whether you have questions about the project's features, encounter any issues, or have suggestions for improvements, we encourage you to get in touch with us.
You can reach us by email here: pratiksha.garkar@mmit.edu.in""")
    pdf_text_con.config(state=tk.DISABLED)
    pdf_text_con.pack(expand=True, fill=tk.BOTH)

    # Adjust column weights to make them expand proportionally
    bottom_section.columnconfigure(0, weight=1)
    bottom_section.columnconfigure(1, weight=300)


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
about_section = tk.Frame(canvas, bg="")

# Place the frames on the canvas
top_section.place(relx=0, rely=0, relwidth=1, relheight=0.25)
bottom_section.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)
middle_section.place(relx=0, rely=0.25, relwidth=1, relheight=0.25)
about_section.place(relx=0, rely=0.5, relwidth=1, relheight=0.25)

# Add text and image to the Home section
home_content()
# Add button and image to the PDF process section
pdf_content()
about_content()
contact_content()
# Start the main event loop
root.mainloop()


