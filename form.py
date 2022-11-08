import tkinter as tk
import tkinter.messagebox
person=''
window=tk.Tk()
window.geometry("400x400")
window.title("Form") 

def clear_field():
    tkinter.messagebox.showinfo("Thank you!")
    
    
label= tk.Label(window, text="please fill the form", font=('Arial', 14))
First_Name=tk.Label(window, text="Enter your First Name:", font=('Arial', 12)).place(x=5, y= 40)
Last_name=tk.Label(window, text="Enter your Last Name:", font=('Arial', 12)).place(x=5, y= 80)
Email_address=tk.Label(window, text="Enter your EmailAddress:", font=('Arial', 12)).place(x= 5, y= 120)
Phone_Number= tk.Label(window, text="Enter your PhoneNumber:", font=('Arial', 12)).place(x= 5, y= 160)

label.pack(fill='x')

textbox1=tk.Entry(window,font=('Arial', 10)).place(y= 40, x=190)
textbox2=tk.Entry(window,font=('Arial', 10)).place(y= 80, x=190)
textbox3=tk.Entry(window,font=('Arial', 10)).place(y=120, x=190)
textbox4=tk.Entry(window,font=('Arial', 10)).place(y=160, x= 190)

button= tk.Button(window, text='Submit', command=clear_field,font=('Arial', 14)).place(x= 150, y=200)



window.mainloop()