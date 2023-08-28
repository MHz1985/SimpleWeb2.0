import folium 
import numpy as np 
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from folium.plugins import MarkerCluster
from folium import plugins

# path_to_xls = "data/Hospital Rankings.xlsx"

def creat_simple_map(width = 600 , height = 400):
    m = folium.Map()

    # set the iframe width and height
    m.get_root().width = f"{width}px"
    m.get_root().height = f"{height}px"
    iframe = m.get_root()._repr_html_()
    return iframe

def get_df(sheet,path_to_xls):
  df = pd.read_excel(path_to_xls, sheet_name=sheet) # reading df
  xls = pd.ExcelFile(path_to_xls)
  all_sheet_names = xls.sheet_names
  if len (df)>0 and (sheet in all_sheet_names):
    return df # getting all unique categories
  else:
    return
# OpenStreetMap      Stamen Toner 
def create_map_from_new_xls(sheet,path_to_xls,starting_location=[10, 10],
                            popup_text_col = 'Hospital',height = 600, width = 800, 
                            tile_type="Stamen Toner", zoom_start=1):
  df = get_df(sheet,path_to_xls=path_to_xls)
  map = folium.Map(location=starting_location, zoom_start=zoom_start, tiles=tile_type)
  marker_cluster = plugins.MarkerCluster().add_to(map)
  map.get_root().width = f"{width}px"
  map.get_root().height = f"{height}px"
  for index, row in df.iterrows():
      if (str(row['Latitude']) != 'nan') and (str(row['Longitude']) != 'nan'): 
        folium.Marker(location=(row['Latitude'],row['Longitude']),
                            radius= 10,
                            color="#007849",
                            popup=row[popup_text_col],
                            fill=False).add_to(marker_cluster)
  return map.get_root()._repr_html_()

def get_all_but_lat_lng(sheet,path_to_xls):
    df=get_df(sheet,path_to_xls)
    df_new=df.drop(['Latitude', 'Longitude'],axis=1)
    df_new.index = np.arange(1,len(df)+1)
    return df_new