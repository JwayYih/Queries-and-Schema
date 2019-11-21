zipcode-queries.py
Using the basicdb package and the geo.json database, write the following functions. 

state_of(zipcode): Returns the name of the state in which zipcode is located.

northernmost(state): Returns the northernmost zipcode in state.

zipcodes_in_city(city_name): Returns the total number of zip codes in the City city_name.

states_by_size(): Returns a list of state names, sorted in order from the state containing the fewest zip codes to the state containing the most. This cannot be done solely using the basicdb interface. You will need to embed your calls to basicdb inside some additional Python code.

classlist.py
Using the basicdb package and the registrar.json database, write a program that takes a single command-line argument and prints out a report on a specified course:

$ python classlistSOLUTION.py 3
Introduction to Asian History meets TH10 in Lecture Hall A
Albert Aziz
Derek Dortmund
Eustace Ennis
Frances Fan
Current enrollment: 4
Remaining capacity: 21
