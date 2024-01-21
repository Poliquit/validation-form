import getpass
from prettytable import PrettyTable

user_data = []
table = PrettyTable()

# Table column
table.field_names = ["ID","Username","Password"]

# ID each data inserted
auto_increment = 1

# Register Function
def register_acc():
  global auto_increment
  username = str(input("Register username: "))
  password = getpass.getpass("Register password: ")
  user_entry = {'ID':auto_increment,'Username':username,'Password':password}
  auto_increment += 1
  return user_entry
  
# Login Function
def login_acc(login_username,login_password):
  for register_user in user_data:
    if register_user['Username'] == login_username and register_user['Password'] == login_password:
      print("Login success!")
      print(f"Account username:{login_username}")
      print(f"Account password:{login_password}")
      return True
  print("Login failed!, please try again")
  return False
  
# register
register = register_acc()
user_data.append(register)

# login
user_name = str(input("Login username:"))
pass_word = getpass.getpass("Login password:")
login_acc(user_name,pass_word)
login_success = login_acc(user_name,pass_word)

# table data
if login_success:
  table.add_row([register['ID'],user_name,pass_word])
  print(table)
  