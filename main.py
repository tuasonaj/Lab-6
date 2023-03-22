def encode():
    password = input('Please enter your password to encode: ')
    encoded_password = ''
    for digit in password:
        encoded_digit = int(digit) + 3
        encoded_password += str(encoded_digit)
    print('Your password has been encoded and stored!')
    print('')

def menu():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        option = int(input("Please enter an option: "))
        if option == 1:
            encode()
        elif option == 3:
            break

menu()













