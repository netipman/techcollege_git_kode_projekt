#Import of the libary mysql to use mysql commands
import mysql.connector
#Connection to the mySQL and the database
db = mysql.connector.connect(host="localhost", user="root", passwd="Test1234!", database="webrus")
mycur = db.cursor()


#Function to login site
def login():
    #While loop to loop if user don't type anything.
    while True:
        print("Login!")
        print("Skriv dit navn: ")
        user_varify = input()
        print("Skriv din kode: ")
        pas_varify = input()
        #Asking the user to put in username and password
        if len(pas_varify) and len(user_varify) != 0:
            #If statement - If the user typed something in the inputs, run this
            sql = "select * from users where username = %s and password = %s"
            #Select statement in mysql to get all from the table users where username and password equals the inputs typed by the user
            mycur.execute(sql, [(user_varify), (pas_varify)])
            #This executes the mysql statement
            results = mycur.fetchall()
            if results:
                #If the user typed in a valid name and password, they will be logged in
                for i in results:
                    print("Velkommen,", user_varify)
                #Break the while loop because the user logged in with all correct information
                input("Tryk enter for at lukke")
                break
            else:
                #Else statement - The user hasn't typed some valid information
                print("Forkert brugernavn eller kodeord")
        else:
            #Else statement - The user didn't type anything to the inputs and will be promnped to do it over and over
            print("Indtast brugernavn eller kodeord")


#Function to create user
def register():
    #While loop to make sure the user types something in the inputs
    while True:
        print("Skriv dit nye brugernavn: ")
        username_info = input()
        #If the user has typed something in the input run the if statement
        if len(username_info) != 0:
            query = "SELECT * FROM users WHERE username = %s"
            #Select all data from the table users where username in the table equals the input typed by the user
            value = (username_info)
            mycur.execute(query, (value,))
            myresult = mycur.fetchall()
            if myresult:
                print("Brugeren findes allerede")
                #If the username already exists in the database, the user has to type in a new username and because of the while loop it will ask again
            else:
                print("Indtast dit nye kodeord")
                password_info = input()
                #If username dosen't exists the user will be prompted to enter a password
                if len(password_info) != 0:
                    #If statement to make sure that the user types in password and not null
                    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
                    val = (username_info, password_info)
                    mycur.execute(sql, val)
                    db.commit()
                    #Runs the sql statement - Inserting into table users the values of username and password the user typed in input
                    print("Din bruger er oprettet med brugernavnet", username_info)
                    login()
                    break
                    #Printing that the user has been created and breaking til while loop
                else:
                    print("Indtast et kodeord!")
        else:
            print("Indtast et brugernavn")


#The start of the script - User has to choose between login or register user - 1 or 2
print("Velkommen til webRus")
while True:
    print("Venligst vælg, om du vil logge ind eller registrere en konto: ")
    print("1. Login")
    print("2. Registrer en bruger")

    userinput = input()
    #If the user types 1 in the input, they will get the function login and if they type 2 they will get the function register
    if userinput == "1":
        login()
        break
    elif userinput == "2":
        register()
        break
    else:
        print("Indtast enten 1 eller 2 - IKKE NOGET ANDET!")