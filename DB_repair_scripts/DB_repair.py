# import pymongo
# from DB_instance import DB_instance

"""This is a Db repair script. has to be tweaked dependent on what has happened to the DB."""

# count = 0
# cities_data = DB_instance('BigData','CitiesData')
# countries_data = DB_instance('BigData', 'CountriesData1')
# final_data = DB_instance('BigData', 'CountriesData')

# countries_data.rename('CountriesData')

# countries_list = []

# for dictionary in final_data.find({ 'Country': { '$exists': 'true' } }):
#     country = dictionary['Country']
#     if country not in countries_list:
#         countries_list.append(country)

# print(len(countries_list))
# print(countries_list)

# for country in countries_list:
#     dictionary = final_data.find_one({ 'Country': country })
#     dictionary.pop('_id', None)
#     countries_data.insert_one(dictionary)

# for country, cities in countries_dict.items():
#     final_data.update_one(
#         {'Country': country},
#         {'$set': {'Cities': cities} },
#         upsert=True
#     )

# for dictionary in x:
# try:
#     dictionary = dictionary['Cities'][0]

#     print(dictionary)
# except KeyError:
#     continue
    

