Project Title: E-commerce Data Engineering with Snowflake
Project Overview
The goal of this project is to design and implement a data engineering pipeline that ingests, transforms, and analyzes e-commerce data using Snowflake as the data warehouse. You will leverage public datasets from Kaggle to simulate real-world scenarios and create a robust data architecture for analytics.
Project Structure and Tools Overview

1.Data Source

   - Kaggle E-commerce Dataset (Olist Brazilian E-Commerce): You’ll use a dataset containing multiple tables (Orders, Customers, Products, etc.) for analysis.

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
   
2. Tools:
   - Apache Airflow: To automate and orchestrate the ETL pipeline.
   - Snowflake: For data storage and layered architecture (Bronze, Silver, Gold).
   - Tableau or Power BI: For data visualization and business insights.
   - GitHub: For version control and code management.

 Detailed Project Steps

 1. Initial Setup and Data Acquisition
   - Set Up GitHub Repository: Create a repository for code and configuration files.
   - Download Dataset: Retrieve the dataset from Kaggle and upload it to a staging area, preparing it for ingestion.

 2. Data Ingestion (Bronze Layer)
   - Data Loading to Snowflake:
     - Objective: Load raw data from Kaggle into Snowflake’s Bronze layer.
     - Steps:
       1. Create Snowflake staging tables for each dataset table (Orders, Customers, etc.).
       2. Write an Airflow DAG to automate loading raw files directly into Snowflake.
   
 3. Data Cleaning and Standardization (Silver Layer)
   - Objective: Clean, deduplicate, and standardize data in Snowflake.
   - Steps:
     1. Write transformations in Snowflake to perform tasks such as:
        - Removing duplicates in Orders or Customers tables.
        - Standardizing date and currency formats.
        - Handling missing values where feasible.
     2. Load cleaned data into Snowflake’s Silver layer tables.
     3. Perform additional quality checks and transformations to ensure consistent data types and format.

4. Aggregation and Enrichment (Gold Layer)
   - Objective: Create analysis-ready tables that aggregate and enrich data for business insights.
   - Steps:
     1. Use Snowflake to execute complex transformations, including:
        - Joining tables to enrich data (e.g., linking Orders with Customers).
        - Calculating metrics like customer lifetime value, average order value, and monthly sales trends.
     2. Store transformed data in Gold layer tables in Snowflake.
     3. Perform final checks for consistency and completeness in this layer to ensure it’s ready for analysis.

 5. Data Analysis and Visualization
   - Objective: Visualize the processed data and extract insights.
   - Steps:
     1. Connect Tableau or Power BI to Snowflake’s Gold layer.
     2. Create dashboards to visualize key insights, such as:
        - Sales Trends: Monthly or seasonal trends to understand peak periods.
        - Customer Segmentation: Based on demographics, purchase history, and lifetime value.
        - Product Analysis: Top products, product category performance, etc.
        - Operational Metrics: Delivery times, customer satisfaction, and feedback analysis.
        
 6. Version Control and Collaboration
   - Objective: Maintain project files and code using GitHub for version control.
   - Steps:
     1. Push code to GitHub after setting up the initial repository.
     2. Organize your project structure by categorizing Airflow DAGs, transformation scripts, SQL queries, and any configuration files.
     3. Update the repository as transformations or visualizations are refined, with commit messages documenting changes.


Expected Outcomes

Business Insights: Key metrics like customer lifetime value, sales trends, and product performance will be visible in your dashboards.

Automated ETL Workflow: Apache Airflow will orchestrate and automate the ETL process, making it easy to rerun or schedule as new data is added.

Layered Data Structure: Snowflake will host clean, organized data in Bronze, Silver, and Gold layers, making it easy to track data quality and transformations.

- Version-Controlled Code: GitHub will store the codebase, transformation scripts, and documentation, aiding reproducibility and collaboration.

Flow chart
Kaggle (Data Source)
      ⬇️
Apache Airflow (ETL Orchestration)
      ⬇️
