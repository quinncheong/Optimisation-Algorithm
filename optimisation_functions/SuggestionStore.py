class SuggestionStore():
    """TBC!!!!!! Schema for SuggestionStore will be as follows:
    {   A: [ (suggestion_type, suggestion, message, constraint_type), (suggestion_type, suggestion, message, constraint_type), 
             (suggestion_type, suggestion, message, constraint_type) ]
        B: [ (suggestion_type, suggestion, message, constraint_type), (suggestion_type, suggestion, message, constraint_type), 
             (suggestion_type, suggestion, message, constraint_type) ]
        C: [ (suggestion_type, suggestion, message, constraint_type), (suggestion_type, suggestion, message, constraint_type), 
             (suggestion_type, suggestion, message, constraint_type) ]
    }
    SuggestionStore = { A:___, B:___, C:___ } where ABC are names of the activity
    """

    def __init__(self, suggestion_dictionary={}):
        self.suggestions = suggestion_dictionary
    
    def new_suggestion(self, name, suggestion_tuple_list):
        """Function takes in name of the activity and a list of tuples containing the constrait to be saved """
        try:
            existing_list = self.suggestions[name]    
        except KeyError:
            existing_list = []

        existing_list += suggestion_tuple_list
        self.suggestions[name] = existing_list

    def new_suggestion_list(self, name, suggestion_tuple_list):
        """Function takes in name of the activity and a list of tuples containing the constrait to be saved """
        try:
            existing_list = self.suggestions[name]    
        except KeyError:
            existing_list = []

        existing_list += suggestion_tuple_list
        self.suggestions[name] = existing_list

    def remove_suggestion(self, name, suggestion):
        for index, suggestion_tuple in enumerate(self.suggestions[name]):
            if suggestion_tuple[0] == suggestion:
                self.suggestions[name].pop(index)
                break

        if self.suggestions[name] == []:
            self.suggestions[name].pop(name, None)
    
    def merge_suggestions(self, itinerary):
        """Function takes in an itinerary in the following form and merges it with the suggestion
            in the itinerary details section and RETURNS the updated itinerary:
         
            Clients itinerary = {Summary: summary, Details: details}
            summary = [X, Y, Z]
                X = {city:'...', country: '...'}
                Y = {city:'...', country: '...'}
                Z = {city:'...', country: '...'}
            details = { A,B,C,D,E,F }
                A - F = name: { activity_name: '...', 24time_on_itinerary: '...', 
                            duration_activity: '...', booking_time: '...', activity_index: '...'
                        }
        """
        
        details = itinerary['Details']
        for name, suggestion_list in self.suggestions.items():
            details[name]['suggestions'] = suggestion_list
        
        itinerary['Details'] = details
        return itinerary





                




         
