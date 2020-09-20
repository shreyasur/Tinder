from tkinter import *
from dbhelper import DBHelper
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
import shutil,os
from tkinter import ttk


class Tinder:

    def __init__(self):

        # when the file is run,the constructor of DBHelper is called , and the file gets connected to database
        self.db = DBHelper()
        self.constructGUI()




    def constructGUI(self):
        self.root = Tk()

        self.root.title("Tinder")
        self.root.minsize(350, 550)
        self.root.maxsize(350, 550)

        self.root.configure(background="#FF655B")
        self.root.iconbitmap(r'C:\Users\acer\Downloads\tinderlogo.ico')

        self.loadloginGUI()
        self.root.mainloop()


    def loadloginGUI(self):

        self.clear()

        self.title = Label(self.root, text="Tinder", bg="#FF655B", fg="#fff")
        self.title.configure(font=("Sans serif", 30, "italic"))
        self.title.pack(pady=(30, 30))

        self.title2 = Label(self.root, text="Kindly Login to proceed", bg="#FF655B", fg="#fff")
        self.title2.configure(font=("Sans serif", 18, "bold"))
        self.title2.pack(pady=(5, 20))

        self.frame1 = Frame(self.root)
        self.frame1.pack(pady=(5, 15))

        self.emailLabel = Label(self.frame1, text=" Enter email", bg="#FF655B", fg="#fff")
        self.emailLabel.configure(font=("Times", 14))
        self.emailLabel.pack(side=LEFT)

        self.emailInput = Entry(self.frame1)
        self.emailInput.pack(side=RIGHT, ipady=5, ipadx=20)

        self.frame2 = Frame(self.root)
        self.frame2.pack(pady=(5, 15))

        self.passwordLabel = Label(self.frame2, text=" Enter Password", bg="#FF655B", fg="#fff")
        self.passwordLabel.configure(font=("Times", 14))
        self.passwordLabel.pack(side=LEFT)

        self.passwordInput = Entry(self.frame2)
        self.passwordInput.pack(side=RIGHT, ipady=5, ipadx=20)

        self.login = Button(self.root, text="Login", bg="#fff", fg="#000", width=20, height=2,
                            command=lambda: self.doLogin())
        self.login.pack(pady=(10, 15))

        self.title3 = Label(self.root, text="Not a member Yet? Sign Up now", bg="#FF655B", fg="#fff")
        self.title3.pack(pady=(5, 10))

        self.register = Button(self.root, text="Sign Up ", bg="#fff", fg="#000", command=lambda: self.loadRegisterGUI())
        self.register.pack()

    def loadRegisterGUI(self):

        self.clear()

        self.title = Label(self.root, text="Tinder", bg="#FF655B", fg="#fff")
        self.title.configure(font=("Sans serif", 30, "italic"))
        self.title.pack(pady=(10, 10))

        self.nameLabel = Label(self.root, text="Enter Name", bg="#FF655B", fg="#fff")
        self.nameLabel.pack()

        self.nameInput = Entry(self.root)
        self.nameInput.pack()

        self.emailLabel = Label(self.root, text="Enter email", bg="#FF655B", fg="#fff")
        self.emailLabel.pack()

        self.emailInput = Entry(self.root)
        self.emailInput.pack()

        self.passwordLabel = Label(self.root, text="Enter Password", bg="#FF655B", fg="#fff")
        self.passwordLabel.pack()

        self.passwordInput = Entry(self.root)
        self.passwordInput.pack()

        self.ageLabel = Label(self.root, text="Enter Age", bg="#FF655B", fg="#fff")
        self.ageLabel.pack()

        self.ageInput = Entry(self.root)
        self.ageInput.pack()

        self.genderLabel = Label(self.root, text="Enter Gender", bg="#FF655B", fg="#fff")
        self.genderLabel.pack()

        self.genderInput = Entry(self.root)
        self.genderInput.pack()

        self.locationLabel = Label(self.root, text="Enter Location", bg="#FF655B", fg="#fff")
        self.locationLabel.pack()

        self.locationInput = Entry(self.root)
        self.locationInput.pack()

        self.bioLabel = Label(self.root, text="Enter Bio", bg="#FF655B", fg="#fff")
        self.bioLabel.pack()

        self.bioInput = Entry(self.root)
        self.bioInput.pack()

        #self.dpLabel = Label(self.root, text="Upload Dp", bg="#E7497C", fg="#fff")
        #self.dpLabel.pack()

        #self.dpInput = Entry(self.root)
        #self.dpInput.pack()

        self.register = Button(self.root, text="Register", bg="#fff", fg="#000", command=lambda: self.doRegister())
        self.register.pack(pady=(10, 10))

        self.frame = Frame(self.root)
        self.frame.pack(pady=(10))

        self.message = Label(self.frame, text="Go Back To Login", bg="#FF655B", fg="#fff")
        self.message.pack(side=LEFT)

        self.loginBtn = Button(self.frame, text="Login", command=lambda: self.loadloginGUI())
        self.loginBtn.pack(side=RIGHT)

    def doRegister(self):

        name = self.nameInput.get()
        email = self.emailInput.get()
        password = self.passwordInput.get()
        age = self.ageInput.get()
        gender = self.genderInput.get()
        location = self.locationInput.get()
        bio = self.bioInput.get()
        #dp = self.dpInput.get()

        # call dbhelper

        response = self.db.performRegistration(name, email, password, age, gender, location, bio, "avatar2.png")

        if (response == 1):
            messagebox.showinfo("Registration Successful", "Completed!")

        else:
            messagebox.showerror("Error", "Failed!")

    def doLogin(self):

        email = self.emailInput.get()
        password = self.passwordInput.get()

        # send this data to the database and check if the user exists or notp

        self.data = self.db.checkLogin(email, password)
        if len(self.data) > 0:

            self.user_id=self.data[0][0]

            # print the GUI
            self.loadUserProfile(self.data)


        else:
            messagebox.showinfo("Error", "Incorrect Credentials")

    def loadUserProfile(self,data):

        self.userProfileGUI(data)

    def clear(self):

        for i in self.root.pack_slaves():
            i.destroy()

    def headerMenu(self):

        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile",command=lambda :self.loadOwnProfile())
        filemenu.add_command(label="Edit Profile",command = lambda : self.loadEditProfileGUI())
        filemenu.add_command(label="View Profile",command = lambda : self.fetchOtherUsersData())
        filemenu.add_command(label="LogOut", command=lambda: self.logout())

        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals",command= lambda : self.showProposals())
        helpmenu.add_command(label="My Requests",command= lambda : self.showRequests())
        helpmenu.add_command(label="My Matches",command= lambda : self.showMatches())

    def loadOwnProfile(self):

        data=self.db.loadOwnData(self.user_id)
        self.loadUserProfile(data)


    def loadEditProfileGUI(self):

        self.clear()

        self.title = Label(self.root, text="Tinder", bg="#FF655B", fg="#fff")
        self.title.configure(font=("Sans serif", 30, "italic"))
        self.title.pack(pady=(10, 10))

        self.ageLabel = Label(self.root, text="Edit Age", bg="#FF655B", fg="#fff")
        self.ageLabel.pack()

        self.ageInput = Entry(self.root)
        self.ageInput.pack()

        self.locationLabel = Label(self.root, text="Edit Location", bg="#FF655B", fg="#fff")
        self.locationLabel.pack()

        self.locationInput= Entry(self.root)
        self.locationInput.pack()

        self.bioLabel = Label(self.root, text="Edit Bio", bg="#FF655B", fg="#fff")
        self.bioLabel.pack()

        self.bioInput = Entry(self.root)
        self.bioInput.pack()

        self.fileInput=Button(self.root,text="Change Profile Picture",command=lambda:self.uploadFile())
        self.fileInput.pack(pady=(5,5))

        self.filename=Label(self.root)
        self.filename.pack(pady=(5,5))

        self.editBtn = Button(self.root, text="Edit Profile", command=lambda: self.editProfile())
        self.editBtn.pack()

    def uploadFile(self):

        self.pathname=filedialog.askopenfilename(initialdir="/images",title="Something")
        self.filename['text']=self.pathname

    def editProfile(self):

        age=self.ageInput.get()
        location = self.locationInput.get()
        bio= self.bioInput.get()
        actual_filename=self.pathname.split("/")[-1]
        response=self.db.editProfile(age,location,bio,actual_filename,self.user_id)

        if response==1:
            destination="C:\\Users\\acer\\PycharmProjects\\tinder\\images\\" + self.pathname.split("/")[-1]
            shutil.copyfile(self.pathname,destination)

            messagebox.showinfo("Success","Profile edited successfully")

        else:
            messagebox.showerror("Error","Some error occurred")










    def showProposals(self):

      data=self.db.fetchProposals(self.user_id)

      new_data=[]

      for i in data:

          i=i[3:]
          new_data.append((i))



      self.userProfileGUI(new_data,mode=3)

    def showRequests(self):

        data = self.db.fetchRequests(self.user_id)

        new_data = []

        for i in data:
            i = i[3:]
            new_data.append((i))

        self.userProfileGUI(new_data, mode=3)

    def showMatches(self):

        data = self.db.fetchMatches(self.user_id)

        new_data = []

        for i in data:
            i = i[3:]
            new_data.append((i))

        self.userProfileGUI(new_data, mode=3)



    # mode is used here so that the next prvious propose button isn't displayed in the logged in users page

    def userProfileGUI(self, data,mode=1,index=0):

        self.clear()

        self.headerMenu()

         #Image (For later)

        imageUrl = "images/{}".format(data[index][-1])

        load = Image.open(imageUrl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack()

        # 1. Name
        self.nameLabel = Label(self.root, text=data[index][1], bg="#FF655B", fg="#fff")
        self.nameLabel.configure(font=("Times", 18))
        self.nameLabel.pack(pady=(30, 15))

        self.frame = Frame(self.root)
        self.frame.pack(pady=(2, 20))
        # 2. Age
        self.ageLabel = Label(self.frame, text=str(data[index][4]) + " years old", bg="#FF655B", fg="#fff")
        self.ageLabel.configure(font=("Times", 18))
        self.ageLabel.pack(side=LEFT)
        # 3. Gender
        self.genderLabel = Label(self.frame, text=str(data[index][5]), bg="#FF655B", fg="#fff")
        self.genderLabel.configure(font=("Times", 18))
        self.genderLabel.pack(side=LEFT)
        # 4. Location
        self.locationLabel = Label(self.frame, text=" from " + str(data[index][6]), bg="#FF655B", fg="#fff")
        self.locationLabel.configure(font=("Times", 18))
        self.locationLabel.pack(side=LEFT)

        if mode==2:
            self.frame2 = Frame(self.root)
            self.frame2.pack(pady=(20, 20))

            self.previous = Button(self.frame2, text="Previous",command=lambda : self.viewOtherUsers(data,index,invoker=2,mode=2))
            self.previous.pack(side=LEFT)

            self.propose = Button(self.frame2, text="Propose",command= lambda:self.proposeUser(data[index][0]))
            self.propose.pack(side=LEFT)

            self.next = Button(self.frame2, text="Next",command=lambda : self.viewOtherUsers(data,index,invoker=1,mode=2))
            self.next.pack(side=RIGHT)

        # Edit Profile button

        if mode==3:

                self.frame2 = Frame(self.root)
                self.frame2.pack(pady=(20, 20))

                self.previous = Button(self.frame2, text="Previous",
                                       command=lambda: self.viewOtherUsers(data, index, invoker=2,mode=3))
                self.previous.pack(side=LEFT)


                self.next = Button(self.frame2, text="Next",
                                   command=lambda: self.viewOtherUsers(data, index, invoker=1,mode=3))
                self.next.pack(side=RIGHT)

            # Edit Profile button

    def proposeUser(self,receiver_id):

        sender_id=self.user_id
        receiver_id=receiver_id

        response=self.db.propose(sender_id,receiver_id)

        if response==1:
            messagebox.showinfo("Proposal Sent","Fingers Crossed")

        elif response==-1:
            messagebox.showerror("Already Proposed","Proposal can't be sent more than once")

        else:
            messagebox.showerror("Error","Some Error Occured")

    def logout(self):

        self.root.destroy()
        self.constructGUI()


    def fetchOtherUsersData(self):

        #fetch data of all the other users except the logged in user

        data= self.db.fetchOtherUsersData(self.user_id)

        self.viewOtherUsers(data,index=-1,mode=2)

        

    def viewOtherUsers(self,data,index=0,invoker=0,mode=0):

        if invoker == 1:

            if (index == len(data) - 1):
                self.userProfileGUI(data, mode=mode, index=0)
            else:
                self.userProfileGUI(data, mode=mode, index=index + 1)
        elif invoker==2:

            if (index == 0):
                self.userProfileGUI(data, mode=mode, index=len(data)-1)
            else:
                self.userProfileGUI(data, mode=mode, index=index - 1)

        else:

            self.userProfileGUI(data, mode=2, index=0)







obj = Tinder()
