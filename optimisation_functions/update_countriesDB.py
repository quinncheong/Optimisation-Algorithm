import pymongo
from .DB_instance import DB_instance

collection = DB_instance('BigData','CountriesData')

for dictionary in x:

    newdict = {}

    try:
        country_name = dictionary['country']
    except NameError:
        country_name == None

    try:
        city_name = dictionary['name']
    except NameError:
        city_name == None
    
    newdict['Country'] = country_name
    newdict['City'] = city_name

    collection.insert_one(dict(newdict))