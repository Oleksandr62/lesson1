def format_price(price):
    price = float(price)
    done = (f'{price:.3f}')
    return done


price = '76.24'
p = format_price(price)


print(f'Ціна: {p} гривень')