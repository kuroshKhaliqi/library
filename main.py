from tkinter import *

books_label_list = [
    {
        "author": 'Craig Steele',
        "title": 'Step By Step Coding Course',
        "img_url": "book_img/Step_By_Step_Coding_Course.jpg"
    },{
        "author": 'Cory Althoff',
        "title": 'Self Taught Programmer',
        "img_url": "book_img/Self_Taught_Programmer.jpg"
    },{
        "author": 'Philip Robbins',
        "title": 'Python Programming',
        "img_url": "book_img/Python_Programming.jpg"
    },{
        "author": 'Eric Matthes',
        "title": 'Python Crash Course',
        "img_url": "book_img/Python_Crash_Course.jpg"
    }

]

def create_book_ui(book_data, books_panel){
    book_frame = Frame(books_panel)
    #configur book fair grid columns and rows
    img = PhotoImage(file=book_data.img_url)
    img_label = Label(book_frame, image=img)
    img_label.grid(row=0, column=0 )
    #add the label for the title and the author with the book frame as parent next
    #  place the into the frame using grid
}

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
#HW: create the main panel frame(the greeen container)with main frame as parent
main_panel = Frame(main_frame, bg='green')
# place this main panel into the main frame using .grid
main_panel.grid(row=0, column=1, sticky=NSEW)
#configue the rows and colums of main panel 
main_panel.rowconfigure(index=0, minsize=0.2 * WIN_HEIGHT)
main_panel.rowconfigure(index=1, minsize=0.8 * WIN_HEIGHT)
main_panel.columnconfigure(index=0, minsize=0.7 * WIN_WIDTH)
# Create the frames for the 2 blue container with main panel as parent
blue_frame1 = Frame(main_panel, bg='blue')
blue_frame2 = Frame(main_panel, bg='blue')
# place the 2 blue containers using .grid 
blue_frame1.grid(row=0, column=0, sticky=NSEW, pady=10)
blue_frame2.grid(row=1, column=0, sticky=NSEW, pady=20)

# Searching______________________________________________
search_image = PhotoImage(file="search icon.png")
search_btn = Button(blue_frame1, image=search_image)
search_btn.grid(row=0, column=0)
search_field = Entry(blue_frame1, text='Start Searching...', width=30, bg='yellow', font=('Arial', 35))
search_field.grid(row=0, column=1, pady=10)

my_book_btn = Button(blue_frame1, text='My Books', font=('Arial', 35))
my_book_btn.grid(row=1, column=1, sticky=NSEW)

# Book panel



#HW: style the search button width height and bg the search field and my book btn(hint: go online and search how to style buttons on tkinter)

mainloop()