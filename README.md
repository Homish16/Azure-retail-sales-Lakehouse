# Azure Retail Sales Lakehouse

End-to-end Azure Data Engineering project implementing a Retail Sales Lakehouse using Azure Data Factory, Azure Data Lake Storage Gen2 (ADLS Gen2), Azure Databricks, PySpark, and SQL. The project features a metadata-driven ingestion framework based on the Medallion Architecture (Bronze, Silver, Gold).

## 🛠️ Tech Stack

* **Cloud Platform:** Microsoft Azure
* **Storage:** Azure Data Lake Storage Gen2 (ADLS Gen2)
* **Data Integration:** Azure Data Factory
* **Processing:** Azure Databricks
* **Languages:** PySpark, SQL
* **Architecture:** Medallion Architecture (Bronze, Silver, Gold)
* **File Formats:** CSV, Parquet

## 📌 Project Progress

| Sprint | Status |
|---------|--------|
| Sprint 1 – Metadata Driven Ingestion | ✅ Completed |
| Sprint 2 – Incremental Loading | ✅ Completed |
| Sprint 3 – Metadata & Watermark Framework | ✅ Completed |
| Sprint 4 – Bronze → Silver Transformation | 🚧 In Progress |
| Sprint 5 – Silver → Gold Transformation | ⬜ Planned |
| Sprint 6 – Data Serving & Optimization | ⬜ Planned |

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

  

## Sprint 3 – Azure SQL Metadata Framework

### Features Implemented

* Created Azure SQL Server and Azure SQL Database.
* Designed `watermark_metadata` table for runtime metadata.
* Configured Azure SQL Linked Service and Dataset in ADF.
* Implemented dynamic watermark lookup using Lookup Activity.
* Refactored the pipeline into a Parent–Child architecture using Execute Pipeline activity.

  

## 🚀 Sprint 4 – Bronze to Silver Transformation

## Objective

Transform raw Bronze datasets into clean, validated and analytics-ready Silver datasets using PySpark in Azure Databricks.

---

## Customers Dataset ✅

### Tasks Completed

- Read customer data from Bronze layer (CSV)
- Applied explicit DDL schema
- Performed data profiling
    - Row Count
    - Null Value Analysis
    - Duplicate Record Analysis
- Implemented business rule validations
    - Customer_ID should not be NULL
    - Customer_ID should be unique
    - First_Name should not be NULL
    - Last_Name should not be NULL
    - Customer_Segment should not be NULL
    - Registration_Date should not be in the future
    - Email format validation
- Applied data standardization
    - Trimmed whitespace from text columns
- Wrote cleansed data to Silver layer in Parquet format
- Read Silver dataset back for validation
- Verified row counts

### Validation Summary

| Layer | Row Count |
|--------|----------:|
| Bronze | 5000 |
| Silver | 5000 |

✅ No data loss during transformation.


## Technologies Used

- Azure Data Lake Storage Gen2
- Azure Databricks
- Unity Catalog
- PySpark
- Parquet
- Azure Managed Identity
- External Locations

  

## Sprint 4 Progression


Sprint 4

✅ Customers: Bronze -> Silver
✅ Products: Bronze -> Silver
✅ Stores: Bronze -> Silver
🚧 Sales
