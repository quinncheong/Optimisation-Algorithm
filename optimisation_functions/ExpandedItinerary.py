from .DB_instance import DB_instance

class ExpandedItinerary(object):
    """Takes in an itinerary with the following schema:
    Clients itinerary = {Summary: summary, Details: details}
    summary = [X, Y, Z]
        X = {City:'...', Country: '...'}
        Y = {City:'...', Country: '...'}
        Z = {City:'...', Country: '...'}

    details = { A,B,C,D,E,F }
        A - F = activity_name: { activity_name: '...', 24time_on_itinerary: '...', 
                    duration_activity: '...', booking_time: '...', activity_index: '...',
                    Country: '...'
                }
    """

    def __init__(self, itinerary):
        self.client_itinerary = itinerary
        self.informative_itinerary = None #Will eventually be in self.details but updated with DB info
        self.summary = itinerary['Summary']
        self.details = itinerary['Details']

    def expand(self):
        # Function converts clients itinerary to an expanded itinerary by appending items from backend

        def Merge(dict1, dict2): 
            res = {**dict1, **dict2} 
            return res
        
        new_details = {}

        for activity_name, activity_dictionary in self.details.items():
            attractions_collection = activity_dictionary['Country'].capitalize() + 'Attractions'
            country_DB = activity_dictionary['Country'].capitalize() + 'Data'
            collection = DB_instance(country_DB, attractions_collection)
            
            results = collection.find({ 'Activity': activity_name })
            activity_dictionary = Merge(activity_dictionary, results[0])
            new_details[activity_name] = activity_dictionary

        self.informative_itinerary = new_details
    
    # def add_attraction(self, attraction, country):
    #     # add an expanded attraction which has is updated from backend
    #     self.informative_itinerary.append(attraction)
    #     self.expand(country)

    # def remove_attraction(self, attraction_name):
    #     to_remove = False
    #     for attraction in self.informative_itinerary:
    #         if attraction['Activity'] == attraction_name:
    #             to_remove = attraction
    #             break
    #     if to_remove:
    #         self.informative_itinerary.remove(to_remove)
    
    def time_check(self, sleep_duration):
        time_left = 24 - sleep_duration
        time_used = 0
        for city in self.informative_itinerary:
            time_used += city['time_client']
        time_left -= time_used
        if time_left >= 3:
            return time_left
        return None

    
    def get_opening_hours(self, activity_name):
        try:
            opening_hours = self.informative_itinerary[activity_name]['Opening_hours']
        except KeyError:
            opening_hours = None

        if opening_hours == 'Temporarily_closed':
            opening_hours = 0
        
        if opening_hours == None:
            return None
        elif opening_hours == 0:
            return 0

        opening_hours_dict = {}

        def convert_to_24h(string):
            """string will be in the form x:xxyy where x = numbers in 12h and yy = PM/AM
            etc 5:00AM or 12:00PM or 3:00PM"""

            first_index = string.find(':')
            hour = string[:first_index + 1]
            mins = string[2:4]
            timeframe = string[-2:]

            if timeframe == 'AM':

                if len(hour) == 2:
                    string_start = ''
                else:
                    string_start = '0'

                if hour == '12':
                    hour = '00'
                return string_start + hour + mins


            if timeframe == 'PM':
                
                to_add = '12'

                if hour == '12':
                    to_add = '0'
                
                new_hour = str(int(hour) + int(to_add))

                return new_hour + mins     

        for string in opening_hours:
            string = string.replace(' ', '')
            first_index = string.find(':')
            second_index = string.find('-')
            day = string[:first_index]
            opening_time = convert_to_24h(string[first_index: second_index])
            closing_time = convert_to_24h(string[second_index + 1:])

            opening_hours[day] = (opening_time, closing_time)
        
        return opening_hours_dict


    def get_client_hours(self, activiity_name):
        """24time_on_itinerary will be in a string in the form of xxxx - xxxx where xxxx
        are 24h clock notations. E.g 1300 - 1500"""
        client_activity_hours = self.informative_itinerary[activiity_name]['24time_on_itinerary']
        hours_dict = {
            'activity_start': client_activity_hours[0:4],
            'activity_end': client_activity_hours[-4:]
        }

        return hours_dict
    
    def get_parameter(self, activity_name, parameter):
        detail = self.informative_itinerary[activity_name][parameter]
        return detail


# x = [{'City': 'Singapore', 'Country': 'Singapore'}]
# y = {
#     'Singapore Flyer': {'name': 'Singapore Flyer', 'time': '1200', 'fun': 'no', 'Country': 'Singapore'},
#     'Gardens by the Bay': {'Country': 'Singapore'},
#     'Singapore Zoo': {'Country': 'Singapore'}
# }

# itinerary = {'Summary':x, 'Details':y }

# z = ExpandedItinerary(itinerary)
# z.expand()
# print(z.informative_itinerary)

