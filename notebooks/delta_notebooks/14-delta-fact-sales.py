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
GOLD_FACT_SALES_PATH = GOLD_BASE_PATH +"fact_sales"
GOLD_DELTA_SALES_PATH = GOLD_DELTA_PATH +"fact_sales"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Read Gold Parquet Data

# COMMAND ----------

df_fact_sales = spark.read.format("parquet").load(GOLD_FACT_SALES_PATH)
display(df_fact_sales.limit(20))
df_fact_sales.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Write to Delta Table

# COMMAND ----------

(df_fact_sales.write
.format("delta")
.mode("overwrite")
.save(GOLD_DELTA_SALES_PATH))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Verifying Delta

# COMMAND ----------

dbutils.fs.ls(GOLD_FACT_SALES_PATH)
dbutils.fs.ls(GOLD_DELTA_SALES_PATH)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Post Migration Validation: row count, schema validation & sample records display

# COMMAND ----------

df_delta_sales = spark.read.format("delta").load(GOLD_DELTA_SALES_PATH)
display(df_delta_sales.limit(20))
df_delta_sales.printSchema()
df_delta_sales.count()

# COMMAND ----------

