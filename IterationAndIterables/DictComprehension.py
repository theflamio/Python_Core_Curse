
# Dict Comprehension Syntax {key_expr(item): value_expre(item) for item in iterable}

country_to_capital = { 'United Kingdom': 'London',
                       'Brazil': 'Brasilia',
                       'Morocco': 'Rabat',
                       'Sweden': 'Stockholm' }

capital_to_country = {capital: country for country, capital in country_to_capital.items()}
print(capital_to_country)

# Comprehension expressions can be arbitrarily complex "agreed"
# Avoid excessive complexity
# Put complex expressions in separate functions for readability