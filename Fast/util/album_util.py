import fetch_data
import Constants
import pandas as pd
import json

def album_data():

    my_list=fetch_data.get_db_data(Constants.album_query)

    df = pd.DataFrame(my_list, columns=['AlbumId', 'Title','ArtistId'])
    json_df=df.to_json(orient=Constants.records)
    parsed=json.loads(json_df)
    
    return parsed
