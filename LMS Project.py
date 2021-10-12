import datetime
# import os
# os.getcwd()

class LMS:
    """This class is used to keep record of books library"""
    """It has total four module :"Display Books","Issue Books","Add Books" """
    def __init__(self,List_of_books,library_name):
        self.List_of_books="List_of_books.txt" ## This is module to create in the LMS File project which located in pycharm in main folder
        ## We need to define library name
        self.library_name=library_name
        self.books_dict={} # Information all about books name ,render name in this
        Id= 101  # THis is id of book ,start from this id

        """Now How we can read the file so that we  have to create the file handling  then we can read all books title which present in the module """
        with open(self.List_of_books) as bk: 
            content=bk.readlines()
            # Now I want to read each line so for that i have to apply the loop
            for line in content:
                """ Now using this line  i will update this books dictionary """
                self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
                "lender_name":"","Issue_data":"","Status":"Available"}})
                Id=Id + 1
                """Now show the books dictionary"""
    """Now we have to create another function for the display books"""

    def display_books(self):
        print("------------------------List of Books-----------------------")
        print("Books ID", "\t", "Title")
        print("------------------------------------------------------------")

        """Now I want kay of dictionary and value of dictioary , So Now ,"""

        for key, value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"-[",value.get("Status"),"]")

        """Now how we can Issue the books So that we have to  create new one fucntion"""

    """ Function for issuing Books"""
    def Issue_books(self):
        books_id=input("Enter the book ID : ")
        current_date=datetime.datetime.now().strftime("%Y-%m %d %H:%M:%S")
        if books_id in self.books_dict.keys() :#and not self.books_dict[books_id]["Status"] == "Available":
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"This books is already issued to {self.books_dict[books_id]['Student_name']} \
                    on {self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books() # In case books is not avaible
            elif self.books_dict[books_id]['Status']=="Available":
                your_name = input("Enter the Student name: ")
                self. books_dict[books_id]["Student_name"] = your_name
                self.books_dict[books_id]["Issue_date"] = current_date


                self.books_dict[books_id]["Status"]="Already Issued" #"""if books is availble then we need to change status"""
                print("Books Issued Succesfully !!!!! \n")
            else:
                print("Books ID not found!!!")
                return self.Issue_books()


    """ Now further is Add a book """

    def add_books(self):
        new_books = input("Enter books title: ")
        if new_books== "":
            return self.add_books()

        elif len(new_books) > 25 :
            print("Books title is too long!!!!! Title lenght lenght should be 20 chars")
            return self.add_books()

        else:
            with open(self.List_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1) :{'books_title':new_books,'Student_name':"",
                'Issue_date':"",'Status':"Available"}})
                print(f"\nThis books'{new_books}' has been added successfully!!!!!\n")
    def return_books(self):
        books_id = input("Enter the books ID:")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"]=="Available":
                print("This book is already avaiilable in library. Please check your book ID")
                return self.return_books()  ### cheeck the return the fuction
            elif not self.books_dict[books_id]["Status"]=="Available":
                self.books_dict[books_id]["Student_name"]=""
                self.books_dict[books_id]["Issue_date"]=""
                # self.books_dict[books_id]["Status"]="Available"
                print("Successfully Updated !!!! \n")
            else:
                print("Book Id not found")
                """how we can run this application"""

try:
    myLMS=LMS("List_of_books","Python's")
    press_key_list  = {"D": "Dispaly Books","I":"Issue Books","A":"Add Books","R":"Return Book","Q":"Quite"}
    key_press= False
    while not (key_press =="q"):
        print(f"\n-----------------Welcome To {myLMS.library_name} Library management System----------- \n")
        for key,value in press_key_list.items():
            print("Press",key,"To",value)
        key_press=input("Press Key:").lower()
        if key_press =="i":
            print("\nCureent selection :issue books\n")
            myLMS.Issue_books()
        elif key_press == "a":
            print("\nCurrent Selection : Add Book\n")
            myLMS.add_books()
        elif key_press =="d":
            print("\nCurrent Selection : Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection : Return Books\n")
            myLMS.return_books()
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
    print("Something went Wrong . Please check input!!!!!!!")




        # file=open(self.List_of_books)
        # data=file.readlines()
        # print(data)
        #
l= LMS("List_of_books.txt","Python's Library") # This is for the instatiated the Class of LMS
print(l.display_books())

"""
In this project we use the :
OOPS Method
Function
File Handling
Data Structure
Control Structure
Looping Concept
Specific Keys
"""



#
# import pyttsx3
# import PyPDF2
# book=open("Basic german.pdf","rb")
#
# pdfReader=PyPDF2#..`...PdfFileReader(book)
# pages=pdfReader. ## numPages means number of pages
# print(pages)
# speaker=pyttsx3.init()  ## init means initialization to speak
# page=pdfReader.getPage(18) #getpafe means starting reading page
# text=page.extractText() # extractText means extarct the text from pdf
# speaker.say(text)
# speaker.runAndWait()
# speaker=pyttsx3.init()
# speaker.say("""Ich heiße Hans Homann. → Er heißt Hans Homann.
# 2 Ich komme aus Wien.
# 3 Ich arbeite für das Österreichische Fernsehen.
# 4 Ich spreche natürlich Deutsch, aber auch Englisch und Spanisch.
# 5 Ich lese gern Kriminalromane.
# 6 Ich fahre auch gern Ski und schwimme viel.
# 7 Ich sehe gern alte Filme mit Marlene Dietrich.
# 8 Ich schlafe oft lange.
# 9 Ich reise gern.
# 10 Und ich helfe am Wochenende alten Leutend
#  """)
# speaker.runAndWait()