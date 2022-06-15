<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <h1>Data Warehouse Reporting</h1>
    <center>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo">
    </center>
    <p>Estimated time needed: <strong>30</strong> minutes.</p>
    <h1>About This SN Labs Cloud IDE</h1>
    <p>This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia. You will also need an instance of DB2 running in IBM Cloud.</p>
    <h1>Scenario</h1>
    <p>You are a data engineer hired by an ecommerce company named SoftCart.com . The company retails download only items like E-Books, Movies, Songs etc. The company has international presence and customers from all over the world. You have designed the schema for the data warehouse in the previous assignment. Data engineering is a team game. Your senior data engineer reviewed your design. Your schema design was improvised to suit the production needs of the company. In this assignment you will generate reports out of the data in the data warehouse.</p>
    <h2>Objectives</h2>
    <p>In this assignment you will:</p>
    <ul>
      <li>Load data into Data Warehouse</li>
      <li>Write aggregation queries</li>
      <li>Create MQTs</li>
    </ul>
    <h1>Tools / Software</h1>
    <ul>
      <li>Cloud instance of IBM DB2 database</li>
    </ul>
    <h1>Note - Screenshots</h1>
    <p>Throughout this lab you will be prompted to take screenshots and save them on your own device. You will need these screenshots to either answer graded quiz questions or to upload as your submission for peer review at the end of this course. You can use various free screengrabbing tools to do this or use your operating system's shortcut keys to do this (for example Alt+PrintScreen in Windows).</p>
    <h1>About the dataset</h1>
    <p>The dataset you would be using in this assignment is not a real life dataset. It was programmatically created for this assignment purpose.</p>
    <h1>Prerequisites</h1>
    <p>You need access to a cloud instance of IBM DB2 to proceed with this assignment.</p>
    <p>If you do not have an instance of IBM DB2 on cloud, follow the instructions in this <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/instructional-labs.md.html?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0321ENSkillsNetwork26764238-2021-01-01" target="_new">lab</a> to create one.</p>
    <h1>Exercise 1 - Load data into the Data Warehouse</h1>
    <p>In this exercise you will load the data into the tables.</p>
    <p>You will load the data provided by the company in csv format.</p>
    <h3>Task 1 - Load data into the dimension table DimDate</h3>
    <p>Download the data from <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimDate.csv?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0321ENSkillsNetwork26764238-2021-01-01">this link</a></p>
    <p>Load this data into DimDate table.</p>
    <p>Take a screenshot of the first 5 rows in the table DimDate.</p>
    <p>Name the screenshot <code>DimDate.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 2 - Load data into the dimension table DimCategory</h3>
    <p>Download the data from <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCategory.csv?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0321ENSkillsNetwork26764238-2021-01-01">this link</a></p>
    <p>Load this data into DimCategory table.</p>
    <p>Take a screenshot of the first 5 rows in the table DimCategory.</p>
    <p>Name the screenshot <code>DimCategory.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 3 - Load data into the dimension table DimCountry</h3>
    <p>Download the data from <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCountry.csv?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0321ENSkillsNetwork26764238-2021-01-01">this link</a></p>
    <p>Load this data into DimCountry table.</p>
    <p>Take a screenshot of the first 5 rows in the table DimCountry.</p>
    <p>Name the screenshot <code>DimCountry.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 4 - Load data into the fact table FactSales</h3>
    <p>Download the data from <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/FactSales.csv?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0321ENSkillsNetwork26764238-2021-01-01">this link</a></p>
    <p>Load this data into FactSales table.</p>
    <p>Take a screenshot of the first 5 rows in the table FactSales.</p>
    <p>Name the screenshot <code>FactSales.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h1>Exercise 2 - Queries for data analytics</h1>
    <p>In this exercise you will query the data you have loaded in the previous exercise.</p>
    <h3>Task 5 - Create a grouping sets query</h3>
    <p>Create a grouping sets query using the columns country, category, totalsales.</p>
    <p>Take a screenshot of the sql and the output rows.</p>
    <p>Name the screenshot <code>groupingsets.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 6 - Create a rollup query</h3>
    <p>Create a rollup query using the columns year, country, and totalsales.</p>
    <p>Take a screenshot of the sql and the output rows.</p>
    <p>Name the screenshot <code>rollup.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 7 - Create a cube query</h3>
    <p>Create a cube query using the columns year, country, and average sales.</p>
    <p>Take a screenshot of the sql and the output rows.</p>
    <p>Name the screenshot <code>cube.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 8 - Create an MQT</h3>
    <p>Create an MQT named total_sales_per_country that has the columns country and total_sales.</p>
    <p>Take a screenshot of the sql.</p>
    <p>Name the screenshot <code>mqt.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
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
          <td>2021-12-12</td>
          <td>0.1</td>
          <td>Ramesh Sannareddy</td>
          <td>Created initial version</td>
        </tr>
        <tr>
          <td>2022-02-02</td>
          <td>0.2</td>
          <td>Ramesh Sannareddy</td>
          <td>Updated version</td>
        </tr>
      </tbody>
    </table>
    <p>Copyright (c) 2022 IBM Corporation. All rights reserved.</p>
  </body>
</html>