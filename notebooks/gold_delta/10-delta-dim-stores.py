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
# MAGIC ### Configurations

# COMMAND ----------

GOLD_BASE_PATH   = "abfss://gold@stretaillakehouse01.dfs.core.windows.net/"
GOLD_DELTA_PATH = "abfss://gold-delta@stretaillakehouse01.dfs.core.windows.net/"
GOLD_DIM_STORE_PATH = GOLD_BASE_PATH +"dim_store"
GOLD_DELTA_DIM_STORE_PATH = GOLD_DELTA_PATH +"dim_store"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Reading Gold Parquet Data

# COMMAND ----------

df_dim_store = spark.read.format("parquet").load(GOLD_DIM_STORE_PATH)
df_dim_store.show()

# COMMAND ----------

df_dim_store.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Write Delta Table

# COMMAND ----------

(
    df_dim_store.write
    .mode("overwrite")
    .format("delta")
    .save(GOLD_DELTA_DIM_STORE_PATH)
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Validate Delta

# COMMAND ----------

dbutils.fs.ls(GOLD_DELTA_PATH)
dbutils.fs.ls(GOLD_DELTA_DIM_STORE_PATH)

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### Reading Delta Table

# COMMAND ----------

df_delta_store = (
    spark.read
    .format("delta")
    .load(GOLD_DELTA_DIM_STORE_PATH)
)

display(df_delta_store)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Verification after migration to Delta format. Checking row count, validating schema, verifying few records

# COMMAND ----------

df_delta_store.count()

# COMMAND ----------

df_delta_store.printSchema()

# COMMAND ----------

display(df_delta_store.limit(10))