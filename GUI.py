
#-----------------------------------------
#--------------MAIN PROGRAMM--------------
#-----------------------------------------
from tkinter import filedialog
from tkinter import *
import os
import sys
import shutil
import filecmp
import time
HEIGHT = 700
WIDTH = 800


TEXT = ""
FileDir = ""
TestsFolderDir = ""




root = Tk()

#-------------------------------
#--------------GUI--------------
#-------------------------------

def get_tests_dir (arg):
	# root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	global TestsFolderDir 
	TestsFolderDir = filedialog.askdirectory()
	SetTests(TestsFolderDir)
	# print(TestsFolderDir)


def get_file_location(arg):
	global FileDir 
	FileDir = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Pascal files","*.pas"),("all files","*.*")))
	SetDir(FileDir)
	# print(pas_file_location)


canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.place(relx = 0.1, rely = 0.1)


#-------------------------------
#--------FILE DIRECTION---------
#-------------------------------

fr1 = Frame(root, bg = "#4e5ca0", bd = 1, width = 300, height = 150)
fr1.grid(row = 0, column = 0)
# fr1.pack(side = LEFT)

NameText = Label(fr1, text = "Enter the direction of file:", fg = "#2473f2")
NameText.place(relx = 0.1, rely = 0.1, width = 150)

NameEntry = Entry(fr1, bd = 1, fg = "#2473f2")
NameEntry.place(relx = 0.1, rely = 0.25, width = 150)

def SetDir(arg):
	global NameEntry
	NameEntry.insert(0, arg)

DirFileBtn = Button(fr1, text = "...", bg = "#c2d8f9", font = "arial 14")
DirFileBtn.place(relx = 0.61, rely = 0.25, width = 30, height = 20)
DirFileBtn.bind("<Button-1>", get_file_location)



NameEntry.insert(0, TEXT)
#-------------------------------
#--------COUNT OF TESTS---------
#-------------------------------

fr2 = Frame(root, bg = "#4e5ca0", bd = 5, width = 300, height = 150)
fr2.grid(row = 0, column = 1)
#fr2.pack(side = "top")

CountText = Label(fr2, text = "Enter count of tests:", fg = "#2473f2")
CountText.place(relx = 0.1, rely = 0.1, width = 150)

CountEntry = Entry(fr2, bd = 1)
CountEntry.place(relx = 0.1, rely = 0.25, width = 150)

#-------------------------------
#--------TESTS DIRECTION--------
#-------------------------------

fr3 = Frame(root, bg = "#4e5ca0", bd = 0, width = 300, height = 150)
fr3.grid(row = 0, column = 2)
#fr3.pack(side = "top")

DirText = Label(fr3, text = "Enter the direction of tests:", fg = "#2473f2")
DirText.place(relx = 0.1, rely = 0.1, width = 150)

DirEntry = Entry(fr3, bd = 1)
DirEntry.place(relx = 0.1, rely = 0.25, width = 150)

def SetTests(arg):
	DirEntry.insert(0, arg)

DirTestsBtn = Button(fr3, text = "...", bg = "#c2d8f9", font = "arial 14")
DirTestsBtn.place(relx = 0.61, rely = 0.25, width = 30, height = 20)
DirTestsBtn.bind("<Button-1>", get_tests_dir)

# 

# print(root.filename)

#-------------------------------
#--------ACCEPT LOGIC-----------
#-------------------------------

def accept(arg):
	FN = NameEntry.get()    #File Dir
	TD = DirEntry.get()		#Tests Dir
	CT = CountEntry.get()	#Count of Tests
	if FN == "" or TD == "" or CT == "":
		print("Enter all arguments!")
	else:
		print("FileDir: " + str(FN))
		# print("TestsFolderDir: " + str(TD))
		# print("Count of tests: " + str(CT))
		

		filename = FN.split('/')[-1].split(".")[0]
		print(filename)
		direct = NameEntry

		out = open('../answer.txt',"w")
		os.system('fpc ' + FN)
		NFN = FN.replace(".pas",".exe")
		shutil.copyfile(NFN, TD + filename + '.exe')
		a = []
		try:
		    os.remove(TD + '/input.txt')
		except:
		    k = 0
		for i in range(1, int(CT) + 1):
		    if i <=9:
		        num = '0' + str(i)
		    else:
		       num = str(i)
		    print('TD = '+TD)   
		    command = TD + '/' + num
		    os.rename(command, TD + '/input.txt')
		    os.system('start /min ' + TD + filename + '.exe')
		    time.sleep(0.1)
		    os.rename(TD + '/input.txt', command)
		    
		    com = 'FC ' + command + '.a output.txt'
		    
		    if os.system(com) == 0:
		        print(num, '+', command + '.a')
		        a.append(True)
		    else:
		        print(num, '-', command)
		        a.append(False)

		print("Файли, що не пройшли перевірку:", file = out)
		for x in a:
		    k+=1
		    if x == False:
		        out.write(str(k)+"\n")
		k = 0
		out.close()
"""
		try:
		    os.remove('../prog/' + filename + '.o')
		    os.remove('../prog/' + filename + '.exe')
		    os.remove('../tests/' + filename + '.exe')
		#    os.remove('../tests/output.txt')
		except:
		    k = 0
		#filecmp.cmp(command + '.a' , 'output.txt', shallow=False)
"""

# C:/Users/Pk/Desktop/programming/Python/checker/qwe/q.pas
# C:/Users/Pk/Desktop/programming/Python/checker/tests
AcceptBtn = Button(root, text = "Accept", bg = "#c2d8f9")
AcceptBtn.place(relx = 0.8, rely = 0.5)
AcceptBtn.bind("<Button-1>", accept)

root.mainloop()


#-----------------------------------------
#--------------MAIN PROGRAMM--------------
#-----------------------------------------