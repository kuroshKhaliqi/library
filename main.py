from tkinter import *
WIN_WIDTH = 1700
WIN_HEIGHT = 900
window = Tk()
window.geometry('1700x900')
main_frame = Frame(window, bg="black")
main_frame.pack(fill=BOTH, expand=True)
# Configure the grid of the frame using main_frame.rowconfigure() 
main_frame.columnconfigure(index=0, minsize= 0.3 * WIN_WIDTH)
main_frame.columnconfigure(index=1, minsize=0.7 * WIN_WIDTH )
main_frame.rowconfigure(index=0, minsize=WIN_HEIGHT )


side_nav = Frame(main_frame)
side_nav.grid(row=0, column=0, sticky=NSEW)
# create the widget (buttons)
brand = Label(side_nav, text="Libib", font=('Arial', 30) )
brand.grid(row=0, column=0)
# btn1 = Button(side_nav, text="Home")
# btn2 = Button(side_nav, text="Settings")
# btn3 = Button(side_nav, text="About")
# place the buttons on the side_nave using .grid(..)
# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=0)
# btn3.grid(row=2, column=0)
btn_list = ['Library', 'Add Items', 'Add Collection', 'Publish', 'Lending', 'Managers', 'Barcodes', 'Dashboards', 'Reports']
current_row=1
for x in range(0, len(btn_list)):
    btn1 = Button(side_nav, text=btn_list[x], font=('Arial', 20))
    btn1.grid(row=current_row, column=0, sticky=EW, pady=20, padx=200)
    current_row +=1




mainloop()