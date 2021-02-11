from hasht import HashTable

ht = HashTable()

phone_numbers = ["555-555-5555", "444-444-4444"]
tesla_models = ['Teslas model X', 'Tesla model Y', 'Tesla model 3']
companies = ['Airbnb', 'Uber', 'Digital Ocean', 'Clubhouse']

ht.insert('phoneDirectory', phone_numbers)
ht.insert('teslaDirectory', tesla_models)
ht.insert('companiesDirectory', companies)

phone_numbers = None
tesla_models = None
companies = None

ht.remove('teslaDirectory')

phone_numbers = ht.retrive('phoneDirectory')
tesla_models = ht.retrive('teslaDirectory')
companies = ht.retrive('companiesDirectory')

print(phone_numbers.key if phone_numbers != None else phone_numbers)
print(tesla_models.key if tesla_models != None else tesla_models)
print(companies.key if companies != None else companies)