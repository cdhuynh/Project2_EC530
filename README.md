# Project2_EC530

This repository contains the general functionality in which the program will interpret a JSON file and determine whether the input is in the correct format. Following this, the program will produce a JSON file in return. 

The minimum required are the fields: "Name" and "Age". Each module will specify what it is required for the program to correctly parse the information through the use of a json schema. It will then be validated in the backend of the program. 

The database of choice is MongoDB.

The project will use Flask for developing a web application and creating the RESTful API. In addition, React Native will be used to develop a basic mobile application. The primary purpose of these two technologies is to create an API and have a simple UI that can be interacted with. 




# Chat Module:

Creating the chat module requires two phases for completion. The first implementation will be as follows:

1. Create a response to a received piece of data (in this case, receiving a message). 
2. Take that data (initial format will be a json file for simplicity) and store the data into a "database" (we'll assume we linked a database but actual implementation will come at a later time). 
3. Convert the API to a REstful API. This will be done using Flask framework. 


