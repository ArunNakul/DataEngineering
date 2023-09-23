#Supported join types include: 'inner', 'outer', 'full', 'fullouter', 'full_outer',
# 'leftouter', 'left', 'left_outer', 'rightouter', 'right', 'right_outer', 'leftsemi', 
#'left_semi', 'semi', 'leftanti', 'left_anti', 'anti', 'cross'.

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.master('local').appName('dfanti').getOrCreate()

df = spark.read.csv("datasets/csv/accounts.csv",header = True,inferSchema = True)
df_addr = spark.read.csv("datasets/csv/address.csv",header = True,inferSchema = True)
df.show()
df_addr.show()
df.join(df_addr,df_addr.accountno == df.accountno,'leftanti').show()

df.join(df_addr,df_addr.accountno == df.accountno,'left_anti').show()



