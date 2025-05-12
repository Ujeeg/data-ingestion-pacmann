#   Modular ETL Pipeline for Multi-Source Data Integration into PostgreSQL

    This project showcases my ability to design and implement a robust ETL (Extract, Transform, Load) pipeline to integrate data from diverse sources into a PostgreSQL database. The pipeline automates the extraction, transformation, and loading of data from PostgreSQL, JSON files, and Excel spreadsheets, addressing the challenge of data silos and enabling efficient data analysis. I focused on modularity, maintainability, and data quality throughout the development process.

##   Key Features

    * **Multi-Source Data Extraction:** Extracts data from PostgreSQL databases, JSON files, and Excel spreadsheets using Python and libraries like SQLAlchemy and Pandas. This demonstrates my ability to work with various data formats and sources.
    * **Modular ETL Architecture:** Implements a modular design with separate modules for each stage (extract, transform, load), promoting code reusability, maintainability, and scalability. This reflects my understanding of software engineering best practices.
    * **Data Transformation with Pandas:** Utilizes Pandas for efficient data cleaning, transformation, and aggregation, including data merging, filtering, and schema conversion. This highlights my data manipulation and analysis skills.
    * **Automated Data Processing:** Automates the entire ETL process using Python scripts, eliminating manual data handling and ensuring consistent data updates. This showcases my ability to build efficient and automated solutions.
    * **Robust Data Loading:** Loads transformed data into a PostgreSQL database (designed for NeonDB) using SQLAlchemy, with considerations for data integrity and efficient data storage.
    * **Configuration Management:** Employs environment variables for secure and flexible configuration of database credentials and file paths, adhering to security best practices.
    * **Database Schema Design:** Designed and implemented the PostgreSQL database schema using SQL to support the data requirements of the pipeline.

##   Directory Structure

    ```
    ├── src/
    │   ├── extract/         # Code for data extraction from various sources
    │   │   ├── extract_db.py     # Extracts data from PostgreSQL database
    │   │   ├── extract_excel.py  # Extracts data from Excel files
    │   │   ├── extract_json.py   # Extracts data from JSON files
    │   ├── transform/       # Code for data transformation
    │   │   ├── transform.py      # Transforms data using Pandas DataFrames
    │   ├── export/          # Code for exporting data
    │   │   ├── export_to_csv.py  # Exports DataFrames to CSV files
    │   ├── load/            # Code for loading data into the database
    │   │   ├── load_to_neon.py   # Loads data from CSVs to PostgreSQL (NeonDB)
    │   │   ├── script.sql        # SQL script to create database tables
    │   ├── extract_transform_export_data.py # Main script for ETL process
    │   ├── load_csv_to_db.py      # Main script to load CSVs to database
    ├── data_wrangling.ipynb  # Jupyter Notebook for data exploration and analysis
    ├── .env                  # Environment variables (not committed to repo)
    ├── README.md             # Documentation
    ```

##   Dependencies

    * Python 3.x
    * Libraries: `pandas`, `sqlalchemy`, `python-dotenv`
    * Install dependencies: `pip install -r requirements.txt` (It's recommended to create a `requirements.txt` file to list all dependencies)

##   Setup

    1.  **Environment Variables:**
        * Create a `.env` file in the root directory.
        * Populate it with your database connection details and file paths (see `.env.example` for an example structure).
        * **Important:** Do not commit the `.env` file to version control for security reasons.

    2.  **Database Setup:**
        * Execute the SQL script `src/script.sql` in your PostgreSQL database to create the required tables.

##   Usage

    1.  **Run ETL Pipeline:**
        * Execute the main ETL script to extract, transform, and export data:
            ```bash
            python src/extract_transform_export_data.py
            ```
        * This will generate CSV files in directories named with the current date.

    2.  **Load Data to Database:**
        * Execute the script to load the CSV files into the PostgreSQL database:
            ```bash
            python src/load_csv_to_db.py
            ```
        * Ensure that the file paths in this script are configured correctly.

##   Code Highlights

    * **`src/extract/`:**
        * Contains modules for extracting data from different sources (PostgreSQL, Excel, JSON).
        * Demonstrates my ability to handle various data formats and database connections.

    * **`src/transform/transform.py`:**
        * Implements data transformation logic using Pandas, showcasing my skills in data cleaning, manipulation, and feature engineering.
        * Includes functions for merging data, extracting information, and reshaping data for loading.

    * **`src/load/load_to_neon.py`:**
        * Handles loading transformed data into the PostgreSQL database, ensuring data integrity and efficient writing.
        * Includes functions for establishing database connections and managing table operations.

##   Reflection

    This project provided me with valuable hands-on experience in designing and building a complete ETL pipeline. The modular design proved to be highly beneficial for code organization and debugging, allowing for easier maintenance and future enhancements.

    One of the main challenges was handling data inconsistencies across different sources. I addressed this by implementing robust data validation and transformation rules within the transformation module. This experience reinforced the importance of data quality in ETL processes.
