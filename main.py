def encode(password):
    string_password = str(password)
    password_digits = [] # creates individual digits
    encoded_password = ""

    for i in range(len(string_password)):
        password_digits.append(string_password[i])

    for i, digit in enumerate(password_digits): # convert back into string
        password_digits[i] = int(digit)

    for digit in password_digits: # encodes digits
        if digit in range(0, 7):
            digit += 3
            encoded_password += str(digit)
        elif digit == 7:
            encoded_password += "0"
        elif digit == 8:
            encoded_password += "1"
        elif digit == 9:
            encoded_password += "2"
        elif digit == 0:
            encoded_password += "3"

    return encoded_password
def decode(classified):
    password = ''
    for i in classified:
        receiver = int(i)
        receiver -= 3
        if receiver < 0:
            receiver += 10
        password += str(receiver)
    print(f"The encoded password is {classified}, and the original password is {password}")
    print("")


if __name__ == "__main__":
    stop_menu = False
    user_password = 0
    user_encoded_password = ""

    while stop_menu is False:
        print("Menu")
        print("-------------")
        print("1. Encode \n2. Decode \n3. Quit\n")
        user_option = int(input("Please enter an option: "))

        if user_choice == 1: # encodes user password
            user_password = str(input("Please enter your password to encode: "))
            user_encoded_password = encode(user_password)
            print("Your password has been encoded and stored!")

        elif user_choice == 2:
            decode(user_encoded_password)
        elif user_choice == 3:
            stop_menu = True
            break
        print()





if __name__ == "__main__": # main function
    stop_menu = False
    password = 0
    encoded_password = ""

    while stop_menu is False: # loops menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_option = int(input("Please enter an option: "))

        if user_option == 1: # encodes password
            password = str(input("Please enter your password to encode: "))
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif user_option == 2:
            decode(encoded_password)
        elif user_option == 3:
            stop_menu = True
            break # ends program
        print()

