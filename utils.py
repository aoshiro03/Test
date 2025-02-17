def namelengthCheck(name):
    if len(name) < 3:
        print('name must be at least 3 chracter')
    elif len(name) > 50:
        print('name can be a maxmum of 50 characters')
    else:
        print(f'I am {name}')
