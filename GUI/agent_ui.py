import tkinter as tk

window = tk.Tk()
window.geometry("1000x500")
window.title("Agent/Owner")

top_frame = tk.Frame(width=2000)
heading = tk.Label(master = top_frame, text = "Agent/Owner").pack()
top_frame.pack(fill = tk.X )

main = tk.Frame(width=2000)

main.grid_columnconfigure(0, weight=1)
main.grid_columnconfigure(1, weight=1)

input_label = tk.Label(master = main, text = "Enter Property ID:")
input_label.grid(row=0, column = 0, padx=20)

property = tk.Entry(master=main).grid(row=0, column=1, padx=20)
rent = tk.Button(master=main, text="RENT").grid(row=1, column=0, pady=20)
sell = tk.Button(master=main, text="SELL").grid(row=1, column=1, pady=20)

main.pack(fill = tk.X)

output_prop = tk.Frame(width = 1000, bg="yellow")
prop_lbl = tk.Label(master=output_prop, text = "Properties", bg="yellow").pack()
output_prop.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

output_trans = tk.Frame(width = 1000, bg="green")
trans_lbl = tk.Label(master=output_trans, text = "Transactions", bg="green").pack()
output_trans.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

window.mainloop()