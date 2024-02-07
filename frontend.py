import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from frontendfunctions import *

# running_flag
running_flag = False

def update_parkinglot(*args):
    try:
        lot = data[select_park_var.get()]
    except:
        lot = ["Enter a park first"]
        pass

    # Remove the previous selectlot option menu, if exists
    if hasattr(update_parkinglot, '_selectlot'):
        update_parkinglot._selectlot.destroy()

    # Create a new selectlot option menu
    selectlot = ctk.CTkOptionMenu(window, values=lot, command=selectlot_callback)
    selectlot.set("Select parking lot")
    selectlot.grid(row=2, column=0, padx=10, pady=10)

    # Store the new selectlot option menu reference
    update_parkinglot._selectlot = selectlot


def show_options():
    if schedule_var.get():
        try:
            show_options.option_menu.destroy()
        except:
            pass
        # Create an OptionMenu widget
        option_var = ctk.StringVar()
        option_menu = ctk.CTkOptionMenu(window, variable=option_var,
                                        values=["Today at 7 am", "Tomorrow at 7 am", "Day after tomorrow at 7 am"])
        option_menu.set("Select schedule time")
        option_menu.grid(row=7, column=0, padx=10, pady=10)

        # Store the OptionMenu widget reference
        show_options.option_menu = option_menu
    else:
        # Remove the OptionMenu widget when the checkbox is unchecked
        if hasattr(show_options, 'option_menu'):
            show_options.option_menu.destroy()


# Gui
window = ctk.CTk()
window.geometry("900x400")

days = getday()
data = {
    "Book a pass for Garibaldi Provincial Park": ['Chekamus - Parking [AM]', 'Chekamus - Parking [PM]', 'Diamond Head - Parking', 'Rubble Creek - Parking'],
    "Book a pass for Golden Ears Provincial Park": ['Alouette Lake Boat Launch Parking - Parking',
                                                    'Alouette Lake South Beach Day-Use Parking Lot - Parking [AM]',
                                                    'Alouette Lake South Beach Day-Use Parking Lot - Parking [PM]',
                                                    'Gold Creek Parking Lot - Parking [AM]', 'Gold Creek Parking Lot - Parking [PM]',
                                                    'West Canyon Trailhead Parking Lot - Parking [AM]',
                                                    'West Canyon Trailhead Parking Lot - Parking [PM]'],
    "Book a pass for Joffre Lakes Provincial Park": ['Joffre Lakes - Trail, 1 pass', 'Joffre Lakes - Trail , 2 pass',
                                                    'Joffre Lakes - Trail 3 pass', 'Joffre Lakes - Trail 4 pass']
}

# Create label
label = ctk.CTkLabel(window, text="Welcome to the BC Passes booking automation App", fg_color="transparent",
                     font=('Helvetica', 24))
label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nswe")

# Select park Option menu
select_park_var = ctk.StringVar()
select_park_var.trace('w', update_parkinglot)
selectpark = ctk.CTkOptionMenu(window, variable=select_park_var, values=list(data.keys()), command=selectpark_callback)
selectpark.set("Select a park")
selectpark.grid(row=1, column=0, padx=10, pady=10)

update_parkinglot()

# Select day Option menu
selectday = ctk.CTkOptionMenu(window, values=days, command=selectday_callback)
selectday.grid(row=1, column=1, padx=10, pady=10)
selectday.set("Select a day")

# Reset button
reset_button = ctk.CTkButton(window, fg_color="orange", hover_color="#363636", text="Reset",
                             command=lambda: reset_button_event(selectpark, selectday, update_parkinglot,
                                                                tries_entry, schedule_var, show_options))
reset_button.grid(row=8, column=1, padx=10, pady=10)

# Stop button
stop_button = ctk.CTkButton(window, fg_color="red", hover_color="#363636", text="Stop", command=lambda: stop_button_event(
    selectpark, selectday, update_parkinglot, tries_entry, schedule_var, show_options))
stop_button.grid(row=8, column=2, padx=10, pady=10)

# Submit button
submit_button = ctk.CTkButton(window, fg_color="green", hover_color="#363636", text="Submit",
                              command=lambda: submit_button_event(selectpark, selectday, update_parkinglot,
                                                                  tries_entry, schedule_checkbox, show_options))
submit_button.grid(row=8, column=0, padx=10, pady=10)

tries_entry = ctk.CTkEntry(window, font=('Helvetica', 10), placeholder_text="Default is 5")
tries_entry.grid(row=6, column=2, padx=20, pady=10)

tries_label = ctk.CTkLabel(window, text="Input the number of search attempts to secure the ticket * ->",
                           fg_color="transparent", font=('Helvetica', 13))
tries_label.grid(row=6, column=1, padx=10, pady=10)

# Checkbox - Schedule
schedule_var = ctk.BooleanVar()
schedule_checkbox = ctk.CTkCheckBox(window, text="Schedule", variable=schedule_var, command=show_options)
schedule_checkbox.grid(row=7, column=0, padx=10, pady=10)

additional_text = ctk.CTkLabel(window, text="* If you want to keep trying to get a ticket, input as many number of tries as you want. But if you are scheduling, only try a couple of times",
                               fg_color="transparent", font=('Helvetica', 13))
additional_text.grid(row=9, column=0, columnspan=3, padx=10, pady=10, sticky="w")


window.mainloop()

