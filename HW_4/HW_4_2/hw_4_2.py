tel_num = input('Please input your mobile number: ')

def refresh_num(tel_num:str):
    if tel_num.startswith('0'):
        tel_num = tel_num.replace('0', '', 1)
        if not tel_num.startswith('+996'):
            tel_num = '+996' + tel_num
    if not tel_num.startswith('+996'):
        tel_num = '+996' + tel_num

    print(tel_num)

refresh_num(tel_num)
