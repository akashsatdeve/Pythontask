#initialize the dictionary
the_data={}
def function_data():
  name=input("enter the name:")
  age=input("enter the age:")
  address=input("enter the address:")
  email=input("enter the email")
  roll_no=input("enter the roll no:")
  the_data[name]={"age":age,"address":address,"email":email,"roll_no":roll_no}
  print(the_data)

function_data()  