# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:38:33 2023

@author: user
"""
import tkinter as tk
from tkinter import messagebox

def show_home():
    # messagebox.showinfo("Home", "Welcome to the Home Page!")
    # Top Section
    top_section = tk.Frame(root, bg="lightblue")
    top_section.place(relx=0, rely=0, relwidth=1, relheight=0.33)

def show_about():
    # messagebox.showinfo("About", "This is a simple Tkinter menu example.")
    # Bottom Section
    bottom_section = tk.Frame(root, bg="lightcoral")
    bottom_section.place(relx=0, rely=0.67, relwidth=1, relheight=0.33)
    

def show_pdf():
    # messagebox.showinfo("PDF Process", "Welcome to the Home Page!")
    # Middle Section
    middle_section = tk.Frame(root, bg="lightgreen")
    middle_section.place(relx=0, rely=0.33, relwidth=1, relheight=0.34)


def show_contact():
    messagebox.showinfo("Contact", "Contact information goes here.")

# Create a main window
root = tk.Tk()

# Set the window state to maximized (works across different resolutions)
root.wm_state("zoomed")

# Set a title for the window
root.title("SimplyPDF")
root.iconbitmap("logo1.ico")

# set the size of window
# root.geometry("1920x1080+0+0")

# Create a menu bar
menubar = tk.Menu(root)

# Add menus to the menu bar
home_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Home", menu=home_menu)
home_menu.add_command(label="Visit Home Page", command=show_home)

pdf_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="PDF Process", menu=pdf_menu)
pdf_menu.add_command(label="Visit PDF Process", command=show_pdf)

about_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Visit About Page", command=show_about)

contact_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Contact", menu=contact_menu)
contact_menu.add_command(label="Contact Us", command=show_contact)

# Configure the root window with the menu
root.config(menu=menubar)



# Start the main event loop
root.mainloop() 







