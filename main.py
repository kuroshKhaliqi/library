from tkinter import *
from tkinter import messagebox

library_data_list = [
    {
        "id": 1,
        "author": 'Craig Steele',
        "title": 'Step By Step Coding Course',
        "img_url": "book_img/placeholder.png",
        "catagory": "Programming",
        "price": 7
    }
    ,{
        "id": 2,
        "author": 'Cory Althoff',
        "title": 'Self Taught Programmer',
        "img_url": "./book_img/placeholder.png",
        "catagory": "Programming",
        "price": 5
    },{
        "id": 3,
        "author": 'Philip Robbins',
        "title": 'Python Programming',
        "img_url": "./book_img/placeholder.png",
        "catagory": "Programming",
        "price": 15
    },{
        "id": 4,
        "author": 'Eric Matthes',
        "title": 'Python Crash Course',
        "img_url": "./book_img/placeholder.png",
        "catagory": "Programming",
        "price": 12
    },{
        "id": 5,
        "author": 'Author 1Book 1',
        "title": 'Book 1',
        "img_url": "./book_img/placeholder.png",
        "catagory": "Horror",
        "price": 2
    },{
        "id": 6,
        "author": 'Author 2',
        "title": 'Book 2',
        "img_url": "./book_img/placeholder.png",
        "catagory": "Cartoons",
        "price": 7
    }
]

# Homework : 
# Add 6 more books
# Resize the books images  using GIMP and when you exprot them export them as .png

def filter_by_catagory(catagory, book_library_data):
    catagory_array = []
    for x in range(0, len(book_library_data)):
        current_book = book_library_data[x]
        if current_book['catagory'] == catagory:
            catagory_array.append(current_book)
    return catagory_array
# read all the book data one by one
#for each book check if current Book Catagiry equals the catagory you took as argument
#if the current book catagory we add the book to the array

def filter_by_price(min_price, max_price, library_data_list):
    price_array = []
    for x in range(0, len(library_data_list)):
            current_book_data = library_data_list[x]
            if current_book_data["price"] >= min_price and current_book_data["price"] <= max_price:
                price_array.append(current_book_data)
    return price_array

def filter_by_author(author,books_data):
    author_array =[]
    for x in range (0, len(books_data)):
        current_book = books_data[x]
        books_author_lowercase = current_book['author'].lower()
        author_lowercase = author.lower()
        if books_author_lowercase.__contains__(author_lowercase):
            author_array.append(current_book)
    return author_array

def search_book_by_name(book_name, library_data_list):
    #read the book list
    for x in range(0, len(library_data_list)):
        current_book = library_data_list[x]
        if current_book["title"] == book_name:
            return current_book
    return None
    #take the data of the books


def create_book_ui(book_data, books_panel, row, column):
    book_frame = Frame(books_panel)
    #configur book fair grid columns and rows
    img = PhotoImage(file=book_data["img_url"])
    img_label = Label(book_frame, image=img)
    img_label.image = img
    img_label.grid(row=0, column=0 )
    #add the label for the title and the author with the book frame as parent next
    title_label = Label(book_frame, text=book_data["title"])
    title_label.grid(row=1, column=0)
    author_label = Label(book_frame, text=book_data["author"])
    author_label.grid(row=2, column=0)
    price_label = Label(book_frame, text=f'${book_data["price"]}')
    price_label.grid(row=3, column=0)
    #  place the into the frame using grid
    book_frame.grid(row=row, column=column)

def display_books(books_data_list, books_panel):
    books_frames = books_panel.winfo_children()
    for x in range(len(books_frames)):
        current_frame = books_frames[x]
        current_frame.destroy()
    for x in range(0, len(books_data_list)):
        current_book = books_data_list[x]
        print(current_book)
        create_book_ui(current_book, books_panel, 0, x)


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

filtered_books = []
side_nav = Frame(main_frame)
side_nav.grid(row=0, column=0, sticky=NSEW)
# create the widget (buttons)
brand = Label(side_nav, text="Libib", font=('Arial', 30) )
brand.grid(row=0, column=0)
# homework
# develop the diplay filtred books function 
def display_filtered_books(author_name_entry):
    global books_conteinter
    author_name = author_name_entry.get()
    filtered_books = filter_by_author(author_name, library_data_list)
    if len(filtered_books) == 0:
        messagebox.showinfo(title="Search Completed", message="Book with that author was not found. Please recheck")
    else:
        display_books(filtered_books, books_conteinter)

