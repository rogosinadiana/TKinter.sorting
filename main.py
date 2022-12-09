from tkinter import *
from tkinter import ttk
def sort():
    sorted_list = [33,14,31,61,3,1,149]
    sorted_list.sort()
    lbl_name_2['text'] = sorted_list[0]
    lbl_name_3['text'] = sorted_list[1]
    lbl_name_4['text'] = sorted_list[2]
    lbl_name_5['text'] = sorted_list[3]
    lbl_name_6['text'] = sorted_list[4]
    lbl_name_7['text'] = sorted_list[5]
    lbl_name_8['text'] = sorted_list[6]
root = Tk()
root.title('СОРТИРОВКА')
root.geometry('350x350')
lbl_name_1 = Label(text='33,14,31,61,3,1,149')
lbl_name_1.pack()
button_change_label_1 = Button(text='ОТСОРТИРОВАТЬ', command=sort)
button_change_label_1.pack()
lbl_name_2=Label(text='')
lbl_name_2.pack()
lbl_name_3=Label(text='')
lbl_name_3.pack()
lbl_name_4=Label(text='')
lbl_name_4.pack()
lbl_name_5=Label(text='')
lbl_name_5.pack()
lbl_name_6=Label(text='')
lbl_name_6.pack()
lbl_name_7=Label(text='')
lbl_name_7.pack()
lbl_name_8=Label(text='')
lbl_name_8.pack()
root.mainloop()




