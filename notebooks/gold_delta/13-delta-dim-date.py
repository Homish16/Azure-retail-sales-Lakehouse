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
GOLD_DIM_DATE_PATH = GOLD_BASE_PATH +"dim_date"
GOLD_DELTA_DATE_PATH = GOLD_DELTA_PATH +"dim_date"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Reading Gold Layer Data

# COMMAND ----------

df_delta_date = spark.read.format("parquet").load(GOLD_DIM_DATE_PATH)
df_delta_date.display()

# COMMAND ----------

df_delta_date.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Write to Delta

# COMMAND ----------

(
df_delta_date.write.format("delta")
.mode("overwrite")
.save(GOLD_DELTA_DATE_PATH)
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Validate Delta

# COMMAND ----------

dbutils.fs.ls(GOLD_DELTA_PATH)
dbutils.fs.ls(GOLD_DELTA_DATE_PATH)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Post Migration Validation: Row count,schema validation and sample records

# COMMAND ----------

df_delta_date = spark.read.format("delta").load(GOLD_DELTA_DATE_PATH)
df_delta_date.count()

# COMMAND ----------

df_delta_date.printSchema()
display(df_delta_date.limit(10))

# COMMAND ----------

