from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local').appName("pyspark-read-csv").getOrCreate()

df = spark.read.csv( "datasets/csv/accounts.csv", inferSchema=True, header=True )
df_addr = spark.read.csv( "datasets/csv/address.csv", inferSchema=True, header=True )

#method 1
tableJoin = [df.accountno == df_addr.accountno]
join_df = df.join(df_addr,tableJoin,'left')
join_df = join_df.drop('accountno')

df.show()
df_addr.show()
join_df.show()

#method 2
df.join(df_addr,    
               df.accountno == df_addr.accountno,
               "inner").drop(df.accountno).show()

