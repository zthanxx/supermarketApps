import tkinter as tk
import json

# Parse the JSON object
json_data = '{"all_items": [{"item": "susu", "harga": 50000}, {"item": "daging", "harga": 20000}, {"item": "lampu", "harga": 15000}, {"item": "masker", "harga": 25000}, {"item": "apel", "harga": 30000}]}'
data = json.loads(json_data)

# Create the main window
window = tk.Tk()
window.title('Super Market Chasier')
topFrame=tk.Frame(window,bd=10,relief=tk.RIDGE)
topFrame.pack(side=tk.TOP)
labelTitle=tk.Label(topFrame, text ='Hello This is Super Super Market Chasier Apps' , font=('arial',16,'bold'))
labelTitle.grid(row=0,column=0)
label = tk.Label(window, text="Total: 0")
label.pack(side=tk.BOTTOM)
# Create the check buttons and entry fields
menuFrame=tk.Frame(window, bd =10, relief= tk.RIDGE)
menuFrame.pack(side=tk.LEFT)

vars = []
entries = []
check_buttons = []
for i, item in enumerate(data["all_items"]):
    var = tk.IntVar()
    var.set(item["harga"])
    vars.append(var)
    check_button = tk.Checkbutton(menuFrame, text=item["item"], variable=var)
    check_button.grid(row=i, column=0, sticky='w')
    entry = tk.Entry(menuFrame)
    entry.grid(row=i, column=1, sticky='w')
    entries.append(entry)
    check_buttons.append(check_button)

# Create the function that calculates the value of each checked check button multiplied by the corresponding entry value
def calculate_total():
    total = 0
    for item, var, entry in zip(data["all_items"], vars, entries):
        if var.get() == 1:
            if len(entry.get()) > 0:
                total += item["harga"] * int(entry.get())
            else:
                total += item["harga"]
    label.config(text=f"Total: RP. {total}")
    print(total)
flag = False

dis_check_buttons = [check_buttons[1],check_buttons[2],check_buttons[4],entries[1],entries[2],entries[4]]
def toggle_check_buttons():
    if toggle_button["text"] == "Show only Promotion Items":
        toggle_button.config(text="Show All Items")
    else:
        toggle_button.config(text="Show only Promotion Items")
    global flag
    if flag:
        state = 'normal'
        
        flag = False
    else:
        state = 'disabled'
      
        flag = True
    for dis_check_button in dis_check_buttons:
        dis_check_button.config(state=state)

# Create the "Toggle" button
toggle_button = tk.Button(window, text='Show only Promotion Items', command=toggle_check_buttons)
toggle_button.pack(side=tk.TOP)

# Create the "Calculate" button
calculate_button = tk.Button(window, text="Calculate", command=calculate_total)
calculate_button.pack(side=tk.BOTTOM)





# Run the Tkinter event loop
window.mainloop()