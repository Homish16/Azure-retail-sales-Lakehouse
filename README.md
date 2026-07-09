# Azure Retail Sales Lakehouse

End-to-end Azure Data Engineering project implementing a Retail Sales Lakehouse using Azure Data Factory, Azure Data Lake Storage Gen2 (ADLS Gen2), Azure Databricks, PySpark, and SQL. The project features a metadata-driven ingestion framework based on the Medallion Architecture (Bronze, Silver, Gold).


# Project Architecture

<p align="center">
  <img src="Architecture/lakehouse_architecture.drawio.png" alt="Architecture" width="900"/>
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

- ## Sprint 4 Completion – Bronze to Silver Layer

Completed the Bronze to Silver implementation for all four datasets (Customers, Products, Stores, and Sales).

### Sales Bronze → Silver Pipeline

Implemented the complete Sales transformation pipeline using Azure Databricks and PySpark.

#### Data Processing

- Read Sales data from Bronze layer
- Applied explicit schema
- Performed data profiling
- Duplicate record analysis
- Mandatory field validation
- Numeric validation
- Date validation
- Customer referential integrity validation
- Product referential integrity validation
- Store referential integrity validation
- Business enrichment
  - Gross_Price
  - Final_Price
- Domain validation
- Wrote cleansed data to Silver layer in Parquet format
- Performed post-write validation

### Project Documentation

- Added Bronze to Silver notebooks to GitHub
- Created project architecture diagram using draw.io
- Embedded architecture diagram in README
- Improved notebook documentation and markdown structure
- Cleaned notebook by removing unnecessary debugging cells

### Current Project Status

- ✅ Metadata-Driven Ingestion
- ✅ Bronze Layer
- ✅ Silver Layer
- ⏳ Gold Layer (Next Sprint)

### Technologies

- Azure Databricks
- PySpark
- Azure Data Lake Storage Gen2
- Parquet

## Sprint 5 – Gold Layer Development (Part 1): Date Dimension

### Objective
Started the Gold Layer implementation by building the Date Dimension (`dim_date`) from the Silver Sales dataset. The objective was to create a reusable calendar dimension for analytical reporting and Power BI dashboards.

### Tasks Completed

- Created notebook: `05-Date-Dimension-Silver-to-Gold`
- Read Sales data from Silver Layer (Parquet).
- Calculated minimum and maximum sales dates using aggregate functions.
- Generated a complete calendar using:
  - `sequence()`
  - `explode()`
- Built the Date Dimension with the following attributes:
  - Date
  - Date_Key (YYYYMMDD)
  - Year
  - Quarter
  - Month_Number
  - Month_Name
  - Week_Number
  - Day_Number
  - Day_Name
  - Is_Weekend
- Applied business logic to identify weekends.
- Performed data quality validation:
  - Row Count
  - Null Check
  - Duplicate Check
  - Schema Validation
- Successfully wrote the Date Dimension to the Gold Layer and validated the output.

### Key Learnings

- Difference between Spark DataFrames, Row objects and Python objects.
- Practical usage of:
  - `sequence()`
  - `explode()`
  - `date_format()`
  - `year()`
  - `quarter()`
  - `month()`
  - `weekofyear()`
  - `dayofmonth()`
  - `dayofweek()`
  - `when()` / `otherwise()`
- Understood why Date Dimensions are essential in dimensional modeling.
- Learned that Spark DataFrames are immutable while Python variables can be reassigned to newer DataFrame references.
- Discussed enterprise coding practices such as maintaining a single DataFrame variable through chained transformations.

- Developed the Gold Product,Store and Customer Dimension (dim_product,dim_store & dim_customer) from the Silver layer.
- Performed schema validation, sample data validation, row count, null value analysis, and duplicate key validation.
- Identified 14 NULL values in Product_Brand and retained them due to the absence of business rules or trusted reference data for imputation.
- Performed product price profiling using descriptive statistics and derived a new business attribute Price_Category using quartile-based thresholds (Budget, Standard,       Premium, Luxury).
- Validated the derived Price_Category distribution (250 products in each category) and successfully published the Product Dimension to the Gold layer.
- Reviewed and standardized Customer, Store, and Product Gold notebooks for consistent ETL structure and validation practices.
