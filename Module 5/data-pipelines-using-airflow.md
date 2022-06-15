<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <h1>Data Pipelines Using Apache AirFlow</h1>
    <center>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo">
    </center>
    <p>Estimated time needed: <strong>30</strong> minutes.</p>
    <h1>About This SN Labs Cloud IDE</h1>
    <p>This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and Apache Airflow running in a Docker container.</p>
    <h2>Important Notice about this lab environment</h2>
    <p>Please be aware that sessions for this lab environment are not persistent. A new environment is created for you every time you connect to this lab. Any data you may have saved in an earlier session will get lost. To avoid losing your data, please plan to complete these labs in a single session.</p>
    <h1>Scenario</h1>
    <p>Write a pipeline that analyzes the web server log file, extracts the required lines(ending with html) and fields(time stamp, size ) and transforms (bytes to mb) and load (append to an existing file.)</p>
    <h2>Objectives</h2>
    <p>In this assignment you will author an Apache Airflow DAG that will:</p>
    <ul>
      <li>Extract data from a web server log file</li>
      <li>Transform the data</li>
      <li>Load the transformed data into a csv file</li>
    </ul>
    <h1>Tools / Software</h1>
    <ul>
      <li>Apache AirFlow</li>
    </ul>
    <h1>Note - Screenshots</h1>
    <p>Throughout this lab you will be prompted to take screenshots and save them on your own device. You will need these screenshots to either answer graded quiz questions or to upload as your submission for peer review at the end of this course. You can use various free screengrabbing tools to do this or use your operating system's shortcut keys to do this (for example Alt+PrintScreen in Windows).</p>
    <h1>Exercise 1 - Prepare the lab environment</h1>
    <p>Before you start the assignment:</p>
    <ul>
      <li>Start Apache Airflow.</li>
      <li>Download the dataset from the source to the destination mentioned below.</li>
    </ul>
    <p>Source : <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/accesslog.txt" target="_blank" rel="external">https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/accesslog.txt</a><br>Destination : /home/project/airflow/dags/capstone</p>
    <h1>Exercise 2 - Create a DAG</h1>
    <h3>Task 1 - Define the DAG arguments</h3>
    <p>Create a DAG with these arguments.</p>
    <ul>
      <li>owner</li>
      <li>start_date</li>
      <li>email</li>
    </ul>
    <p>You may define any suitable additional arguments.</p>
    <p>Take a screenshot of the code you used clearly showing the above arguments.</p>
    <p>Name the screenshot <code>dag_args.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 2 - Define the DAG</h3>
    <p>Create a DAG named <code>process_web_log</code> that runs daily.</p>
    <p>Use suitable description.</p>
    <p>Take a screenshot of the code you used to define the DAG.</p>
    <p>Name the screenshot <code>dag_definition.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 3 - Create a task to extract data</h3>
    <p>Create a task named <code>extract_data</code>.</p>
    <p>This task should extract the ipaddress field from the web server log file and save it into a file named extracted_data.txt</p>
    <p>Take a screenshot of the task code.</p>
    <p>Name the screenshot <code>extract_data.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 4 - Create a task to transform the data in the txt file</h3>
    <p>Create a task named <code>transform_data</code>.</p>
    <p>This task should filter out all the occurrences of ipaddress "198.46.149.143" from extracted_data.txt and save the output to a file named <code>transformed_data.txt</code>.</p>
    <p>Take a screenshot of the task code.</p>
    <p>Name the screenshot <code>transform_data.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 5 - Create a task to load the data</h3>
    <p>Create a task named <code>load_data</code>.</p>
    <p>This task should archive the file <code>transformed_data.txt</code> into a tar file named <code>weblog.tar</code>.</p>
    <p>Take a screenshot of the task code.</p>
    <p>Name the screenshot <code>load_data.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 6 - Define the task pipeline</h3>
    <p>Define the task pipeline as per the details given below:</p>
    <table>
      <thead>
        <tr>
          <th>Task</th>
          <th>Functionality</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>First task</td>
          <td><code>extract_data</code></td>
        </tr>
        <tr>
          <td>Second task</td>
          <td><code>transform_data</code></td>
        </tr>
        <tr>
          <td>Third task</td>
          <td><code>load_data</code></td>
        </tr>
      </tbody>
    </table>
    <p>Take a screenshot of the task pipeline section of the DAG.</p>
    <p>Name the screenshot <code>pipeline.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h1>Exercise 3 - Getting the DAG operational.</h1>
    <p>Save the DAG you defined into a file named <code>process_web_log.py</code>.</p>
    <h3>Task 7 - Submit the DAG</h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot <code>submit_dag.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 8 - Unpause the DAG</h3>
    <p>Take a screenshot of the command you used and the output.</p>
    <p>Name the screenshot <code>unpause_dag.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 9 - Monitor the DAG</h3>
    <p>Take a screenshot of the DAG runs for the Airflow console.</p>
    <p>Name the screenshot <code>dag_runs.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
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
        <tr>
          <td>2022-30-01</td>
          <td>0.2</td>
          <td>Alison Woolford</td>
          <td>Updated version</td>
        </tr>
      </tbody>
    </table>
    <p>Copyright (c) 2022 IBM Corporation. All rights reserved.</p>
  </body>
</html>
