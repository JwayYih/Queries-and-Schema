#rename file to remove the '-'  zipcodequeries.py if you want to use the test file
from basicdb import *

#state_of(zipcode): Returns the name of the state in which zipcode is located.
def state_of(zipcode):
    load_db('geo.json')
    rows = select(where(db_from('geozipcodes'), 'Zip Code', zipcode), 'State')
    return rows[0]
              
#northernmost(state): Returns the northernmost zipcode in state.
def northernmost(state):
    load_db('geo.json')
    rows = select(orderby(where(db_from('geozipcodes'), 'State', state), 'Latitude'), 'Zip Code')
    return rows[-1]
    
#zipcodes_in_city(city_name): Returns the total number of zip codes in the City city_name.
def zipcodes_in_city(city_name): 
    load_db('geo.json')
    rows = count(where(db_from('geozipcodes'), 'City', city_name))
    return rows


def states_by_size():
    load_db('geo.json')
    state_list=distinct(select(db_from('geozipcodes'), 'State'))
    state_dict={}  
    for state in state_list:
        if state != 'State':
            total_zip=count(where(db_from('geozipcodes'), 'State', state))
            state_dict.update({state : total_zip})      
    state_dict_sorted_desc=sorted(state_dict.items(), key=operator.itemgetter(1),reverse=True)
    return state_dict_sorted_desc



















