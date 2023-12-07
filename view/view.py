import tkinter
from PIL import Image, ImageTk


class P9verbals:
    bg='#3d6466'

def load_frame1():
    print('bag of dicks')
    
    #importCSV('P5TestPlan.csv')
   
def load_frame2():
    test = Model('pop', 1995)
    sup = test.getAll()
    print(sup['date'])

def load_frame3():
    print('butts')

def place_holder():
    pass
    
def load_main(frame, image):   
    frame.pack_propagate(False)
    bace_image = Image.open(image)
    print('dd')
    #rezized_image = bace_image.resize((341,256))
    print('d')
    rezized_image = Image.open(image).resize((200,200))
    logo_img = ImageTk.PhotoImage(rezized_image)
    #logo_widget = tkinter.Label(frame, image = logo_img).image = logo_img
    logo_widget = tkinter.Label(frame, image = logo_img, width=200, height=200, bg=P9verbals.bg)
    logo_widget.image = logo_img
    logo_widget.pack()
    tkinter.Label(frame, text = 'sup', bg = P9verbals.bg, fg = 'white', font=('TkMenuFont', 14)).pack()
    tkinter.Button(frame, text = 'hello', font=('TkMenuFont', 14), bg = P9verbals.bg, fg = 'white', cursor = 'hand2', activeforeground = 'red', activebackground = 'blue', command =lambda: load_frame1()).pack(pady= 20)
    tkinter.Button(frame, text = 'bob', font=('TkMenuFont', 14), bg = P9verbals.bg, fg = 'white', cursor = 'hand2', activeforeground = 'red', activebackground = 'blue', command =lambda: load_frame2()).pack(pady= 20)
    tkinter.Button(frame, text = 'sam', font=('TkMenuFont', 14), bg = P9verbals.bg, fg = 'white', cursor = 'hand2', activeforeground = 'red', activebackground = 'blue', command =lambda: load_frame3()).pack(pady= 20)

def main():
    root = tkinter.Tk()
    root.title('Hello')
    #root.eval('tk::PlaceWindow . center')
    menu_bar = tkinter.Menu(root)
    file_menu = tkinter.Menu(menu_bar, tearoff=0)

    file_menu.add_separator()
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="testk", command=place_holder)
    file_menu.add_command(label="testl", command=place_holder)

    x = int(root.winfo_screenwidth() // 2)
    y = int(root.winfo_screenheight() * 0.1)
    print(x, y)

    root.geometry('500x600+' + str(x) + '+' + str(y))

    #tkinter.Frame(root, width=500, height=400, bg=P9verbals.bg).grid(row = 0, column = 0)
    frame_1 = tkinter.Frame(root, width=500, height=600, bg=P9verbals.bg)
    frame_2 = tkinter.Frame(root, bg=P9verbals.bg)
    frame_1.grid(row = 0, column = 0)
    for frame in (frame_1, frame_2):
        frame.grid(row = 0, column = 0)
    
    load_main(frame_1, '../assets/placeholder.png')

    root.mainloop()

if __name__ == "__main__":
    main()
