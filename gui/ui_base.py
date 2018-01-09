import tkinter as tk
from db_func.menu_func import get_net_worth, display_holdings, update_holding, delete_holding, make_holding
from db_func.login import login, make_user
# from gui.backend import
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
		for F in (StartPage, Login, NewUser, Menu):
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
	def login_func(tb1, tb2, controller):
		username = tb1.get()
		password = tb2.get()
		user_id = login(username, password)
		if (user_id != -1):
			controller.show_frame(Menu)


	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Please enter your username and password", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		username_label = tk.Label(self, text="Enter your username")
		username_label.pack()
		username = tk.Entry(self)
		username.pack()

		password_label = tk.Label(self, text="Enter your password")
		password_label.pack()

		password = tk.Entry(self, show="*")
		password.pack()

		login_button = tk.Button(self, text="Login", command=lambda: Login.login_func(username, password, controller))
		login_button.pack()

		home_button = tk.Button(self, text="Back home", command=lambda: controller.show_frame(StartPage))
		home_button.pack()

class NewUser(tk.Frame):
	def make_user_func(tb1, tb2, tb3, controller):
		username = tb1.get()
		password = tb2.get()
		password2 = tb3.get()
		make_user(username, password, password2)
		controller.show_frame(StartPage)
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Please enter a username and password", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		username_label = tk.Label(self, text="Enter your username")
		username_label.pack()
		username = tk.Entry(self)
		username.pack()

		password_label = tk.Label(self, text="Enter your password")
		password_label.pack()
		password = tk.Entry(self, show="*")
		password.pack()

		password_label2 = tk.Label(self, text="Enter your password again")
		password_label2.pack()
		password2 = tk.Entry(self, show="*")
		password2.pack()

		make_button = tk.Button(self, text="Make User", command=lambda: NewUser.make_user_func(username, password, password2, controller))
		make_button.pack()


		home_button = tk.Button(self, text="Back home", command=lambda: controller.show_frame(StartPage))
		home_button.pack()

class Menu(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Please enter a username and password", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		home_button = tk.Button(self, text="Back home", command=lambda: controller.show_frame(StartPage))
		home_button.pack()
def run_app():
	app = pymarketApp()
	app.geometry('{}x{}'.format(500,500))
	app.mainloop()





