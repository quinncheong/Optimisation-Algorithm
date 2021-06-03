# Importing key classes
from optimisation_functions.ExpandedItinerary import ExpandedItinerary
from optimisation_functions.SuggestionStore import SuggestionStore
from optimisation_functions.L2Check_functions import verify_EI_time


def optimise_itinerary(itinerary):
    """Takes in a normal itinerary and optimises it, returning a suggestion tuple list"""
    expanded_i = ExpandedItinerary(itinerary)
    expanded_i.expand()
    suggestion_tuple_list = verify_EI_time(itinerary)
    return suggestion_tuple_list

