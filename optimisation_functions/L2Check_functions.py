import datetime as dt

from .DB_instance import DB_instance
from .ExpandedItinerary import ExpandedItinerary
from .SuggestionStore import SuggestionStore


def string_to_bool(string):
    if string.lower() == 'true':
        return True
    elif string.lower() == 'false':
        return False
    else:
        return string


def type_check(informative_itinerary, key_to_check, value_to_check, return_match):
    # checks for a specific key value pair in the informative itinerary and returns a list of names
    namelist = []
    value_to_check = string_to_bool(value_to_check)

    if return_match == True:
        if value_to_check == 'all':
            for name, location_set in informative_itinerary.items():
                try:
                    if location_set[key_to_check]:
                        namelist.append(name)
                except KeyError:
                    continue

        else:
            for name, location_set in informative_itinerary.items():
                try:
                    if location_set[key_to_check] == value_to_check:
                        namelist.append(name)
                except KeyError:
                    namelist.append(name)

    elif return_match == False:
        if value_to_check == 'all':
            for name, location_set in informative_itinerary.items():
                try:
                    if location_set[key_to_check]:
                        continue
                except KeyError:
                    namelist.append(name)
                else:
                    namelist.append(name)

        else:
            for name, location_set in informative_itinerary.items():
                try:
                    if location_set[key_to_check] == value_to_check:
                        continue
                except KeyError:
                    namelist.append(name)
                else:
                    namelist.append(name)
        
    return namelist
    

def key_location_checker(expanded_itinerary):
    # This function will check if all locations are key locations and return a SuggestionStore
    '''informative_itinerary schema: 'A' = { name:'A', time_client:'2h', booking_time: 1400, activity_index: 0, recommended_time:'3h', rank: 1, opening_hours: '0800-1800', days_closed: [Saturday, Sunday], free_days:[1 Sunday of each month], peak_human_traffic: [morning, afternoon], nearby_locations:['Italy_C_1'], long: ..., lat: ..., new_activity_index: None  }'''

    informative_itinerary = expanded_itinerary.informative_itinerary
    namelist = type_check(informative_itinerary, 'Key_location', 'true', False)

    suggestion_store = SuggestionStore()

    for name in namelist:
        suggestion_tuple_list = [('key_location', f'REMOVE {name}', 'none', 'soft')]
        suggestion_store.new_suggestion(name, suggestion_tuple_list)

    return suggestion_store.suggestions


def passes_checker(expanded_itinerary):
    # Checks if attraction has any passes which can be used and returns names with passes
    informative_itinerary = expanded_itinerary.informative_itinerary
    passes_namelist = type_check(informative_itinerary, 'Passes', 'true', True)

    return passes_namelist


def passes_scale_checker(expanded_itinerary):
    passes_namelist = passes_checker(expanded_itinerary)
    pass


def single_time_check(expanded_itinerary, activity_name):
    """Checks a specific activity's timeslot and verifies if it falls within the operating hours
    of that activity."""
    """date will be in for the form yyyy-mm-dd"""

    weekly_opening_hours = expanded_itinerary.get_opening_hours(activity_name)
    client_activity = expanded_itinerary.get_client_hours(activity_name)
    activity_date = expanded_itinerary.get_parameter(activity_name, 'date')

    year = int(activity_date[0:4])
    month = int(activity_date[5:7])
    day = int(activity_date[-2:])
    date_object = dt.datetime(year, month, day)
    day_name = date_object.strftime("%A")
    
    if weekly_opening_hours == 0:
        suggestion_type = None #For now leave it as None
        suggestion = f'SHIFT {activity_name}'
        message = f'Activity start or end timing does not fall within operating hours of {activity_name} as it is closed for today'
        constraint_type = 'Red'
        suggestion_tuple = (suggestion_type, suggestion, message, constraint_type)
        return suggestion_tuple
        
    day_hours = weekly_opening_hours[day_name]

    opening_time, closing_time = int(day_hours[0]), int(day_hours[1])
    client_start, client_end = int(client_activity['activity_start']), int(client_activity['activity_end'])

    if client_start <= opening_time or client_start >= closing_time or client_end <= opening_time or client_end >= closing_time:

        """ Suggestion tuple schema TBC!!!!
        A: [ (suggestion_type, suggestion, message, constraint_type) ]
        where A is the activity_name"""
        
        suggestion_type = None #For now leave it as None
        suggestion = f'SHIFT {activity_name}'
        message = f'Activity start or end timing does not fall within operating hours of {activity_name}. Opening time is {day_hours[0]} and closing time is {day_hours[1]}'
        constraint_type = 'Red'
        suggestion_tuple = (suggestion_type, suggestion, message, constraint_type)

        return suggestion_tuple
    
    return None


def verify_EI_time(expanded_itinerary):
    suggestion_tuple_list = []
    all_activity_list = list(expanded_itinerary.details.keys())
    for activity in all_activity_list:
        suggestion_tuple = single_time_check(expanded_itinerary, activity)
        suggestion_tuple_list.append(suggestion_tuple)
    return suggestion_tuple_list

x = [{'City': 'Singapore', 'Country': 'Singapore'}]
y = {
    'Singapore Flyer': {'name': 'Singapore Flyer', 'time': '1200', 'fun': 'no', 'Country': 'Singapore', '24time_on_itinerary': '2200 - 2330', 'date': '2020-10-20'}
    # 'Gardens by the Bay': {'Country': 'Singapore'},
    # 'Singapore Zoo': {'Country': 'Singapore'}
}

itinerary = ExpandedItinerary({'Summary':x, 'Details':y})
itinerary.expand()
# print(itinerary.informative_itinerary)
suggestion_tuple_list = verify_EI_time(itinerary)
print(suggestion_tuple_list)
# print(suggestion_tuple)
# key_store = key_location_checker(itinerary)
# print(key_store)