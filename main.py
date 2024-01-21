def register():
  username = str(input("Enter username:"))
  password = str(input("Enter password:"))
  return username, password
  
def main():
  print("Welcome to Registration")
  user,pwd = register()
  print(f'Registration Successful! Username:{user} Password:{pwd}')
if __name__ == "__main__":
  main()