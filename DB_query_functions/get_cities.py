from optimisation_functions.DB_instance import DB_instance

def get_cities(country):
    """takes in a country and makes a search to the DB to get the array of cities
    stores in the database for that country. Returns the array of cities from DB."""
    collection = DB_instance('BigData', 'CountriesData')
    document = collection.find_one({'Country': country})
    try:
        temp_list = document['Cities']
    except KeyError:
        temp_list = None
    
    return temp_list

    