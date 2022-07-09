phone_number=input("Enter Phone Number: ")
if (phone_number.isdigit()):
    if (len(phone_number)==10):
        print("Phone number format  correctly")
    else:
        print("Phone number format is invalid, length is less than 10")
else:
    print("The phone number format is invalid, contains an invalid character")


  