def show_filtered_by_author():
    pop_up = Toplevel()
    label1 = Label(pop_up, text="Please give author name.")
    label1.pack()
    author_name_entry = Entry(pop_up)
    author_name_entry.pack()
    btn  = Button(pop_up, text="Submmit", command=lambda: display_filtered_books(author_name_entry))
    btn.pack()


# develop this function
def display_filtered_by_price(min_entry, max_entry):
    global books_conteinter
    # collect the data from the entries
    min_price = float(min_entry.get())
    max_price = float(max_entry.get())
    # use the filter_by_price function to filter the books
    filtered_books = filter_by_price(min_price, max_price, library_data_list)
    # display the filtered books
    display_books(filtered_books,books_conteinter )


def show_filtered_by_price():
    pop_up = Toplevel()
    min_label = Label(pop_up, text="Min Price")
    min_label.pack()
    min_entry = Entry(pop_up)
    min_entry.pack()
    max_label = Label(pop_up, text="Max Price")
    max_label.pack()
    max_entry = Entry(pop_up)
    max_entry.pack()
    submit_btn = Button(pop_up, text = "Enter", command=lambda: display_filtered_by_price(min_entry, max_entry))
    submit_btn.pack()
def show_all_books():
    global library_data_list, books_conteinter
    display_books(library_data_list, books_conteinter)
btn_list = ['Library', 'Filter By Author', 'Filter By Price', 'Publish', 'Lending', 'Managers', 'Barcodes', 'Dashboards', 'Reports']
current_row=1
for x in range(0, len(btn_list)):
    btn1 = None
    if btn_list[x] == "Filter By Author":
        btn1 = Button(side_nav, text=btn_list[x], font=('Arial', 20), command=show_filtered_by_author)
    elif btn_list[x] == "Library":
        btn1 = Button(side_nav, text=btn_list[x], font=('Arial', 20), command=show_all_books)
    elif btn_list[x] == "Filter By Price":
        btn1 = Button(side_nav, text=btn_list[x], font=('Arial', 20), command=show_filtered_by_price)
    else:
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
books_conteinter = Frame(main_panel, bg='blue')
# place the 2 blue containers using .grid 
blue_frame1.grid(row=0, column=0, sticky=NSEW, pady=10)
books_conteinter.grid(row=1, column=0, sticky=NSEW, pady=20)

# Searching______________________________________________

search_field = Entry(blue_frame1, text='Start Searching...', width=30, bg='yellow', font=('Arial', 35))
search_field.grid(row=0, column=1, pady=10)

def handle_search(event):
    global library_data_list
    book_title = search_field.get()
    search_result = search_book_by_name(book_title, library_data_list=library_data_list) 
    if search_result  !=  None:
        messagebox.showinfo("Book found", f'Book found: {search_result["title"]} by {search_result["author"]}')
    else:
        messagebox.showerror("Book not found", f"No books with the name {book_title}")
       # display a pop up with the nam and the author of the book and a sucsess message
       #else display  a error message

search_image = PhotoImage(file="search icon.png")
search_btn = Button(blue_frame1, image=search_image)
search_btn.grid(row=0, column=0)
search_btn.bind('<Button-1>', handle_search)


my_book_btn = Button(blue_frame1, text='My Books', font=('Arial', 35))
my_book_btn.grid(row=1, column=1, sticky=NSEW)

# Book panel
books_conteinter.columnconfigure(index=0,minsize=200)
books_conteinter.columnconfigure(index=1,minsize=200)
books_conteinter.columnconfigure(index=2,minsize=200)
books_conteinter.columnconfigure(index=3,minsize=200)
books_conteinter.columnconfigure(index=4,minsize=200)

display_books(library_data_list, books_conteinter)


#HW: style the search button width height and bg the search field and my book btn(hint: go online and search how to style buttons on tkinter)

mainloop()