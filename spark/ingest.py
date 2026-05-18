from pyspark.sql import SparkSession

spark=(SparkSession.builder
.appName("UberBronze")
.getOrCreate())

df=spark.read.csv(
"data/raw/uber.csv",
header=True
)

df.write.format(
"iceberg"
).mode(
"overwrite"
).save(
"bronze.uber"
)
