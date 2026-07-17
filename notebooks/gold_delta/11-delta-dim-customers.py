# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook Objective
# MAGIC
# MAGIC ### Convert the Gold Parquet table to Delta format in the gold-delta container and validate the migration by verifying storage structure, schema, row count, and sample records.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Imports

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC ### Configuration

# COMMAND ----------

GOLD_BASE_PATH   = "abfss://gold@stretaillakehouse01.dfs.core.windows.net/"
GOLD_DELTA_PATH = "abfss://gold-delta@stretaillakehouse01.dfs.core.windows.net/"
GOLD_DIM_CUSTOMER_PATH = GOLD_BASE_PATH +"dim_customer"
GOLD_DELTA_CUSTOMER_PATH = GOLD_DELTA_PATH +"dim_customer"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Reading Gold Parquet Data

# COMMAND ----------

df_dim_customer = spark.read.format("parquet").load(GOLD_DIM_CUSTOMER_PATH)
display(df_dim_customer.limit(10))
df_dim_customer.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Write to Delta Table

# COMMAND ----------

(df_dim_customer.write.format("delta").mode("overwrite").save(GOLD_DELTA_CUSTOMER_PATH))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Validate Delta

# COMMAND ----------

dbutils.fs.ls(GOLD_DELTA_PATH)
dbutils.fs.ls(GOLD_DELTA_CUSTOMER_PATH)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Read Delta Table

# COMMAND ----------

df_dim_customer = spark.read.format("delta").load(GOLD_DELTA_CUSTOMER_PATH)
df_dim_customer.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Migration Validation: row count, schema validation, sample records

# COMMAND ----------

df_dim_customer.count()

# COMMAND ----------

df_dim_customer.printSchema()

# COMMAND ----------

display(df_dim_customer.limit(10))