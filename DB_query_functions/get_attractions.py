from .get_cities import get_cities
from optimisation_functions.DB_instance import DB_instance

def get_attractions(country, city):
    database_name = country + 'Data'
    collection_name = city + 'Attractions'
    collection = DB_instance(database_name, collection_name)
    documents = collection.find({ 'Activity': { '$exists':'True' } })
    activity_list = []
    for document in documents:
        attraction = document['Activity']
        activity_list.append(attraction)
    
    return activity_list

    
