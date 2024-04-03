import pycountry

for country in pycountry.countries:
    print(country.alpha_2, country.name)