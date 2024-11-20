# large file log_file csv file in 10 gb -
# datetime, logtype, event, userid, transaction_id

# how many number of records by logtype
# how many records generated per hour basis


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, date_format, to_timestamp
spark = SparkSession.builder.appName(name="Log Analysis").getOrCreate()

# reading the file
df = spark.read.csv(path="C:/Users/91702/Desktop/log.csv", header=True, inferSchema=True)

df.printSchema()
df = df.withColumn("datetime", to_timestamp(col("datetime"), "dd-MM-yyyy HH:mm:ss"))
# performing aggregation on grouped data by logtype
logtype_counts = df.groupBy("logtype").count()
print("Logtype Counts:")
logtype_counts.show()

# Count records generated per hour
hourly_counts = df.withColumn("hour", date_format(col("datetime"), "yyyy-MM-dd HH:00")) \
                       .groupBy("hour").count() \
                       .orderBy("hour")

print("Hourly Counts:")
hourly_counts.show()