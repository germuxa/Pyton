import sqlite3
import requests
import json
connection = sqlite3.connect("istep_DB.sl3", 5)
url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
cur = connection.cursor()
response = requests.get(url)
content = response.content.decode('utf-8')
data = json.loads(content)

usd_rate = None
for currency in data:
    if currency['cc'] == 'USD':
        usd_rate = currency['rate']
        break


class CurrencyConverter:
    def __init__(self, usd_rate):
        self.usd_rate = usd_rate

    def convert_to_usd(self, amount):
        return amount / self.usd_rate

print(f"{amount} local currency = {usd_amount:.2f} USD")
usd_converter = CurrencyConverter(usd_rate)
amount = float(input("Enter the amount of your local currency: "))
usd_amount = usd_converter.convert_to_usd(amount)
cur.execute("INSERT INTO first_table (name) VALUES {usd_amount:.2f};")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()