from tkinter import *
from tkinter import messagebox
import pickle

def registration():
    label_error = None

    frame = Frame(root, bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor='n')

    label = Label(frame, text="Sign Up", font="16")
    label.place(relwidth=1, relheight=0.1)

    label_login = Label(frame, text="Login :")
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    login_register = Entry(frame)
    login_register.place(relx=0.4, rely=0.2, relwidth=0.55, relheight=0.1)

    label_password1 = Label(frame, text="Password:")
    label_password1.place(rely=0.4, relheight=0.1, relwidth=0.35)

    password1 = Entry(frame, show="*")
    password1.place(rely=0.4, relheight=0.1, relwidth=0.55, relx=0.4)

    label_password2 = Label(frame, text="Password:")
    label_password2.place(rely=0.6, relheight=0.1, relwidth=0.35)

    password2 = Entry(frame, show="*")
    password2.place(rely=0.6, relheight=0.1, relwidth=0.55, relx=0.4)

    button = Button(frame, text="Sign up",command=lambda:signup())
    button.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.15)
    
    def signup():
        nonlocal label_error
        error = ""

        if label_error:
            label_error.destroy()

        if len(login_register.get()) == 0:
            error = "*login error"
        elif len(password1.get()) < 5:
            error = "*your password is too short. It must be at least 5 characters"
        elif not password1.get() == password2.get():
            error = "*password error"
        else:
            save()
        label_error = Label(frame, text=error, fg="red")
        label_error.place(rely=0.7)
    
    def save():
        data = {login_register.get(): password1.get()}
        try:
            with open("login_data.pickle", "wb") as f:
                pickle.dump(data, f)
        except Exception as e:
            messagebox.showerror("Error!", f"An error occurred while saving: {e}")

def login_form():
    frame = Frame(root, bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor="n")

    label = Label(frame, text="Sign in")
    label.place(relwidth = 1, relheight=0.1)

    label_login = Label(frame, text="Login :")
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    enter_login = Entry(frame)
    enter_login.place(relx=0.4, rely=0.2, relwidth=0.55, relheight=0.1)

    label_password = Label(frame, text="Password:")
    label_password.place(rely=0.4, relheight=0.1, relwidth=0.35)

    enter_password = Entry(frame, show="*")
    enter_password.place(rely=0.4, relheight=0.1, relwidth=0.55, relx=0.4)

    button = Button(frame, text="Sign in", command=lambda: login_pass())
    button.place(relx=0.3, rely=0.8, relheight=0.15, relwidth=0.5)
    
    def login_pass():
        try:
            with open("login_data.pickle", "rb") as f:
                data = pickle.load(f)
                if enter_login.get() in data and enter_password.get() == data[enter_login.get()]:
                    messagebox.showinfo("Welcome", "Welcome to my world")
                    img2 = PhotoImage(file="img/bg2.gif")
                    background_label2 = Label(root, image=img2)
                    background_label2.place(relx=0.5, rely=0.5, anchor="center")
                else:
                    messagebox.showerror("Error!", "Invalid login or password!")
        except Exception as e:
            messagebox.showerror("Error!", f"An error occurred while reading: {e}")

root = Tk()
root.title("Login Form")
root.geometry("550x550")
root.resizable(False, False)

root.option_add("*Font", "Oswald")
root.option_add("*Background", "blue")

img = PhotoImage(file="img/bg3.gif")
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

button_signup = Button(root, text="Sign Up", bg="blue", fg="white", command=registration)
button_signup.place(relx=0.2, rely=0.1, relwidth=0.3)

button_signin = Button(root, text="Sign In", bg="blue", fg="white", command=login_form)
button_signin.place(relx=0.5, rely=0.1, relwidth=0.3)

root.mainloop()
