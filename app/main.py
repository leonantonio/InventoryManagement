"""
Antonio Leon 
08/07/2023
Inventory Management App
"""
from tkinter import *
from tkinter import ttk
import tkinter as tk
import datetime
import sys
import subprocess

#Store deparments.
produce = []
deli = []
meat = []
dairy = []
candy = []
frozen = []
house = []
    
window = Tk()
window.geometry("1050x700")
window.title("Inventory Management App")
window.configure(bg="#adadad")
icon = PhotoImage(file="C:\\Users\\jose-\\OneDrive\\Documentos\\Python Programs\\InventoryManagement\\app\\icon.png")
window.iconphoto(True, icon)

def load_list():
    try:
        with open("data_base.txt", "r", encoding="utf8") as _f:
            for line in _f:
                department, name, qty, price = line.strip().split(", ")
                department = department.split(": ")[1]
                name = name.split(": ")[1]
                qty = int(qty.split(": ")[1])
                price = float(price.split(": $")[1])
                
                if department == "Produce":
                    produce.append([department, name, qty, price])
                elif department == "Deli":
                    deli.append([department, name, qty, price])
                elif department == "Meat":
                    meat.append([department, name, qty, price])
                elif department == "Dairy":
                    dairy.append([department, name, qty, price])
                elif department == "Candy":
                    candy.append([department, name, qty, price])
                elif department == "House":
                    house.append([department, name, qty, price])
                elif department == "Frozen":
                    frozen.append([department, name, qty, price])

        return produce, deli, meat, dairy, candy, house, frozen

    except FileNotFoundError:
        # If the file doesn't exist yet, return empty lists
        return [], [], [], [], [], [], []
load_list()

def reset():
    window.destroy()
    subprocess.Popen([sys.executable] + sys.argv)
        
#Canvas.
canvas1 = tk.Canvas(window, width=1025, height=45, bg="#0388A6", highlightthickness=1, highlightbackground="black")
canvas1.pack(padx=5, pady=5)

canvas2 = tk.Canvas(window, width=1025, height= 624, bg="#63BBF2", highlightthickness=1, highlightbackground="black")
canvas2.pack(padx=5, pady=5)

canvas3 = tk.Canvas(window, width=250, height= 550, bg="#63BBF2", highlightthickness=1, highlightbackground="black")
canvas2.create_window(140, 335, window=canvas3)

def about():
    
    canvas4 = tk.Canvas(window, width=730, height= 550, bg="#63BBF2", highlightthickness=1, highlightbackground="black")
    canvas2.create_window(645, 335, window=canvas4)
    
    label_version = Label(canvas4, text="Version 0.0.1\nReleased August 20, 2023", font=("times new roman", 15), bg="#63BBF2")
    canvas4.create_window(350, 500, window=label_version)

def last_time_saved():
    
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.strftime("%D %H:%M:%S")
    
    return current_time

