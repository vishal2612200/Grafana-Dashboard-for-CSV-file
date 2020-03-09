# Grafana-Dashboard-for-CSV-file
This Project is based on Python Flask. User will be able to generate Grafana Dashboard using CSV file generated from MyFitnessPal Android App.


Note:Sample data file has been uploaded to data Folder. This file has been downloaded from some website providing user an sample csv file for MyFitnessPal Android App.

# Application View

![grafana project gif](https://user-images.githubusercontent.com/37480057/76222570-c45bc900-6240-11ea-896f-4645423d6563.gif)


# Problem Statement
Language: Any

Must work in: Linux (anything server side)

MyFitnessPal is a mobile app used to track food & energy intake, exercise, and more. It supports CSV data export (e.g. through email) to facilitate archival, but this style is a bit antiquated for manual viewing.

A simple website that accepts CSV exports and renders nice visual representations using Grafana would be much better for users. This should be feasible to complete in a few days since all of the major components already exist.

# Solution
 This Application take CSV file as an input -> convert into sql table -> Load into SQL Table -> Grafana Dashboard is generated based on the data of SQL Table.
 
 Flow Chart for Solution
 
 ![solution flow for grafana](https://user-images.githubusercontent.com/37480057/76214133-206b2100-6232-11ea-831b-f70975d41c4f.png)

# Technologies Used

<ul>
  <li>Python Flask</li>
  <li>MYSQL</li>
  <li>Grafana</li>
 
    
 ## Python Libraries used
 

  <li>sqlalchemy</li>
  <li>pandas</li>
  </ul>
  
 # How to Setup the Application
Step 1) Download the zip file of the project and extract it to your local system.

Step 2) Open the terminal to the project folder location.

### Specifying the path in the terminal

<pre>cd location_of_the_folder </pre>

Step 3) Instaling the packages

<pre>pip install -r requirements.txt</pre>

Step 4) Open Your PHPMYADMIN on your local system and create an SQL Table with an name <b>grafanatesting</b> i.e can be change to your table name also but don't forgot to change table name inside the app.py if you have changed the name of SQL Table.

Step 5) ADD username and password for phpmyadmin inside the app.py i.e Comment has been defined to specify the location 

Step 6) Running the Project on the local system

 <pre> python app.py </pre>

Step 7) Open given link on your browser

<pre> http://localhost:5000 </pre>

# Error Possibilities
Some possibilites where error can be found
## Modulenofounderror

  Solve this error by running the following command:

<pre>pip install module_name </pre>

## Giving an N/A value on the Dashboard
<ul>
  <li> Please verify the format of CSV file with the sample file present inside the Data Folder.It can possible that you are trying the application with the wrong file format for this application.</li>
  <li> Please verify SQL Table name, username and password inside the app.py file. Wrong SQL connection can also lead to N/A value on dashboard.</li>
</ul>
  
# How does Application Work

At the Home screen, User will have an option for uploading CSV file to the Application. After file uploading process ,it gets load into SQL table and then it get redirected to an Grafana Dashboard Page.

# Some Changes That have to be Made in defaults.ini file of Grafana
These changes are being done to resolve the problem of<b> "localhost can't be resolved" </b>inside the iframe of the browser.

<b>set cookie SameSite attribute. defaults to lax. can be set to “lax”, “strict” and “none”</b>

<pre>cookie_samesite = none</pre>

<b>set to true if you want to allow browsers to render Grafana in a. default is false.</b>
<pre>allow_embedding = true</pre>


#################################### Anonymous Auth ######################
[auth.anonymous]
<b> enable anonymous access<b>
  <pre>enabled = true</pre>

<b>Now Restart the grafana server, To make the changes in effect.</b>

<b>Reference:</b> https://community.grafana.com/t/dashboard-using-iframe-not-opening-in-web-broweser-window/19304/8
