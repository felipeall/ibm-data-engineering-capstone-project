<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <h1>Hands on Lab - ETL</h1>
    <center>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo">
    </center>
    <p>Estimated time needed: <strong>30</strong> minutes.</p>
    <h1>About This SN Labs Cloud IDE</h1>
    <p>This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and MySQL database running in a Docker container. You will also need an instance of DB2 running in IBM Cloud.</p>
    <h2>Important Notice about this lab environment</h2>
    <p>Please be aware that sessions for this lab environment are not persistent. A new environment is created for you every time you connect to this lab. Any data you may have saved in an earlier session will get lost. To avoid losing your data, please plan to complete these labs in a single session.</p>
    <h1>Scenario</h1>
    <p>You are a data engineer at an e-commerce company. You need to keep data synchronized between different databases/data warehouses as a part of your daily routine. One task that is routinely performed is the sync up of staging data warehouse and production data warehouse. Automating this sync up will save you a lot of time and standardize your process. You will be given a set of python scripts to start with. You will use/modify them to perform the incremental data load from MySQL server which acts as a staging warehouse to the IBM DB2 which is a production data warehouse. This script will be scheduled by the data engineers to sync up the data between the staging and production data warehouse.</p>
    <h2>Objectives</h2>
    <p>In this assignment you will write a python program that will:</p>
    <ul>
      <li>Connect to IBM DB2 data warehouse and identify the last row on it.</li>
      <li>Connect to MySQL staging data warehouse and find all rows later than the last row on the datawarehouse.</li>
      <li>Insert the new data in the MySQL staging data warehouse into the IBM DB2 production data warehouse.</li>
    </ul>
    <h1>Tools / Software</h1>
    <ul>
      <li>MySQL Server</li>
      <li>IBM DB2 database running on IBM Cloud</li>
    </ul>
    <h1>Note - Screenshots</h1>
    <p>Throughout this lab you will be prompted to take screenshots and save them on your own device. You will need these screenshots to either answer graded quiz questions or to upload as your submission for peer review at the end of this course. You can use various free screengrabbing tools to do this or use your operating system's shortcut keys to do this (for example Alt+PrintScreen in Windows).</p>
    <h1>Prepare the lab environment</h1>
    <p>Before you start the assignment:</p>
    <p>Step 1: Start MySQL server</p>
    <p>Step 2: Create a database named <code>sales</code></p>
    <p>Step 3: Download the file below</p>
    <p><a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/sales.sql" target="_blank" rel="external">https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/sales.sql</a></p>
    <p>Step 4: Import the data in the file <code>sales.sql</code> into the <code>sales</code> database.</p>
    <p>Step 5: Verify that you can access your cloud instance of IBM DB2 server.</p>
    <p>Step 6: Download the mysqlconnect.py python programs from link below.</p>
    <p><a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/mysqlconnect.py" target="_blank" rel="external">https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/mysqlconnect.py</a></p>
    <p>Step 7: mysqlconnect.py has the sample code to help you understand how to connect to MySQL using Python.</p>
    <p>Step 8: Modify mysqlconnect.py suitably and make sure you are able to connect to the MySQL server instance on the Theia environment.</p>
    <p>Step 9: Download the db2connect.py python programs from link below.</p>
    <p><a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/db2connect.py" target="_blank" rel="external">https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/db2connect.py</a></p>
    <p>Step 10: db2connect.py has the sample code to help you understand how to connect to the cloud instance of IBM DB2 using Python.</p>
    <p>Step 11: Modify db2connect.py suitably and make sure you are able to connect to your cloud instance of IBM DB2 from the Theia environment.</p>
    <p>Step 12: Download the file below</p>
    <p><a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/sales.csv" target="_blank" rel="external">https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/sales.csv</a></p>
    <p>Step 13: Load sales.csv into a table named <code>sales_data</code> on your cloud instance of IBM DB2 database.</p>
    <p>Step 14: <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/automation.py" target="_blank" rel="external">https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/automation.py</a></p>
    <p>You will be using automation.py as a scafolding program to execute the tasks in this assignment</p>
    <h1>Exercise 1 - Automate loading of incremental data into the data warehouse</h1>
    <p>One of the routine tasks that is carried out around a data warehouse is the extraction of daily new data from the operational database and loading it into the data warehouse. In this exercise you will automate the extraction of incremental data, and loading it into the data warehouse.</p>
    <h3>Task 1 - Implement the function get_last_rowid()</h3>
    <p>In the program automation.py implement the function get_last_rowid()</p>
    <p>This function must connect to the DB2 data warehouse and return the last rowid.</p>
    <p>Take a screenshot of the python code clearly showing the implementation of the function get_last_rowid().</p>
    <p>Name the screenshot <code>get_last_rowid.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 2 - Implement the function get_latest_records()</h3>
    <p>In the program automation.py implement the function get_latest_records()</p>
    <p>This function must connect to the MySQL database and return all records later than the given last_rowid.</p>
    <p>Take a screenshot of the python code clearly showing the implementation of the function get_latest_records().</p>
    <p>Name the screenshot <code>get_latest_records.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 3 - Implement the function insert_records()</h3>
    <p>In the program automation.py implement the function insert_records()</p>
    <p>This function must connect to the DB2 data warehouse and insert all the given records.</p>
    <p>Take a screenshot of the python code clearly showing the implementation of the function insert_records().</p>
    <p>Name the screenshot <code>insert_records.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 4 - Test the data synchronization</h3>
    <p>Run the program automation.py and test if the synchronization is happening as expected.</p>
    <p>Take a screenshot of the program output .</p>
    <p>Name the screenshot <code>synchronization.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <p>End of the assignment.</p>
    <h2>Authors</h2>
    <p>Ramesh Sannareddy</p>
    <h3>Other Contributors</h3>
    <p>Rav Ahuja</p>
    <h2>Change Log</h2>
    <table>
      <thead>
        <tr>
          <th>Date (YYYY-MM-DD)</th>
          <th>Version</th>
          <th>Changed By</th>
          <th>Change Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>2021-13-12</td>
          <td>0.1</td>
          <td>Ramesh Sannareddy</td>
          <td>Created initial version</td>
        </tr>
      </tbody>
    </table>
    <p>Copyright (c) 2022 IBM Corporation. All rights reserved.</p>
  </body>
</html>
