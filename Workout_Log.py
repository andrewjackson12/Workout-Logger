#First solo project attempted
#Software to log exercises completed in a workout
#Software to create exercise objects and log them in a txt file to be saved
from tkinter import*
import os
from tkinter import messagebox

#---------Main------------
class Workout_Log:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1275x625+0+0")
        self.root.title("Exercise Logging Software")
        bg_colour = "purple3"
        title = Label(self.root, text="Exercise Logging Software", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg=bg_colour, fg="Black", relief=GROOVE)
        title.pack(fill = X)

        #NEED TO CREATE EXERCISE OBJECT AFTER SKELETON DESIGN

        #---------Variables---------
        self.exercise_type = StringVar()
        self.exercise_notes = StringVar()
        self.sets_count = IntVar()

        #---------Exercise Creation Frame-----------
        ec_frame = LabelFrame(self.root, text = "Create Exercise Log", font = ("times new roman", 20, 'bold'), bd = 10, fg = 'Black', bg = bg_colour)
        ec_frame.place(x = 0, y = 70, relwidth=0.6, relheight= 0.6)
        #EXERCISE TYPE
        ename_label = Label(ec_frame, text ="Exercise Name", bg = bg_colour, fg = "Black", font = ('times new roman', 15, 'bold'))
        ename_label.grid(row = 0, column=0, padx = 20, pady = 5)
        ename_txt = Entry(ec_frame, width = 20, textvariable = self.exercise_type, font = 'arial 15', bd = 7, relief=GROOVE)
        ename_txt.grid(row = 0, column = 1, padx = 10, pady = 20)
        #SETS
        
        sets_label = Label(ec_frame, text ="No. of Sets", bg = bg_colour, fg = "Black", font = ('times new roman', 15, 'bold'))
        sets_label.grid(row = 1, column=0, padx = 20, pady = 5)
        sets_int = Entry(ec_frame, width = 20, textvariable = self.sets_count, font = 'arial 15', bd = 7, relief=GROOVE)
        sets_int.grid(row = 1, column = 1, padx = 10, pady = 20)
        #NOTES
        notes_label = Label(ec_frame, text ="Notes", bg = bg_colour, fg = "Black", font = ('times new roman', 15, 'bold'))
        notes_label.grid(row = 2, column=0, padx = 20, pady = 5)
        notes_txt = Entry(ec_frame, width = 20, textvariable = self.exercise_notes, font = 'arial 15', bd = 7, relief=GROOVE)
        notes_txt.grid(row = 2, column = 1, padx = 10, pady = 20)
        
        #CREATE EXERCISE BUTTON
        #NEED TO ADD FUNCTION IN BRACKETS ONCE COMPLETED
        create_ex_button = Button(ec_frame, text = 'Create Exercise', bg="White", fg = "Black", font = ('times new roman', 15, 'bold'))
        create_ex_button.grid(row = 3, column= 1, padx= 20, pady= 20)
        #Frame for saving or clearing log
        save_clear_frame = LabelFrame(self.root, text = "Save/Clear Log", font = ('times new roman', 20, 'bold'),bd = 10, fg = 'Black', bg = bg_colour)
        save_clear_frame.place(x = 0, y = 430, relwidth=0.6, relheight= 0.35)
        #Saving and clearing buttons
        save_button = Button(save_clear_frame, text = 'Save Log', font = ('times new roman', 20, 'bold'), bg = "White", fg="Black", height=2,width=15)
        save_button.grid(row=0,column=0,padx=25,pady=50)

        clear_button = Button(save_clear_frame, text = 'Clear Log', font = ('times new roman', 20, 'bold'), bg = "White", fg="Black", height=2,width=15)
        clear_button.grid(row=0,column=1,padx=25,pady=50)

        #LOG PREVIEW WINDOW
        log_prev = Frame(self.root, bd = 10, relief=GROOVE)
        log_prev.place(x=770,y=80,width=500,height=540)
        log_label = Label(log_prev, text = 'Workout Log', font=('times new roman', 20, 'bold'),bd=7,relief=GROOVE)
        log_label.pack(fill=X)
        scroll_y = Scrollbar(log_prev, orient=VERTICAL)
        self.txtprev =  Text(log_prev, yscrollcommand=scroll_y.set)
        scroll_y.pack(fill=Y, side=RIGHT)
        self.txtprev.pack(fill=BOTH, expand=True)
        

        return
        
root = Tk()
obj = Workout_Log(root)
root.mainloop()