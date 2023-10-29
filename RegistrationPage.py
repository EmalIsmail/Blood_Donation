from tkinter import *
from tkinter.ttk import Treeview
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import sqlite3
import matplotlib.pyplot as plt

def Eligibility():
    # FUNCTIONS ----------------------------------------------------------------------------------------------------------------------------------------

    def Blood_Percentage():

        y = [38.67,27.42,22.02,5.88,2.55,1.99,1.11,0.36]
        x = ['O+','A+','B+','AB+','O-','A-','B-','AB-']

        plt.bar(x,y, color=('#8F1D21','#FFB3A7','#F7CA18','#1F4788','#7A942E','#049372','#6C7A89','#8D608C'))
        plt.ylabel("Percentage(%)")
        plt.xlabel("Blood Group")
        plt.title("Blood Type Distribution in the World")

        plt.show()

    def Eligibility_Submit():

            global firstname
            global lastname
            global bloodgroup
            global gender
            global weight
            global age
            global Haemoglobin
            global Donation_interval
            global Question_one
            global Question_two
            global Question_three

            firstname = str(First_Name_Edit.get())
            lastname = str(Last_Name_Edit.get())
            bloodgroup = str(Blood_Group_Edit.get())
            gender = str(Gender_Edit.get())
            weight = int(Weight_Edit.get())
            age = int(Age_Edit.get())
            Haemoglobin = float(Haemoglobin_Edit.get())
            Donation_interval = int(Donation_Interval_Edit.get())
            Question_one = str(Q1_Edit.get())
            Question_two = str(Q2_Edit.get())
            Question_three = str(Q3_Edit.get())


            conn = sqlite3.connect('BloodDonation.db')
            curser = conn.cursor()


            curser.execute("SELECT Min_Weight FROM Verification")
            min_value_weight = curser.fetchone()


            curser.execute("SELECT Max_Weight FROM Verification")
            max_value_weight = curser.fetchone()

            curser.execute("SELECT Min_Age FROM Verification")
            min_value_Age = curser.fetchone()

            curser.execute("SELECT Max_Age FROM Verification")
            max_value_Age = curser.fetchone()

            curser.execute("SELECT Min_Haemoglobin FROM Verification")
            min_value_Haemoglobin = curser.fetchone()

            curser.execute("SELECT Max_Haemoglobin FROM Verification")
            max_value_Haemoglobin = curser.fetchone()

            curser.execute("SELECT Min_Donation_Interval FROM Verification")
            Min_value_Donation_Interval = curser.fetchone()

            curser.execute("SELECT Max_Donation_Interval FROM Verification")
            Max_value_Donation_Interval = curser.fetchone()

            curser.execute("SELECT Q1 FROM Verification")
            Q1_value = curser.fetchone()

            curser.execute("SELECT Q2 FROM Verification")
            Q2_value = curser.fetchone()

            curser.execute("SELECT Q3 FROM Verification")
            Q3_value = curser.fetchone()


    # End of Inputs to Doner's Table -----------------------------------------------------------------------------------------------------------------

            try:

                if int(min_value_weight[0]) <= weight and int(max_value_weight[0]) >= weight:

                    if int(min_value_Age[0]) <= age and int(max_value_Age[0]) >= age:

                        if float(min_value_Haemoglobin[0]) <= Haemoglobin and float(max_value_Haemoglobin[0]) >= Haemoglobin:

                            if int(Min_value_Donation_Interval[0]) <= Donation_interval and int(Max_value_Donation_Interval[0]) >= Donation_interval:

                                if str(Q1_value[0]) == Question_one:

                                    if str(Q2_value[0]) == Question_two:

                                        if str(Q3_value[0]) == Question_three:
                                            tkinter.messagebox.showinfo(title="Eligibility Result",
                                                                    message="Congratulations, You are Eligibile to Donate blood'")
                                            curser.execute('''CREATE TABLE IF NOT EXISTS `Donors`( `First_Name` TEXT, `Last_Name` TEXT, `Blood_Group` TEXT, `Age` INTEGER,`Weight`INTEGER,`Donation_Interval` INTEGER,
                                                                     `Haemoglobin` TEXT, `Gender` TEXT, `Question_1` TEXT, `Question_2` TEXT, `Question_3` TEXT);''')

                                            curser.execute('''insert into Donors (`First_Name` , `Last_Name`, `Blood_Group`, `Age` ,`Weight`,`Donation_Interval`,
                                                                     `Haemoglobin`, `Gender`, `Question_1`, `Question_2`, `Question_3`) values (?, ?, ?, ?, ?,?, ?,?, ?,?, ?)''',
                                                           (firstname, lastname, bloodgroup, age, weight,
                                                            Donation_interval, Haemoglobin, gender, Question_one,
                                                            Question_two, Question_three))

                                            conn.commit()
                                        else:
                                            tkinter.messagebox.showinfo(title="Eligibility Result",
                                                                        message="Invalid!, You are not Eligibile to Donate blood")
                                    else:
                                        tkinter.messagebox.showinfo(title="Eligibility Result",
                                                                    message="Invalid!, You are not Eligibile to Donate blood")
                                else:
                                    tkinter.messagebox.showinfo(title="Eligibility Result",
                                                                message="Invalid!, You are not Eligibile to Donate blood")
                            else:
                                tkinter.messagebox.showinfo(title="Eligibility Result",
                                                            message="Invalid!, You are not Eligibile to Donate blood")
                        else:
                            tkinter.messagebox.showinfo(title="Eligibility Result",
                                                        message="Invalid!, You are not Eligibile to Donate blood")
                    else:
                        tkinter.messagebox.showinfo(title="Eligibility Result",
                                                    message="Invalid!, You are not Eligibile to Donate blood")
                else:
                    tkinter.messagebox.showinfo(title="Eligibility Result",
                                                message="Invalid!, You are not Eligibile to Donate blood")

            except:
                tkinter.messagebox.showinfo(title="Eligibility Result",
                                            message="Invalid!, You are not Eligibile to Donate blood")

    def Eligibility_Report():

        global firstname
        global lastname
        global bloodgroup
        global gender
        global weight
        global age
        global Haemoglobin
        global Donation_interval
        global Question_one
        global Question_two
        global Question_three

        registerRoot.destroy()
        E_Report = Tk()
        E_Report.title("Eligibility Report")
        E_Report.geometry("480x640")

        bg_img = ImageTk.PhotoImage(Image.open('result.jpg'))
        bg_label = Label(E_Report, image=bg_img)
        bg_label.place(x=0, y=0)

        E_Firstname = Label(E_Report)
        E_Firstname.place(x=125, y=219)
        E_Firstname.config(text=firstname)

        E_Lastname = Label(E_Report)
        E_Lastname.place(x=125, y=245)
        E_Lastname.config(text=lastname)

        E_BloodGroup = Label(E_Report, text="Blood Group")
        E_BloodGroup.place(x=135, y=275)
        E_BloodGroup.config(text=bloodgroup)

        E_Gender = Label(E_Report, text="Gender")
        E_Gender.place(x=110, y=305)
        E_Gender.config(text=gender)

        E_Weight = Label(E_Report, text="Weight")
        E_Weight.place(x=110, y=340)
        E_Weight.config(text=weight)

        E_Haemoglobin = Label(E_Report, text="Haemoglobin")
        E_Haemoglobin.place(x=333, y=343)
        E_Haemoglobin.config(text=Haemoglobin)

        E_Donation_Interval = Label(E_Report, text="Donation Interval")
        E_Donation_Interval.place(x=345, y=215)
        E_Donation_Interval.config(text=Donation_interval)

        E_Age = Label(E_Report, text="Age")
        E_Age.place(x=270, y=268)
        E_Age.config(text=age)

        E_Question1 = Label(E_Report, text="Q1")
        E_Question1.place(x=95, y=395)
        E_Question1.config(text=Question_one)

        E_Question2 = Label(E_Report, text="Q2")
        E_Question2.place(x=95, y=470)
        E_Question2.config(text=Question_two)

        E_Question3 = Label(E_Report, text="Q3")
        E_Question3.place(x=95, y=540)
        E_Question3.config(text=Question_three)

        E_Report.mainloop()

    def Read_doners_list():

        Details = Button(registerRoot, text="More Details", bg="#264348", fg="white", relief=FLAT,
                         command=More_Details)
        Details.pack()
        Details.place(x=905, y=715, width=80, height=27)

        tree = ttk.Treeview(registerRoot, height=27, column=("column1", "column2", "column3"), show='headings')
        tree.place(x=898, y=140)
        tree.heading("#1", text="First Name")
        tree.column("column1", minwidth=0,width=115)
        tree.heading("#2", text="Last Name")
        tree.column("column2", minwidth=0, width=115)
        tree.heading("#3", text="Blood Group")
        tree.column("column3", minwidth=0, width=119)



        conn = sqlite3.connect('BloodDonation.db')
        curser = conn.cursor()
        curser.execute('SELECT * FROM Donors')
        rows= curser.fetchall()

        for row in rows:
            tree.insert("",tk.END, values=row)

    def More_Details():

        donorslist = Tk()
        donorslist.title("Donor's List")
        donorslist.geometry("790x600")

        tree = ttk.Treeview(donorslist, height=29, column=("column1", "column2", "column3","column4","column5","column6","column7","column8"
                                                           ,"column9","column10","column11"), show='headings')
        tree.place(x=0, y=0)
        tree.heading("#1", text="First Name")
        tree.column("column1", minwidth=0, width=70)
        tree.heading("#2", text="Last Name")
        tree.column("column2", minwidth=0, width=70)
        tree.heading("#3", text="Blood Group")
        tree.column("column3", minwidth=0, width=80)
        tree.heading("#4", text="Age")
        tree.column("column4", minwidth=0, width=60)
        tree.heading("#5", text="Weight")
        tree.column("column5", minwidth=0, width=80)
        tree.heading("#6", text="Donation Interval")
        tree.column("column6", minwidth=0, width=70)
        tree.heading("#7", text="Haemoglobin")
        tree.column("column7", minwidth=0, width=80)
        tree.heading("#8", text="Gender")
        tree.column("column8", minwidth=0, width=65)
        tree.heading("#9", text="Question 1")
        tree.column("column9", minwidth=0, width=70)
        tree.heading("#10", text="Question 2")
        tree.column("column10", minwidth=0, width=70)
        tree.heading("#11", text="Question 3")
        tree.column("column11", minwidth=0, width=70)

        conn = sqlite3.connect('BloodDonation.db')
        curser = conn.cursor()
        curser.execute('SELECT * FROM Donors')
        rows = curser.fetchall()

        for row in rows:
            tree.insert("", tk.END, values=row)

        donorslist.mainloop()

    # END OF FUNCTIONS --------------------------------------------------------------------------------------------------------------------------------------------------------

    registerRoot = Tk()
    registerRoot.title("Eligibility Requirements")
    registerRoot.attributes('-fullscreen', True)
    registerRoot.configure(background="#59ABE3")

    RegLblBg=Frame(registerRoot, width=1203, height=160, background='#264348').place(x=50,y=90)
    lblUName=Label(registerRoot, text="Eligibilty Requirment", font=('Georgia', 15), background="#264348", fg="#ffffff")
    lblUName.pack()
    lblUName.place(x=400, y=100)
    entryBG = Frame(registerRoot, width=490, height=615, background='#d9d9da').place(x=405,y=140)
    topScndFrame = Frame(registerRoot,width=1400, height=70,  background='#264348').pack(side=TOP)

    # PICTURES ---------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Setting it up
    img = ImageTk.PhotoImage(Image.open("Eligibility_Design.PNG"))
    img1 = ImageTk.PhotoImage(Image.open("Eligibility_Design_1.PNG"))

    #Displaying it
    imglabel = Label(registerRoot, image=img, relief=FLAT,background="#485563").place(x=50, y=140)
    imglabel1 = Label(registerRoot, image=img1, relief=FLAT,background="#485563").place(x=895, y=140)

    #LABELS & TEXT BOXES--------------------------------------------------------------------------------------------------------------------------------------------------------

    First_Name_Label=Label(registerRoot, text="First name", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    First_Name_Label.place(x =444, y=150)
    First_Name_Edit=Entry(registerRoot, relief=FLAT, font=('Georgia',9), fg="#1b2937",textvariable=None, background="#ffffff",width=50, bd=8,justify=LEFT) #Firstname Label and Edit Text
    First_Name_Edit.place(x = 444, y=170)

    Last_Name_Label=Label(registerRoot, text="Last name", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Last_Name_Label.place(x =444, y=210)
    Last_Name_Edit=Entry(registerRoot, relief=FLAT, font=('Georgia',9), fg="#1b2937",textvariable=None, background="#ffffff",width=50, bd=8, justify=LEFT) #Lastname Label and Edit Text
    Last_Name_Edit.place(x = 444, y=230)

    Blood_Group_Label=Label(registerRoot, text="Blood Group", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Blood_Group_Label.place(x =444, y=270)
    Blood_Group_Edit=Entry(registerRoot, relief=FLAT, font=('Georgia',9), fg="#1b2937",textvariable=None,background="#ffffff",width=50, bd=8, justify=LEFT) #Blood Group Label and Edit text
    Blood_Group_Edit.place(x = 444, y=290)

    Weight_Label=Label(registerRoot, text="Weight (Kgs)", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Weight_Label.place(x =444, y=330)
    Weight_Edit=Entry(registerRoot, relief=FLAT, font=('Georgia',9), fg="#1b2937",background="#ffffff",width=50, bd=8, justify=LEFT)    #Weight Label and Edit Text
    Weight_Edit.place(x = 444, y=350)

    Haemoglobin_Label=Label(registerRoot, text="Haemoglobin (L/g)", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Haemoglobin_Label.place(x =444, y=390)
    Haemoglobin_Edit=Entry(registerRoot, relief=FLAT, font=('Georgia',9), fg="#1b2937",textvariable=None,background="#ffffff",width=50, bd=8, justify=LEFT)  #Haemogolobin Label and Edit Text
    Haemoglobin_Edit.place(x = 444, y=410)

    Donation_Interval_Label=Label(registerRoot, text="Donation Interval (Weeks)", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Donation_Interval_Label.place(x =444, y=450)
    Donation_Interval_Edit=Entry(registerRoot, relief=FLAT, font=('Georgia',9), fg="#1b2937",textvariable=None,background="#ffffff",width=50, bd=8, justify=LEFT)  # Donation Interval Label and Edit Text
    Donation_Interval_Edit.place(x = 444, y=470)

    Gender_Label=Label(registerRoot, text="Gender (Male/Female)", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Gender_Label.place(x =444, y=510)
    Gender_Edit=Entry(registerRoot, relief=FLAT, font=('Georgia',9), fg="#1b2937",textvariable=None,background="#ffffff",width=50, bd=8, justify=LEFT)  #Gender Label and Edit Text
    Gender_Edit.place(x = 444, y=530)

    Age_Label=Label(registerRoot, text="Age (17-60)", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Age_Label.place(x =444, y=570)
    Age_Edit=Entry(registerRoot, relief=FLAT, font=('Georgia',9), fg="#1b2937",textvariable=None,background="#ffffff",width=50, bd=8, justify=LEFT)  #Gender Label and Edit Text
    Age_Edit.place(x = 444, y=590)

    Q1_Label=Label(registerRoot, text="How is your general health? (Good/Bad)", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Q1_Label.place(x =444, y=630)
    Q1_Edit=Entry(registerRoot, relief=FLAT, font=('Georgia',7), fg="#1b2937",textvariable=None,background="#ffffff",width=19, bd=8, justify=LEFT)  #Question - 1 Label and Edit Text
    Q1_Edit.place(x = 730, y=630)

    Q2_Label=Label(registerRoot, text="Have you had a fever in last three weeks? (Yes/No)", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Q2_Label.place(x =444, y=670)
    Q2_Edit=Entry(registerRoot, relief=FLAT, font=('Georgia',7), fg="#1b2937",textvariable=None,background="#ffffff",width=19, bd=8, justify=LEFT)  #Question - 2 Label and Edit Text
    Q2_Edit.place(x = 730, y=670)

    Q3_Label=Label(registerRoot, text="have you had an symptoms of infection? (Yes/No)", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Q3_Label.place(x =444, y=710)
    Q3_Edit=Entry(registerRoot, relief=FLAT, font=('Georgia',7), fg="#1b2937",textvariable=None,background="#ffffff",width=19, bd=8, justify=LEFT)  #Question - 3 Label and Edit Text
    Q3_Edit.place(x = 730, y=710)


    #BUTTONS------------------------------------------------------------------------------------------------------------------------------------------------------
    RegloginBtn=Button(registerRoot, text="Submit", bg="#5B3256", fg="white", relief = FLAT, command=Eligibility_Submit)
    RegloginBtn.pack()
    RegloginBtn.place(x = 710, y=100, width=80, height=27)

    RegExitBtn=Button(registerRoot, text="Exit", bg="#C93756", fg="white", relief = FLAT, command=registerRoot.destroy)
    RegExitBtn.pack()
    RegExitBtn.place(x = 1000, y=100, width=80, height=27)

    Show_Report=Button(registerRoot, text="Report", bg="#5B3256", fg="white", relief = FLAT, command=Eligibility_Report)
    Show_Report.pack()
    Show_Report.place(x = 615, y=100, width=80, height=27)

    Blood_Distribution =Button(registerRoot, text="Blood Distrbution", bg="#5B3256", fg="white", relief = FLAT, command=Blood_Percentage)
    Blood_Distribution.pack()
    Blood_Distribution.place(x = 800, y=100, width=100, height=27)

    Doners_List=Button(registerRoot, text="Donors List", bg="#5B3256", fg="white", relief = FLAT, command=Read_doners_list)
    Doners_List.pack()
    Doners_List.place(x = 910, y=100, width=80, height=27)

    #Page Tittle-----------------------------------------------------------------------------------------------------------------------------------------------------


    mainloop()

def sign_up():


    SignUp = Tk()
    SignUp.title("Login")
    SignUp.attributes('-fullscreen', True)
    SignUp.configure(background="#59ABE3")

    def Sign_Up_Function():
        Sign_firstname = str(Sign_First_Name_Edit.get())
        Sign_lastname = str(Sign_Last_Name_Edit.get())
        Sign_Email = str(Email_Edit.get())
        Sign_Password = str(Password_Edit.get())
        Sign_Confirm_Password = str(Confirm_Password_Edit)

        # DATABASE ------------------------------------------------------------------------------------------------------------------------------------------

        conn = sqlite3.connect('BloodDonation.db')
        curser = conn.cursor()

        curser.execute('''CREATE TABLE IF NOT EXISTS `Sign_Up` (`First_Name`
                    TEXT NOT NULL,`Last_Name`	TEXT NOT NULL,`Email`	TEXT NOT NULL,`Password` TEXT NOT NULL,`Confim_Password` TEXT NOT NULL);''')

        curser.execute(
            '''insert into `Sign_Up` (`First_Name`,`Last_Name`,`Email`,`Password`,`Confim_Password`) values (?, ?, ?, ?, ?)''',
            (Sign_firstname, Sign_lastname, Sign_Email, Sign_Password, Sign_Confirm_Password))

        conn.commit()

        tkinter.messagebox.showinfo(title="Eligibility Result",
                                    message="You have signed up successfully!")



    # VARIBALE DECLARE ----------------------------------------------------------------------------------------------------------------------------------------------

    RegLblBg = Frame(SignUp, width=490, height=160, background='#264348').place(x=405, y=90)
    lblUName = Label(SignUp, text="Please fill this form to create an account!", font=('Georgia', 8),
                     background="#264348", fg="#ffffff")
    lblUName.pack()
    lblUName.place(x=410, y=100)
    signup_entryBG = Frame(SignUp, width=490, height=615, background='#d9d9da').place(x=405, y=140)
    signup_topScndFrame = Frame(SignUp, width=1400, height=70, background='#264348').pack(side=TOP)


    # TEXT BOXES AND LABELS --------------------------------------------------------------------------------------------------------------------------------------------------------

    Sign_First_Name_Label = Label(SignUp, text="First name", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Sign_First_Name_Label.place(x=444, y=150)
    Sign_First_Name_Edit = Entry(SignUp, relief=FLAT, font=('Georgia', 9), fg="#1b2937", textvariable=None,
                                 background="#ffffff", width=50, bd=8,
                                 justify=LEFT)  # Firstname Label and Edit Text
    Sign_First_Name_Edit.place(x=444, y=170)

    Sign_Last_Name_Label = Label(SignUp, text="Last name", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Sign_Last_Name_Label.place(x=444, y=210)
    Sign_Last_Name_Edit = Entry(SignUp, relief=FLAT, font=('Georgia', 9), fg="#1b2937", textvariable=None,
                                background="#ffffff", width=50, bd=8, justify=LEFT)  # Lastname Label and Edit Text
    Sign_Last_Name_Edit.place(x=444, y=230)

    Email_Label = Label(SignUp, text="Email (Username)", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Email_Label.place(x=444, y=270)
    Email_Edit = Entry(SignUp, relief=FLAT, font=('Georgia', 9), fg="#1b2937", textvariable=None,
                       background="#ffffff",
                       width=50, bd=8, justify=LEFT)  # Email Label and Edit text
    Email_Edit.place(x=444, y=290)

    Password_Label = Label(SignUp, text="Password", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
    Password_Label.place(x=444, y=330)
    Password_Edit = Entry(SignUp, show="*", relief=FLAT, font=('Georgia', 9), fg="#1b2937", background="#ffffff", width=50,
                          bd=8,
                          justify=LEFT)  # Password Label and Edit Text
    Password_Edit.place(x=444, y=350)

    Confirm_Password_Label = Label(SignUp, text="Confirm Password", font=('Ariel', 9), background="#d9d9da",
                                   fg="BLACK")
    Confirm_Password_Label.place(x=444, y=390)
    Confirm_Password_Edit = Entry(SignUp,show="*", relief=FLAT, font=('Georgia', 9), fg="#1b2937", textvariable=None,
                                  background="#ffffff", width=50, bd=8,
                                  justify=LEFT)  # Haemogolobin Label and Edit Text
    Confirm_Password_Edit.place(x=444, y=410)

    # BUTTONS------------------------------------------------------------------------------------------------------------------------------------------------------
    Sign_Up_bt = Button(SignUp, text="Sign up", bg="#5B3256", fg="white", relief=FLAT, command=Sign_Up_Function)
    Sign_Up_bt.pack()
    Sign_Up_bt.place(x=444, y=450, width=80, height=27)

    RegExitBtn = Button(SignUp, text="Exit", bg="#C93756", fg="white", relief=FLAT, command=SignUp.destroy)
    RegExitBtn.pack()
    RegExitBtn.place(x=810, y=100, width=80, height=27)

    Log_in_bt = Button(SignUp, text="Login", bg="#C93756", fg="white", relief=FLAT, command=None)
    Log_in_bt.pack()
    Log_in_bt.place(x=715, y=100, width=80, height=27)

    # Page Tittle-----------------------------------------------------------------------------------------------------------------------------------------------------
    mainloop()

    # END OF FUNCTION SIGN UP PAGE----------------------------------------------------------------------------

def login_Check():

    Login_User = str(Username_Edit.get())
    Login_Pass = str(Login_Password_Edit.get())

    conn = sqlite3.connect("BloodDonation.db")

    result = conn.execute('SELECT * FROM SIGN_UP WHERE EMAIL = ? AND PASSWORD = ?', (Login_User,Login_Pass))
    if (result.fetchall()):

        tkinter.messagebox.showinfo(title="Login correct", message="Valid user")
        Login.destroy()
        Eligibility()

    else:
        tkinter.messagebox.showinfo(title="Login incorrect", message="Invalid user")
        print("Failed!")

Login = Tk()
Login.title("Login")
Login.attributes('-fullscreen', True)
Login.configure(background="#59ABE3")

RegLblBg = Frame(Login, width=1203, height=160, background='#264348').place(x=50, y=90)
lblUName = Label(Login, text="Please enter your Username and Password to Login!", font=('Georgia', 8),
                     background="#264348", fg="#ffffff")
lblUName.pack()
lblUName.place(x=410, y=100)
entryBG = Frame(Login, width=490, height=615, background='#d9d9da').place(x=405, y=140)
topScndFrame = Frame(Login, width=1400, height=70, background='#264348').pack(side=TOP)

# PICTURES ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Setting it up
img = ImageTk.PhotoImage(Image.open("Log_In_Design.jpg"))
img1 = ImageTk.PhotoImage(Image.open("Sign_Up_Design.PNG"))
img2 = ImageTk.PhotoImage(Image.open("login_icon.jpg"))

# Displaying Labels
imglabel = Label(Login, image=img, relief=FLAT, background="#485563").place(x=50, y=140)
imglabel1 = Label(Login, image=img1, relief=FLAT, background="#485563").place(x=895, y=140)
imglabel2 = Label(Login, image=img2, relief=FLAT, background="#d9d9da").place(x=570, y=180)

# TEXT BOXES AND LABELS --------------------------------------------------------------------------------------------------------------------------------------------------------

Username_Label = Label(Login, text="Username", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
Username_Label.place(x=444, y=330)
Username_Edit = Entry(Login, relief=FLAT, font=('Georgia', 9), fg="#1b2937", background="#ffffff", width=50, bd=8,
                          justify=LEFT)  # Username Label and Edit Text
Username_Edit.place(x=444, y=350)

Login_Password_Label = Label(Login, text="Password", font=('Ariel', 9), background="#d9d9da", fg="BLACK")
Login_Password_Label.place(x=444, y=390)
Login_Password_Edit = Entry(Login,show="*", relief=FLAT, font=('Georgia', 9), fg="#1b2937", textvariable=None,
                                background="#ffffff", width=50, bd=8, justify=LEFT)  # Password Label and Edit Text
Login_Password_Edit.place(x=444, y=410)

# BUTTONS------------------------------------------------------------------------------------------------------------------------------------------------------
Log_in_bt = Button(Login, text="Login", bg="#5B3256", fg="white", relief=FLAT, command=login_Check)
Log_in_bt.pack()
Log_in_bt.place(x=444, y=450, width=80, height=27)

Log_signup_bt = Button(Login, text="Sign Up", bg="#C93756", fg="white", relief=FLAT, command=sign_up)
Log_signup_bt.pack()
Log_signup_bt.place(x=1050, y=680, width=80, height=27)

RegExitBtn = Button(Login, text="Exit", bg="#C93756", fg="white", relief=FLAT, command=Login.destroy)
RegExitBtn.pack()
RegExitBtn.place(x=815, y=100, width=80, height=27)

# Page Tittle-----------------------------------------------------------------------------------------------------------------------------------------------------
mainloop()

