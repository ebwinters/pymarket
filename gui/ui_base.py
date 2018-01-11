import tkinter as tk
from PIL import ImageTk, Image
from db_func.menu_func import get_net_worth, display_holdings, update_holding, delete_holding, make_holding
from db_func.login import login, make_user
# from gui.backend import
import sys
LARGE_FONT = ("Verdana", 12)

loginid = 0
current_holdings =[]
def set_login_id(user_id):
	global loginid
	loginid = user_id

def get_login_id():
	return loginid

def set_current_holdings(holdlist):
	global current_holdings
	current_holdings = holdlist

def get_current_holdings():
	return current_holdings
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
		for F in (StartPage, Login, NewUser, Menu, Create, Update, Remove, Success, Holdings):
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

		photo = tk.PhotoImage(file="/Users/Ethan/Desktop/pymarket/gui/pymarket.gif")
		w1 = tk.Label(self, image=photo)
		w1.image = photo
		w1.pack()
		

		label = tk.Label(self, text="Welcome to pymarket", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		login_button = tk.Button(self, text="Login", command=lambda: controller.show_frame(Login))
		login_button.pack()
		new_user_button = tk.Button(self, text="New User", command=lambda: controller.show_frame(NewUser))
		new_user_button.pack()

		quit_button = tk.Button(self, text="Logout/Quit", command=lambda: sys.exit())
		quit_button.pack()

class Login(tk.Frame):
	def login_func(tb1, tb2, controller):
		username = tb1.get()
		password = tb2.get()
		user_id = login(username, password)
		if (user_id != -1):
			set_login_id(user_id)
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


def check_holdings(self, parent,controller):
	set_current_holdings(display_holdings(get_login_id(), "pymarket.db"))
	# Holdings.display_data()
	controller.show_frame(Holdings)

class Menu(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Select an option", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		check_button = tk.Button(self, text="Check holdings", command=lambda: check_holdings(self, parent, controller))
		check_button.pack()

		create_button = tk.Button(self, text="Create holding", command=lambda: controller.show_frame(Create))
		create_button.pack()

		update_button = tk.Button(self, text="Update holding", command=lambda: controller.show_frame(Update))
		update_button.pack()

		remove_button = tk.Button(self, text="Remove holding", command=lambda: controller.show_frame(Remove))
		remove_button.pack()

		home_button = tk.Button(self, text="Back home", command=lambda: controller.show_frame(StartPage))
		home_button.pack()

class Holdings(tk.Frame):
	def __init__(self, parent, controller):
		# Holdings.display_data(self,parent,controller)
		tk.Frame.__init__(self, parent)
		frame = tk.Frame(self)
		frame.pack()
		bottom_frame = tk.Frame(self)
		bottom_frame.pack(side='bottom')
		display_button = tk.Button(frame, text="Display", command=lambda: display_data(frame))
		display_button.pack(side='top')
		home_button = tk.Button(bottom_frame, text="Back home", command=lambda: controller.show_frame(Menu))
		home_button.pack(side='bottom')
def display_data(frame):
	for holding in get_current_holdings():
		line = 'holdingId: ' + str(holding[0]) + ', abbreviation: ' + str(holding[2]) + ', shares/holdings: ' + str(holding[3]) + ', bought at: ' + str(holding[4]) 
		holdingId = tk.Label(frame, text=line, font=LARGE_FONT, borderwidth=1)
		holdingId.pack(fill='x')

	net_worth = get_net_worth(get_login_id(), "pymarket.db")
	net_label = tk.Label(frame, text=net_worth, font=LARGE_FONT, borderwidth=1)
	net_label.pack(fill='x')	

	
		

			




		

class Create(tk.Frame):
	def create_the_holding(user_id, tb1, tb2, tb3, tb4, db_name, controller):
		abbreviation = tb1.get()
		holdings = tb2.get()
		bought_at = tb3.get()
		cryptocurrency = tb4.get()
		make_holding(user_id, abbreviation, holdings, bought_at, cryptocurrency, db_name)
		controller.show_frame(Success)

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Enter abbreviation", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		abbreviation = tk.Entry(self)
		abbreviation.pack()

		label = tk.Label(self, text="Enter amount of shares", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		shares = tk.Entry(self)
		shares.pack()

		label = tk.Label(self, text="Enter bought at price", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		bought_at = tk.Entry(self)
		bought_at.pack()

		label = tk.Label(self, text="Enter 0 for cryptocurrency, 1 for stock", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		cryptocurrency = tk.Entry(self)
		cryptocurrency.pack()

		create_button = tk.Button(self, text="Create Holding", command=lambda: Create.create_the_holding(get_login_id(), abbreviation, shares, bought_at, cryptocurrency, "pymarket.db", controller))
		create_button.pack()

		home_button = tk.Button(self, text="Back home", command=lambda: controller.show_frame(Menu))
		home_button.pack()

class Update(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Please enter a username and password", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		home_button = tk.Button(self, text="Back home", command=lambda: controller.show_frame(Menu))
		home_button.pack()

class Remove(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Please enter a username and password", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		home_button = tk.Button(self, text="Back home", command=lambda: controller.show_frame(Menu))
		home_button.pack()

class Success(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Success", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		home_button = tk.Button(self, text="Back home", command=lambda: controller.show_frame(Menu))
		home_button.pack()

def run_app():
	app = pymarketApp()
	app.geometry('{}x{}'.format(500,500))
	app.mainloop()





