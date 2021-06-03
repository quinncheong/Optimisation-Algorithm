import pymongo
from DB_instance import DB_instance

"""This is a Db repair script. has to be tweaked dependent on what has happened to the DB."""

cities_data = DB_instance('BigData', 'CitiesData')
countries_data = DB_instance('BigData', 'CountriesData')

# countries_to_check = ['Argentina', 'Belgium', 'Brazil', 'Canada', 'Chile']

country_list = []
for doc in cities_data.find():
    if doc['Country'] not in country_list:
        country_list.append(doc['Country'])

print(len(country_list))

# for country, cities in final_d.items():
#     countries_data.update_one(
#         {'Country': country},
#         {'$set': {'Cities': cities} },
#     )


