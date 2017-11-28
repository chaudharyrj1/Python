char=input("Enter Your Character")
if (char.__len__() > 1):
    print("Please Enter an Alphabate")
else:
    if char.isalpha()==True:
        if (char.lower() in ('a','e','i','o','u')):
          print("Vowel Entered")
        else:
          print("Consonant Entered")
    else:
         print("Please Enter an Alphabate")