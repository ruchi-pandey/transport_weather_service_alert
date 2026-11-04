import osmnx as ox
import pandas as pd

place = "Kathmandu, Nepal"

# Broad tag set: catches bus stops, platforms, stations, and route stops
tags = {
    "public_transport":["stop_position","platform","station"],
    "highway": ["bus_stop"],
    "amenity":["bus_stop"],
    "railway": ["station","halt","tram_stop"]
}

gdf = ox.features_from_place(place, tags=tags)

# Keep only point features (platforms/ways would give polygon centroids)
gdf = gdf[gdf.geometry.geom_type == "Point"]

#Pull lat/lon
gdf=gdf.to_crs(epsg=4326)
gdf["lat"]=gdf.geometry.y
gdf["lon"]=gdf.geometry.x

# Pull a usable name (OSM name tags vary; fall back through common keys)
def pick_name(row):
    for key in ("name", "name:en", "name:ne","ref", "operator"):
        val = row.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()
    return None
    
gdf["stop_name"] = gdf.apply(pickname, axis=1)