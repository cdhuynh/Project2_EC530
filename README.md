# Project2_EC530

This repository contains the general functionality in which the program will interpret a JSON file and determine whether the input is in the correct format. Following this, the program will produce a JSON file in return. 

The minimum required are the fields: "Name" and "Age". Each module will specify what it is required for the program to correctly parse the information. 


# Chat Module:

Creating the chat module requires two phases for completion. The first implementation will be as follows:

1. Create a response to a received piece of data (in this case, receiving a message). 
2. Take that data (initial format will be a json file for simplicity) and store the data into a "database" (we'll assume we linked a database but actual implementation will come at a later time). 
3. Convert the API to a REstful API. This will be done using Flask framework. 
