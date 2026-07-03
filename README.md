# Azure Retail Sales Lakehouse

End-to-end Azure Data Engineering project implementing a Retail Sales Lakehouse using Azure Data Factory, Azure Data Lake Storage Gen2 (ADLS Gen2), Azure Databricks, PySpark, and SQL. The project features a metadata-driven ingestion framework based on the Medallion Architecture (Bronze, Silver, Gold).

# Project Architecture
<p align="center">
  <img src="architecture/lakehouse_architecture.drawio.png" alt="Azure Retail Sales Lakehouse Architecture" width="850"/>
</p>



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
| Sprint 4 – Bronze → Silver Transformation | ✅ Completed |
| Sprint 5 – Silver → Gold Transformation | ⬜ Planned |
| Sprint 6 – Data Serving & Optimization | ⬜ Planned |


## Sprint 1 - Metadata-Driven Ingestion ✅

* Created Azure Data Lake Storage Gen2 with Bronze, Silver, and Gold containers.
* Designed a realistic retail sales dataset consisting of Customers, Products, Stores, Sales, and a metadata configuration file.
* Developed a metadata-driven Azure Data Factory pipeline using:

  * Lookup Activity
  * ForEach Activity
  * Parameterized Datasets
  * Copy Activity
* Successfully ingested Bronze CSV files into the Silver layer as Parquet files.

  

## Sprint 2 - Pipeline Control ✅

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


## Products Bronze → Silver

- Read product data from Bronze layer (CSV)
- Applied explicit DDL schema
- Performed data profiling
    - Row Count
    - Null Value Analysis
    - Duplicate Record Analysis
- Implemented business rule validations
    - Product_ID should not be NULL
    - Product_ID should be unique
    - Product_Name should not be NULL
    - Product_Category should not be NULL
    - Product_SubCategory should not be NULL
    - Product_Brand should not be NULL
    - Product_Price should be greater than 0
    - Product_Unit should not be NULL
    - Product_Launch_Date should not be in the future
- Applied data standardization
    - Trimmed whitespace from text columns
- Wrote cleansed data to Silver layer in Parquet format
- Read Silver dataset back for validation
- Verified row counts

### Validation Summary

| Layer | Row Count |
|--------|----------:|
| Bronze | 1000 |
| Silver | 1000 |

✅ No data loss during transformation.


 ## Stores Bronze → Silver
- Read store data from Bronze layer (CSV)
- Applied explicit DDL schema
- Performed data profiling
    - Row Count
    - Null Value Analysis
    - Duplicate Record Analysis
- Implemented business rule validations
    - Store_ID should not be NULL
    - Store_ID should be unique
    - Store_Name should not be NULL
    - Country should not be NULL
    - State should not be NULL
    - City should not be NULL
    - Store_Type should not be NULL
    - Employee_Count should be greater than 0
    - Opening_Date should not be in the future
- Applied data standardization
    - Trimmed whitespace from text columns
- Wrote cleansed data to Silver layer in Parquet format
- Read Silver dataset back for validation
- Verified row counts

### Validation Summary

| Layer | Row Count |
|--------|----------:|
| Bronze | 100 |
| Silver | 100 |

✅ No data loss during transformation.


## Technologies Used

- Azure Data Lake Storage Gen2
- Azure Databricks
- Unity Catalog
- PySpark
- Parquet
- Azure Managed Identity
- External Locations

- ## Sales Bronze -> Silver 

Implemented the complete Sales Bronze to Silver ETL pipeline using Azure Databricks and PySpark.

### Key Features

- Read Sales data from Bronze layer (CSV)
- Applied explicit schema for data consistency
- Performed data profiling
  - Record count
  - Null value analysis
  - Duplicate analysis

### Data Quality Validations

- Duplicate record removal
- Mandatory field validation
- Numeric validation
  - Quantity > 0
  - Unit Price > 0
  - Discount Amount ≥ 0
- Date validation
  - Sale_DateTime should not be in the future
- Domain validation
  - Payment Method
  - Order Status

### Referential Integrity

Validated Sales records against Silver master datasets using PySpark joins:

- Customer validation
- Product validation
- Store validation

### Business Enrichment

Created derived business columns:

- Gross_Price = Quantity × Unit_Price
- Final_Price = Gross_Price − Discount_Amount

### Output

- Cleaned dataset written to Silver layer in Parquet format
- Post-write validation performed by comparing row counts and verifying sample records

### Technologies

- Azure Databricks
- PySpark
- Azure Data Lake Storage Gen2
- Parquet

  


