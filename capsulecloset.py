import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import date

# colours for my prototype
BURGUNDY = "#7A1230"
CREAM = "#F7EEDC"

# Where my clothes are saved
FOLDER = os.path.dirname(os.path.abspath(__file__))
CLOTHES_FILE = os.path.join(FOLDER, "clothes.csv")

# Options for the dropdown menus
CATEGORIES = ["Tops", "Bottoms", "Dresses", "Outerwear", "Shoes", "Accessories"]
SEASONS = ["Summer", "Autumn", "Winter", "Spring", "All Seasons"]

# Make the main window
root = tk.Tk()
root.title("CapsuleCloset")
root.geometry("900x600")
root.configure(bg=CREAM)

# Sidebar on the left
sidebar = tk.Frame(root, bg=BURGUNDY, width=180)
sidebar.pack(side="left", fill="y")

title = tk.Label(sidebar, text="CapsuleCloset", bg=BURGUNDY, fg=CREAM, font=("Helvetica", 16, "bold"))
title.pack(pady=30, padx=20)

# Main area on the right
content = tk.Frame(root, bg=CREAM)
content.pack(side="right", fill="both", expand=True)

# ---------- Pages ----------
def clear_page():
    # remove everything in the content area before showing a new page
    for widget in content.winfo_children():
        widget.destroy()

def save_clothing_to_file(name, category, season, colour):
    file_exists = os.path.exists(CLOTHES_FILE)
    with open(CLOTHES_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["name", "category", "season", "colour", "image", "date_added", "last_worn"])
        writer.writerow([name, category, season, colour, "", date.today().isoformat(), ""])

def show_home():
    clear_page()
    tk.Label(content, text="Let's Choose an Outfit!", bg=CREAM, fg=BURGUNDY, font=("Helvetica", 24, "bold")).pack(pady=40)

def load_clothes():
    if not os.path.exists(CLOTHES_FILE):
        return []
    with open(CLOTHES_FILE, newline="") as file:
        return list(csv.DictReader(file))

def save_all_clothes(clothes):
    with open(CLOTHES_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "category", "season", "colour", "image", "date_added", "last_worn"])
        writer.writeheader()
        writer.writerows(clothes)

def days_since_worn(item):
    if item["last_worn"] == "":
        last_date = item["date_added"]
    else:
        last_date = item["last_worn"]
    return (date.today() - date.fromisoformat(last_date)).days

def mark_worn_today(name):
    clothes = load_clothes()
    for item in clothes:
        if item["name"] == name:
            item["last_worn"] = date.today().isoformat()
    save_all_clothes(clothes)
    
def show_wardrobe():
    clear_page()
    tk.Label(content, text="My Wardrobe", bg=CREAM, fg=BURGUNDY, font=("Helvetica", 24, "bold")).pack(pady=(30, 10))

    tk.Label(content, text="Season", bg=CREAM, fg=BURGUNDY, font=("Helvetica", 13)).pack()
    season_filter = ttk.Combobox(content, values=["All"] + SEASONS, state="readonly", width=20)
    season_filter.set("All")
    season_filter.pack(pady=(0, 15))

    list_area = tk.Frame(content, bg=CREAM)
    list_area.pack()

    def draw_list():
        for widget in list_area.winfo_children():
            widget.destroy()

        chosen = season_filter.get()
        count = 0
        for item in load_clothes():
            if chosen == "All" or item["season"] == chosen or item["season"] == "All Seasons":
                text = item["name"] + "  ·  " + item["category"] + "  ·  " + item["season"] + "  ·  " + item["colour"]
                tk.Label(list_area, text=text, bg=CREAM, fg=BURGUNDY, font=("Helvetica", 14)).pack(anchor="w", pady=3)
                count = count + 1

        if count == 0:
            tk.Label(list_area, text="No clothes here yet!", bg=CREAM, fg=BURGUNDY, font=("Helvetica", 14)).pack()

    season_filter.bind("<<ComboboxSelected>>", lambda event: draw_list())
    draw_list()
    
