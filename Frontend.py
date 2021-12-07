from os import add_dll_directory
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from PIL import ImageTk
import psycopg2
from tkinter_custom_button import TkinterCustomButton
import tkinter.messagebox


root=tk.Tk()
root.configure(background='#ffff99')
employee_id = ""
password_employee = ""
manager_id = ""
password_manager = ""
iid=""
eid=""
did=""
dept_no=""
root.geometry("900x650")
canvas=tk.Canvas(root,width=900,height=650)
canvas.grid(columnspan=5,rowspan=5)

tk.Label(root, text='Some File').grid(row=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)
#canvas.configure(background='#ffff99')
root.title('Pharmaceutical Compnay Database')

title_bar = Frame(root, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)

def on_resize(event):
    # resize the background image to the size of label
    image = bg.resize((event.width, event.height), Image.ANTIALIAS)
    # update the image of the label
    l.image = ImageTk.PhotoImage(image)
    l.config(image=l.image)

bg=Image.open("bg3.png")
l = tk.Label(root)
l.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
l.bind('<Configure>', on_resize) # on_resize will be executed whenever label l is resized
#root.wm_attributes("-transparentcolor", 'white')
def PageOne():
    
    def EmployeeLogin():
        button1.destroy()
        button2.destroy()
        
        #logo_label.destroy()
        label1=Label(root,text="Employee Login Portal",font=('Times_New_Roman',35))
        label1.grid(column=1,row=0)
        label1.configure(background='white')
        def open_popup(msg):
            top= Toplevel(root)
            top.geometry("750x250")
            top.title("OOPS")
            Label(top, text= msg, font=('Times_New_Roman',15)).place(x=150,y=80)
        def EmployeedetailsPage(*args):
            print("username : " + username.get())
            print("password : " + password.get())
            employee_id = username.get()
            password_employee = password.get()
            connection=psycopg2.connect(user="postgres",
                            password="// write password here",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
            cur=connection.cursor()
            cur.execute("SELECT Password from LOGININFO where " + "Employee_ID = " + "'{}'".format(employee_id))
            output=cur.fetchall()
            
            incorrect_password = False
            if output == []:
                open_popup("User name doesn't exist, please check again!")
            else:
                if(password_employee != str(output[0][0])):
                    open_popup("Password entered for " + employee_id + " is incorrect, please enter again!")
                    if(incorrect_password == False):
                        incorrect_password = True

                      
              
            usernameLabel.destroy()
            usernameEntry.destroy()
            IIDentry.destroy()
            passwordLabel.destroy()
            label1.destroy()
            Backbutton1.destroy()
            Loginbutton.destroy()
            
            cur.execute("SELECT Fname, Lname, EID, Job_Position, Salary, Age, Start_Date, Dept_No from EMPLOYEE where " + "EID = " + "'{}'".format(employee_id))
            output=cur.fetchall()
            if output == [] or incorrect_password:
                output = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
            else:
                output = output[0]

                
            label2=Label(root,text="Profile",font=('Times_New_Roman',35))
            label2.grid(column=1,row=0)
            label2.configure(background='white')

            lbl1=Label(root, text="First Name", fg='red', font=("Helvetica", 16))
            lbl1.place(x=80, y=250)
            lfld1=Label(root, text= output[0], fg='black', font=("Helvetica", 16))
            lfld1.configure(background='white')
            lfld1.place(x=250, y=250)

            lbl2=Label(root, text="Last Name", fg='red', font=("Helvetica", 16))
            lbl2.place(x=80, y=350)
            lfld2=Label(root, text=output[1], fg='black', font=("Helvetica", 16))
            lfld2.configure(background='white')
            lfld2.place(x=250, y=350)

            lbl3=Label(root, text="Employee ID", fg='red', font=("Helvetica", 16))
            lbl3.place(x=80, y=450)
            lfld3=Label(root, text=output[2], fg='black', font=("Helvetica", 16))
            lfld3.configure(background='white')
            lfld3.place(x=250, y=450)

            lbl4=Label(root, text="Job Position", fg='red', font=("Helvetica", 16))
            lbl4.place(x=80, y=550)
            lfld4=Label(root, text=output[3], fg='black', font=("Helvetica", 16))
            lfld4.configure(background='white')
            lfld4.place(x=250, y=550)

            lbl5=Label(root, text="Salary", fg='red', font=("Helvetica", 16))
            lbl5.place(x=450, y=250)
            lfld5=Label(root, text=output[4], fg='black', font=("Helvetica", 16))
            lfld5.configure(background='white')
            lfld5.place(x=650, y=250)

            lbl6=Label(root, text="Age", fg='red', font=("Helvetica", 16))
            lbl6.place(x=450, y=350)
            lfld6=Label(root, text=output[5], fg='black', font=("Helvetica", 16))
            lfld6.configure(background='white')
            lfld6.place(x=650, y=350)

            lbl7=Label(root, text="Start Date", fg='red', font=("Helvetica", 16))
            lbl7.place(x=450, y=450)
            lfld7=Label(root, text=output[6], fg='black', font=("Helvetica", 16))
            lfld7.configure(background='white')
            lfld7.place(x=650, y=450)

            lbl8=Label(root, text="Department Number", fg='red', font=("Helvetica", 16))
            lbl8.place(x=450, y=550)
            lfld8=Label(root, text=output[7], fg='black', font=("Helvetica", 16))
            lfld8.configure(background='white')
            lfld8.place(x=650, y=550)

            connection.commit()
            connection.close()

            



            def Logout():
                usernameLabel.destroy()
                passwordLabel.destroy()
                usernameEntry.destroy()
                IIDentry.destroy()
                label1.destroy()
                Loginbutton.destroy()
                Backbutton1.destroy()
                label2.destroy()
                Loginbutton.destroy()
                Logoutbutton.destroy()
                lbl8.destroy()
                lbl1.destroy()
                lbl2.destroy()
                lbl3.destroy()
                lbl4.destroy()
                lbl5.destroy()
                lbl6.destroy()
                lbl7.destroy()
                lfld8.destroy()
                lfld1.destroy()
                lfld2.destroy()
                lfld3.destroy()
                lfld4.destroy()
                lfld5.destroy()
                lfld6.destroy()
                lfld7.destroy()
                
                PageOne()

            Logoutbutton=Button(root,text="Logout ",font=('Times_New_Roman',15),command=Logout)
            Logoutbutton.grid(column=0,row=0)    
            Logoutbutton.configure(background='white')    

            

        def backButton1():
            usernameLabel.destroy()
            passwordLabel.destroy()
            usernameEntry.destroy()
            IIDentry.destroy()
            label1.destroy()
            Loginbutton.destroy()
            Backbutton1.destroy()
            
            PageOne()
        Backbutton1=Button(root,text="Back ",font=('Times_New_Roman',15),command=backButton1)
        Backbutton1.grid(column=0,row=0)    
        Backbutton1.configure(background='white')

        usernameLabel = Label(root, text="Employee ID",font=('Times_New_Roman',15))
        usernameLabel.grid(row=1, column=0)
        usernameLabel.configure(background='white')
        username = StringVar()
        usernameEntry = Entry(root, textvariable=username)
        usernameEntry.grid(row=1, column=1,padx=5,pady=5,ipady=10)  
        usernameEntry.configure(background='white')

     #password label and password entry box
        passwordLabel = Label(root,text="Password",font=('Times_New_Roman',15))
        passwordLabel.grid(row=2, column=0) 
        passwordLabel.configure(background='white') 
        password = StringVar()
        IIDentry = Entry(root, textvariable=password, show='*')
        IIDentry.grid(row=2, column=1,padx=5,pady=5,ipady=10)
        IIDentry.configure(background='white') 
        Loginbutton=Button(root,text="Login ",font=('Times_New_Roman',25),command=EmployeedetailsPage)
        Loginbutton.grid(column=2,row=2)
        Loginbutton.configure(background='white')

    def ManagerLogin():
        button1.destroy()
        button2.destroy()
        
        #logo_label.destroy()
        label1=Label(root,text="Manager Login Portal",font=('Times_New_Roman',35))
        label1.grid(column=1,row=0)
        label1.configure(background='white')

        def backButton1():
            usernameLabel.destroy()
            passwordLabel.destroy()
            usernameEntry.destroy()
            IIDentry.destroy()
            label1.destroy()
            Loginbutton.destroy()
            Backbutton1.destroy()
            
            PageOne()


        def ManagerPage2():
            def open_popup(msg):
                top= Toplevel(root)
                top.geometry("750x250")
                top.title("Child Window")
                Label(top, text= msg, font=('Times_New_Roman',15)).place(x=150,y=80)
            print("username : " + username.get())
            print("password : " + password.get())
            employee_id = username.get()
            password_employee = password.get()
            connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
            cur=connection.cursor()
            
            cur.execute("SELECT Password from LOGININFO where " + "Employee_ID = " + "'{}'".format(employee_id))
            output=cur.fetchall()
            connection.commit()
            connection.close()
            incorrect_password = False
            if output == []:
                open_popup("User name doesn't exist, please check again!")
            else:
                temp = employee_id[::-1]
                if(not(temp[2] == "M" and len(employee_id) >= 4 or employee_id == "AA01")):
                     open_popup(employee_id + " is not a manager or admin!")
                elif(password_employee != str(output[0][0])):
                    open_popup("Password entered for " + employee_id + " is incorrect, please enter again!")
                    if(incorrect_password == False):
                        incorrect_password = True
                    
 
            usernameLabel.destroy()
            passwordLabel.destroy()
            usernameEntry.destroy()
            IIDentry.destroy()
            label1.destroy()
            Loginbutton.destroy()
            Backbutton1.destroy()
            
            def AddDrug():
                Accounting.destroy()
                button3.destroy()
                button1.destroy()
                Rawbutton1.destroy()
                EmpDetails.destroy()
                ViewDetails.destroy()
                Logoutbutton.destroy()

                def Insertdata():
                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    cur.execute("INSERT INTO DRUG VALUES (" + str(drugid.get()) + "," + "'{}'".format(name.get()) + "," +  str(price.get()) + ","  + "'{}'".format(com.get()) + ")")
                   
                    open_popup("Drug data added successfully!")

                    connection.commit()
                    connection.close()


                def Back():
                    Label1.destroy()
                    lbl1.destroy()
                    lbl2.destroy()
                    lbl3.destroy()
                    lbl4.destroy()
                    lfld1.destroy()
                    lfld2.destroy()
                    lfld3.destroy()
                    lfld4.destroy()
                    Backbutt.destroy()
                    SubmitButton.destroy()
                    ManagerPage2()

                Label1=Label(root, text="Add Drug Details", fg='Black', font=("Helvetica", 20))
                Label1.grid(column=1,row=0)

                lbl1=Label(root, text="Drug ID", fg='red', font=("Helvetica", 16))
                lbl1.place(x=80, y=150)
                drugid=IntVar()
                lfld1=Entry(root, textvariable= drugid)
                lfld1.configure(background='white')
                lfld1.place(x=250, y=150)

                lbl2=Label(root, text="Drug Name", fg='red', font=("Helvetica", 16))
                lbl2.place(x=80, y=250)
                name=StringVar()
                lfld2=Entry(root, textvariable=name)
                lfld2.configure(background='white')
                lfld2.place(x=250, y=250)

                lbl3=Label(root, text="Price", fg='red', font=("Helvetica", 16))
                lbl3.place(x=80, y=350)
                price=IntVar()
                lfld3=Entry(root, textvariable=price)
                lfld3.configure(background='white')
                lfld3.place(x=250, y=350)

                lbl4=Label(root, text="Composition", fg='red', font=("Helvetica", 16))
                lbl4.place(x=80, y=450)
                com=StringVar()
                lfld4=Entry(root, textvariable=com)
                lfld4.configure(background='white')
                lfld4.place(x=250, y=450)

                

                Backbutt=Button(root,text="Back",font=('Times_New_Roman',25),command=Back)
                Backbutt.grid(column=1,row=4)
                Backbutt.configure(background='white')

                SubmitButton=Button(root,text="Submit",font=('Times_New_Roman',25),command=Insertdata)
                SubmitButton.grid(column=2,row=4)
                SubmitButton.configure(background='white')

            button3=Button(root,text="Add Drug Data",font=('Times_New_Roman',25),command=AddDrug)
            button3.grid(column=2,row=1)
            button3.configure(background='white')
            

            def Viewdrugstatus():
                Accounting.destroy()
                button3.destroy()
                Logoutbutton.destroy()
                ViewDetails.destroy()
                button1.destroy()
                EmpDetails.destroy()
                Rawbutton1.destroy()
                
                def Back():
                    
                    bt2.destroy()
                    bt3.destroy()
                    bt4.destroy()
                    bt5.destroy()
                    bt7.destroy()
                    EmpDetails.destroy()
                    bt6.destroy()
                    DrugLabel.destroy()
                    drugEntry.destroy()
                    Backbutton.destroy()
                    
                    ManagerPage2()

                Backbutton=Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                Backbutton.grid(column=2,row=0)  
                Backbutton.configure(background='white')    
                
                DrugLabel = Label(root,text="Drug ID",font=('Times_New_Roman',15))
                DrugLabel.grid(row=0, column=0)  
                DrugLabel.configure(background='white')
                DID = StringVar()
                drugEntry = Entry(root, textvariable=DID)
                drugEntry.grid(row=0, column=1,padx=5,pady=5,ipady=10) 
                drugEntry.configure(background='white')

                

                def formPage():
                    Backbutton.destroy()
                    bt2.destroy()
                    bt3.destroy()
                    bt4.destroy()
                    bt5.destroy()
                    bt6.destroy()
                    bt7.destroy()
                    DrugLabel.destroy()
                    drugEntry.destroy()

                    def Backform():
                        
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()
                        Backbuttonf.destroy()
                        Updatebuttonf.destroy()
                        Deletebuttonf.destroy()
                        insertbuttonf.destroy()
                        Viewdrugstatus()

                    def open_popup(msg):
                        top= Toplevel(root)
                        top.geometry("750x250")
                        top.title("OOPS")
                        Label(top, text= msg, font=('Times_New_Roman',15)).place(x=150,y=80)   

                    print("did : " + DID.get())
                
                    did = DID.get()
                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    cur.execute("SELECT DrugID from FORMULATION where " + "DrugID = " + "'{}'".format(did))
                    output=cur.fetchall()
                    
                    if output == []:
                        open_popup("Drug ID doesn't exist, please check again!")
                    connection.commit()
                    connection.close()

                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    cur.execute("SELECT PID, Testing, Conclusion, RID, DrugID from FORMULATION where " + "DrugID = " + "'{}'".format(did))
                    output=cur.fetchall()
                    connection.commit()
                    connection.close()
                    if(output == []):
                        output = ["N/A", "N/A", "N/A", "N/A", "N/A"]
                    elif (employee_id[0] != "F" ):
                        output = ["N/A", "N/A", "N/A", "N/A", "N/A"]
                        open_popup("Access denied")
                    else:
                        output = output[0]

                    lbl1=Label(root, text="Process ID", fg='red', font=("Helvetica", 16))
                    lbl1.place(x=80, y=250)
                    lfld1=Label(root, text= output[0], fg='black', font=("Helvetica", 16))
                    lfld1.configure(background='white')
                    lfld1.place(x=250, y=250)

                    lbl2=Label(root, text="Testing", fg='red', font=("Helvetica", 16))
                    lbl2.place(x=80, y=350)
                    lfld2=Label(root, text=output[1], fg='black', font=("Helvetica", 16))
                    lfld2.configure(background='white')
                    lfld2.place(x=250, y=350)

                    lbl3=Label(root, text="Conclusion", fg='red', font=("Helvetica", 16))
                    lbl3.place(x=80, y=450)
                    lfld3=Label(root, text=output[2], fg='black', font=("Helvetica", 16))
                    lfld3.configure(background='white')
                    lfld3.place(x=250, y=450)

                    lbl4=Label(root, text="Raw Material ID", fg='red', font=("Helvetica", 16))
                    lbl4.place(x=80, y=550)
                    lfld4=Label(root, text=output[3], fg='black', font=("Helvetica", 16))
                    lfld4.configure(background='white')
                    lfld4.place(x=250, y=550)

                    lbl5=Label(root, text="Drug ID", fg='red', font=("Helvetica", 16))
                    lbl5.place(x=450, y=250)
                    lfld5=Label(root, text=output[4], fg='black', font=("Helvetica", 16))
                    lfld5.configure(background='white')
                    lfld5.place(x=650, y=250)

                    def Deletef():

                        print("did : " + DID.get())
                
                        did = DID.get()
                        connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                        cur=connection.cursor()
                        cur.execute("DELETE from FORMULATION where " + "DrugID = " + did)
                        cur.execute("SELECT * from FORMULATION")
                        output=cur.fetchall()
                        print(output)
                        if output == []:
                            open_popup("Drug ID doesn't exist, please check again!")
                        else:
                            open_popup("Deleted Successfully")    
                        connection.commit()
                        connection.close()

                    def Updatef():
                        a=Label(root, text="Process ID", fg='red', font=("Helvetica", 16))
                        a.place(x=80, y=250)
                        ai=IntVar()
                        aent=Entry(root,textvariable=ai)
                        aent.place(x=250,y=250)

                        b=Label(root, text="Testing", fg='red', font=("Helvetica", 16))
                        b.place(x=80, y=350)
                        bi=StringVar()
                        bent=Entry(root,textvariable=bi)
                        bent.place(x=250,y=350)
                        

                        c=Label(root, text="Conclusion", fg='red', font=("Helvetica", 16))
                        c.place(x=80, y=450)
                        ci=StringVar()
                        cent=Entry(root,textvariable=ci)
                        cent.place(x=250,y=450)
                        

                        d=Label(root, text="Raw Material ID", fg='red', font=("Helvetica", 16))
                        d.place(x=80, y=550)
                        di=IntVar()
                        dent=Entry(root,textvariable=di)
                        dent.place(x=250,y=550)
                        

                        e=Label(root, text="Drug ID", fg='red', font=("Helvetica", 16))
                        e.place(x=450, y=250)
                        ei=IntVar()
                        eent=Entry(root,textvariable=ei)
                        eent.place(x=650,y=250)

                        def update():
                            connection=psycopg2.connect(user="postgres",
                                password="//",
                                host="127.0.0.1",
                                port="5432",
                                database="pharmacompany")
                            cur=connection.cursor()
                            #UPDATE FORMULATION SET PID = 1, TESTING = "NO", CONCLUSION = "NO", RID = 1, DRUGID = 001
                            cur.execute("UPDATE FORMULATION SET PID = " +  str(ai.get()) + "," + "Testing = " + "'{}'".format(bi.get()) + "," + "Conclusion = " + "'{}'".format(ci.get()) + "," + "RID = " + str(di.get()) + ","  + "DrugID = " + str(ei.get()) + " where " + "DrugID = " + did)
                            cur.execute("SELECT * from FORMULATION")
                            output=cur.fetchall()
                            print(output)
                            if output == []:
                                open_popup("Drug ID doesn't exist, please check again!")
                            else:
                                open_popup("Updated Successfully")  
                                
                            connection.commit()
                            connection.close()

                        def Back():
                            a.destroy()
                            b.destroy()
                            c.destroy()
                            d.destroy()
                            e.destroy()
                            aent.destroy()
                            bent.destroy()
                            cent.destroy()
                            dent.destroy()
                            eent.destroy()
                            Backbutton12.destroy()
                            Savebutton.destroy()
                            formPage()
                            #UPDATE FOMULATION SET VAR = VALUE, WHERE DRUG ID = 001

                        

                        Backbutton12=Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                        Backbutton12.grid(column=2,row=0)  
                        Backbutton12.configure(background='white')    

                        Savebutton=Button(root,text="Save ",font=('Times_New_Roman',15),command=update)
                        Savebutton.grid(column=3,row=0)  
                        Savebutton.configure(background='white') 


                        Deletebuttonf.destroy()
                        Updatebuttonf.destroy()
                        Backbuttonf.destroy()  
                        insertbuttonf.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()

                        
                    def Insertf():
                        Backbuttonf.destroy()
                        Updatebuttonf.destroy()
                        Deletebuttonf.destroy()
                        insertbuttonf.destroy()
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()

                        def Backinsertf():
                            t1.destroy()
                            t11.destroy()
                            t2.destroy()
                            t22.destroy()
                            t3.destroy()
                            t33.destroy()
                            t4.destroy()
                            t44.destroy()
                            t5.destroy()
                            t55.destroy()
                            Submitbutton.destroy()
                            Buttoninsertfback.destroy()
                            formPage()

                        def Submit():

                            connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                            cur=connection.cursor()
                            cur.execute("INSERT INTO FORMULATION VALUES (" + str(t.get()) + "," + "'{}'".format(ti.get()) + "," + "'{}'".format(tj.get()) + "," + str(tk.get()) + ","  + str(tl.get()) + ")")
                        
                            open_popup(" Data added successfully!")

                            connection.commit()
                            connection.close()


                        t1=Label(root,text="Process ID",fg='red', font=("Helvetica", 16))
                        t1.place(x=80, y=250)
                        t=IntVar()
                        t11=Entry(root,textvariable=t)
                        t11.place(x=250,y=250)

                        t2=Label(root,text="Testing",fg='red', font=("Helvetica", 16))
                        t2.place(x=80, y=350)
                        ti=StringVar()
                        t22=Entry(root,textvariable=ti)
                        t22.place(x=250,y=350)

                        t3=Label(root,text="Conclusion",fg='red', font=("Helvetica", 16))
                        t3.place(x=80, y=450)
                        tj=StringVar()
                        t33=Entry(root,textvariable=tj)
                        t33.place(x=250,y=450)

                        t4=Label(root,text="Raw Material ID",fg='red', font=("Helvetica", 16))
                        t4.place(x=80, y=550)
                        tk=IntVar()
                        t44=Entry(root,textvariable=tk)
                        t44.place(x=250,y=550)

                        t5=Label(root,text="Drug ID",fg='red', font=("Helvetica", 16))
                        t5.place(x=450, y=250)
                        tl=IntVar()
                        t55=Entry(root,textvariable=tl)
                        t55.place(x=650,y=250)

                        Buttoninsertfback=Button(root,text="Back ",font=('Times_New_Roman',15),command=Backinsertf)
                        Buttoninsertfback.grid(column=1,row=0)  
                        Buttoninsertfback.configure(background='white')

                        Submitbutton=Button(root,text="Submit ",font=('Times_New_Roman',15),command=Submit)
                        Submitbutton.grid(column=2,row=0)  
                        Submitbutton.configure(background='white')


                    Backbuttonf=Button(root,text="Back ",font=('Times_New_Roman',15),command=Backform)
                    Backbuttonf.grid(column=1,row=0)  
                    Backbuttonf.configure(background='white') 

                    Updatebuttonf=Button(root,text="Update ",font=('Times_New_Roman',15),command=Updatef)
                    Updatebuttonf.grid(column=2,row=0)  
                    Updatebuttonf.configure(background='white') 

                    Deletebuttonf=Button(root,text="Delete ",font=('Times_New_Roman',15),command=Deletef)
                    Deletebuttonf.grid(column=3,row=0)  
                    Deletebuttonf.configure(background='white')   

                    insertbuttonf=Button(root,text="Add New Data",font=('Times_New_Roman',15),command=Insertf)
                    insertbuttonf.grid(column=4,row=0)
                    insertbuttonf.configure(background='white')


                def CSPage():
                    Backbutton.destroy()
                    bt2.destroy()
                    bt3.destroy()
                    bt4.destroy()
                    bt5.destroy()
                    bt6.destroy()
                    bt7.destroy()
                    DrugLabel.destroy()
                    drugEntry.destroy()

                    def Backcs():
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()
                        lbl6.destroy()
                        lfld6.destroy()
                        Backbuttoncs.destroy()
                        Updatebuttoncs.destroy()
                        Deletebuttoncs.destroy()
                        insertbuttoncs.destroy()
                        Viewdrugstatus()

                    def open_popup(msg):
                        top= Toplevel(root)
                        top.geometry("750x250")
                        top.title("OOPS")
                        Label(top, text= msg, font=('Times_New_Roman',15)).place(x=150,y=80)   

                    print("did : " + DID.get())
                
                    did = DID.get()
                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    cur.execute("SELECT * from CLINICAL_STUDY")
                    output=cur.fetchall()
                    print(output)
                    cur.execute("SELECT Drug_ID from CLINICAL_STUDY where " + "Drug_ID = " + "'{}'".format(did))
                    output=cur.fetchall()
                    
                    if output == []:
                        open_popup("Drug ID doesn't exist, please check again!")

                    connection.commit()
                    connection.close()

                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")    
                    
                    cur=connection.cursor()
                    cur.execute("SELECT Phase_ID, Drug_in_study, Phase, Conclusion, Drug_ID, Emp_ID from CLINICAL_STUDY where " + "Drug_ID = " + "'{}'".format(did))
                    output=cur.fetchall()

                    if(output == []):
                        output = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
                    elif (employee_id[0] != "C" and employee_id[1]!="S"):
                        output = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
                        open_popup("Access denied")    
                    else:
                        output = output[0]    

                    connection.commit()
                    connection.close()    

                    lbl1=Label(root, text="Phase ID", fg='red', font=("Helvetica", 16))
                    lbl1.place(x=80, y=250)
                    lfld1=Label(root, text= output[0], fg='black', font=("Helvetica", 16))
                    lfld1.configure(background='white')
                    lfld1.place(x=250, y=250)

                    lbl2=Label(root, text="Drug In Study", fg='red', font=("Helvetica", 16))
                    lbl2.place(x=80, y=350)
                    lfld2=Label(root, text=output[1], fg='black', font=("Helvetica", 16))
                    lfld2.configure(background='white')
                    lfld2.place(x=250, y=350)

                    lbl3=Label(root, text="Phase", fg='red', font=("Helvetica", 16))
                    lbl3.place(x=80, y=450)
                    lfld3=Label(root, text=output[2], fg='black', font=("Helvetica", 16))
                    lfld3.configure(background='white')
                    lfld3.place(x=250, y=450)

                    lbl4=Label(root, text="Conclusion", fg='red', font=("Helvetica", 16))
                    lbl4.place(x=80, y=550)
                    lfld4=Label(root, text=output[3], fg='black', font=("Helvetica", 16))
                    lfld4.configure(background='white')
                    lfld4.place(x=250, y=550)

                    lbl5=Label(root, text="Drug ID", fg='red', font=("Helvetica", 16))
                    lbl5.place(x=450, y=250)
                    lfld5=Label(root, text=output[4], fg='black', font=("Helvetica", 16))
                    lfld5.configure(background='white')
                    lfld5.place(x=650, y=250)

                    lbl6=Label(root, text="Employee ID", fg='red', font=("Helvetica", 16))
                    lbl6.place(x=450, y=350)
                    lfld6=Label(root, text=output[5], fg='black', font=("Helvetica", 16))
                    lfld6.configure(background='white')
                    lfld6.place(x=650, y=350)


                    def DeleteCS():

                        print("did : " + DID.get())
                
                        did = DID.get()

                        connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                        
                        cur=connection.cursor()
                        cur.execute("DELETE from CLINICAL_STUDY where " + "Drug_ID = " + did)
                        cur.execute("SELECT * from CLINICAL_STUDY")
                        output=cur.fetchall()
                        if output == []:
                            open_popup("Drug ID doesn't exist, please check again!")
                        else:
                            open_popup("Deleted Successfully")    

                        connection.commit()
                        connection.close()    


                    def UpdateCS():

                        def Back():
                            a.destroy()
                            b.destroy()
                            c.destroy()
                            d.destroy()
                            e.destroy()
                            f.destroy()
                            aent.destroy()
                            bent.destroy()
                            cent.destroy()
                            dent.destroy()
                            eent.destroy()
                            fent.destroy()
                            Backbutton12.destroy()
                            Savebutton.destroy()
                            CSPage()

                         


                        Deletebuttoncs.destroy()
                        Updatebuttoncs.destroy()
                        Backbuttoncs.destroy()  
                        insertbuttoncs.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()
                        lfld6.destroy()
                        lbl5.destroy()
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl6.destroy()

                        a=Label(root, text="Phase ID", fg='red', font=("Helvetica", 16))
                        a.place(x=80, y=250)
                        ai=IntVar()
                        aent=Entry(root,textvariable=ai)
                        aent.place(x=250,y=250)
                        

                        b=Label(root, text="Drug In Study", fg='red', font=("Helvetica", 16))
                        b.place(x=80, y=350)
                        bi=StringVar()
                        bent=Entry(root,textvariable=bi)
                        bent.place(x=250,y=350)
                        

                        c=Label(root, text="Phase", fg='red', font=("Helvetica", 16))
                        c.place(x=80, y=450)
                        ci=StringVar()
                        cent=Entry(root,textvariable=ci)
                        cent.place(x=250,y=450)
                        

                        d=Label(root, text="Conclusion", fg='red', font=("Helvetica", 16))
                        d.place(x=80, y=550)
                        di=StringVar()
                        dent=Entry(root,textvariable=di)
                        dent.place(x=250,y=550)
                        

                        e=Label(root, text="Drug ID", fg='red', font=("Helvetica", 16))
                        e.place(x=450, y=250)
                        ei=IntVar()
                        eent=Entry(root,textvariable=ei)
                        eent.place(x=650,y=250)

                        f=Label(root, text="Employee ID", fg='red', font=("Helvetica", 16))
                        f.place(x=450, y=350)
                        fi=StringVar()
                        fent=Entry(root,textvariable=fi)
                        fent.place(x=650,y=350)


                        def update():
                            connection=psycopg2.connect(user="postgres",
                                password="//",
                                host="127.0.0.1",
                                port="5432",
                                database="pharmacompany")
                            cur=connection.cursor()
                            
                            cur.execute("UPDATE CLINICAL_STUDY SET Phase_ID = " + str(ai.get()) + "," + "Drug_in_study = " + "'{}'".format(bi.get()) + "," + "Phase = " + str(ci.get()) + "," + "Conclusion = " + "'{}'".format(di.get()) + ","  + "Drug_ID = " + str(ei.get()) + "," + "Emp_ID = " + "'{}'".format(fi.get()) + " where " + "Drug_ID = " + did)
                            cur.execute("SELECT * from CLINICAL_STUDY")
                            output=cur.fetchall()
                            print(output)
                            if output == []:
                                open_popup("Drug ID doesn't exist, please check again!")
                            else:
                                open_popup("Updated Successfully")  
                                
                            connection.commit()
                            connection.close()


                        Backbutton12=Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                        Backbutton12.grid(column=2,row=0)  
                        Backbutton12.configure(background='white')    

                        Savebutton=Button(root,text="Save ",font=('Times_New_Roman',15),command=update)
                        Savebutton.grid(column=3,row=0)  
                        Savebutton.configure(background='white')   

                    def Insertf():
                        Backbuttoncs.destroy()
                        Updatebuttoncs.destroy()
                        Deletebuttoncs.destroy()
                        insertbuttoncs.destroy()
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()
                        lbl6.destroy()
                        lfld6.destroy()

                        def Backinsertf():
                            t1.destroy()
                            t11.destroy()
                            t2.destroy()
                            t22.destroy()
                            t3.destroy()
                            t33.destroy()
                            t4.destroy()
                            t44.destroy()
                            t5.destroy()
                            t55.destroy()
                            t6.destroy()
                            t66.destroy()
                            Submitbutton.destroy()
                            Buttoninsertfback.destroy()
                            formPage()

                        def Submit():

                            connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                            cur=connection.cursor()
                            cur.execute("INSERT INTO CLINICAL_STUDY VALUES (" + str(t.get()) + "," + "'{}'".format(ti.get()) + "," + str(tm.get()) + "," + "'{}'".format(tj.get()) + "," + str(tk.get()) + ","  + "'{}'".format(tl.get()) + ")")
                        
                            open_popup(" Data added successfully!")

                            connection.commit()
                            connection.close()


                        t1=Label(root,text="Phase ID",fg='red', font=("Helvetica", 16))
                        t1.place(x=80, y=250)
                        t=IntVar()
                        t11=Entry(root,textvariable=t)
                        t11.place(x=250,y=250)

                        t2=Label(root,text="Drug in study",fg='red', font=("Helvetica", 16))
                        t2.place(x=80, y=350)
                        ti=StringVar()
                        t22=Entry(root,textvariable=ti)
                        t22.place(x=250,y=350)

                        t6=Label(root,text="Phase",fg='red', font=("Helvetica", 16))
                        t6.place(x=80, y=450)
                        tm=IntVar()
                        t66=Entry(root,textvariable=tm)
                        t66.place(x=250,y=450)

                        t3=Label(root,text="Conclusion",fg='red', font=("Helvetica", 16))
                        t3.place(x=80, y=550)
                        tj=StringVar()
                        t33=Entry(root,textvariable=tj)
                        t33.place(x=250,y=550)

                        t4=Label(root,text="Drug ID",fg='red', font=("Helvetica", 16))
                        t4.place(x=450, y=250)
                        tk=IntVar()
                        t44=Entry(root,textvariable=tk)
                        t44.place(x=650,y=250)

                        t5=Label(root,text="Employee ID",fg='red', font=("Helvetica", 16))
                        t5.place(x=450, y=350)
                        tl=StringVar()
                        t55=Entry(root,textvariable=tl)
                        t55.place(x=650,y=350)

                        Buttoninsertfback=Button(root,text="Back ",font=('Times_New_Roman',15),command=Backinsertf)
                        Buttoninsertfback.grid(column=1,row=0)  
                        Buttoninsertfback.configure(background='white')

                        Submitbutton=Button(root,text="Submit ",font=('Times_New_Roman',15),command=Submit)
                        Submitbutton.grid(column=2,row=0)  
                        Submitbutton.configure(background='white') 

                    
                    Backbuttoncs=Button(root,text="Back ",font=('Times_New_Roman',15),command=Backcs)
                    Backbuttoncs.grid(column=1,row=0)  
                    Backbuttoncs.configure(background='white')  

                    Updatebuttoncs=Button(root,text="Update ",font=('Times_New_Roman',15),command=UpdateCS)
                    Updatebuttoncs.grid(column=2,row=0)  
                    Updatebuttoncs.configure(background='white') 

                    Deletebuttoncs=Button(root,text="Delete ",font=('Times_New_Roman',15),command=DeleteCS)
                    Deletebuttoncs.grid(column=3,row=0)  
                    Deletebuttoncs.configure(background='white')

                    insertbuttoncs=Button(root,text="Add New Data",font=('Times_New_Roman',15),command=Insertf)
                    insertbuttoncs.grid(column=4,row=0)
                    insertbuttoncs.configure(background='white')


                def ManufacturingPage():
                    Backbutton.destroy()
                    bt2.destroy()
                    bt3.destroy()
                    bt4.destroy()
                    bt5.destroy()
                    bt6.destroy()
                    bt7.destroy()
                    DrugLabel.destroy()
                    drugEntry.destroy()

                    def BackManu():
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()
                        lbl6.destroy()
                        lfld6.destroy()
                        Backbuttonm.destroy()
                        UpdatebuttonM.destroy()
                        DeletebuttonM.destroy()
                        insertbuttonM.destroy()
                        Viewdrugstatus()

                    def open_popup(msg):
                        top= Toplevel(root)
                        top.geometry("750x250")
                        top.title("OOPS")
                        Label(top, text= msg, font=('Times_New_Roman',15)).place(x=150,y=80)   

                    print("did : " + DID.get())
                
                    did = DID.get()

                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    
                    cur=connection.cursor()
                    cur.execute("SELECT * from MANUFACTURING")
                    output=cur.fetchall()
                    print(output)
                    cur.execute("SELECT D_ID from MANUFACTURING where " + "D_ID = " + "'{}'".format(did))
                    output=cur.fetchall()
                    
                    if output == []:
                        open_popup("Drug ID doesn't exist, please check again!")

                    connection.commit()
                    connection.close()

                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")    
                    
                    cur=connection.cursor()
                    cur.execute("SELECT Machinery, Status, Start_date, Last_date, D_ID, EmpID from MANUFACTURING where " + "D_ID = " + "'{}'".format(did))
                    output=cur.fetchall()

                    
                    if(output == []):
                        output = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
                    elif (employee_id[0] != "M"):
                        output = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
                        open_popup("Access denied")    
                    else:
                        output = output[0]     

                    connection.commit()
                    connection.close()    
                           

                    lbl1=Label(root, text="Machinery", fg='red', font=("Helvetica", 16))
                    lbl1.place(x=80, y=250)
                    lfld1=Label(root, text= output[0], fg='black', font=("Helvetica", 16))
                    lfld1.configure(background='white')
                    lfld1.place(x=250, y=250)

                    lbl2=Label(root, text="Status", fg='red', font=("Helvetica", 16))
                    lbl2.place(x=80, y=350)
                    lfld2=Label(root, text=output[1], fg='black', font=("Helvetica", 16))
                    lfld2.configure(background='white')
                    lfld2.place(x=250, y=350)

                    lbl3=Label(root, text="Start Date", fg='red', font=("Helvetica", 16))
                    lbl3.place(x=80, y=450)
                    lfld3=Label(root, text=output[2], fg='black', font=("Helvetica", 16))
                    lfld3.configure(background='white')
                    lfld3.place(x=250, y=450)

                    lbl4=Label(root, text="Last Date", fg='red', font=("Helvetica", 16))
                    lbl4.place(x=80, y=550)
                    lfld4=Label(root, text=output[3], fg='black', font=("Helvetica", 16))
                    lfld4.configure(background='white')
                    lfld4.place(x=250, y=550)

                    lbl5=Label(root, text="Drug ID", fg='red', font=("Helvetica", 16))
                    lbl5.place(x=450, y=250)
                    lfld5=Label(root, text=output[4], fg='black', font=("Helvetica", 16))
                    lfld5.configure(background='white')
                    lfld5.place(x=650, y=250)

                    lbl6=Label(root, text="Employee ID", fg='red', font=("Helvetica", 16))
                    lbl6.place(x=450, y=350)
                    lfld6=Label(root, text=output[5], fg='black', font=("Helvetica", 16))
                    lfld6.configure(background='white')
                    lfld6.place(x=650, y=350)

                    def DeleteM():

                        print("did : " + DID.get())
                
                        did = DID.get()
                        connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                        cur=connection.cursor()
                        cur.execute("DELETE  from MANUFACTURING where " + "D_ID = " + did)
                        cur.execute("SELECT * from MANUFACTURING")
                        output=cur.fetchall()
                        if output == []:
                            open_popup("Drug ID doesn't exist, please check again!")
                        else:
                            open_popup("Deleted Successfully")    

                        connection.commit()
                        connection.close()    


                    def UpdateM():

                        def Back():
                            a.destroy()
                            b.destroy()
                            c.destroy()
                            d.destroy()
                            e.destroy()
                            f.destroy()
                            aent.destroy()
                            bent.destroy()
                            cent.destroy()
                            dent.destroy()
                            eent.destroy()
                            fent.destroy()
                            Savebutton.destroy()
                            Backbutton12.destroy()
                            ManufacturingPage()

                        DeletebuttonM.destroy()
                        UpdatebuttonM.destroy()
                        Backbuttonm.destroy()  
                        insertbuttonM.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()
                        lfld6.destroy()
                        lbl6.destroy()
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()

                        a=Label(root, text="Machinery", fg='red', font=("Helvetica", 16))
                        a.place(x=80, y=250)
                        ai=StringVar()
                        aent=Entry(root,textvariable=ai)
                        aent.place(x=250,y=250)

                        b=Label(root, text="Status", fg='red', font=("Helvetica", 16))
                        b.place(x=80, y=350)
                        bi=StringVar()
                        bent=Entry(root,textvariable=bi)
                        bent.place(x=250,y=350)
                        

                        c=Label(root, text="Start Date", fg='red', font=("Helvetica", 16))
                        c.place(x=80, y=450)
                        ci=StringVar()
                        cent=Entry(root,textvariable=ci)
                        cent.place(x=250,y=450)
                        

                        d=Label(root, text="Last Date", fg='red', font=("Helvetica", 16))
                        d.place(x=80, y=550)
                        di=StringVar()
                        dent=Entry(root,textvariable=di)
                        dent.place(x=250,y=550)

                        e=Label(root, text="Drug ID", fg='red', font=("Helvetica", 16))
                        e.place(x=450, y=250)
                        ei=IntVar()
                        eent=Entry(root,textvariable=ei)
                        eent.place(x=650,y=250)

                        f=Label(root, text="Employee ID", fg='red', font=("Helvetica", 16))
                        f.place(x=450, y=350)
                        fi=StringVar()
                        fent=Entry(root,textvariable=fi)
                        fent.place(x=650,y=350)

                        def update():
                            connection=psycopg2.connect(user="postgres",
                                password="//",
                                host="127.0.0.1",
                                port="5432",
                                database="pharmacompany")
                            cur=connection.cursor()
                            cur.execute("drop trigger if exists t on manufacturing;")
                            cur.execute("drop function if exists quantity();")
                            cur.execute("CREATE FUNCTION quantity() RETURNS trigger AS $$BEGIN	IF (new.status = 'Complete' and old.status='In-Production') THEN UPDATE exports SET quantity = quantity + 10 WHERE exports.drug_identification =new.d_id; return new; END IF; return null; END; $$ LANGUAGE plpgsql;")
                            cur.execute("create TRIGGER t AFTER update on manufacturing for each row execute procedure quantity();")
                            cur.execute("UPDATE MANUFACTURING SET Machinery = " + "'{}'".format(ai.get()) + "," + "Status = " + "'{}'".format(bi.get()) + "," + "Start_date = " + "'{}'".format(ci.get()) + "," + "Last_date = " + "'{}'".format(di.get()) + ","  + "D_ID = " + str(ei.get()) + "," + "EmpID = " + "'{}'".format(fi.get()) + " where " + "D_ID = " + did)
                            cur.execute("SELECT * from MANUFACTURING")
                            output=cur.fetchall()
                            print(output)
                            if output == []:
                                open_popup("Drug ID doesn't exist, please check again!")
                            else:
                                open_popup("Updated Successfully")  
                                
                            connection.commit()
                            connection.close()

                        Backbutton12=Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                        Backbutton12.grid(column=2,row=0)  
                        Backbutton12.configure(background='white')    

                        Savebutton=Button(root,text="Save ",font=('Times_New_Roman',15),command=update)
                        Savebutton.grid(column=3,row=0)  
                        Savebutton.configure(background='white')

                    def Insertf():
                        Backbuttonm.destroy()
                        UpdatebuttonM.destroy()
                        DeletebuttonM.destroy()
                        insertbuttonM.destroy()
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()
                        lbl6.destroy()
                        lfld6.destroy()

                        def Backinsertf():
                            t1.destroy()
                            t11.destroy()
                            t2.destroy()
                            t22.destroy()
                            t3.destroy()
                            t33.destroy()
                            t4.destroy()
                            t44.destroy()
                            t5.destroy()
                            t55.destroy()
                            t6.destroy()
                            t66.destroy()
                            Submitbutton.destroy()
                            Buttoninsertfback.destroy()
                            formPage()

                        def Submit():

                            connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                            cur=connection.cursor()
                            cur.execute("INSERT INTO MANUFACTURING VALUES (" + "'{}'".format(t.get()) + "," + "'{}'".format(ti.get())  + "," + "'{}'".format(tm.get()) + "," + "'{}'".format(tj.get()) + "," + str(tk.get()) + ","  + "'{}'".format(tl.get()) + ")")
                        
                            open_popup(" Data added successfully!")

                            connection.commit()
                            connection.close()


                        t1=Label(root,text="Machinery",fg='red', font=("Helvetica", 16))
                        t1.place(x=80, y=250)
                        t=StringVar()
                        t11=Entry(root,textvariable=t)
                        t11.place(x=250,y=250)

                        t2=Label(root,text="Status",fg='red', font=("Helvetica", 16))
                        t2.place(x=80, y=350)
                        ti=StringVar()
                        t22=Entry(root,textvariable=ti)
                        t22.place(x=250,y=350)

                        t6=Label(root,text="Start Date",fg='red', font=("Helvetica", 16))
                        t6.place(x=80, y=450)
                        tm=StringVar()
                        t66=Entry(root,textvariable=tm)
                        t66.place(x=250,y=450)

                        t3=Label(root,text="Last Date",fg='red', font=("Helvetica", 16))
                        t3.place(x=80, y=550)
                        tj=StringVar()
                        t33=Entry(root,textvariable=tj)
                        t33.place(x=250,y=550)

                        t4=Label(root,text="Drug ID",fg='red', font=("Helvetica", 16))
                        t4.place(x=450, y=250)
                        tk=IntVar()
                        t44=Entry(root,textvariable=tk)
                        t44.place(x=650,y=250)

                        t5=Label(root,text="Employee ID",fg='red', font=("Helvetica", 16))
                        t5.place(x=450, y=350)
                        tl=StringVar()
                        t55=Entry(root,textvariable=tl)
                        t55.place(x=650,y=350)

                        Buttoninsertfback=Button(root,text="Back ",font=('Times_New_Roman',15),command=Backinsertf)
                        Buttoninsertfback.grid(column=1,row=0)  
                        Buttoninsertfback.configure(background='white')

                        Submitbutton=Button(root,text="Submit ",font=('Times_New_Roman',15),command=Submit)
                        Submitbutton.grid(column=2,row=0)  
                        Submitbutton.configure(background='white') 


                    Backbuttonm=Button(root,text="Back ",font=('Times_New_Roman',15),command=BackManu)
                    Backbuttonm.grid(column=1,row=0)  
                    Backbuttonm.configure(background='white') 

                    UpdatebuttonM=Button(root,text="Update ",font=('Times_New_Roman',15),command=UpdateM)
                    UpdatebuttonM.grid(column=2,row=0)  
                    UpdatebuttonM.configure(background='white') 

                    DeletebuttonM=Button(root,text="Delete ",font=('Times_New_Roman',15),command=DeleteM)
                    DeletebuttonM.grid(column=3,row=0)  
                    DeletebuttonM.configure(background='white')
                    insertbuttonM=Button(root,text="Add New Data",font=('Times_New_Roman',15),command=Insertf)
                    insertbuttonM.grid(column=4,row=0)
                    insertbuttonM.configure(background='white')


                def ExportsPage():
                    Backbutton.destroy()
                    bt2.destroy()
                    bt3.destroy()
                    bt4.destroy()
                    bt5.destroy()
                    bt6.destroy()
                    bt7.destroy()
                    DrugLabel.destroy()
                    drugEntry.destroy()

                    def BackE():
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()
                        lbl6.destroy()
                        lfld6.destroy()
                        Backbuttone.destroy()
                        Updatebuttone.destroy()
                        Deletebuttone.destroy()
                        insertbuttone.destroy()
                        Viewdrugstatus()

                    print("did : " + DID.get())
                
                    did = DID.get()
                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    
                    cur=connection.cursor()
                    cur.execute("SELECT * from EXPORTS")
                    output=cur.fetchall()
                    print(output)
                    cur.execute("SELECT Drug_identification from EXPORTS where " + "Drug_identification = " + "'{}'".format(did))
                    output=cur.fetchall()
                    
                    if output == []:
                        open_popup("Drug ID doesn't exist, please check again!")

                    connection.commit()
                    connection.close()

                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    cur.execute("SELECT Drug_identification, Type, D_name, Locations, Quantity, Employee_ID from EXPORTS where " + "Drug_identification = " + "'{}'".format(did))
                    output=cur.fetchall()

                    if(output == []):
                        output = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]

                    elif (employee_id[0] != "E"):
                        output = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
                        open_popup("Access denied")    
                    else:
                        output = output[0]    

                    connection.commit()
                    connection.close()

                    lbl1=Label(root, text="Drug ID", fg='red', font=("Helvetica", 16))
                    lbl1.place(x=80, y=250)
                    lfld1=Label(root, text= output[0], fg='black', font=("Helvetica", 16))
                    lfld1.configure(background='white')
                    lfld1.place(x=250, y=250)

                    lbl2=Label(root, text="Type", fg='red', font=("Helvetica", 16))
                    lbl2.place(x=80, y=350)
                    lfld2=Label(root, text=output[1], fg='black', font=("Helvetica", 16))
                    lfld2.configure(background='white')
                    lfld2.place(x=250, y=350)

                    lbl3=Label(root, text="Drug Name", fg='red', font=("Helvetica", 16))
                    lbl3.place(x=80, y=450)
                    lfld3=Label(root, text=output[2], fg='black', font=("Helvetica", 16))
                    lfld3.configure(background='white')
                    lfld3.place(x=250, y=450)

                    lbl4=Label(root, text="Locations", fg='red', font=("Helvetica", 16))
                    lbl4.place(x=80, y=550)
                    lfld4=Label(root, text=output[3], fg='black', font=("Helvetica", 16))
                    lfld4.configure(background='white')
                    lfld4.place(x=250, y=550)

                    lbl5=Label(root, text="Quantity", fg='red', font=("Helvetica", 16))
                    lbl5.place(x=450, y=250)
                    lfld5=Label(root, text=output[4], fg='black', font=("Helvetica", 16))
                    lfld5.configure(background='white')
                    lfld5.place(x=650, y=250)

                    lbl6=Label(root, text="Employee ID", fg='red', font=("Helvetica", 16))
                    lbl6.place(x=450, y=350)
                    lfld6=Label(root, text=output[5], fg='black', font=("Helvetica", 16))
                    lfld6.configure(background='white')
                    lfld6.place(x=650, y=350)

                    def DeleteE():

                        print("did : " + DID.get())
                
                        did = DID.get()
                        connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                        cur=connection.cursor()
                        cur.execute("DELETE  from EXPORTS where " + "Drug_identification = "  + did)
                        cur.execute("SELECT * from EXPORTS")
                        output=cur.fetchall()
                        if output == []:
                            open_popup("Drug ID doesn't exist, please check again!")
                        else:
                            open_popup("Deleted Successfully")    
                        connection.commit()
                        connection.close()

                    def UpdateE():

                        def Back():
                            a.destroy()
                            b.destroy()
                            c.destroy()
                            d.destroy()
                            e.destroy()
                            f.destroy()
                            aent.destroy()
                            bent.destroy()
                            cent.destroy()
                            dent.destroy()
                            eent.destroy()
                            fent.destroy()
                            Savebutton.destroy()
                            Backbutton12.destroy()
                            ExportsPage()

                        


                        Deletebuttone.destroy()
                        Updatebuttone.destroy()
                        Backbuttone.destroy()  
                        insertbuttone.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()
                        lfld6.destroy()
                        
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()
                        lbl6.destroy()

                        a=Label(root, text="Drug ID", fg='red', font=("Helvetica", 16))
                        a.place(x=80, y=250)
                        ai=IntVar()
                        aent=Entry(root,textvariable=ai)
                        aent.place(x=250,y=250)

                        b=Label(root, text="Type", fg='red', font=("Helvetica", 16))
                        b.place(x=80, y=350)
                        bi=StringVar()
                        bent=Entry(root,textvariable=bi)
                        bent.place(x=250,y=350)
                        

                        c=Label(root, text="Drug Name", fg='red', font=("Helvetica", 16))
                        c.place(x=80, y=450)
                        ci=StringVar()
                        cent=Entry(root,textvariable=ci)
                        cent.place(x=250,y=450)

                        d=Label(root, text="Locations", fg='red', font=("Helvetica", 16))
                        d.place(x=80, y=550)
                        di=StringVar()
                        dent=Entry(root,textvariable=di)
                        dent.place(x=250,y=550)

                        e=Label(root, text="Quantity", fg='red', font=("Helvetica", 16))
                        e.place(x=450, y=250)
                        ei=IntVar()
                        eent=Entry(root,textvariable=ei)
                        eent.place(x=650,y=250)

                        f=Label(root, text="Employee ID", fg='red', font=("Helvetica", 16))
                        f.place(x=450, y=350)
                        fi=StringVar()
                        fent=Entry(root,textvariable=fi)
                        fent.place(x=650,y=350)

                        def update():
                            connection=psycopg2.connect(user="postgres",
                                password="//",
                                host="127.0.0.1",  
                                port="5432",
                                database="pharmacompany")  
                            cur=connection.cursor()
                            print(ai.get())
                            cur.execute("UPDATE EXPORTS SET Type = " + "'{}'".format(bi.get()) + "," + "Drug_identification = " + str(ai.get()) + "," + "D_name = " + "'{}'".format(ci.get()) + "," + "Locations = " + "'{}'".format(di.get()) + ","  + "Quantity = " + str(ei.get()) + "," + "Employee_ID = " + "'{}'".format(fi.get()) + " where " + "Drug_identification = " + did)
                            cur.execute("SELECT * from EXPORTS")
                            output=cur.fetchall()
                            print(output)
                            if output == []:
                                open_popup("Drug ID doesn't exist, please check again!")
                            else:
                                open_popup("Updated Successfully")  
                                
                            connection.commit()
                            connection.close()

                        Backbutton12=Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                        Backbutton12.grid(column=2,row=0)  
                        Backbutton12.configure(background='white')    

                        Savebutton=Button(root,text="Save ",font=('Times_New_Roman',15),command=update)
                        Savebutton.grid(column=3,row=0)  
                        Savebutton.configure(background='white')     

                    def Insertf():
                        Backbuttone.destroy()
                        Updatebuttone.destroy()
                        Deletebuttone.destroy()
                        insertbuttone.destroy()
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()
                        lbl6.destroy()
                        lfld6.destroy()

                        def Backinsertf():
                            t1.destroy()
                            t11.destroy()
                            t2.destroy()
                            t22.destroy()
                            t3.destroy()
                            t33.destroy()
                            t4.destroy()
                            t44.destroy()
                            t5.destroy()
                            t55.destroy()
                            t6.destroy()
                            t66.destroy()
                            Submitbutton.destroy()
                            Buttoninsertfback.destroy()
                            formPage()

                        def Submit():

                            connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                            cur=connection.cursor()
                            cur.execute("INSERT INTO EXPORTS VALUES ("+ str(t.get()) + "," + "'{}'".format(ti.get())  + "," + "'{}'".format(tm.get()) + "," + "'{}'".format(tj.get()) + ","  + "'{}'".format(tk.get()) + ","  + "'{}'".format(tl.get()) + ")")
                        
                            open_popup(" Data added successfully!")

                            connection.commit()
                            connection.close()


                        t1=Label(root,text="Drug_identification",fg='red', font=("Helvetica", 16))
                        t1.place(x=80, y=250)
                        t=IntVar()
                        t11=Entry(root,textvariable=t)
                        t11.place(x=250,y=250)

                        t2=Label(root,text="Type",fg='red', font=("Helvetica", 16))
                        t2.place(x=80, y=350)
                        ti=StringVar()
                        t22=Entry(root,textvariable=ti)
                        t22.place(x=250,y=350)

                        t6=Label(root,text="D_name",fg='red', font=("Helvetica", 16))
                        t6.place(x=80, y=450)
                        tm=StringVar()
                        t66=Entry(root,textvariable=tm)
                        t66.place(x=250,y=450)

                        t3=Label(root,text="Locations",fg='red', font=("Helvetica", 16))
                        t3.place(x=80, y=550)
                        tj=StringVar()
                        t33=Entry(root,textvariable=tj)
                        t33.place(x=250,y=550)

                        t4=Label(root,text="Quantity",fg='red', font=("Helvetica", 16))
                        t4.place(x=450, y=250)
                        tk=IntVar()
                        t44=Entry(root,textvariable=tk)
                        t44.place(x=650,y=250)

                        t5=Label(root,text="Employee ID",fg='red', font=("Helvetica", 16))
                        t5.place(x=450, y=350)
                        tl=StringVar()
                        t55=Entry(root,textvariable=tl)
                        t55.place(x=650,y=350)

                        Buttoninsertfback=Button(root,text="Back ",font=('Times_New_Roman',15),command=Backinsertf)
                        Buttoninsertfback.grid(column=1,row=0)  
                        Buttoninsertfback.configure(background='white')

                        Submitbutton=Button(root,text="Submit ",font=('Times_New_Roman',15),command=Submit)
                        Submitbutton.grid(column=2,row=0)  
                        Submitbutton.configure(background='white')    

                    Backbuttone=Button(root,text="Back ",font=('Times_New_Roman',15),command=BackE)
                    Backbuttone.grid(column=1,row=0)  
                    Backbuttone.configure(background='white')

                    Updatebuttone=Button(root,text="Update ",font=('Times_New_Roman',15),command=UpdateE)
                    Updatebuttone.grid(column=2,row=0)  
                    Updatebuttone.configure(background='white') 

                    Deletebuttone=Button(root,text="Delete ",font=('Times_New_Roman',15),command=DeleteE)
                    Deletebuttone.grid(column=3,row=0)  
                    Deletebuttone.configure(background='white')

                    insertbuttone=Button(root,text="Add New Data",font=('Times_New_Roman',15),command=Insertf)
                    insertbuttone.grid(column=4,row=0)
                    insertbuttone.configure(background='white')

                def LicensePage():
                    Backbutton.destroy()
                    bt2.destroy()
                    bt3.destroy()
                    bt4.destroy()
                    bt5.destroy()
                    bt6.destroy()
                    bt7.destroy()
                    DrugLabel.destroy()
                    drugEntry.destroy()

                    def BackL():
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lfld3.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        Backbuttonl.destroy()
                        Updatebuttonl.destroy()
                        Deletebuttonl.destroy()
                        insertbuttonl.destroy()
                        Viewdrugstatus()


                    print("did : " + DID.get())
                
                    did = DID.get()
                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    cur.execute("SELECT * from LICENSE")
                    output=cur.fetchall()
                    print(output)
                    cur.execute("SELECT Drug_ID from LICENSE where " + "Drug_ID = " + "'{}'".format(did))
                    output=cur.fetchall()
                    
                    if output == []:
                        open_popup("Drug ID doesn't exist, please check again!")
                    connection.commit()
                    connection.close()

                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    cur.execute("SELECT License_authority, Approved_by, Drug_ID  from LICENSE where " + "Drug_ID = " + "'{}'".format(did))
                    output=cur.fetchall()

                    if(output == []):
                        output = ["N/A", "N/A", "N/A"]
                    else:
                        output = output[0]  

                    connection.commit()
                    connection.close()         

                    lbl1=Label(root, text="License Authority", fg='red', font=("Helvetica", 16))
                    lbl1.place(x=80, y=250)
                    lfld1=Label(root, text= output[0], fg='black', font=("Helvetica", 16))
                    lfld1.configure(background='white')
                    lfld1.place(x=250, y=250)

                    lbl2=Label(root, text="Approved By", fg='red', font=("Helvetica", 16))
                    lbl2.place(x=80, y=350)
                    lfld2=Label(root, text=output[1], fg='black', font=("Helvetica", 16))
                    lfld2.configure(background='white')
                    lfld2.place(x=250, y=350)

                    lbl3=Label(root, text="Drug ID", fg='red', font=("Helvetica", 16))
                    lbl3.place(x=80, y=450)
                    lfld3=Label(root, text=output[2], fg='black', font=("Helvetica", 16))
                    lfld3.configure(background='white')
                    lfld3.place(x=250, y=450)

                    def DeleteL():

                        print("did : " + DID.get())
                
                        did = DID.get()
                        connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                        cur=connection.cursor()
                        cur.execute("DELETE  from LICENSE where " + "Drug_ID = "  + did )
                        cur.execute("SELECT * from LICENSE")
                        output=cur.fetchall()
                        if output == []:
                            open_popup("Drug ID doesn't exist, please check again!")
                        else:
                            open_popup("Deleted Successfully")   

                        connection.commit()
                        connection.close()    

                    def UpdateL():

                        def Back():
                            a.destroy()
                            b.destroy()
                            c.destroy()
                            aent.destroy()
                            bent.destroy()
                            cent.destroy()
                            Savebutton.destroy()
                            
                            Backbutton12.destroy()
                            LicensePage()

                        


                        Deletebuttonl.destroy()
                        Updatebuttonl.destroy()
                        Backbuttonl.destroy()  
                        insertbuttonl.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lbl3.destroy()
                        lbl1.destroy()
                        lbl2.destroy()
                        

                        a=Label(root, text="License Authority", fg='red', font=("Helvetica", 16))
                        a.place(x=80, y=250)
                        ai=StringVar()
                        aent=Entry(root,textvariable=ai)
                        aent.place(x=250,y=250)
                        

                        b=Label(root, text="Approved By", fg='red', font=("Helvetica", 16))
                        b.place(x=80, y=350)
                        bi=StringVar()
                        bent=Entry(root,textvariable=bi)
                        bent.place(x=250,y=350)
                        

                        c=Label(root, text="Drug ID", fg='red', font=("Helvetica", 16))
                        c.place(x=80, y=450)
                        ci=IntVar()
                        cent=Entry(root,textvariable=ci)
                        cent.place(x=250,y=450)

                        def update():
                            connection=psycopg2.connect(user="postgres",
                                password="//",
                                host="127.0.0.1",  
                                port="5432",
                                database="pharmacompany")  
                            cur=connection.cursor()
                            print(ai.get())
                            cur.execute("UPDATE LICENSE SET License_authority = " + "'{}'".format(ai.get()) + "," +  "Approved_by = " + "'{}'".format(bi.get()) + "," +  "Drug_ID = " + str(ci.get()) +  " where " + "Drug_ID = " + did)
                            cur.execute("SELECT * from LICENSE")
                            output=cur.fetchall()
                            print(output)
                            if output == []:
                                open_popup("Drug ID doesn't exist, please check again!")
                            else:
                                open_popup("Updated Successfully")  
                                
                            connection.commit()
                            connection.close()

                        Backbutton12=Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                        Backbutton12.grid(column=2,row=0)  
                        Backbutton12.configure(background='white')    

                        Savebutton=Button(root,text="Save ",font=('Times_New_Roman',15),command=update)
                        Savebutton.grid(column=3,row=0)  
                        Savebutton.configure(background='white') 


                    Backbuttonl=Button(root,text="Back ",font=('Times_New_Roman',15),command=BackL)
                    Backbuttonl.grid(column=1,row=0)  
                    Backbuttonl.configure(background='white')  

                    Updatebuttonl=Button(root,text="Update ",font=('Times_New_Roman',15),command=UpdateL)
                    Updatebuttonl.grid(column=2,row=0)  
                    Updatebuttonl.configure(background='white') 

                    Deletebuttonl=Button(root,text="Delete ",font=('Times_New_Roman',15),command=DeleteL)
                    Deletebuttonl.grid(column=3,row=0)  
                    Deletebuttonl.configure(background='white')    

                    insertbuttonl=Button(root,text="Add New Data",font=('Times_New_Roman',15))
                    insertbuttonl.grid(column=4,row=0)
                    insertbuttonl.configure(background='white')         
                    
                def DrugPage():
                    Backbutton.destroy()
                    bt2.destroy()
                    bt3.destroy()
                    bt4.destroy()
                    bt5.destroy()
                    bt6.destroy()
                    bt7.destroy()
                    DrugLabel.destroy()
                    drugEntry.destroy()

                    def Back():
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lfld4.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        BackButtonDrug.destroy()
                        Viewdrugstatus()

                    print("did : " + DID.get())
                
                    did = DID.get()    

                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    cur.execute("SELECT DID, DName, Price, Composition from DRUG where " + "DID = " + "'{}'".format(did))
                    output=cur.fetchall()

                    if(output == []):
                        output = ["N/A", "N/A", "N/A","N/A"]
                    else:
                        output = output[0]

                    connection.commit()
                    connection.close()    


                    lbl1=Label(root, text="Drug ID", fg='red', font=("Helvetica", 16))
                    lbl1.place(x=80, y=250)
                    lfld1=Label(root, text=output[0], fg='black', font=("Helvetica", 16))
                    lfld1.configure(background='white')
                    lfld1.place(x=250, y=250)

                    lbl2=Label(root, text="Drug Name", fg='red', font=("Helvetica", 16))
                    lbl2.place(x=80, y=350)
                    lfld2=Label(root, text=output[1],fg='black', font=("Helvetica", 16))
                    lfld2.configure(background='white')
                    lfld2.place(x=250, y=350)

                    lbl3=Label(root, text="Price", fg='red', font=("Helvetica", 16))
                    lbl3.place(x=80, y=450)
                    lfld3=Label(root, text=output[2], fg='black', font=("Helvetica", 16))
                    lfld3.configure(background='white')
                    lfld3.place(x=250, y=450)

                    lbl4=Label(root, text="Composition", fg='red', font=("Helvetica", 16))
                    lbl4.place(x=80, y=550)
                    lfld4=Label(root, text=output[3] , fg='black', font=("Helvetica", 16))
                    lfld4.configure(background='white')
                    lfld4.place(x=250, y=550)

                    BackButtonDrug=Button(root,text="Cancel ",font=('Times_New_Roman',15),command=Back)
                    BackButtonDrug.grid(column=2,row=0)  
                    BackButtonDrug.configure(background='white') 

                
                
                bt2=Button(root,text="Formulation",font=('Times_New_Roman',25),command=formPage)
                bt2.grid(column=0,row=2)    
                bt2.configure(background='white')

                bt3=Button(root,text="Clinical Studies ",font=('Times_New_Roman',25),command=CSPage)
                bt3.grid(column=1,row=1)    
                bt3.configure(background='white')

                bt4=Button(root,text="Exports ",font=('Times_New_Roman',25),command=ExportsPage)
                bt4.grid(column=0,row=1)    
                bt4.configure(background='white')

                bt5=Button(root,text="Manufacturing",font=('Times_New_Roman',25),command=ManufacturingPage)
                bt5.grid(column=2,row=1)    
                bt5.configure(background='white')

                

                bt6=Button(root,text="License Information ",font=('Times_New_Roman',25),command=LicensePage)
                bt6.grid(column=2,row=2)    
                bt6.configure(background='white')

                bt7=Button(root,text="View Drug Table ",font=('Times_New_Roman',25),command=DrugPage)
                bt7.grid(column=1,row=2)    
                bt7.configure(background='white')

            ViewDetails=Button(root,text="Drug Status",font=('Times_New_Roman',25),command=Viewdrugstatus)
            ViewDetails.grid(column=1,row=1)    
            ViewDetails.configure(background='white')    

            def Logout():
                button3.destroy()
                button1.destroy()
                ViewDetails.destroy()
                Logoutbutton.destroy()
                Rawbutton1.destroy()
                EmpDetails.destroy()
                usernameLabel.destroy()
                passwordLabel.destroy()
                usernameEntry.destroy()
                IIDentry.destroy()
                Accounting.destroy()
                
                PageOne()
                


            def RegisterEmployee():
                Accounting.destroy()
                button3.destroy()
                button1.destroy()
                Rawbutton1.destroy()
                ViewDetails.destroy()
                Logoutbutton.destroy()
                EmpDetails.destroy()

                def Cancel():
                   Cancelbutton.destroy()
                   Registerbutton.destroy()
                   lbl8.destroy()
                   lbl1.destroy()
                   lbl2.destroy()
                   lbl3.destroy()
                   lbl4.destroy()
                   lbl5.destroy()
                   lbl6.destroy()
                   lbl7.destroy()
                   lbl9.destroy()
                   lfld9.destroy()
                   lbl10.destroy()
                   lfld10.destroy()
                   lfld8.destroy()
                   lfld1.destroy()
                   lfld2.destroy()
                   lfld3.destroy()
                   lfld4.destroy()
                   lfld5.destroy()
                   lfld6.destroy()
                   lfld7.destroy()
                   lbl11.destroy()
                   lfld11.destroy()
                   ManagerPage2()

                def Register():
                   connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                   cur=connection.cursor()
                   cur.execute("INSERT INTO EMPLOYEE VALUES (" + "'{}'".format(fname.get()) + "," + "'{}'".format(lname.get()) + "," + "'{}'".format(EID.get()) + "," + "null" + "," +  "'{}'".format(js.get()) + "," + str(Sal.get()) + ","  + str(age.get()) + ","  + "'{}'".format(addr.get()) + ","  + "'{}'".format(gender.get()) + "," + "'{}'".format(date.get()) + "," + str(dno.get()) + ")")
                   cur.execute("INSERT INTO LOGININFO VALUES (" + "'{}'".format(EID.get()) + "," + str(password1.get()) + ")")
                   open_popup("Employee registered successfully!")

                   connection.commit()
                   connection.close()
                   lbl8.destroy()
                   lbl1.destroy()
                   lbl2.destroy()
                   lbl3.destroy()
                   lbl4.destroy()
                   lbl5.destroy()
                   lbl6.destroy()
                   lbl7.destroy()
                   lbl9.destroy()
                   lfld9.destroy()
                   lbl10.destroy()
                   lfld10.destroy()
                   lfld8.destroy()
                   lfld1.destroy()
                   lfld2.destroy()
                   lfld3.destroy()
                   lfld4.destroy()
                   lfld5.destroy()
                   lfld6.destroy()
                   lfld7.destroy()
                   lbl11.destroy()
                   lfld11.destroy()
                   Cancelbutton.destroy()
                   Registerbutton.destroy()
                   
                   
                   ManagerPage2()

                Cancelbutton=Button(root,text="Cancel ",font=('Times_New_Roman',15),command=Cancel)
                Cancelbutton.grid(column=2,row=0)  
                Cancelbutton.configure(background='white') 

                Registerbutton=Button(root,text="Register",font=('Times_New_Roman',15), command = Register)
                Registerbutton.grid(column=3,row=0)  
                Registerbutton.configure(background='white') 

                lbl1=Label(root, text="First Name", fg='red', font=("Helvetica", 16))
                lbl1.place(x=80, y=150)
                fname=StringVar()
                lfld1=Entry(root, textvariable= fname)
                lfld1.configure(background='white')
                lfld1.place(x=250, y=150)

                lbl2=Label(root, text="Last Name", fg='red', font=("Helvetica", 16))
                lbl2.place(x=80, y=250)
                lname=StringVar()
                lfld2=Entry(root, textvariable=lname)
                lfld2.configure(background='white')
                lfld2.place(x=250, y=250)

                lbl3=Label(root, text="Employee ID", fg='red', font=("Helvetica", 16))
                lbl3.place(x=80, y=350)
                EID=StringVar()
                lfld3=Entry(root, textvariable=EID)
                lfld3.configure(background='white')
                lfld3.place(x=250, y=350)

                lbl4=Label(root, text="Job Position", fg='red', font=("Helvetica", 16))
                lbl4.place(x=80, y=450)
                js=StringVar()
                lfld4=Entry(root, textvariable=js)
                lfld4.configure(background='white')
                lfld4.place(x=250, y=450)

                lbl5=Label(root, text="Salary", fg='red', font=("Helvetica", 16))
                lbl5.place(x=80, y=550)
                Sal=IntVar()
                lfld5=Entry(root, textvariable=Sal)
                lfld5.configure(background='white')
                lfld5.place(x=250, y=550)

                lbl6=Label(root, text="Age", fg='red', font=("Helvetica", 16))
                lbl6.place(x=400, y=150)
                age=IntVar()
                lfld6=Entry(root, textvariable=age)
                lfld6.configure(background='white')
                lfld6.place(x=600, y=150)

                lbl7=Label(root, text="Address", fg='red', font=("Helvetica", 16))
                lbl7.place(x=400, y=250)
                addr=StringVar()
                lfld7=Entry(root, textvariable=addr)
                lfld7.configure(background='white')
                lfld7.place(x=600, y=250)

                lbl8=Label(root, text="Gender", fg='red', font=("Helvetica", 16))
                lbl8.place(x=400, y=350)
                gender=StringVar()
                lfld8=Entry(root, textvariable=gender)
                lfld8.configure(background='white')
                lfld8.place(x=600, y=350)

                lbl9=Label(root, text="Start Date", fg='red', font=("Helvetica", 16))
                lbl9.place(x=400, y=450)
                date=StringVar()
                lfld9=Entry(root, textvariable=date)
                lfld9.configure(background='white')
                lfld9.place(x=600, y=450)

                lbl10=Label(root, text="Department Number",fg='red', font=("Helvetica", 16))
                lbl10.place(x=400, y=550)
                dno=IntVar()
                lfld10=Entry(root, textvariable=dno)
                lfld10.configure(background='white')
                lfld10.place(x=600, y=550) 

                lbl11=Label(root, text="Password",fg='red', font=("Helvetica", 16))
                lbl11.place(x=400, y=650)
                password1=StringVar()
                lfld11=Entry(root, textvariable=password1)
                lfld11.configure(background='white')
                lfld11.place(x=600, y=650) 


                

            button1=Button(root,text="Register Employee ",font=('Times_New_Roman',25),command=RegisterEmployee)
            button1.grid(column=0,row=1)    
            button1.configure(background='white')

            def open_popup(msg):
                    button1.destroy()
                    Rawbutton1.destroy()
                    ViewDetails.destroy()
                    Logoutbutton.destroy()
                    EmpDetails.destroy()
                    top= Toplevel(root)
                    top.geometry("750x250")
                    top.title("OOPS")
                    Label(top, text= msg, font=('Times_New_Roman',15)).place(x=150,y=80)

            def RMStatus():
                Accounting.destroy()
                button3.destroy()
                Rawbutton1.destroy()
                button1.destroy()
                ViewDetails.destroy()
                Logoutbutton.destroy()

                

                def Back():
                    IIDEntry.destroy()
                    IIDlabel.destroy()
                    GetDeet1.destroy()
                    Backbutton.destroy()
                    EmpDetails.destroy()
                    ManagerPage2()


                def RMDetails():
                    Backbutton.destroy()
                    IIDlabel.destroy()
                    IIDEntry.destroy()
                    GetDeet1.destroy()
                    EmpDetails.destroy()

                    print("iid : " + IID.get())
                
                    iid = IID.get()
                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    
                    cur=connection.cursor()
                    cur.execute("SELECT * from RAW_MATERIALS")
                    output=cur.fetchall()
                    print(output)
                    cur.execute("SELECT IID from RAW_MATERIALS where " + "iid = " + "'{}'".format(iid))
                    output=cur.fetchall()
                    
                    if output == []:
                        open_popup("IID doesn't exist, please check again!")
                    connection.commit()
                    connection.close()

                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    cur.execute("SELECT IID, API, quantity from RAW_MATERIALS where " + "iid = " + "'{}'".format(iid))
                    output=cur.fetchall()

                    if(output == []):
                        output = ["N/A", "N/A", "N/A"]
                    else:
                        output = output[0]

                    connection.commit()
                    connection.close()

                    def Back():
                        label.destroy()
                        idlabel1.destroy()
                        idlabel2.destroy()
                        api1.destroy()
                        api2.destroy()
                        quantity1.destroy()
                        quantity.destroy()
                        Backbutton1.destroy()
                        RMStatus()

                    label= Label(root, text="RAW MATERIALS",font=('Times_New_Roman',25))
                    label.grid(row=0, column=0)
                    label.configure(background='white')
                    
                    idlabel1=Label(root,text="Ingredient ID",font=('Times_New_Roman',15))
                    idlabel1.grid(row=1,column=0)
                    idlabel1.configure(background='white')

                    
                    idlabel2=Label(root,text= output[0],font=('Times_New_Roman',15))
                    idlabel2.grid(row=1,column=1)
                    idlabel2.configure(background='white')

                    api1=Label(root,text="Active Pharamaceutical Ingredient",font=('Times_New_Roman',15))
                    api1.grid(row=2,column=0)
                    api1.configure(background='white')

                    api2=Label(root,text=output[1],font=('Times_New_Roman',15))
                    api2.grid(row=2,column=1)
                    api2.configure(background='white')

                    quantity=Label(root,text="Quantity",font=('Times_New_Roman',15))
                    quantity.grid(row=3,column=0)
                    quantity.configure(background='white')

                    quantity1=Label(root,text=output[2],font=('Times_New_Roman',15))
                    quantity1.grid(row=3,column=1)
                    quantity1.configure(background='white')

                    Backbutton1=Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                    Backbutton1.grid(column=2,row=0)  

                Backbutton=Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                Backbutton.grid(column=2,row=0)  

                Backbutton.configure(background='white') 
                IIDlabel= Label(root, text="Ingredient ID",font=('Times_New_Roman',15))
                IIDlabel.grid(row=1, column=0)
                IIDlabel.configure(background='white')
                IID = StringVar()
                IIDEntry = Entry(root, textvariable=IID)
                IIDEntry.grid(row=1, column=1,padx=5,pady=5,ipady=10)  
                IIDEntry.configure(background='white')

                GetDeet1=Button(root,text="Get Ingrdient Status",font=('Times_New_Roman',25),command=RMDetails)
                GetDeet1.grid(column=1,row=2)    
                GetDeet1.configure(background='white')

            Rawbutton1=Button(root,text="Raw Material Status",font=('Times_New_Roman',25),command=RMStatus)
            Rawbutton1.grid(column=0,row=2)    
            Rawbutton1.configure(background='white')

            
            def EmpDeetsView():
                button3.destroy()
                Accounting.destroy()
                ViewDetails.destroy()
                Rawbutton1.destroy()
                EmpDetails.destroy()
                button1.destroy()
                Logoutbutton.destroy()

                def Back():
                    EIDEntry.destroy()
                    EIDlabel.destroy()
                    Viewbutton.destroy()
                    Backbutton.destroy()
                    EmpDetails.destroy()
                    ManagerPage2()

                def open_popup(msg):
                    top= Toplevel(root)
                    top.geometry("750x250")
                    top.title("OOPS")
                    Label(top, text= msg, font=('Times_New_Roman',15)).place(x=150,y=80)

                def ViewEmpPage2():

                    print("eid : " + EID.get())
                    eid = EID.get()
                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    
                    cur.execute("SELECT EID From EMPLOYEE where " + "EID = " + "'{}'".format(eid))
                    output=cur.fetchall()
                    
                    if output == []:
                        open_popup("Employee ID doesn't exist, please check again!")
                    
                    cur.execute("SELECT Fname, Lname, EID, Job_Position, Salary, Age, Address,Gender, Start_Date, Dept_No from EMPLOYEE where " + "EID = " + "'{}'".format(eid))
                    output=cur.fetchall()
                    if output == []:
                        output = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A","N/A","N/A"]
                    elif eid == "AA01":
                        open_popup("Access Denied!")
                        output = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A","N/A","N/A"]
                    else:
                        output = output[0]

                    connection.commit()
                    connection.close()    

                    Viewbutton.destroy()
                    EIDEntry.destroy()
                    EIDlabel.destroy()
                    Backbutton.destroy()

                    def Back():
                        lbl8.destroy()
                        lbl1.destroy()
                        lbl2.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()
                        lbl6.destroy()
                        lbl7.destroy()
                        lbl9.destroy()
                        lfld9.destroy()
                        lbl10.destroy()
                        lfld10.destroy()
                        lfld8.destroy()
                        lfld1.destroy()
                        lfld2.destroy()
                        lfld3.destroy()
                        lfld4.destroy()
                        lfld5.destroy()
                        lfld6.destroy()
                        lfld7.destroy()
                        Backbutton1.destroy()
                        EmpDeetsView()

                    lbl1=Label(root, text="First Name", fg='red', font=("Helvetica", 16))
                    lbl1.place(x=80, y=150)
                    lfld1=Label(root, text= output[0], fg='black', font=("Helvetica", 16))
                    lfld1.configure(background='white')
                    lfld1.place(x=250, y=150)

                    lbl2=Label(root, text="Last Name", fg='red', font=("Helvetica", 16))
                    lbl2.place(x=80, y=250)
                    lfld2=Label(root, text=output[1], fg='black', font=("Helvetica", 16))
                    lfld2.configure(background='white')
                    lfld2.place(x=250, y=250)

                    lbl3=Label(root, text="Employee ID", fg='red', font=("Helvetica", 16))
                    lbl3.place(x=80, y=350)
                    lfld3=Label(root, text=output[2] ,fg='black', font=("Helvetica", 16))
                    lfld3.configure(background='white')
                    lfld3.place(x=250, y=350)

                    lbl4=Label(root, text="Job Position", fg='red', font=("Helvetica", 16))
                    lbl4.place(x=80, y=450)
                    lfld4=Label(root, text=output[3], fg='black', font=("Helvetica", 16))
                    lfld4.configure(background='white')
                    lfld4.place(x=250, y=450)

                    lbl5=Label(root, text="Salary", fg='red', font=("Helvetica", 16))
                    lbl5.place(x=80, y=550)
                    lfld5=Label(root, text=output[4], fg='black', font=("Helvetica", 16))
                    lfld5.configure(background='white')
                    lfld5.place(x=250, y=550)

                    lbl6=Label(root, text="Age", fg='red', font=("Helvetica", 16))
                    lbl6.place(x=350, y=150)
                    lfld6=Label(root, text=output[5], fg='black', font=("Helvetica", 16))
                    lfld6.configure(background='white')
                    lfld6.place(x=550, y=150)

                    lbl7=Label(root, text="Address", fg='red', font=("Helvetica", 16))
                    lbl7.place(x=350, y=250)
                    lfld7=Label(root, text=output[6], fg='black', font=("Helvetica", 16))
                    lfld7.configure(background='white')
                    lfld7.place(x=550, y=250)

                    lbl8=Label(root, text="Gender", fg='red', font=("Helvetica", 16))
                    lbl8.place(x=350, y=350)
                    lfld8=Label(root, text=output[7], fg='black', font=("Helvetica", 16))
                    lfld8.configure(background='white')
                    lfld8.place(x=550, y=350)

                    lbl9=Label(root, text="Start Date", fg='red', font=("Helvetica", 16))
                    lbl9.place(x=350, y=450)
                    lfld9=Label(root, text=output[8], fg='black', font=("Helvetica", 16))
                    lfld9.configure(background='white')
                    lfld9.place(x=550, y=450)

                    lbl10=Label(root, text="Department Number", fg='red', font=("Helvetica", 16))
                    lbl10.place(x=350, y=550)
                    lfld10=Label(root, text=output[9], fg='black', font=("Helvetica", 16))
                    lfld10.configure(background='white')
                    lfld10.place(x=550, y=550)

                    Backbutton1= Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                    Backbutton1.grid(column=2,row=0)    

                Backbutton=Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                Backbutton.grid(column=2,row=0)  

                EIDlabel= Label(root, text="Employee ID",font=('Times_New_Roman',15))
                EIDlabel.grid(row=1, column=0)
                EIDlabel.configure(background='white')
                EID = StringVar()
                EIDEntry = Entry(root, textvariable=EID)
                EIDEntry.grid(row=1, column=1,padx=5,pady=5,ipady=10)  
                EIDEntry.configure(background='white')

                Viewbutton=Button(root,text="View ",font=('Times_New_Roman',15),command=ViewEmpPage2)
                Viewbutton.grid(column=2,row=2)  

            EmpDetails=Button(root,text="View Employees",font=('Times_New_Roman',25),command=EmpDeetsView)
            EmpDetails.grid(column=1,row=2)    
            EmpDetails.configure(background='white')

            def Acc():
                EmpDetails.destroy()
                Accounting.destroy()
                button1.destroy()
                Rawbutton1.destroy()
                button3.destroy()
                ViewDetails.destroy()
                Logoutbutton.destroy()
                
                def Cancel():
                    MaxSal.destroy()
                    CancelButton.destroy()
                    THDetails.destroy()
                    TotDetails.destroy()
                    ManagerPage2()

                CancelButton=Button(root,text="Cancel ",font=('Times_New_Roman',15),command=Cancel)
                CancelButton.grid(column=0,row=0)    
                CancelButton.configure(background='white')    

                def MaxSalary():
                    MaxSal.destroy()
                    CancelButton.destroy()
                    THDetails.destroy()
                    TotDetails.destroy()


                    def Back():
                        lbl2.destroy()
                        lbl1.destroy()
                        lbl10.destroy()
                        lbl3.destroy()
                        lbl4.destroy()
                        lbl5.destroy()
                        lbl6.destroy()
                        lbl7.destroy()
                        lbl8.destroy()
                        lbl9.destroy()
                        Backbutton1.destroy()
                        Acc()

                    Backbutton1=Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                    Backbutton1.grid(column=0,row=0)    
                    Backbutton1.configure(background='white')    

                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    cur.execute("SELECT Dept_No, max(Salary) from EMPLOYEE group by "+ " Dept_No " )
                    output=cur.fetchall()
                    i=0
                    if (employee_id[0] != "A"):
                        output = ["N/A", "N/A", "N/A", "N/A"]
                        open_popup("Access denied")    
                    else:
                        for EMPLOYEE in cur: 
                            for j in range(len(EMPLOYEE)):
                                output = output[j] 
                            i=i+1    

                    connection.commit()
                    connection.close()

                    lbl1=Label(root, text="Department Number", fg='red', font=("Helvetica", 16))
                    lbl1.place(x=80, y=150)
                    lbl2=Label(root, text="Max Salary", fg='red', font=("Helvetica", 16))
                    lbl2.place(x=350, y=150)
                    lbl3=Label(root, text=output[0][0], fg='black', font=("Helvetica", 16))
                    lbl3.place(x=80, y=250)
                    lbl4=Label(root, text=output[1][0], fg='black', font=("Helvetica", 16))
                    lbl4.place(x=80, y=350)
                    lbl5=Label(root, text=output[2][0], fg='black', font=("Helvetica", 16))
                    lbl5.place(x=80, y=450)
                    lbl6=Label(root, text=output[3][0], fg='black', font=("Helvetica", 16))
                    lbl6.place(x=80, y=550)
                    lbl7=Label(root, text=output[0][1], fg='black', font=("Helvetica", 16))
                    lbl7.place(x=350, y=250)
                    lbl8=Label(root, text=output[1][1], fg='black', font=("Helvetica", 16))
                    lbl8.place(x=350, y=350)
                    lbl9=Label(root, text=output[2][1], fg='black', font=("Helvetica", 16))
                    lbl9.place(x=350, y=450)
                    lbl10=Label(root, text=output[3][1],fg='black', font=("Helvetica", 16))
                    lbl10.place(x=350, y=550)

                    



                MaxSal=Button(root,text="Max salary",font=('Times_New_Roman',25),command=MaxSalary)
                MaxSal.grid(column=2,row=2)    
                MaxSal.configure(background='white')
                
                def ThreeHighest():
                    THDetails.destroy()
                    CancelButton.destroy()
                    MaxSal.destroy()
                    TotDetails.destroy()

                    def Back():
                        for i in labels:
                            print("ea: " + str(i))
                            i.destroy()
                        # ea.destroy()
                        # e1.destroy()
                        # e2.destroy()
                        # e3.destroy()
                        # e4.destroy()
                        #e5.destroy()
                        Backbutton2.destroy()
                        Acc()
                       

                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    cur.execute("Select distinct salary,Fname,EID,Dept_No from EMPLOYEE a where 3 >= (select count(distinct salary) from EMPLOYEE b where a.Salary <= b.Salary) order by a.Salary desc;")
                    i=0
                    labels = []
                    if (employee_id[0] != "A"):
                        output = ["N/A", "N/A", "N/A", "N/A"]
                        open_popup("Access denied")  
                    else:
                        for EMPLOYEE in cur: 
                            for j in range(len(EMPLOYEE)):
                                ea = Label(root,width=25,font=('Times_New_roman',13), text=EMPLOYEE[j]) 
                                ea.grid(row=i+1, column=j) 
                                labels.append(ea)
                                e1=Label(root,width=10,font=('Times_New_roman',15),text='Salary',borderwidth=2, relief='ridge',anchor='w',bg='white')
                                e1.grid(row=0,column=0)
                                labels.append(e1)
                                e2=Label(root,width=10,font=('Times_New_roman',15),text='Name',borderwidth=2, relief='ridge',anchor='w',bg='white')
                                e2.grid(row=0,column=1)
                                labels.append(e2)
                                e3=Label(root,width=13,font=('Times_New_roman',15),text='Employee ID',borderwidth=2, relief='ridge',anchor='w',bg='white')
                                e3.grid(row=0,column=2)
                                labels.append(e3)
                                e4=Label(root,width=17,font=('Times_New_roman',15),text='Department Number',borderwidth=2, relief='ridge',anchor='w',bg='white')
                                e4.grid(row=0,column=3)
                                labels.append(e4)
                                #e.insert(END, student[j])
                            i=i+1

                        #e5 = Label(root,width=10, text=EMPLOYEE[j],borderwidth=2,relief='ridge', anchor="w")     
                    #output=cur.fetchall()
                    connection.commit()
                    connection.close()

                    Backbutton2=Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                    Backbutton2.grid(column=0,row=4)    
                    Backbutton2.configure(background='white') 

                THDetails=Button(root,text="Highest Salaries",font=('Times_New_Roman',25),command=ThreeHighest)
                THDetails.grid(column=1,row=2)    
                THDetails.configure(background='white')   

                def TotDeptSal():
                    THDetails.destroy()
                    CancelButton.destroy()
                    MaxSal.destroy()
                    TotDetails.destroy()

                    def Back():
                        #print("INSIDE BACK")
                        for i in labels:
                            print("ea: " + str(i))
                            i.destroy()
                        # ea.destroy()
                        #e5.destroy()
                        Backbutton3.destroy()
                        Acc()
                    connection=psycopg2.connect(user="postgres",
                            password="//",
                            host="127.0.0.1",
                            port="5432",
                            database="pharmacompany")
                    cur=connection.cursor()
                    cur.execute("Select Dept_No,sum(Salary) as TotalSal from EMPLOYEE GROUP BY Dept_No HAVING COUNT(EID)>2;")
                    i=0
                    labels = []
                    if (employee_id[0] != "A"):
                        output = ["N/A", "N/A", "N/A", "N/A"]
                        open_popup("Access denied")  
                    else:
                        for EMPLOYEE in cur: 
                            for j in range(len(EMPLOYEE)):
                                ea = Label(root,width=25,font=('Times_New_roman',13), text=EMPLOYEE[j]) 
                                ea.grid(row=i+1, column=j) 
                                labels.append(ea)
                                e1=Label(root,width=18,font=('Times_New_roman',15),text='Department Number',borderwidth=2, relief='ridge',anchor='w',bg='white')
                                e1.grid(row=0,column=0)
                                labels.append(e1)
                                e2=Label(root,width=15,font=('Times_New_roman',15),text='Total Salary',borderwidth=2, relief='ridge',anchor='w',bg='white')
                                e2.grid(row=0,column=1)
                                labels.append(e2)
                                
                                #e.insert(END, student[j])
                            i=i+1
                            # e5 = Label(root,width=10, text=EMPLOYEE[j],borderwidth=2,relief='ridge', anchor="w")

                    Backbutton3=Button(root,text="Back ",font=('Times_New_Roman',15),command=Back)
                    Backbutton3.grid(column=0,row=3)    
                    Backbutton3.configure(background='white')    

                TotDetails=Button(root,text="Total Salary",font=('Times_New_Roman',25),command=TotDeptSal)
                TotDetails.grid(column=0,row=2)    
                TotDetails.configure(background='white') 

            Accounting=Button(root,text="Accounting",font=('Times_New_Roman',25),command=Acc)
            Accounting.grid(column=2,row=2)    
            Accounting.configure(background='white')

            

            Logoutbutton=Button(root,text="Logout ",font=('Times_New_Roman',15),command=Logout)
            Logoutbutton.grid(column=0,row=0)    
            Logoutbutton.configure(background='white')


        Backbutton1=Button(root,text="Back ",font=('Times_New_Roman',15),command=backButton1)
        Backbutton1.grid(column=0,row=0)    
        Backbutton1.configure(background='white')

        usernameLabel = Label(root, text="Employee ID",font=('Times_New_Roman',15))
        usernameLabel.grid(row=1, column=0)
        usernameLabel.configure(background='white')
        username = StringVar()
        usernameEntry = Entry(root, textvariable=username)
        usernameEntry.grid(row=1, column=1,padx=5,pady=5,ipady=10)  
        usernameEntry.configure(background='white')

  #password label and password entry box
        passwordLabel = Label(root,text="Password",font=('Times_New_Roman',15))
        passwordLabel.grid(row=2, column=0) 
        passwordLabel.configure(background='white') 
        password = StringVar()
        IIDentry = Entry(root, textvariable=password, show='*')
        IIDentry.grid(row=2, column=1,padx=5,pady=5,ipady=10)
        IIDentry.configure(background='white') 
        Loginbutton=Button(root,text="Login ",font=('Times_New_Roman',25),command=ManagerPage2)
        Loginbutton.grid(column=2,row=2)
        Loginbutton.configure(background='white')    

    # logo=Image.open('icon.jpg')
    # logo=ImageTk.PhotoImage(logo)
    # logo_label=tk.Label(image=logo)
    # logo_label.image=logo
    # logo_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    button1=Button(root,text='Employee Login',font=('Times_New_Roman',25),command=EmployeeLogin)
    button1.place(relx=0.5, rely=0.5, anchor=CENTER)
    button1.configure(background='white')

    button2=Button(root,text="Manager Login",font=('Times_New_Roman',25),command=ManagerLogin)
    button2.place(relx=0.5, rely=0.65, anchor=CENTER)
    button2.configure(background='white')

    


PageOne()

root.mainloop()    