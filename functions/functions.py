def show_greeting(name):
    print(f'Hello {name}')
show_greeting('Dima')

def reverse_str(str):
    print(str[::-1])
reverse_str("123")

def get_last_char(str):
    return str[-1]
print(get_last_char('123'))

#default options
def get_hidden_card(card, count_star=4):
    count = '*' * count_star
    return f'{count}{card[-4:]}'

print(get_hidden_card('1234567812345678'))
print(get_hidden_card('1234567812345678', 6))

def f(a=1, b=2, c=3):
    return

print(f(3,))



