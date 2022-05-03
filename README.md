# Project2_EC530

This repository contains the general functionality in which the program will interpret a JSON file and determine whether the input is in the correct format. Following this, the program will produce a JSON file in return. 

The minimum required are the fields: "Name" and "Age". Each module will specify what it is required for the program to correctly parse the information. 


# Core Module:

The core module is designed to make API calls to either the admin or user modules. The initial implementation of a UI will involve using tkinter to create a basic interface.

For the API calls, the core module will have the user of the login interface to select whether they are an admin or a user. Based on the selection, the program will then call a function (admin_thread or user_thread) and spawn the corresponding the thread. There will be a check for the status code; if it is 404/not found, the thread should terminate. If not, then the thread should continue and execute the corresponding module. THe UI will redirect to another page based on this. 

The Admin or User module will then proceed to make their own API calls (primarily chat, EHR access, etc.). 
