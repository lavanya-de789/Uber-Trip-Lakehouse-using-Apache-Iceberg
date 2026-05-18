gold=spark.sql("""

select

pickup_location,

avg(fare_amount) avg_fare,

count(*) total_trips

from silver.uber

group by pickup_location

""")

gold.write.format(
"iceberg"
).save(
"gold.trip_metrics")
