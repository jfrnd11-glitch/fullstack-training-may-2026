#try:
    #age = int(input("Enter age: "))

   # if age < 18:
  #      raise ValueError("Age must be 18 or above")

 #   print("Eligible")

#except ValueError as e:
 #   print("Error:", e)

try:
    age = int(input("Enter age: "))

except Exception as e :
    print("error: {e}")
finally:
    print("welcome")
