from pyspark.sql import *
from datetime import datetime
spark = SparkSession\
    .builder\
        .master('local')\
        .appName("pyspark-section-data-standardization")\
        .getOrCreate()
df_read = spark.read.csv("accounts.csv",header = True,inferSchema=True)
df_read1 = df_read.
df_read.show()
#df = spark.sql("select * f""
 #              WITH Ajay_1 As())