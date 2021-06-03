import pymongo
from DB_instance import DB_instance

"""This is a Db repair script. has to be tweaked dependent on what has happened to the DB."""

countries_data_list = []
countries_data1_list = []
final_list = []
countries_with_no_cities = []
countries_with_no_cities1 = []
countries_to_add_cities = []

countries_data1 = DB_instance('BigData', 'CountriesData1')
countries_data = DB_instance('BigData', 'CountriesData')


for document in countries_data.find():
    try:
        countries_data_list.append(document['Cities'])
    except KeyError:
        countries_with_no_cities.append(document['Country'])

for document in countries_data1.find():
    try:
        countries_data1_list.append(document['Cities'])
    except KeyError:
        countries_with_no_cities1.append(document['Country'])

for i in countries_data1_list:
    if i not in countries_data_list:
        final_list.append(i[0])

for i in countries_with_no_cities:
    if i not in countries_with_no_cities1:
        countries_to_add_cities.append(i)

# print(final_list)
print('...')
print('...')
print('Countries with no cities from CountriesData' + str(countries_with_no_cities))
print('...')
print('...')
print('Countries with no cities from CountriesData1' + str(countries_with_no_cities1))
# print(countries_to_add_cities)

# cities_data = DB_instance('BigData', 'CitiesData')

# cities_list = []

# for city in final_list:
#     document = cities_data.find({'City': city})
#     cities_list.append(document['Country'])
# print(cities_list)
