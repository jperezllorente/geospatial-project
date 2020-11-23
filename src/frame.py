



def collection(city, lim):

    '''
    This function extracts information from those companies(documents) of a MongoDB collection that fulfill the following conditions:
        - The companies need to located in a specific city, which we set as argument depending in our interest.
        - They have to operate in one of this fields: analytics, games-video, mobile, software or web

    It takes as aruments the city we want to explore and the limit of obsevations we want
    
    The function returns an object with the name, city, latitude and lonitude, and category of the company.

    '''
    
    x = pd.DataFrame(companies.find({"offices.city": city, "$or":[{"category_code": "analytics"}, {"category_code": "games-video"},
                                                        
                                                       {"category_code": "mobile"}, {"category_code": "software"}, 
                                                        
                                                       {"category_code": "web"}]}, {
    
    "name":1, "offices.city":1, "offices.latitude":1,
    "offices.longitude":1, "category_code":1}).limit(lim))
    
    return x




def city_df(df,x):

    '''
    The objective of this function is to take eht information from the object obtained with the previous function, and turn it into a dataframe 
    that we can use. 

    It takes as arguments a dataframe(the one created with the previous function) and x (name of the city). This last argument is required as there
    are some observations that have cities we are not interested in.

    Three empty lists are created: city, latitude, longitude. In these lists we are going to store the values of df.offices

    The function iterates thorugh the offices field after using the .get funtion. With a for loop, it identifies if the key is city, latitude 
    or longitude, ad stores the value in the corresponding list

    Afterwards, it adds this threes lists to the original df as new columns.

    Finally, there is a series of commands that clean the dataframe so that there are no problems in future commands.

    '''
    
    r = df.get("offices")
    
    city = []

    latitude = []

    longitude = []


    for i in r:

        for j,k in i[0].items():


                if j == 'city':

                    city.append(k)

                elif j == 'latitude':

                    latitude.append(k)

                elif j == 'longitude':

                    longitude.append(k)


    df["city"] = city

    df["latitude"] = latitude

    df["longitude"] = longitude
    
    df = df.drop(["offices"], axis = 1)
    
    df = df.drop(["_id"], axis = 1)
    
    df = df.drop(df[df.city != x].index)
    
    df = df.dropna(0, how = 'all', thresh = 4)

    return df


def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)

    
def places_df(objeto, category, rango):

    '''
    This function is used with the information extracted from the API. 

    It only requires the object in which we have stored the information extracted (using the extract function from api.py).

    Using the getFromDict function and a for loop, it iterates through the different observations and extracts the values of the name, 
    latitude and longitude of each observation. In the following command lines, we can see the hierarchy that the functon follows to get the wanted value.

    The values are stored in a new list of dictionaries that is then turned into a df

    Also, a column named category is created. In this colum we can check the category of the value (club, starbucks, airport), something we will use
    for creating the map. 

    '''
    
    mapa_nombre = ["venue","name"]
    latitud = ["venue", "location","lat"]
    longitud = ["venue","location","lng"]

    x = []
    
    for diccionario in objeto:
        lista = {}
        lista["name"] = getFromDict(diccionario,mapa_nombre)
        lista["latitud"] = getFromDict(diccionario,latitud)
        lista["longitud"] = getFromDict(diccionario,longitud)
        
        x.append(lista)
        
        df = pd.DataFrame(x)
        
    c = [category for _ in range(rango)]
        
    df["category"] = c

    return df


