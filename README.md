# GEOSPATIAL-PROJECT
![Alt Text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpQYuybUl8_VTEWdMdajTczYfNYmo_Mo5aNQ&usqp=CAU)


## Overview

According to GameDesigning, four of the best cities to work as a gaming developer are: San Francisco, London, Tokyo and Paris we did´t have enough information on Tokyo so we passed on to Paris). So, the objective of this project was to decide which of this cities was better according to the closeness of starbucks facilities, nightclubs/bars, airports and other similar companies. 

## Libraries

* For general practices and commands:

    - Pandas
    - Pymongo -> Mongoclient
    - Math
    - Functools -> Reduce
    -Operator

* For working with API's:
    
    - Json 
    - Requests

- For map visualization:

    - Folium
    - Folium.plugins
    
## Structure

The project is divided in three main sections, and inside each of them we can find the process done to each of the three cities selected. 

**Mongodb**

In the first section the information from a *Mongodb* database is extracted and treated, obtaining three dataframes with companies, their category, city and coordinates(latitude, longitude)

**API Extraction and Visualization**

Next, we extract the information about the starbucks, nightclubs/bars and airports near a specified location from  Foursquare's API. All this information is stored in a dataframe, one for each city. 

Once each dataframe is finished, we create a map in which we can find four kinds of marker depending of the object it is describing and locating (Starbucks, club/bar, airport or company)

**Final Analysis and Conclusions**

The first conclusion we can extract from the visual analysis is that London can be excluded, as the companies that belong to the categories we are interested in are way to disperse and far away from the clubs and starbucks, which means our employees will not be able to enjoy themselves, something we absolutely cannot accept. Therefore, London is out of the way, and we have to choose between Paris or San Francisco.  

Between San Francisco and Paris, the visualizations are not vey different, even though the former has a lot more companies from which developers can learn and exchange ideas and experiences. 

However, after calculating the distance to the closest starbucks, club/bar, company and airport, we can say that the best place to set a new gaming company is **Paris**, as the chosen spot is from which our employees can enjoy a cup of coffe during a break or go out for a drink after a hard day of work. It is close to other companies, and the closest airports are just 12 and 14 km away, which would be more convenient to our managers. 

**Future improvements**

It would have been great to use **geo queries** or python's library **geopandas**, as they would have allowed me to obtian results more precisely. 


