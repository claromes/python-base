email_tmpl = """
Hello, {name}

Buy this beautiful {product} now!

Good for:
{text}

Click and buy: {link}

Only {quantity:d} in stock.

Price $ {price:.2f}.
"""

clients = ["Bruno", "Clarissa", "Maria"]

for client in clients:
    print(email_tmpl.format(
         name = client,
         product = "pen",
         text = "Cool drawings",
         link = "https://clickhere.com",
         quantity = 2,
         price =  29.90
         )
    )