from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x600")
root.title("Heart Diagnose report")
root.configure(background="orange red")


question1_readiobutton = StringVar(value="0")

question_1 = Label(root,text="Do you experience shortness of breath during routine activities?",bg="orange red")
question_1.pack()
question_1_r_1 = Radiobutton(root,text="Yes",variable=question1_readiobutton,value="yes",bg="orange red")
question_1_r_1.pack()
question_1_r_2 = Radiobutton(root,text="No",variable=question1_readiobutton,value="no",bg="orange red")
question_1_r_2.pack()

question2_radiobutton = StringVar(value="0")

question_2 = Label(root,text="Do you experience shortness of breath while at rest/lying down?",bg="orange red")
question_2.pack()
question_2_r_1 = Radiobutton(root,text="Yes",variable=question2_radiobutton,value="yes",bg="orange red")
question_2_r_1.pack()
question_2_r_2 = Radiobutton(root,text="No",variable=question2_radiobutton,value="no",bg="orange red")
question_2_r_2.pack()

question3_readiobutton = StringVar(value="0")

question_3 = Label(root,text="Do you feel short of breath while lying flat and feel the need to stack multiple pillows to sleep well?",bg="orange red")
question_3.pack()
question_3_r_1 = Radiobutton(root,text='Yes',variable=question3_readiobutton,value="yes",bg="orange red")
question_3_r_1.pack()
question_3_r_2 = Radiobutton(root,text="No",variable=question3_readiobutton,value="no",bg="orange red")
question_3_r_2.pack()

question4_readiobutton = StringVar(value="0")

question_4 = Label(root,text="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?",bg="orange red")
question_4.pack()
question_4_r_1 = Radiobutton(root,text='Yes',variable=question4_readiobutton,value="yes",bg="orange red")
question_4_r_1.pack()
question_4_r_2 = Radiobutton(root,text="No",variable=question4_readiobutton,value="no",bg="orange red")
question_4_r_2.pack()

question5_readiobutton = StringVar(value="0")

question_5 = Label(root,text="Do you have swelling in the feet/ ankles/legs (shoes feel tighter) or abdomen?",bg="orange red")
question_5.pack()
question_5_r_1 = Radiobutton(root,text='Yes',variable=question5_readiobutton,value="yes",bg="orange red")
question_5_r_1.pack()
question_5_r_2 = Radiobutton(root,text="No",variable=question5_readiobutton,value="no",bg="orange red")
question_5_r_2.pack()

def fever_score():
    score = 0
    if question1_readiobutton.get() == "yes":
        score = score+10
        print(score)
    if question2_radiobutton.get() =="yes":
        score = score+10
        print(score)
    if question3_readiobutton.get() =="yes":
        score = score+10
        print(score)
    if question4_readiobutton.get() =="yes":
        score = score+10
        print(score)
    if question5_readiobutton.get() =="yes":
        score = score+10
        print(score)
    
    if(score == 0):
        messagebox.showinfo("Error","Please fill the form")
    elif(score <= 10):
        messagebox.showinfo("Report","You do not need to visit a doctor")
    elif(score >= 10 and score <= 30):
        messagebox.showinfo("Report","You may need to visit a doctor")
    else:
        messagebox.showinfo("Report","I strongly reccomend you to visit the doctor")


button1 = Button(root,text="click me",command=fever_score)
button1.pack()
root.mainloop()