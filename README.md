# PostgreSQL Web Application Deployment on Azure

This guide will walk you through deploying a Flask application that connects to a PostgreSQL database to Azure.

## Prerequisites

1. **Azure Account:** Sign up for an Azure account if you haven't already.
2. **Azure CLI:** Install Azure Command-Line Interface (CLI) on your local machine.
3. **PostgreSQL Database:** Create a PostgreSQL database on Azure and note down the connection details.

## Steps to Deploy

1. **Prepare Your Flask App:**
   - Ensure your Flask application runs locally without errors.
   - Create a `requirements.txt` file listing all dependencies.

2. **Create PostgreSQL Database on Azure:**
   - Navigate to the Azure Portal.
   - Create a new PostgreSQL database.
   - Note down the connection details.

3. **Deploy Flask App:**
   - Open Azure CLI and log in to your Azure account.
   - Navigate to your Flask app directory.
   - Run the following command to create a new web app:
     ```
     az webapp up --name <your_app_name> --sku F1 --location <your_region>
     ```
   - Choose Python as the runtime stack during deployment.

4. **Configure Environment Variables:**
   - In the Azure Portal, go to your web app's Configuration settings.
   - Add environment variables for your PostgreSQL connection.

5. **Access Your Streamlit App:**
   - Once deployment is complete, your Streamlit app will be accessible via the URL provided by Azure.

## Reflection
1. I learned a lot, especially on how to use dBeaver to connect with PostgreSQL in azure. My main challenge was because several row consists of long elements which resulted in upload issues.
2. I learned that I always have to make sure my code reads the right table in PostgreSQL, including all the column names.
3. Even until now, I'm not sure whether the issue lies on the front-end or database part. But the website won't show any chart from the database.
4. Oh, and dont use PostgreSQL password that ends with "@", it will save you from unnecessary trouble.
   ![image](https://github.com/gheacs/lab5/assets/132538718/24fc6237-a189-47bc-83f9-1f1b836b9824)
   ![image](https://github.com/gheacs/lab5/assets/132538718/1e852e64-c62d-4600-b7eb-852516200553)



   
