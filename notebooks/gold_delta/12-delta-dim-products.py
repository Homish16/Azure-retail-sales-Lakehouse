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
GOLD_DIM_PRODUCT_PATH = GOLD_BASE_PATH +"dim_product"
GOLD_DELTA_PRODUCT_PATH = GOLD_DELTA_PATH +"dim_product"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Reading Gold Parquet Data

# COMMAND ----------

df_delta_product = spark.read.format("parquet").load(GOLD_DIM_PRODUCT_PATH)
display(df_delta_product.limit(10))
df_delta_product.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Write to Delta

# COMMAND ----------

df_delta_product.write.format("delta").mode("overwrite").save(GOLD_DELTA_PRODUCT_PATH)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Validate Delta

# COMMAND ----------

dbutils.fs.ls(GOLD_DELTA_PATH)
dbutils.fs.ls(GOLD_DELTA_PRODUCT_PATH)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Read Delta Table

# COMMAND ----------

df_delta_product=spark.read.format("delta").load(GOLD_DELTA_PRODUCT_PATH)
display(df_delta_product.limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Post Migration Validation: Row Count,Schema validation, displaying sample records

# COMMAND ----------

df_delta_product.count()

# COMMAND ----------

df_delta_product.printSchema()
display(df_delta_product.limit(20))