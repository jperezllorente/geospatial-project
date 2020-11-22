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
    

Also, for the calculation of distances I have used a function from thie Medium article in which the whole explanation is given with plenty of detail. [Calculate Distance Between GPS Points in Python](https://janakiev.com/blog/gps-points-distance-python/)



## Structure

The project is divided in three main sections, and inside each of them we can find the process done to each of the three cities selected. 

**Mongodb**

In the first section the information from a *Mongodb* database is extracted and treated, obtaining three dataframes with companies, their category, city and coordinates(latitude, longitude)

**API Extraction and Visualization**

Next, we extract the information about the starbucks, nightclubs/bars and airports near a specified location from  Foursquare's API. All this information is stored in a dataframe, one for each city. 

Once each dataframe is finished, we create a map in which we can find four kinds of marker depending of the object it is describing and locating (Starbucks, club/bar, airport or company)

**Final Analysis and Conclusions**

The first conclusion we can extract from the visual analysis is that London can be excluded as the companies that belong to the categories we are interested in are way to disperse and far away from the clubs and starbucks, which means our employees will not be able to enjoy themselves, something we absolutely cannot accept. Therefore, London is out of the way, and we have to choose between Paris or San Francisco.  

In orer to choose the right city for our company we are going to use one from the  Mongodb collection as reference, and we are going to compare the distances to the nearest Starbukcs and airport, and the number of clubs in a 150 meter radius. 

    - The reason we are only checking for one Starbucks is because all establishments are the same and offer the same products, so it was not necessary to have many near the company. The same reasoning can be applied to the airports.
    - The crtieria related to the clubs is focused on the number of establishments found in a 150 meter radius with the company as the centre. The reason for this is that most clubs have different atmospheres and vibes, and it more enjoyable going to different bars.  

The results help us conclude that Paris would be a better option because  the selected lcoation has more clubs in the defined area, and it has a Starbucks and airport closer than the office in San Francisco. The location in Paris has many companies nearby from which our developers can learn and exchange experiences, and plenty of clubs and starbucks for our employees to enjoy themselves after a hard day of work. Also, facing the company's growth, it could be a better option to locate our offices in a city where the industry is growing, instead of doing it in a city where it is solidly established. 


**Future improvements**

It would have been great to use **geo queries** or python's library **geopandas**, as they would have allowed me to obtian results more precisely. 

It would be interesting to choose a randon point based on criteria as the one used in this project insetad of choosing a location based on visualization and other information. Also, a table of scores could be created to determine what values we give to each criteria son that our final decision us based on true evidence. 


