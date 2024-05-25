def format_price(price):
    price = float(price)
    done = (f'{price:.0f}')
    return done


price = '30'
p = format_price(price)


print(f'Ціна: {p}  гривень')