# try:
#     org_bill = int(input("Enter your  Original Bill Amount : "))
#     if org_bill <=0:
#         print("Error : The amount must be greater than zero")
#         raise SystemExit
    
#     else:
#         if org_bill >= 2000:
#             print("You Got 10% Discount")
#             discount = (org_bill * 10)/100
#             final_amount = org_bill - discount
#         else:
#             print("You can't get discount,Purchase for Rs.2000/-")

#         print("-----------BILL-------------")
#         print("Original Bill : ",org_bill)
#         print("Discount (10%) : ",discount)
#         print("Final Amount : ",final_amount)  

# except ValueError:
#     print("Enter Valid amount")

# else:
#     print("Thank You for Purchase")

# finally:
#     print("Bill system Ended")








try:
    org_bill = int(input("Enter your Original Bill Amount: "))

    if org_bill <= 0:
        print("Error: The amount must be greater than zero.")
        raise SystemExit

    if org_bill >= 2000:
        print("You Got 10% Discount")
        discount = (org_bill * 10) / 100
    else:
        print("You can't get a discount. Purchase for Rs.2000/-")

        discount = 0

    final_amount = org_bill - discount

    print("----------- BILL -------------")
    print("Original Bill:", org_bill)
    print("Discount:", discount)
    print("Final Amount:", final_amount)

except ValueError:
    print("Enter a valid amount.")

else:
    print("Thank You for Purchase.")

finally:
    print("Bill System Ended.")