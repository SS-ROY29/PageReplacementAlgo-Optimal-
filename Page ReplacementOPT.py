import random #Imports a random module for randomly generated pages
from tkinter import * #Imports a GUI to use

def Optimal_Page_Replacement(Pages, Frame_Count, OutputTxt):
    Frames = []
    Page_Faults = 0
    OutputTxt.delete("1.0", END)

    #iterates every page to add onto frames
    for i in range(len(Pages)):
        Page = Pages[i]

        #To prevent the same page content to insert in the frame
        if Page not in Frames:
            if len(Frames) < Frame_Count:
                Frames.append(Page)
            else:
                # Look ahead to decide which page to replace
                Future = Pages[i+1:]
                index_list = []

                for Frame_Page in Frames:
                    if Frame_Page in Future:
                        index_list.append(Future.index(Frame_Page))
                    else:
                        # Makes it so it Will not be used again
                        index_list.append(float('inf')) 

                # Replace the page with the farthest next use
                farthest = index_list.index(max(index_list))
                Frames[farthest] = Page

            Page_Faults += 1

        OutputTxt.insert(END, f"Page: {Page} -> Frames: {Frames}\n")

    OutputTxt.insert(END, f"\nTotal Page Faults: {Page_Faults}\n")

#Function to make the randomly Generated Pages
def GeneratePages(MaxPages, Pages): 
    
    for i in range(MaxPages): #The code will randomly generate 10 numbers in logical memory
        Pages.append(random.randint(0,9))
    return Pages

# main code
MaxPages=10
Pages = []
Frame_Count = 3

#Initialize the GUI
Window = Tk()
Window.title("Least Recently Used")
Window.geometry("500x500")

#Frame for the GUI
Frame1 = Frame(Window, width=300, height=300)
Frame1.grid(row=0, column=0)

#Text to show the output of the program
OutputTxt = Text(Window, width= 60, height=20)
OutputTxt.place(relx=0.5, rely=0.6, anchor=CENTER)

#Functions used to make the program
GeneratePages(MaxPages, Pages)
Optimal_Page_Replacement(Pages, Frame_Count, OutputTxt)

#Label to show the pages contained in the memory
RandomNumLbl = Label(Window, text=f"Pages inside inside the memory: {Pages}")
RandomNumLbl.place(relx=0.5, rely=0.1, anchor=CENTER)

#Start the GUI
Window.mainloop()
