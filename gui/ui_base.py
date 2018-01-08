import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class pymarketApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		#we will have a container to contain stuff within the app
		container = tk.Frame(self)

		#fill space alloted(top), expand to all whitespace
		container.pack(side="top", fill="both", expand="True")

		#basic config
		#0 is min size, weight is priority 

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		#a bunch of frames that have one on front that we are interacting with
		self.frames = {

		}
		for F in (StartPage, Login, NewUser):
			frame = F(container, self)
			self.frames[F] = frame

			#stretch everything to size of window nsew
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, container):
		frame = self.frames[container]
		#raise to front
		frame.tkraise()


class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Welcome to pymarket", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		login_button = tk.Button(self, text="Login", command=lambda: controller.show_frame(Login))
		login_button.pack()
		new_user_button = tk.Button(self, text="New User", command=lambda: controller.show_frame(NewUser))
		new_user_button.pack()

class Login(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="login page", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		login_button = tk.Button(self, text="Back home", command=lambda: controller.show_frame(StartPage))
		login_button.pack()

class NewUser(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="new user page", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		login_button = tk.Button(self, text="Back home", command=lambda: controller.show_frame(StartPage))
		login_button.pack()

app = pymarketApp()
app.geometry('{}x{}'.format(500,500))
app.mainloop()





