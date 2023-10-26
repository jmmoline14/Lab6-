#Joseph Moline


def encode(to_be_encoded):

    new_list = ''
    for i in range(len(to_be_encoded)):

        new_value = (3 + int(to_be_encoded[i]))%10
        new_list += str(new_value)
    print(new_list)
    return new_list


# Caleb Gottlieb
def decode(encoded):
    decoded=''
    for i in range(len(encoded)):
        temp=int(encoded[i])-3
        if(temp<0):
            temp=10+temp
        decoded+=str(temp)
    return decoded

if __name__ == '__main__':

    while True:
        print('Menu \n-------------\n1. encode \n2. Decode \n3. Quit')
        user_input = int(input('Please enter an option:'))
        if user_input == 1:
            to_be_encoded = str(input('Please enter a passcode to enter:'))
            encoded_value = encode(to_be_encoded)
            print('Your password has been encoded and stored!')
        elif user_input == 3:
            break
        elif user_input == 2:
            decoded_p=decode(encoded_value)
            print(f'The encoded password is {encoded_value} and the original value password is {decoded_p} ')


