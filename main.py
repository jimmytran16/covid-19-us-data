from covid19.scrape import COVID   #import the COVID class
from pprint import pprint

covid = COVID()                    #instansiate the COVID instance
data = covid.get_covid_data()      #call the get_covid_data function to get the data
pprint(data)