def show_add_clothing():
    clear_page()
    tk.Label(content, text="Add Clothing", bg=CREAM, fg=BURGUNDY, font=("Helvetica", 24, "bold")).pack(pady=(30, 20))

    tk.Label(content, text="Name", bg=CREAM, fg=BURGUNDY, font=("Helvetica", 13)).pack()
    name_box = tk.Entry(content, width=30)
    name_box.pack(pady=(0, 10))

    tk.Label(content, text="Category", bg=CREAM, fg=BURGUNDY, font=("Helvetica", 13)).pack()
    category_box = ttk.Combobox(content, values=CATEGORIES, state="readonly", width=27)
    category_box.set("Tops")
    category_box.pack(pady=(0, 10))

    tk.Label(content, text="Season", bg=CREAM, fg=BURGUNDY, font=("Helvetica", 13)).pack()
    season_box = ttk.Combobox(content, values=SEASONS, state="readonly", width=27)
    season_box.set("All Seasons")
    season_box.pack(pady=(0, 10))

    tk.Label(content, text="Colour", bg=CREAM, fg=BURGUNDY, font=("Helvetica", 13)).pack()
    colour_box = tk.Entry(content, width=30)
    colour_box.pack(pady=(0, 20))

    def on_save():
            name = name_box.get().strip()
            if name == "":
                messagebox.showwarning("Missing name", "Please type a name for this item.")
                return
            save_clothing_to_file(name, category_box.get(), season_box.get(), colour_box.get().strip())
            messagebox.showinfo("Saved!", name + " was added to your wardrobe ♡")
            show_add_clothing()

    save_button = tk.Label(content, text="Add to wardrobe", bg=BURGUNDY, fg=CREAM,
                            font=("Helvetica", 13, "bold"), padx=15, pady=8, cursor="hand2")
    save_button.pack()
    save_button.bind("<Button-1>", lambda event: on_save())

def wear_and_refresh(name):
    mark_worn_today(name)
    show_reminders()

def make_wear_button(row, name):
    button = tk.Label(row, text="Wore it today", bg=BURGUNDY, fg=CREAM, font=("Helvetica", 12, "bold"), padx=10, pady=4, cursor="hand2")
    button.pack(side="left")
    button.bind("<Button-1>", lambda event: wear_and_refresh(name))

def show_reminders():
    clear_page()
    tk.Label(content, text="Haven't Worn Lately", bg=CREAM, fg=BURGUNDY, font=("Helvetica", 24, "bold")).pack(pady=(30, 5))
    tk.Label(content, text="These pieces haven't been worn in 30+ days. Give them some love ♡", bg=CREAM, fg=BURGUNDY, font=("Helvetica", 13)).pack(pady=(0, 20))

    count = 0
    for item in load_clothes():
        days = days_since_worn(item)
        if days >= 30:
            row = tk.Frame(content, bg=CREAM)
            row.pack(pady=4)
            text = item["name"] + "  ·  " + str(days) + " days"
            tk.Label(row, text=text, bg=CREAM, fg=BURGUNDY, font=("Helvetica", 14)).pack(side="left", padx=10)
            make_wear_button(row, item["name"])
            count = count + 1

    if count == 0:
        tk.Label(content, text="You've worn everything recently - nice!", bg=CREAM, fg=BURGUNDY, font=("Helvetica", 14)).pack()


# ---------- Sidebar buttons ----------
def make_nav_button(text, page_function):
    button = tk.Label(sidebar, text=text, bg=BURGUNDY, fg=CREAM, font=("Helvetica", 13), cursor="hand2")
    button.pack(fill="x", pady=8)
    button.bind("<Button-1>", lambda event: page_function())

make_nav_button("Home", show_home)
make_nav_button("Wardrobe", show_wardrobe)
make_nav_button("Add Clothing", show_add_clothing)
make_nav_button("Reminders", show_reminders)

# Show the home page when the app starts
show_home()

# Keep the window open
root.mainloop()

