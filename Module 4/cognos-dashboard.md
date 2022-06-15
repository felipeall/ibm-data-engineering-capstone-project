<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/IDSNlogo.png" width="200" height="200">
    <h1>Hands-on Lab : Getting Started with Cognos Dashboard Embedded</h1>
    <p><strong>Estimated time needed:</strong> 20 minutes</p>
    <p>IBM Cognos Dashboard Embedded (CDE) is an AI-fueled business intelligence service that supports the entire data analytics cycle, from discovery to operationalization. It provides users with data discovery capabilities to visually explore and interact with their data to identify the key insights for improving data driven decisions. Users can perform data discovery and then quickly assemble that information into interactive, visually appealing dashboards; all without the need of formal training.</p>
    <p>In this lab, first you will learn how to login to IBM Cloud Pak for Data platform through IBM Cloud and create a project there. Next, you will learn how to add a Cognos Dashboard Embedded (CDE) service and upload external data files to your project(<ins>supports CSV file only</ins>). Finally, you will learn general navigation around the CDE user interface (UI), and how to start a new dashboard with a template in CDE, populate it with a data visualization as well as save the dashboard.</p>
    <h1>Software Used in this Lab</h1>
    <p>Since for the assignment of this module you will be using IBM Cognos Dashboard Embedded (CDE), so in this lab you will get started with IBM Cognos Dashboard Embedded (CDE) Lite plan service through IBM Cloud as this is available <strong>at no charge for 50 sessions/month</strong>. A session is a <strong>60 minutes period</strong> where users can perform unlimited interactions with an embedded dashboard. Lite plan services are deleted after <strong>30 days of inactivity</strong>.</p>
    <h1>Dataset Used in this Lab</h1>
    <p>The dataset used in this lab comes from the following source: <a href="https://www.kaggle.com/kyanyoga/sample-sales-data?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2021-01-01" target="_blank" rel="external">https://www.kaggle.com/kyanyoga/sample-sales-data</a> under a <strong><a href="https://creativecommons.org/publicdomain/zero/1.0/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2021-01-01" target="_blank" rel="external">CC0: Public Domain license</a></strong>.</p>
    <h1>Objectives</h1>
    <p>After completing this lab, you will be able to:</p>
    <ul>
      <li>Login to IBM Cloud Pak for Data platform through IBM Cloud</li>
      <li>Create a project in IBM Cloud Pak for Data</li>
      <li>Add a Cognos Dashboard Embedded (CDE) service to your created project</li>
      <li>Navigate around the Cognos Dashboard Embedded (CDE) user interface</li>
      <li>Upload external data files to your created project (<ins>Supports .CSV files only</ins>)</li>
      <li>Start a new dashboard with a dashboard template and populate it with a data visualization</li>
    </ul>
    <h1>Exercise 1 : Login to IBM Cloud Pak for Data and Create a Project</h1>
    <p>In this exercise, you will how to login to IBM Cloud Pak for Data platform through IBM Cloud and create a project there.</p>
    <h2>Task A : (optional) Create an Instance of Watson Studio / Cloud Pak for Data</h2>
    <ul>
      <li><strong><ins>If you already have an instance of Watson Studio / Cloud Pak for Data , skip Task A.</ins></strong></li>
    </ul>
    <ol>
      <li>
        <p>Go to <a href="https://cloud.ibm.com/login?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2021-01-01" target="_blank" rel="external">cloud.ibm.com/login</a>.</p>
      </li>
      <li>
        <p>Enter your <strong>IBMid</strong> (the email ID you used to sign up for IBM Cloud) and click <strong>Continue</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.A.2.png" width="400" height="460">
      </li>
    </ol><br>
    <ol start="3">
      <li>
        <p>Enter your <strong>password</strong> and click <strong>Log in</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.A.3.png" width="400" height="411">
      </li>
    </ol><br>
    <ol start="4">
      <li>
        <p>Click <strong>Navigation Menu Icon</strong> on the top left side.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.A.4.png" width="400" height="667">
      </li>
    </ol><br>
    <ol start="5">
      <li>
        <p>From the navigation Menu sidebar, click <strong>Watson</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.A.5.png" width="250" height="873">
      </li>
    </ol><br>
    <ol start="6">
      <li>
        <p>Now from the section <strong>Explore our other offerings</strong>, click IBM Watson Studio <strong>Try for free</strong>. You will be redirected to IBM Cloud Pak (<a href="https://dataplatform.cloud.ibm.com/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2021-01-01" target="_blank" rel="external">dataplatform.cloud.ibm.com</a>) for Data platform.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.A.6.png" width="919" height="200">
      </li>
    </ol><br>
    <ol start="7">
      <li>
        <p><strong>Select a region</strong> matching the region of your IBM Cloud account. Then click <strong>Log in with your IBMid</strong></p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.A.7.png" width="821" height="500">
      </li>
    </ol><br>
    <ol start="8">
      <li>
        <p>Click <strong>Go to IBM Cloud Pak for Data</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.A.8.png" width="620" height="400">
      </li>
    </ol><br>
    <ol start="9">
      <li>
        <p>You have successfully logged in to the IBM Cloud Pak for Data platform.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.A.9.png" width="865" height="500">
      </li>
    </ol><br>
    <h2>Task B : Login to IBM Cloud Pak for Data</h2>
    <ul>
      <li><strong><ins>If you just completed Task A, you will already be logged in, so skip Task B.</ins></strong></li>
    </ul>
    <ol>
      <li>
        <p>Go to <a href="https://dataplatform.cloud.ibm.com/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2021-01-01" target="_blank" rel="external">dataplatform.cloud.ibm.com</a>.</p>
      </li>
      <li>
        <p>Enter your <strong>IBMid</strong> (the email ID you used to sign up for IBM Cloud), <strong>password</strong> and select a <strong>region</strong>, same one you used for IBM Cloud account and IBM Cloud Pak for Data(if you have completed Task A).</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.B.2.png" width="400" height="560">
      </li>
    </ol><br>
    <ol start="3">
      <li>
        <p>Click <strong>Go to IBM Cloud Pak for Data</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.B.3.png" width="620" height="400">
      </li>
    </ol><br>
    <ol start="4">
      <li>
        <p>You have successfully logged in to the IBM Cloud Pak for Data platform.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.B.4.png" width="865" height="500">
      </li>
    </ol><br>
    <h2>Task C : Create a New Project</h2>
    <ol>
      <li>
        <p>On the IBM Cloud Pak for Data welcome page, click <strong>Create a project</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.C.1.png" width="471" height="300">
      </li>
    </ol><br>
    <ol start="2">
      <li>
        <p>Click <strong>Create an empty project</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.C.2.png" width="1145" height="300">
      </li>
    </ol><br>
    <ol start="3">
      <li>
        <p>Write <strong>Capstone Project</strong> as name of the project and click <strong>Add</strong> on Select storage service if no storage service appears. <ins>If a storage appears, proceed to step 6 directly</ins>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.C.3.png" width="938" height="300">
      </li>
    </ol><br>
    <ol start="4">
      <li>
        <p>You will be redirected to a new page. On the <strong>Create</strong> tab, select <strong>Lite</strong> plan. Then click <strong>Create</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.C.4.png" width="862" height="500">
      </li>
    </ol><br>
    <ol start="5">
      <li>
        <p>Now you will be redirected to the previous new project page. Click <strong>Refresh</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.C.5.png" width="938" height="300">
      </li>
    </ol><br>
    <ol start="6">
      <li>
        <p>Once you see a storage service, click <strong>Create</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.C.6.png" width="867" height="500">
      </li>
    </ol><br>
    <ol start="7">
      <li>
        <p>You have successfully created a project. Click <strong>IBM Cloud Pak for Data</strong> at the top left to go back to homepage.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/1.C.7.png" width="997" height="350">
      </li>
    </ol><br>
    <h1>Exercise 2 : Add a CDE service and Upload External Data</h1>
    <p>In this exercise, you will learn how to add a Cognos Dashboard Embedded (CDE) service and upload external data files to your project.</p>
    <h2>Task A : Add a CDE service</h2>
    <ol>
      <li>
        <p>From IBM Cloud Pak for Data homepage, click <strong>Projects</strong> under Quick navigation.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/2.A.1.png" width="581" height="400">
      </li>
    </ol><br>
    <ol start="2">
      <li>
        <p>Select <strong>Capstone Project</strong> you created earlier.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/2.A.2.png" width="530" height="300">
      </li>
    </ol><br>
    <ol start="3">
      <li>
        <p>On the <strong>Settings</strong> page, from the <strong>Associated services</strong> section, click <strong>Add service</strong> and select <strong>Dashboard</strong> from the list.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/2.A.3.png" width="864" height="500">
      </li>
    </ol><br>
    <ol start="4">
      <li>
        <p>Click <strong>New service</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/2.A.4.png" width="865" height="200">
      </li>
    </ol><br>
    <ol start="5">
      <li>
        <p>Click <strong>IBM Cognos Dashboard Embedded</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/2.A.5.png" width="520" height="300">
      </li>
    </ol><br>
    <ol start="6">
      <li>
        <p>On the <strong>Create</strong> tab, select a close <strong>region</strong> and <strong>Lite</strong> plan. Then click <strong>Create</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/2.A.6.png" width="951" height="500">
      </li>
    </ol><br>
    <ol start="7">
      <li>
        <p>Select <strong>IBM Cognos Dashboard Embedded</strong> service and click <strong>Associate service</strong> to add the service to <strong>Capstone Project</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/2.A.7.png" width="1157" height="250">
      </li>
    </ol><br>
    <ol start="8">
      <li>
        <p>Once the service association status appears green, <strong>close</strong> the associate service page.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/2.A.8.png" width="1144" height="250">
      </li>
    </ol><br>
    <h2>Task B : Upload External Data Files(<strong>Supports .CSV Files Only</strong>)</h2>
    <ol>
      <li>
        <p>Download the file <a href="car_sales_data_sample.csv">car_sales_data_sample.csv</a>.</p>
      </li>
      <li>
        <p>On the <strong>Assets</strong> page, click <strong>Find and add data</strong> icon. Under Load tab, click <strong>browse</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/2.B.2.png" width="1053" height="250">
      </li>
    </ol><br>
    <ol start="3">
      <li>
        <p>Browse to the file download location, select the downloaded <strong>CSV</strong> file, and click <strong>Open</strong>.</p>
      </li>
      <li>
        <p>Once upload completes, <strong>car_sales_data_sample.csv</strong> will appear under <strong>Data assets</strong> section.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/2.B.4.png" width="842" height="250">
      </li>
    </ol><br>
    <h1>Exercise 3 : Navigate around CDE UI and Start a New Dashboard with a Template</h1>
    <p>In this exercise, you will learn general navigation around the CDE user interface (UI), and how to start a new dashboard with a template in CDE, populate it with a data visualization as well as save the dashboard.</p>
    <ol>
      <li>
        <p>On the <strong>Overview</strong> page of Capstone Project project, click <strong>Add to project</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/3.1.png" width="1160" height="200">
      </li>
    </ol><br>
    <ol start="2">
      <li>
        <p>Select <strong>Dashboard</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/3.2.png" width="795" height="300">
      </li>
    </ol><br>
    <ol start="3">
      <li>
        <p>Name the dashboard as <strong>Simple Dashboard</strong>. Then select a <strong>Cognos Dashboard Embedded service</strong> from the list and click <strong>Create</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/3.3.png" width="831" height="500">
      </li>
    </ol><br>
    <ol start="4">
      <li>
        <p>Select the <strong>tabbed dashboard style</strong>. This will allow you to have multiple pages for your dashboards. Select the <strong>one-panel template</strong>. Click <strong>OK</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/3.4.png" width="943" height="500">
      </li>
    </ol><br>
    <ol start="5">
      <li>
        <p>Now you have created a new dashboard using the dashboard template.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/3.5.png" width="911" height="500">
      </li>
    </ol><br>
    <ol start="6">
      <li>
        <p>Click <strong>Sources</strong> icon from the <strong>Navigation</strong> panel to open the data source panel. Then click <strong>Add a source</strong> icon.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/3.6.png" width="911" height="500">
      </li>
    </ol><br>
    <ol start="7">
      <li>
        <p>Select <strong>Data assets</strong>. Select <strong>car_sales_data_sample.csv</strong> and click <strong>Select</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/3.7.png" width="911" height="500">
      </li>
    </ol><br>
    <ol start="8">
      <li>
        <p>From the <strong>Navigation</strong> panel, select <strong>Sources</strong> to open the data source panel, if it is not already open. The <strong>Data Source</strong> panel displays the file <strong>car_sales_data_sample.csv</strong>. Click on <strong>car_sales_data_sample.csv</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/3.8.png" width="100" height="322">
      </li>
    </ol><br>
    <ol start="9">
      <li>
        <p>From the <strong>Data Source</strong> panel, select <strong>SALES</strong>. Drag it to the <strong>Panel</strong> and release.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/3.9.png" width="726" height="400">
      </li>
    </ol><br>
    <ol start="10">
      <li>
        <p>Now you have successfully started to populate your dashboard with data visualizations too!</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/3.10.png" width="525" height="400">
      </li>
    </ol><br>
    <ol start="11">
      <li>
        <p>To save the newly created dashboard, click <strong>Save</strong> icon.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%205/Lab%20-%20Getting%20Started%20with%20Cognos%20Dashboard%20Embedded/images/3.11.png" width="371" height="100">
      </li>
    </ol><br>
    <h3>Congratulations! You have completed the Lab.</h3>
    <h3></h3>
    <h1>Author(s)</h1>
    <ul>
      <li><a href="https://www.linkedin.com/in/sandipsahajoy/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2021-01-01" target="_blank" rel="external">Sandip Saha Joy</a></li>
    </ul>
    <h2>Other Contributor(s)</h2>
    <h1>Changelog</h1>
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Version</th>
          <th>Changed by</th>
          <th>Change Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>2020-10-07</td>
          <td>1.0</td>
          <td>Sandip Saha Joy</td>
          <td>Initial version created</td>
        </tr>
      </tbody>
    </table>
    <h2></h2>
    <h3 align="center">© IBM Corporation 2020. All rights reserved.</h3>
    <h3></h3>
  </body>
</html>