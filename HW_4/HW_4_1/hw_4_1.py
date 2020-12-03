string = input('Please input any sentence: ')

def refresh(string:str):
    string = string.capitalize()
    if not string.endswith('.'):
        string = string + '.'

    print(string)

refresh(string)