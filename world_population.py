import json

from country_codes import get_country_code
filename = 'country-by-population.json'
with open(filename) as f:
    pop_data = json.load(f)
    
for pop_dict in pop_data:
    country_name = pop_dict['country']
    population = int(float(pop_dict['population']))
    code = get_country_code(country_name)
    if code:
        print(code + ": " + str(population))
    else:
        print('ERROR - ' + country_name)
    print(country_name + ": " + str(population)) 
