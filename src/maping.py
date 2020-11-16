
import folium

def mapa(inicial_lat, inicial_long, zoom):

    '''
    This function takes the coordinates(latitude, longitude) of certain point, and creates a map with a zoom of our choosing

    '''
    
    x = folium.Map(location = [inicial_lat,inicial_long], zoom_start = zoom)

    return x





def offices(df, mapa): 

    '''
    This function adds a marker for all the businesses that we have in our original df to the map created with the previous function (mapa()). 

    It takes as arguments the dataframe we want to use and the map in which we want to insert the markers (a lightblue and black briefcase). 

    This function is focused in seting the markers for the companies we extracted form the Mongodb collection.

    '''

    for i,row in df.iterrows():

            office = {
                "location" : [row["latitude"], row["longitude"]],
                "tooltip" : row["name"]
            }
            icon = Icon( color = "lightblue",
                        prefix = "fa",
                        icon = "briefcase",
                        icon_color = "black"
            )

            Marker (**office,icon = icon).add_to(mapa)





def full_map(df, map_):

    '''
    As the previous function, this ones creates markers and inserts them in the map of our choosing using the information extracted from the API.

    In this case, as we just wanted to check for clubs, starbucks and airports, the funtion wont work fot other values. 

    It takes as arguments the dataframe in which we have stores all the API's information, and the map in which we want to insert the markers:
        - starbucks -> green and white coffe cup
        - airports -> black and white plane
        - clubs -> white and black glass

    '''
    
    for i,row in df.iterrows():
        
        if row["category"] == "starbucks":
            
            coffe = {
                "location" : [row["latitud"], row["longitud"]],
                "tooltip" : row["name"]
            }
            icon = Icon( color = "green",
                        prefix = "fa",
                        icon = "coffee",
                        icon_color = "white"
            )

            Marker (**coffe,icon = icon).add_to(map_)
        
        elif row["category"] == "airport" : 
            
            plane = {
                "location" : [row["latitud"], row["longitud"]],
                "tooltip" : row["name"]
            }
            icon = Icon( color = "black",
                        prefix = "fa",
                        icon = "plane",
                        icon_color = "white"
            )

            Marker (**plane,icon = icon).add_to(map_)
            
        elif row["category"] == "club" :
            
            party = {
                "location" : [row["latitud"], row["longitud"]],
                "tooltip" : row["name"]
            }
            icon = Icon( color = "white",
                        prefix = "fa",
                        icon = "glass",
                        icon_color = "black"
            )

            Marker (**party,icon = icon).add_to(map_)

    return map_