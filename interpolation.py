email_tmpl = """
Hello, %(name)s
 
Buy this beautiful %(product)s now!

Good for:
%(text)s

Click and buy: %(link)s

Only %(quantity)d in stock.

Price $ %(price).2f.
"""

clients = ["Bruno", "Clarissa", "Maria"]

for client in clients:
    print(email_tmpl % {
        "name": client,
        "product": "pen",
        "text": "Cool drawings",
        "link": "https://clickhere.com",
        "quantity": 2,
        "price": 29.90
        }
    )