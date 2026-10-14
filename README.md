Transport\_Weather\_Service\_Alert

Impact of Severe weather events(rain, snow, extreme heat) on the local subway/bus schedule

**The Datasets:**

- GTFS aka the public transit data like NYC MTA/TFL \- i want to try making one for Nepal or an earthquake one for Japan or Bhutan or Mumbai Floods.  
  * [Transitland • Browse places: Tokyo, Tokyo, Japan](https://www.transit.land/places/Japan/Tokyo/Tokyo)   
  * [croyla/mumbai-gtfs: GTFS feed for bus operators in Mumbai and surrounding regions (BEST, TMT, KDMT)](https://github.com/croyla/mumbai-gtfs)   
  * [KDMT) GTFS Schedule Feed \- Mobility Database](https://mobilitydatabase.org/feeds/gtfs/mdb-3138)   
- Historical Weather data \- Open-Meteo API/ NOAA

**Problem Statement:**

* A scheduled daily pipeline,   
  * **Extract** \- Transit logs for stop and delays in public transport whilst matching them with weather observations at regular intervals (1 hour recommended)  
  * **Transform** \-   
    * ID missing values and clean data  
    * Aggregate metrics? \- calculate average delay time in mins for every transit route.  (e.g., sensors going offline during severe storms).  
    * Write transformed data in a db format (like parquet?) divided by year, month and route

**Key Engineering Challenges:**

- Time-series alignment (joining data points timestamped at irregular intervals, e.g., matching a train arriving at 08:14 AM with hourly weather at 08:00 AM).  
  - Designing an efficient file partitioning strategy (avoiding the "small file problem" in storage lakes).

