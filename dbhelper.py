# to import mysql.connector , we need to download pip install mysql.connector
import mysql.connector


class DBHelper:
    def __init__(self):

        # connect to the database
        # to connect we need the IP address where the database is,user name which is always root, password which is not fixed,database name
        # 127.0.0.1 is the IP Address of our own computer
        # we can either write host="127.0.0.1" or host="localhost"

        # try and except is used for error handling,if there is a error, a message is displayed instead of the code crashing
        # to check create an object like obj1=DBHelper() , to see whether it is successful or not
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="tinder")

            # cursor helps in interacting with the database
            self.mycursor = self.conn.cursor()
            print("Database connection successful")
        except:
            print("Not connected")

    def checkLogin(self, email, password):

        # perform login

        query = "SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email, password)
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()

        return data

    def loadOwnData(self, user_id):

        # perform login

        query = "SELECT * FROM users WHERE user_id ={}".format(user_id)
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()

        return data

    def performRegistration(self, name, email, password, age, gender, location, bio, dp):

        query = "INSERT INTO users (user_id,name,email,password,age,gender,location,bio,dp)VALUES(NULL,'{}','{}','{}',{},'{}','{}','{}','{}')".format(
            name, email, password, age, gender, location, bio,dp);

        try:

            self.mycursor.execute(query)

            # for write operation use commit

            self.conn.commit()
            return 1

        except:
            return 0

    def fetchOtherUsersData(self,user_id):

        query="SELECT * FROM users WHERE user_id NOT LIKE {}".format(user_id)

        self.mycursor.execute(query)
        data=self.mycursor.fetchall()
        return data

    def propose(self,sender_id,receiver_id):

        query="INSERT INTO proposals (proposal_id,sender_id,receiver_id) VALUES (NULL,{},{})".format(sender_id,receiver_id)

        try:
            response=self.relationshipExits(sender_id,receiver_id)
            if response==1:
                self.mycursor.execute(query)
                self.conn.commit()
                return 1
            else:
                return -1

        except:
            return 0
    def relationshipExits(self,sender_id,receiver_id):

        query= "SELECT * FROM proposals WHERE sender_id={} AND receiver_id={}".format(sender_id,receiver_id)

        self.mycursor.execute(query)
        data=self.mycursor.fetchall()

        if len(data)>0:
            return 0

        else:
            return 1


    def fetchProposals(self,sender_id):

        query="SELECT * FROM proposals p JOIN users u ON u.user_id=p.receiver_id WHERE p.sender_id={}".format(sender_id)

        self.mycursor.execute(query)
        data=self.mycursor.fetchall()



        return data

    def fetchRequests(self, receiver_id):

        query = "SELECT * FROM proposals p JOIN users u ON u.user_id=p.sender_id WHERE p.receiver_id={}".format(
            receiver_id)

        self.mycursor.execute(query)
        data = self.mycursor.fetchall()

        return data

    def fetchMatches(self, user_id):

        query = "SELECT * FROM proposals p JOIN users u ON u.user_id=p.sender_id WHERE p.sender_id IN (SELECT p.receiver_id FROM proposals p WHERE p.sender_id={}) AND p.receiver_id={}".format(user_id,user_id)

        self.mycursor.execute(query)
        data = self.mycursor.fetchall()

        return data

    def editProfile(self,age,location,bio,dp,user_id):

        query="UPDATE users SET age={},location='{}',bio='{}',dp='{}' WHERE user_id={}".format(age,location,bio,dp,user_id)
        print(query)

        try:
            self.mycursor.execute(query)
            self.conn.commit()
            return 1
        except:
            return  0






