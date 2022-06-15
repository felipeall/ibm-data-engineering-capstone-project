<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <h1>ETL and Data Pipelines using Apache AirFlow</h1>
    <h2>Assignment overview</h2>
    <p>This assignment is in two parts, ETL and Data Pipelines using Apache AirFlow.</p>
    <h3>ETL</h3>
    <p>In this first part of the assignment, you will perform four exercises, but before proceeding with the assignment, you will prepare the lab environment by starting MySQL server, MongoDB server, and then downloading the files database from the given link. Further, you will import the data in the JSON file to a database and a collection, and the data in the SQL file to the MySQL server. You will also verify your access to the cloud instance of the IBM DB2 server. The first exercise requires you to extract the data from the sales tables in MySQL and from the MongoDB database into CSV format.</p>
    <p>In the second exercise, you will transform the OLTP data to suit the data warehouse schema, read the OLTP data in the CSV format, add/edit/drop columns based on the data warehouse schema, and then save the transformed data into a new CSV file. In the third exercise, you will perform a series of tasks to transform the data. You will load the transformed data into the data warehouse, read the transformed data in the CSV format, load the transformed data into the data warehouse, and then, verify that the data is loaded properly. The final exercise requires you to automate the extraction of daily incremental data, and load yesterday's data into the data warehouse. You will download the python script from this link provided and use it as a template to write a python script that automatically loads yesterday's data from the production database into the data warehouse. After performing each task, take a screenshot of the command you used and its output, and name the screenshot.</p>
    <h3>Data Pipelines using Apache AirFlow</h3>
    <p>In this second part of the assignment, you will perform a couple of exercises, but before proceeding with the assignment, you will prepare the lab environment by starting the <strong>Apache Airflow</strong> and then downloading the dataset from the source (link provided) to the mentioned destination. In the first exercise, you will perform a series of tasks to create a DAG that runs daily. You will create a task that extracts the IP address and the date fields from the webserver log file and then saves it into a CSV file. The next task creation requires you to transform the date field into <em>YYYYMMMDD</em> format and save the output into a CSV file. In the final task creation, you will load the data by archiving the transformed CSV file into a TAR file. Before moving on to the next exercise, you will define the task pipeline as per the given details.</p>
    <p>In the second exercise, you will get the DAG operational by saving the defined DAG into a PY file. Further, you will submit, unpause and then monitor the DAG runs for the Airflow console. After performing each task, take a screenshot of the command you used and its output, and name the screenshot.</p>
  </body>
</html>
