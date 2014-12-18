"""
Map.py
Parse data from a csv file into a geoJSON object and plot to map
"""
import geojson

import parse as p

def create_map(data_file):
    #Define the type of GeoJSON we're creating
    geo_map = {"type": "FeatureCollection"}

    #Define the empty list to collect each point to graph
    item_list = []

    #Iterate over our data to create GeoJSON document.
    #We're using enumerate() so we get the line, as well
    #the index, which is the line number
    for index, line in enumerate(data_file):

        #Skip any zero coordinate as this will throw off the map
        if line['X'] == "0" or line['Y'] == "0":
            continue

        #Setup a new dictionary for each iteration
        data = {}

        #Assign line items to appropiate GeoJSON fields
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],'description': line['Descript'],'data': line['Date']}
        data['geometry'] = {'type': 'Point','coordinates': (line['X'],line['Y'])}

        #Add data dictionary to our item_list
        item_list.append(data)

    #For each point in our item_list, we add the point to our
    #dictionary. setdefault creates a key called 'features' that
    #has a value type of an empty list. With each iteration, we
    #are appending our point to that list.
    for point in item_list:
        geo_map.setdefault('features', []).append(point)

    #Now that all data is parsed in GeoJSON write it to a file so we
    #can upload it to gist.github.com
    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))

def main():
    data = p.parse(p.MY_FILE,",")

    return create_map(data)

if __name__ == "main":
    main()
