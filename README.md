# Azure retail sales Lakehouse

End-to-end Azure Data Engineering project implementing a Retail Sales Lakehouse using Azure Data Factory, Azure Data Lake Storage Gen2 (ADLS Gen2), Azure Databricks, PySpark, and SQL. The project features a metadata-driven ingestion framework based on the Medallion Architecture (Bronze, Silver, Gold).

## 🛠️ Tech Stack

* **Cloud Platform:** Microsoft Azure
* **Storage:** Azure Data Lake Storage Gen2 (ADLS Gen2)
* **Data Integration:** Azure Data Factory
* **Processing:** Azure Databricks
* **Languages:** PySpark, SQL
* **Architecture:** Medallion Architecture (Bronze, Silver, Gold)
* **File Formats:** CSV, Parquet


## 🚀 Project Progress

### Sprint 1 - Metadata-Driven Ingestion ✅

* Created Azure Data Lake Storage Gen2 with Bronze, Silver, and Gold containers.
* Designed a realistic retail sales dataset consisting of Customers, Products, Stores, Sales, and a metadata configuration file.
* Developed a metadata-driven Azure Data Factory pipeline using:

  * Lookup Activity
  * ForEach Activity
  * Parameterized Datasets
  * Copy Activity
* Successfully ingested Bronze CSV files into the Silver layer as Parquet files.

### Sprint 2 - Pipeline Control ✅

* Implemented metadata-based file activation using the `Is_Active` flag.
* Added an If Condition activity to dynamically control file ingestion.
* Verified that inactive datasets are skipped without modifying the pipeline.
