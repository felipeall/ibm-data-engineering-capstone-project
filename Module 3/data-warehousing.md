<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <h1>Data Warehousing</h1>
    <center>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo">
    </center>
    <p>Estimated time needed: <strong>60</strong> minutes.</p>
    <h1>About This SN Labs Cloud IDE</h1>
    <p>This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and PostgreSQL database running in a Docker container.</p>
    <h2>Important Notice about this lab environment</h2>
    <p>Please be aware that sessions for this lab environment are not persistent. A new environment is created for you every time you connect to this lab. Any data you may have saved in an earlier session will get lost. To avoid losing your data, please plan to complete these labs in a single session.</p>
    <h1>Scenario</h1>
    <p>You are a data engineer hired by an ecommerce company named SoftCart.com . The company retails download only items like E-Books, Movies, Songs etc. The company has international presence and customers from all over the world. The company would like to create a data warehouse so that it can create reports like</p>
    <ul>
      <li>total sales per year per country</li>
      <li>total sales per month per category</li>
      <li>total sales per quarter per country</li>
      <li>total sales per category per country</li>
    </ul>
    <p>You will use your data warehousing skills to design and implement a data warehouse for the company.</p>
    <h2>Objectives</h2>
    <p>In this assignment you will:</p>
    <ul>
      <li>Design a Data Warehouse using the pgAdmin ERD design tool.</li>
      <li>Create the schema in the Data Warehouse</li>
    </ul>
    <h1>Tools / Software</h1>
    <ul>
      <li>ERD Design Tool of pgAdmin</li>
      <li>PostgreSQL Database Server</li>
    </ul>
    <h1>Note - Screenshots</h1>
    <p>Throughout this lab you will be prompted to take screenshots and save them on your own device. You will need these screenshots to either answer graded quiz questions or to upload as your submission for peer review at the end of this course. You can use various free screengrabbing tools to do this or use your operating system's shortcut keys to do this (for example Alt+PrintScreen in Windows).</p>
    <h1>About the dataset</h1>
    <p>The dataset you would be using in this assignment is not a real life dataset. It was programmatically created for this assignment purpose.</p>
    <h1>Prerequisites</h1>
    <p>If you do not have an instance of IBM DB2 on cloud, follow the instructions in this <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/instructional-labs.md.html?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0321ENSkillsNetwork26764238-2021-01-01" target="_new">lab</a> to create one.</p>
    <h1>Exercise 1 - Design a Data Warehouse</h1>
    <p>The ecommerce company has provied you the sample data.</p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/ecom-sample-data.png" alt="">
    </p>
    <p>You will start your project by designing a Star Schema for the warehouse by identifying the columns for the various dimension and fact tables in the schema. Name your database as softcart</p>
    <h3>Task 1 - Design the dimension table softcartDimDate</h3>
    <p>Using the ERD design tool design the table softcartDimDate. The company is looking at a granularity of a day. Which means they would like to have the ability to generate the report on yearly, monthly, daily, and weekday basis.</p>
    <p>Here is a partial list of fields to serve as an example:</p>
    <p>dateid<br>month<br>monthname<br>...<br>...<br></p>
    <p>Take a screenshot of the table softcartDimDate in the ERD tool clearly showing all the fieldnames and data types.</p>
    <p>Name the screenshot <code>softcartDimDate.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 2 - Design the dimension table softcartDimCategory</h3>
    <p>Using the ERD design tool design the table softcartDimCategory.</p>
    <p>Take a screenshot of the table softcartDimCategory in the ERD tool clearly showing all the fieldnames and data types.</p>
    <p>Name the screenshot <code>softcartDimCategory.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 3 - Design the dimension table softcartDimItem</h3>
    <p>Using the ERD design tool design the table softcartDimItem.</p>
    <p>Take a screenshot of the table softcartDimItem in the ERD tool clearly showing all the fieldnames and data types.</p>
    <p>Name the screenshot <code>softcartDimItem.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 4 - Design the dimension table softcartDimCountry</h3>
    <p>Using the ERD design tool design the table softcartDimCountry.</p>
    <p>Take a screenshot of the table softcartDimCountry in the ERD tool clearly showing all the fieldnames and data types.</p>
    <p>Name the screenshot <code>softcartDimCountry.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 5 - Design the fact table softcartFactSales</h3>
    <p>Using the ERD design tool design the table softcartFactSales.</p>
    <p>Take a screenshot of the table softcartFactSales in the ERD tool clearly showing all the fieldnames and data types.</p>
    <p>Name the screenshot <code>softcartFactSales.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 6 - Design the relationships</h3>
    <p>Using the ERD design tool design the required relationships(one-to-one, one-to-many etc) amongst the tables.</p>
    <p>Take a screenshot of the entire ERD clearly showing all the relationships amongst the tables.</p>
    <p>Name the screenshot <code>softcartRelationships.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h1>Exercise 2 - Create the schema</h1>
    <p>In this exercise you will create the schema of the data warehouse.</p>
    <h3>Task 7 - Create the schema.</h3>
    <p>Download the schema sql from ERD tool and create the schema in a database named <code>staging</code>.</p>
    <p>Take a screenshot showing the success of the schema creation.</p>
    <p>Name the screenshot <code>createschema.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
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