# covid-19-us-data

covid-19-us-data is a Python library used for retrieving real time data on the latest covid-19 cases based on in the U.S

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install covid-19-us-data.

```bash
pip install covid-19-us-data
```

## Usage

```python
from covid19.scrape import COVID   #import the COVID class

covid = COVID()                    #instansiate the COVID instance
data = covid.get_covid_data()      #call the get_covid_data function to get the data
# format of data = [ <stateName>: [<0:totalCases>, <1:newCases>, <2:totalDeaths>, <3:newDeaths>, <4:totalRecovered>, <5:activeCases>, <6:totalCases/1M pop>, <7: Deaths / 1M pop>, <8:Test/ 1M pops>, <9:population>, <10:projections>], ... ]
```