Bronze Layer in Snowflake (Raw Data Storage)
      ⬇️
Silver Layer in Snowflake (Standardized, Cleaned Data)
      ⬇️
Gold Layer in Snowflake (Enriched, Analysis-Ready Data)
      ⬇️
Data Visualization in Tableau/Power BI (Connected to Gold Layer)
⬅️    ⬆️
         GitHub (Version Control for Code & Scripts)






Flow chart Explanation

Here’s a brief explanation of each stage in your data pipeline:


1. Kaggle (Data Source)  
   - Action: Download the e-commerce dataset, which contains various tables, like Orders, Products, and Customers.

2. Apache Airflow (ETL Orchestration)  
   - Action: Use Airflow to manage ETL workflows, automating data movement and initial transformations.

3. Bronze Layer in Snowflake (Raw Data Storage)  
   - Action: Load raw data into Snowflake’s Bronze Layer for storage, preserving its original form.

4. Silver Layer in Snowflake (Cleaned Data)  
   - Action: Store cleaned and standardized data in the Silver Layer for further processing.

5. Gold Layer in Snowflake (Enriched Data)  
   - Action: Store final, analysis-ready data in the Gold Layer.

6. Data Visualization (Tableau or Power BI)  
   - Action: Connect visualization tools to the Gold Layer to build dashboards and insights.

7. GitHub (Version Control)  
   - Action: Store all Airflow scripts, DAGs, and documentation on GitHub for version control and project management. 

This structure streamlines data processing from ingestion to analysis, with GitHub supporting development tracking.









GIT HUB DOCUMENTATION:

ecommerce-etl-project/
├── dags/                       Airflow DAGs
│   ├── ecommerce_etl_dag.py
│   └── utils/                  Optional: Utility functions for transformations
├── sql/                        SQL files for transformations
│   ├── bronze_to_silver.sql
│   ├── silver_to_gold.sql
│   └── create_tables.sql
├── scripts/                    Python scripts for data extraction or transformations
│   ├── data_extraction.py
│   └── data_transformation.py
├── requirements.txt            Python dependencies
├── README.md                   Project documentation
└── .gitignore                  Ignore files you don’t want to push to GitHub


Commands used for installing and creating the apache airflow 

cd ~/Documents/E-commerce_project. -        # Navigate to the project directory

python3 -m venv venv -                                   # Create virtual environment named `venv`

source venv/bin/activate -                              # Activate the virtual environment
conda activate airflow-env

export AIRFLOW_VERSION=2.6.3

export PYTHON_VERSION=3.10.15

export CONSTRAINT_URL=“https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint “${CONSTRAINT_URL}”.                                        # Install Apache Airflow

pip install apache-airflow-providers-snowflake.     # Install Snowflake provider for Airflow
airflow db init           # Initialize the Airflow database (run if not already initialized)

airflow db check.                     # Check if the Airflow database is connected successfully

airflow users create --username <your-username> --firstname <Your-First-Name> --lastname <Your-Last-Name> --role Admin --email <your-email>

airflow webserver --port 8080          # Start the Airflow web server


# In a new terminal window, activate your environment and start the scheduler
airflow scheduler

ps aux | grep airflow                     # List Airflow processes

kill  -9 <Process-ID>                      # Kill specific Airflow processes

cd ~/airflow         # To airflow directory

nano airflow.cfg                #to edit config file


Versions Used
Python: 3.10
Airflow: 2.6.3
Snowflake Provider: 5.8.0


 
Credentials:  AIRFLOW:   Prasad24/Dolbyatmos@24
MYSQL :  Prasad/6855
Snowflake: Sprasad245/ Dolbyatmos@24  

Airflow to snowflake connection:

user='SPRASAD245', 
password='<your_password>', 
account=‘IFGIGDD-OF30041', 
warehouse='<your_warehouse>', 
database='<your_database>', 
schema='<your_schema>'



Airflow to MySQL connection:


cd ~/airflow         # To airflow directory
nano airflow.cfg                #to edit config file




