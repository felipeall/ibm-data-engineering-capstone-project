<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <h1>Querying data in NoSQL databases</h1>
    <center>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo">
    </center>
    <p>Estimated time needed: <strong>30</strong> minutes.</p>
    <p>It is highly recommened that you finish the <a href="https://labs.cognitiveclass.ai/tools/theia/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0321ENSkillsNetwork26764238-2021-01-01&#x26;md_instructions_url=https%3A%2F%2Fcf-courses-data.s3.us.cloud-object-storage.appdomain.cloud%2FIBM-DB0151EN-SkillsNetwork%2Flabs%2FFinal+Assignment%2FSetup+and+Practice+Assignment.md" target="_blank">Setup and Practice Assignment Lab</a> before you proceed with this Assignment.</p>
    <h1>About This SN Labs Cloud IDE</h1>
    <p>This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and Mongodb running in a Docker container.</p>
    <h2>Important Notice about this lab environment</h2>
    <p>Please be aware that sessions for this lab environment are not persisted. Every time you connect to this lab, a new environment is created for you. Any data you may have saved in the earlier session would get lost. Plan to complete these labs in a single session, to avoid losing your data.</p>
    <h1>Scenario</h1>
    <p>You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MongoDB as a NoSQL database. You will be using MongoDB to store the e-commerce catalog data.</p>
    <h2>Objectives</h2>
    <p>In this assignment you will:</p>
    <ul>
      <li>import data into a MongoDB database.</li>
      <li>query data in a MongoDB database.</li>
      <li>export data from MongoDB.</li>
    </ul>
    <h1>Tools / Software</h1>
    <ul>
      <li>MongoDB Server</li>
      <li>MongoDB Command Line Backup Tools</li>
    </ul>
    <h1>Note - Screenshots</h1>
    <p>Throughout this lab you will be prompted to take screenshots and save them on your own device. You will need these screenshots to either answer graded quiz questions or to upload as your submission for peer review at the end of this course. You can use various free screengrabbing tools to do this or use your operating system's shortcut keys to do this (for example Alt+PrintScreen in Windows).</p>
    <h1>Exercise 1 - Check the lab environment</h1>
    <p>Before you proceed with the assignment :</p>
    <ul>
      <li>Check if you have the 'mongoimport' and 'mongoexport' installed on the lab, otherwise install them.</li>
      <li>Download the <code>catalog.json</code> file from <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json" target="_blank" rel="external">https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json</a>.</li>
    </ul>
    <h1>Exercise 2 - Working with MongoDB</h1>
    <h3>Task 1 - Import 'catalog.json' into mongodb server into a database named 'catalog' and a collection named 'electronics'</h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>mongoimport.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 2 - List out all the databases</h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>list-dbs.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 3 - List out all the collections in the database <code>catalog</code>.</h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>list-collections.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 4 - Create an index on the field "type"</h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>create-index.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 5 - Write a query to find the count of laptops</h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>mongo-query-laptops.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 6 - Write a query to find the number of mobile phones with screen size of 6 inches.</h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>mongo-query-mobiles1.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 7. Write a query to find out the average screen size of <code>smart phones</code>.</h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>mongo-query-mobiles2.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 8 - Export the fields <code>_id</code>, "type", "model", from the 'electronics' collection into a file named <code>electronics.csv</code></h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>mongoexport.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <p>End of assignment.</p>
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
          <td>2021-14-18</td>
          <td>0.1</td>
          <td>Ramesh Sannareddy</td>
          <td>Created initial version</td>
        </tr>
      </tbody>
    </table>
    <p>Copyright (c) 2021 IBM Corporation. All rights reserved.</p>
  </body>
</html>