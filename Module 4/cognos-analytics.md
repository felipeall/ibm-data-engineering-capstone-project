<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <center>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo">
    </center>
    <p>Estimated time needed: <strong>30</strong> minutes.</p>
    <h1>Scenario</h1>
    <p>You are a data engineer at an e-commerce company. Your company has finished setting up a datawarehouse. Now you are assigned the responsibility to design a reporting dashboard that reflects the key metrics of the business.</p>
    <h2>Objectives</h2>
    <p>In this assignment you will:</p>
    <ul>
      <li>Create a dashboard using Cognos Analytics</li>
    </ul>
    <h2>Tools / Software</h2>
    <ul>
      <li>IBM Cognos Analytics (You can either use IBM Cognos Analytics or Cognose Dashboard Embedded and Watson Studio)</li>
      <li>Cloud instance of IBM DB2 database</li>
    </ul>
    <h2>Note - Screenshots</h2>
    <p>Throughout this lab you will be prompted to take screenshots and save them on your own device. You will need these screenshots to either answer graded quiz questions or to upload as your submission for peer review at the end of this course. You can use various free screengrabbing tools to do this or use your operating system's shortcut keys to do this (for example Alt+PrintScreen in Windows).</p>
    <h2>Pre-requisites</h2>
    <ul>
      <li>
        <p>If you plan to use the IBM Cognos Analytics Trial version to do this lab, it is presumed that you have worked on it already. If you want to brush up the basics of using Cognos Analytics , it is recommeneded that you finish the <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%205%20-%20Different%20Methods%20for%20Creating%20Dashboard%20Visualizations%20with%20Cognos%20Analytics/instructions.md.html?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0321ENSkillsNetwork26764238-2021-01-01" target="_blank">this lab </a>.</p>
      </li>
      <li>
        <p>If your Cognos Analytics trial has expired, it is highly recommened that you finish the <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/labs/WatsonCDE/HandsOn_WatsonStudioCDE.md.html?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0321ENSkillsNetwork26764238-2021-01-01" target="_blank">Setup and Practice Assignment </a>before you proceed with this assignment using Cognos Dashboard Embedded and Watson Studio.</p>
      </li>
    </ul>
    <h2>Environment Setup</h2>
    <p>Before you proceed with the assignment :</p>
    <ul>
      <li>Download the data from this <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/analytics/ecommerce.csv?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0321ENSkillsNetwork26764238-2021-01-01">link</a></li>
    </ul>
    <h1></h1>
    <h2>Exercise 1 - Load data into the data warhouse</h2>
    <h3>Task 1 - Import data</h3>
    <p>Import data in the file "ecommerce.csv" (You have downloaded this data in exercise 1). into a table named <code>sales_history</code></p>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>dataimport.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 2 - List top 10 rows</h3>
    <p>List the first 10 rows in the table <code>sales_history</code></p>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>top10rows.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h1>Exercise 2 - Create data source in Cognos.</h1>
    <h3>Task 3 - Create a data source in Cognos that points to the table <code>sales_history</code> in your IBM DB2 database.</h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>datasource.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h1>Exercise 3 - Create dashboard</h1>
    <h3>Task 4 - Create a line chart</h3>
    <p>Create a line chart of month wise total sales for the year 2020.</p>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>linechart.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 5 - Create a pie chart</h3>
    <p>Create a pie chart of category wise total sales.</p>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot as <code>piechart.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
    <h3>Task 6 - Create a bar chart</h3>
    <p>Create a bar chart of Quarterly sales of mobile phones</p>
    <p>Take a screenshot of the bar chart.</p>
    <p>Name the screenshot as <code>barchart.jpg</code>. (images can be saved with either .jpg or .png extension)</p>
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
          <td>2021-11-23</td>
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