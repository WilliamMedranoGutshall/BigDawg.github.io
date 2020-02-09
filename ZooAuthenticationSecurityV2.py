#************************************************
# BigDawg Zoo Authentication Application
#
# Author: William Medrano Gutshall
# IT 499
#************************************************

import hashlib #Needed to access the MD5 Hashing
jobMenuSelect = "Empty"
#Testing dictionary - all passwords are abcd to speed up testing - to use remove """ from this dictionary and move to actual dictionary
"""authenticationDict = {"Will": {"userPassword":"e2fc714c4727ee9395f324cd2e7f331f", "userJob":"Human Resources"}, 
                      "Michelle":{"userPassword":"e2fc714c4727ee9395f324cd2e7f331f", "userJob":"Zookeeper"},
                      "Briana":{"userPassword":"e2fc714c4727ee9395f324cd2e7f331f", "userJob":"Veterinarian"},
                      "Celina":{"userPassword":"e2fc714c4727ee9395f324cd2e7f331f", "userJob":"Administrator"},
                      "Mike":{"userPassword":"e2fc714c4727ee9395f324cd2e7f331f", "userJob":"Labor"}}"""
# Test Passwords are: Will W1ll, Michelle M1che!!e, Briana Br1@n@, Celina Ce!1n@, and Mike M!k3
authenticationDict = {"Will": {"userPassword":"8466ede3b496487a0fa8798e42f27b4c", "userJob":"Human Resources"}, 
                      "Michelle":{"userPassword":"17152a5a3dab5fed1ce9bba52b27bdcb", "userJob":"Zookeeper"},
                      "Briana":{"userPassword":"e9b6917b5c783b3a7d1c6650526541ae", "userJob":"Veterinarian"},
                      "Celina":{"userPassword":"77f2aa944838a0f793fbb418dd846a4e", "userJob":"Administrator"},
                      "Mike":{"userPassword":"62287d8863f49abd304a5991abbf4d75", "userJob":"Labor"}}     

#************Hashing*******************************
#User Name Storage
def hashingMethod(passwordToHash):
    hashedPassWord = hashlib.md5(passwordToHash.encode())
    hashedPassWordHex = hashedPassWord.hexdigest()
    return hashedPassWordHex
#****************************************************************************

