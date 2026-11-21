import osmnx as ox
import pandas as pd

place = "Kathmandu, Nepal"

# Broad tag set: catches bus stops, platforms, stations, and route stops
tags = {
    "public_transport": ["stop_position", "platform", "station"],
    "highway": ["bus_stop"],
    "amenity": ["bus_station"],
    "railway": ["station", "halt", "tram_stop"],
}

gdf = ox.features_from_place(place, tags=tags)

# Keep only point features (platforms/ways would give polygon centroids)
gdf = gdf[gdf.geometry.geom_type == "Point"]

# Pull lat/lon
gdf = gdf.to_crs(epsg=4326)
gdf["lat"] = gdf.geometry.y
gdf["lon"] = gdf.geometry.x

# Pull a usable name (OSM name tags vary; fall back through common keys)
def pick_name(row):
    for key in ("name", "name:en", "name:ne", "ref", "operator"):
        val = row.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()
    return None

gdf["stop_name"] = gdf.apply(pick_name, axis=1)

# Build a stops.txt-shaped frame
stops = pd.DataFrame({
    "stop_id": gdf.index.map(lambda i: f"OSM_{i[0]}_{i[1]}"),  # OSM type + id
    "stop_name": gdf["stop_name"],
    "stop_lat": gdf["lat"],
    "stop_lon": gdf["lon"],
})

# Drop nameless duplicates / rows you can't label
stops = stops.dropna(subset=["stop_name"]).drop_duplicates(subset=["stop_lat", "stop_lon"])

print(f"{len(stops)} stops")
print(stops.head())

stops.to_csv("stops.txt", index=False)