def view_deparment():
    
    canvas_view_department = tk.Canvas(window, width=730, height= 550, bg="#63BBF2", highlightthickness=1, highlightbackground="black")
    canvas2.create_window(645, 335, window=canvas_view_department)
    
    tittleLabel = tk.Label(canvas_view_department, text="View Department", font=("times new roman", 20), bg="#03658C")
    canvas_view_department.create_window(335, 30, window=tittleLabel)
    
    department_box = ttk.Combobox(canvas_view_department, width=20, values=["Produce", "Deli", "Meat", "Dairy", "Candy", "Frozen", "House"], state="readonly")
    canvas_view_department.create_window(90, 30, window=department_box )
    
    def view_department_input():
        
        selected_department = department_box.get()
        
        tree = ttk.Treeview(canvas_view_department, columns=("Department", "Item", "Qty", "Price"), height=20)
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Department", width=170)  
        tree.column("Item", width=220)
        tree.column("Qty", width=150)          
        tree.column("Price", width=150)
        
        scrollbar = ttk.Scrollbar(canvas_view_department, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        canvas_view_department.create_window(720, 300, window=scrollbar)
        
        tree.heading("#1", text="Department")
        tree.heading("#2", text="Item")
        tree.heading("#3", text="Qty")
        tree.heading("#4", text="Price")
        
        if selected_department == "Produce":
            for department, item, qty, price in produce:
                tree.insert("", tk.END, values=(department, item, qty, price))
            canvas_view_department.create_window(365, 300, window=tree)
        elif selected_department == "Deli":
            for department, item, qty, price in deli:
                tree.insert("", tk.END, values=(department, item, qty, price))
            canvas_view_department.create_window(365, 300, window=tree)
        elif selected_department == "Meat":
            for department, item, qty, price in meat:
                tree.insert("", tk.END, values=(department, item, qty, price))
            canvas_view_department.create_window(365, 300, window=tree)
        elif selected_department == "Dairy":
            for department, item, qty, price in dairy:
                tree.insert("", tk.END, values=(department, item, qty, price))
            canvas_view_department.create_window(365, 300, window=tree)
        elif selected_department == "Candy":
            for department, item, qty, price in candy:
                tree.insert("", tk.END, values=(department, item, qty, price))
            canvas_view_department.create_window(365, 300, window=tree)
        elif selected_department == "House":
            for department, item, qty, price in house:
                tree.insert("", tk.END, values=(department, item, qty, price))
            canvas_view_department.create_window(365, 300, window=tree)
        elif selected_department == "Frozen":
            for department, item, qty, price in frozen:
                tree.insert("", tk.END, values=(department, item, qty, price))
            canvas_view_department.create_window(365, 300, window=tree)
        else:
            print("\nWrong input!\n")
            
    button_get_input = tk.Button(canvas_view_department, text="Enter", bg="white", command=view_department_input, width=19, height=1)
    canvas_view_department.create_window(90, 55, window=button_get_input)

def add_item():
    
    canvas = tk.Canvas(window, width=730, height= 550, bg="#63BBF2", highlightthickness=1, highlightbackground="black")
    canvas2.create_window(645, 335, window=canvas)
    
    def limit_input(*args):
        input_text = entry.get()
        if len(input_text) > 25:
            entry.set(input_text[:25])     
    entry = tk.StringVar()
    entry.trace("w", limit_input)
    
    def validate_integer(P):
        if P == "" or P.isdigit() and 0 <= int(P) <= 999999:
            return True
        return False
    validate_input_cmd = window.register(validate_integer)
    
    def validate_float(P):
        if P == "" or P == "-" or P == "." or P == "-.":
            return True
        try:
            float(P)
            return True
        except ValueError:
            return False
    validate_float = window.register(validate_float)
    
    #Tittle.
    label_tittle1 = tk.Label(canvas, text="   Add Item   ", font=("times new roman", 20), bg="#03658C")
    canvas.create_window(360, 30, window=label_tittle1)
    
    #Item name.
    label_name = tk.Label(canvas, text="Enter item name", font=("times new roman", 15), bg="#63BBF2")
    canvas.create_window(160, 95, window=label_name)
    entry_name = tk.Entry(canvas, width=25, textvariable=entry)
    canvas.create_window(160, 125, window=entry_name)
    
    #Item Qty.
    label_qty = tk.Label(canvas, text="Enter item qty", font=("times new roman", 15), bg="#63BBF2")
    canvas.create_window(360, 95, window=label_qty)
    entry_qty = tk.Entry(canvas, width=25, validate="key", validatecommand=(validate_input_cmd, "%P"))
    canvas.create_window(360, 125, window=entry_qty)
    
    #Item price.
    label_price = tk.Label(canvas, text="Enter item price", font=("times new roman", 15), bg="#63BBF2")
    canvas.create_window(560, 95, window=label_price)
    entry_price = tk.Entry(canvas, width=25, validate="key", validatecommand=(validate_float, "%P"))
    canvas.create_window(560, 125, window=entry_price)
    
    #Select department box.
    label_department = tk.Label(canvas, text="Select department", font=("times new roman", 14), bg="#63BBF2")
    canvas.create_window(358, 195, window=label_department)
    department_box = ttk.Combobox(canvas, width=22, values=["Produce", "Deli", "Meat", "Dairy", "Candy", "Frozen", "House"], state="readonly")
    canvas.create_window(358, 225, window=department_box )
    
    def get_input():
        item_name = entry_name.get().capitalize()
        item_qty = entry_qty.get()
        item_price = entry_price.get()
        selected_department = department_box.get()
        
        def print_item_added():
            label_item_added = tk.Label(canvas, text="Item was added!", font=("times new roman", 20), bg="white")
            canvas.create_window(360, 400, window=label_item_added)
            
            def remove_label():
                label_item_added.destroy()
            window.after(5000, remove_label)
            
        def print_fill_boxes():
            label_fill_boxes = tk.Label(canvas, text="***Fill all entry boxes!***", font=("times new roman", 20), bg="red")
            canvas.create_window(360, 400, window=label_fill_boxes)
            
            def remove_label():
                label_fill_boxes.destroy()
            window.after(5000, remove_label)
            
        if selected_department == "Produce":
            produce.append([selected_department, item_name, item_qty, item_price])
            print_item_added()
        elif selected_department == "Deli":
            deli.append([selected_department, item_name, item_qty, item_price])
            print_item_added()
        elif selected_department == "Meat":
            meat.append([selected_department, item_name, item_qty, item_price])
            print_item_added()
        elif selected_department == "Dairy":
            dairy.append([selected_department, item_name, item_qty, item_price])
            print_item_added()
        elif selected_department == "Candy":
            candy.append([selected_department, item_name, item_qty, item_price])
            print_item_added()
        elif selected_department == "House":
            house.append([selected_department, item_name, item_qty, item_price])
            print_item_added()
        elif selected_department == "Frozen":
            frozen.append([selected_department, item_name, item_qty, item_price])
            print_item_added()
        else: 
            print_fill_boxes()
    
    button_get_input = tk.Button(canvas, text="Enter", bg="white", command=get_input, width=10, height=1)
    canvas.create_window(360, 320, window=button_get_input)

def delete_item():
    
    canvas_delete_item = tk.Canvas(window, width=730, height= 550, bg="#63BBF2", highlightthickness=1, highlightbackground="black")
    canvas2.create_window(645, 335, window=canvas_delete_item)
    
    tittleLabel = tk.Label(canvas_delete_item, text="Delete Item", font=("times new roman", 20), bg="#03658C")
    canvas_delete_item.create_window(348, 30, window=tittleLabel)
    
    #Functions to limit the user's input.
    def limit_input(*args):
        input_text = entry.get()
        if len(input_text) > 25:
            entry.set(input_text[:25])     
    entry = tk.StringVar()
    entry.trace("w", limit_input)
    
    enterItemName = tk.Label(canvas_delete_item, text="Enter Item Name", font=("times new roman", 15), bg="#63BBF2")
    canvas_delete_item.create_window(350, 95, window=enterItemName)
    
    entry_name = tk.Entry(canvas_delete_item, width=55, textvariable=entry)
    canvas_delete_item.create_window(350, 120, window=entry_name)
    
    def  get_input():
        item_name = entry_name.get().capitalize()
        
        for items in [produce, deli, meat, dairy, candy, house, frozen]:
            for item in items:
                department, name, qty, price = item
                if name == item_name:
                    items.remove(item)
                    addedItemLabel = tk.Label(canvas_delete_item, text="Item was deleted", font=("times new roman", 25), bg="white")
                    canvas_delete_item.create_window(360, 420, window=addedItemLabel)
                    def remove_label():
                        addedItemLabel.destroy()
                    window.after(5000, remove_label)
                    return
        removedItemLabel = tk.Label(canvas_delete_item, text="***Item was not found!***", font=("times new roman", 25), bg="red")
        canvas_delete_item.create_window(365, 420, window=removedItemLabel)
        def remove_label():
            removedItemLabel.destroy()
        window.after(5000, remove_label)
            
    button_get_input = tk.Button(canvas_delete_item, text="Enter", bg="white", command=get_input, width=10, height=1)
    canvas_delete_item.create_window(350, 150, window=button_get_input)
    
def add_qty():
    
    canvas_add_qty = tk.Canvas(window, width=730, height= 550, bg="#63BBF2", highlightthickness=1, highlightbackground="black")
    canvas2.create_window(645, 335, window=canvas_add_qty)
    
    tittleLabel = tk.Label(canvas_add_qty, text="   Add Qty Item   ", font=("times new roman", 20), bg="#03658C")
    canvas_add_qty.create_window(350, 30, window=tittleLabel)
    
    #Functions to delimit the user's input.
    def limit_input(*args):
        input_text = entry.get()
        if len(input_text) > 25:
            entry.set(input_text[:25])     
    entry = tk.StringVar()
    entry.trace("w", limit_input)
    
    def validate_integer(P):
        if P == "" or P.isdigit() and 0 <= int(P) <= 999999:
            return True
        return False
    validate_input_cmd = window.register(validate_integer)
    
    #Labels and entry boxes.
    enterItemName = tk.Label(canvas_add_qty, text="Enter Item Name", font=("times new roman", 15), bg="#63BBF2")
    canvas_add_qty.create_window(350, 95, window=enterItemName)
    
    entry_name = tk.Entry(canvas_add_qty, width=55, textvariable=entry)
    canvas_add_qty.create_window(350, 120, window=entry_name)
    
    enterQtyLabel = tk.Label(canvas_add_qty, text="Enter Qty", font=("times new roman", 15), bg="#63BBF2")
    canvas_add_qty.create_window(348, 165, window=enterQtyLabel)
    
    entry_qty= tk.Entry(canvas_add_qty, width=55, validate="key", validatecommand=(validate_input_cmd, "%P"))
    canvas_add_qty.create_window(350, 190, window=entry_qty)
    
    def get_input():
        item_name = entry_name.get().capitalize()
        item_qty = (int(entry_qty.get()))
    
        for department, items in [("Produce", produce), ("Deli", deli), ("Meat", meat), ("Dairy", dairy), ("Candy", candy), ("Household", house), ("Frozen", frozen)]:
            for item in items:
                department, name, qty, price = item
                if name == item_name:
                    item[2] += item_qty
                    added_qty = tk.Label(canvas_add_qty, text="Added!", font=("times new roman", 25), bg="white")
                    canvas_add_qty.create_window(360, 420, window=added_qty)
                    def remove_label():
                        added_qty.destroy()
                    window.after(5000, remove_label)
                    return
    
    button_get_input = tk.Button(canvas_add_qty, text="Enter", bg="white", command=get_input, width=10, height=1)
    canvas_add_qty.create_window(350, 240, window=button_get_input)

def delete_qty():
    
    canvas_delete_qty = tk.Canvas(window, width=730, height= 550, bg="#63BBF2", highlightthickness=1, highlightbackground="black")
    canvas2.create_window(645, 335, window=canvas_delete_qty)
    
    tittleLabel = tk.Label(canvas_delete_qty, text="   Delete Qty Item   ", font=("times new roman", 20), bg="#03658C")
    canvas_delete_qty.create_window(350, 30, window=tittleLabel)
    
    #Functions to delimit the user's input.
    def limit_input(*args):
        input_text = entry.get()
        if len(input_text) > 25:
            entry.set(input_text[:25])     
    entry = tk.StringVar()
    entry.trace("w", limit_input)
    
    def validate_integer(P):
        if P == "" or P.isdigit() and 0 <= int(P) <= 999999:
            return True
        return False
    validate_input_cmd = window.register(validate_integer)
    
    #Labels and entry boxes.
    enterItemName = tk.Label(canvas_delete_qty, text="Enter Item Name", font=("times new roman", 15), bg="#63BBF2")
    canvas_delete_qty.create_window(350, 95, window=enterItemName)
    
    entry_name = tk.Entry(canvas_delete_qty, width=55, textvariable=entry)
    canvas_delete_qty.create_window(350, 120, window=entry_name)
    
    enterQtyLabel = tk.Label(canvas_delete_qty, text="Enter Qty", font=("times new roman", 15), bg="#63BBF2")
    canvas_delete_qty.create_window(348, 165, window=enterQtyLabel)
    
    entry_qty= tk.Entry(canvas_delete_qty, width=55, validate="key", validatecommand=(validate_input_cmd, "%P"))
    canvas_delete_qty.create_window(350, 190, window=entry_qty)
    
    def get_input():
        item_name = entry_name.get().capitalize()
        item_qty = (int(entry_qty.get()))
    
        for department, items in [("Produce", produce), ("Deli", deli), ("Meat", meat), ("Dairy", dairy), ("Candy", candy), ("Household", house), ("Frozen", frozen)]:
            for item in items:
                department, name, qty, price = item
                if name == item_name:
                    item[2] -= item_qty
                    added_qty = tk.Label(canvas_delete_qty, text="Deleted!", font=("times new roman", 25), bg="white")
                    canvas_delete_qty.create_window(360, 420, window=added_qty)
                    def remove_label():
                        added_qty.destroy()
                    window.after(5000, remove_label)
                    return
    button_get_input = tk.Button(canvas_delete_qty, text="Enter", bg="white", command=get_input, width=10, height=1)
    canvas_delete_qty.create_window(350, 240, window=button_get_input)

def save_list():
    with open("data_base.txt", "w", encoding="utf8") as _f:
        for items in [produce, deli, meat, dairy, candy, frozen, house]:
            for item in items:
                _f.write(f"Department: {item[0]}, Name: {item[1]}, Qty: {int(item[2])}, Price: ${float(item[3])}\n")
                
            
    def remove_label():
        label_saved_list.destroy()
    window.after(5000, remove_label)
    
    label_saved_list = tk.Label(canvas1, text="Saved!", font=("times new roman", 15), bg="white", width=8, height=1)
    canvas1.create_window(250, 23, window=label_saved_list)
    
    label_last_saved = tk.Label(canvas3, text=f"Last time saved: {last_time_saved()}", font=("times new roman", 10), bg="white",)
    canvas3.create_window(120, 520, window=label_last_saved)

#Labels.
title_label = tk.Label(canvas2, text="      Inventory Management      ", font=("times new roman", 25), bg="#63BBF2")
canvas2.create_window(512, 29, window=title_label)

tools_label = tk.Label(canvas3, text="      Tools      ", font=("times new roman", 20), bg="#03658C")
canvas3.create_window(120, 30, window=tools_label)
    
#Buttons in canvas1.
reset_button = tk.Button(canvas1, text="Reset", relief=FLAT, bg="white", command=reset, width=10, height=1)
canvas1.create_window(50, 23, window=reset_button)

save_button = tk.Button(canvas1, text="Save", relief=FLAT, bg="white", command=save_list, width=10, height=1)
canvas1.create_window(140, 23, window=save_button)

about_button = tk.Button(canvas1, text="About", relief=FLAT, bg="white", command=about)
canvas1.create_window(998, 23, window=about_button)
    
#Buttons in canvas3 (Tools).
add_item_button = tk.Button(canvas3, text="Add Item", relief=FLAT, bg="white", width=20, height=1, command=add_item)
canvas3.create_window(120, 75, window=add_item_button)

delete_item_button = tk.Button(canvas3, text="Delete Item", relief=FLAT, bg="white", width=20, height=1, command=delete_item)
canvas3.create_window(120, 110, window=delete_item_button)

view_department_button = tk.Button(canvas3, text="View Department", relief=FLAT, bg="white", width=20, height=1, command=view_deparment)
canvas3.create_window(120, 145, window=view_department_button)

add_qty_item_button = tk.Button(canvas3, text="Add Qty Item", relief=FLAT, bg="white", width=20, height=1, command=add_qty)
canvas3.create_window(120, 180, window=add_qty_item_button)

delete_qty_item_button = tk.Button(canvas3, text="Delete Qty Item", relief=FLAT, bg="white", width=20, height=1, command=delete_qty)
canvas3.create_window(120, 215, window=delete_qty_item_button)

view_department_value_button = tk.Button(canvas3, text="View Department Value", relief=FLAT, bg="white", width=20, height=1)
canvas3.create_window(120, 250, window=view_department_value_button)

window.mainloop()