#*************Staff Menus by job title****************************************
#Menu for Zookeeper
def staffZooKeeper(displayName):
    """Provides the menu options for a user that is assigned the zookeeper job title."""
    jobMenuSelect = "Empty"         
    try:
        while jobMenuSelect is not "l":
            print("\nWelcome Zookeeper", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print(displayName, "your daily duties include:\nChecking on the animals.")
                print("Reporting abnormalities to veterinarian staff.\nFeeding the animals.")
                print("Cleaning the animal enclosures.\n")
    except:     #For Error Handling
        print("Error occured during menu selection.\nPlease restart program.")   
    return

#Menu for Veterinarian
def staffVet(displayName):
    """Provides the menu options for a user that is assigned the veterinarian job title."""
    jobMenuSelect = "Empty"
    try:
        while jobMenuSelect is not "l":
            print("\nWelcome Veterinarian", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print(displayName, "your daily duties include:\nPerforming wellness checks.")
                print("Treating sick or injured animals.\nGuiding the zookeepers on nutritional needs of the animals.")
                print("Filling out all medical records for animals treated.\n")
    except:        #For Error Handling
        print("Error occured during menu selection.\nPlease restart program.")
    return

#Menu for Staff Administrator
def staffAdmin(displayName):
    """Provides the menu options for a user that is assigned the administrator title."""
    jobMenuSelect = "Empty"
    try:
        while jobMenuSelect is not "l":
            print("\nWelcome Administrator", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print(displayName, "your daily duties include:\nCoordinating daily activities of all the staff.")
                print("Procurement of zoo supplies.\nProviding financial information to accounting.")
                print("Customer service issue resolutions.\n")
    except:   #For Error Handling
        print("Error occured during menu selection.\nPlease restart program.")
    return

#Menu for HR Administrator
def staffAdminHR(displayName):
    """Provides the menu options for a user that is assigned the job title of Human Resource Administrator."""
    jobMenuSelect = "Empty"
    try:
        while jobMenuSelect is not "l":
            print("\nWelcome Human Resource administrator", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print(displayName, "your daily duties include:\nMonitor staffing requirements.")
                print("Discipline employees as needed.\nHire high quality staff to provide best guest experience.")
                print("Maintain employee records in zoo system.\n")
    except:
        print("Error occured during menu selection.\nPlease restart program.")
    return

#Menu for General Labor Staff
def staffWorker(displayName):
    """Provides the menu options for a user that is assigned the Labor job title."""
    jobMenuSelect = "Empty"
    try:
        while jobMenuSelect is not "l":
            print("\nWelcome Staff Memeber", displayName)
            jobMenuSelect = input("\n\nPlease choose a menu option:\nl - Logoff\nd - Display your daily duties\n")
            while (jobMenuSelect is not "l") and (jobMenuSelect is not "d"):
                jobMenuSelect = input("\n\nPlease Try Again:\nl - Logoff\nd - Display your daily duties\n")
            if jobMenuSelect is "d":
                print(displayName, "your daily duties include:\nEnsure that work area is clean and ready to be opened on time.")
                print("Assist guests as needed.\nProvide feedback to supervisor on improving customer experience.")
                print("Make sure area is cleaned up before clocking out for the day.\n")
    except:
        print("Error occured during menu selection.\nPlease restart program.")
    return
#*****************************************************************


#**********Main Program*******************************************
def main():
    """Main method that includes the main menu for authentication."""
    #Variable definitions for main program
    userNameIn = "Empty"
    passWordIn = "Empty"
    authenticationCounter = 0
    userJob = "Empty"
    dictPassword = " "
    dictJob = " "
    
    while authenticationCounter <= 3:
        try:
            print ("Welcome to the BigDawg Zoo of San Antonio\n")             
            #User Entry Block
            userNameIn = input("Please Enter Your User Name to Continue\nOr type Exit to Shutdown Application")
            while len(userNameIn) > 10:                   #Used to prevent buffer overflow attacks 
                try:
                    userNameIn = input("Sorry, usernames are 10 characters or less.\nPlease Enter Your User Name to Continue\nOr type Exit to Shutdown Application")
                except:
                    print("Error occured during input collection.\nPlease restart program.")
            #Allows user to end program
            if userNameIn == "exit" or userNameIn == "Exit":
                break            
            if userNameIn in authenticationDict:
                print("Welcome to BigDawgZoo ", userNameIn)
                passWordIn = input("\nPlease provide your password")
                while (len(passWordIn) < 4) or (len(passWordIn) > 10): #Prevents too small of passwords and buffer overflow attacks from too long on input
                    try:
                        passWordIn = input("Sorry, passwords are between 4 and 10 characters.\nPlease Enter Your Password to Continue")
                    except:
                        print("Error occured during input collection.\nPlease restart program.")
                dictPassword = authenticationDict[userNameIn]["userPassword"]    
                dictJob = authenticationDict[userNameIn]["userJob"]
                passwordHashed = hashingMethod(passWordIn)
                if (passwordHashed == dictPassword):
                    authenticationCounter = 0
                    userJob = dictJob
                    if userJob == "Zookeeper":
                        staffZooKeeper(userNameIn)
                    elif userJob == "Veterinarian":
                        staffVet(userNameIn)
                    elif userJob == "Administrator":
                        staffAdmin(userNameIn)
                    elif userJob == "Human Resources":
                        staffAdminHR(userNameIn)
                    elif userJob == "Labor":
                        staffWorker(userNameIn)
                    else:
                        print("\nI'm sorry. The system is unable to resolve your current position.")
                        print("\nPlease see your administrator to resolve this issue.")                               
                else:
                    print("\n\n\n")
                    print("Sorry, This is not the correct pasword, please try again.") 
                    authenticationCounter = authenticationCounter + 1
                    print("Attempt ", authenticationCounter, " of 3")
                    if authenticationCounter == 3:
                        break
                    print("\nPlease try again or contact your admin for assistance.\n\n")       
            else:
                print("\n\n\n")
                print("Sorry, This is not a valid user, please try again.")   
                authenticationCounter = authenticationCounter + 1
                print("Attempt ", authenticationCounter, " of 3")
                if authenticationCounter == 3:
                    break
                print("\nPlease try again or contact your admin for assistance.\n\n")          
        except:
            print("Error occured.\nPlease restart program.")
            
    print("\nHave a Great Day\n")
  
#**********************************************************************************          
        
    
    



main()