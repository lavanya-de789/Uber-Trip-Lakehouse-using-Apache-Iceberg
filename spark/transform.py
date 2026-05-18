from pyspark.sql.functions import *

df=spark.read.format(
"iceberg"
).load(
"bronze.uber"
)

clean=df.filter(
col("trip_distance")>0
)

clean=clean.withColumn(
"trip_minutes",
(
unix_timestamp(
"dropoff_datetime")
-
unix_timestamp(
"pickup_datetime")
)/60
)

clean.write.format(
"iceberg"
).mode(
"overwrite"
).save(
"silver.uber")
