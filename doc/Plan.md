# A plan for automating testing of an App interacts via REST API

<a name="Table of Contents"></a>
# Table of contents
1. [Precondition](#precondition)
2. [Auto Cases](#auto-cases)
   1. [Integration](#integration)
   2. [Unit](#unit)
   3. [System](#system)
3. [Tools Used](#tools-used)
4. [Risks](#possible-risks-in-automation)
5. [Interval time assessment](#interval-time-assessment-in-hours)

# Task:

Testing an application utilizing a REST API that enables users to interact 
with various items typically found in a shop. Additionally, observed 
Unit, Integration, and System tests, which encompass the core functionality of the application.

<a name="Pecondition"></a>
## Precondition:
1. Download zip file with existing files: app.py, db, run, models, resources and requirements.txt 
2. Install all requirements from requirements.txt, via command ``pip3 install -r requirements.txt`` in Terminal
3. Create Virtual Environment (venv) using command ```python3 -m venv venv```
4. Activate venv via command ``venv\Scripts\activate``
5. Launch an app on URL - http://127.0.0.1:5000

[To Table of Content ⬆](#table-of-contents)

<a name="Auto Cases"></a>
# Auto Cases

<a name="Integration"></a>
## Integration

**Testing Creating, Updating and Deleting for Item**
#### Steps:
1. Create Store and save it into Data Base
2. Create an Item with parameters
3. Checking that Item doesn't exist in a Store
4. Save the Item into the Data Base
5. Checking that Item has appeared in the Store
6. Delete the Item from the Store
7. Checking Item is not in the Store

**Testing Relationship of the Store**
### Steps:
1. Create Store and save it into Data Base
2. Create an Item with parameters
3. Save the Store into the Data Base
4. Save the Item into the Data Base
5. Checking that Store have a name "test store"

**Testing Creating, Updating and Deleting for Store**
### Steps:
1. Checking that Store doesn't exist in a Data Base
2. Save Store into a Data Base
3. Checking that Store has appeared in the Data Base
4. Delete the Store
5. Checking that Store is not in the Data Base

**Testing Relationship of the Item**
### Steps:
1. Create Store and save it into Data Base
2. Create an Item with parameters
3. Save the Store into the Data Base
4. Save the Item into the Data Base
5. Checking that Store has 1 item
6. Checking that Item name is "test_item"

**Checking Item has correct JSON format and it has appeared**
### Steps:
1. Create a Store
2. Create an Item
3. Save Store into the Data Base
4. Save Item into the Data Base
5. Assert the JSON format of the Item

**Testing User, Create, Read, Update, Delete**
### Steps:
1. Create the User with name of "test" and password of "abcd"
2. Checking that name of the User is 'test'
3. Checking that ID of the User in the Table is "1"
4. Save User into the Data Base
5. Checking that name of the User is 'test'
6. Checking that ID of the User in the Table is "1"


<a name="System"></a>
## System

**Testing GET request of an Item, without authorization**
#### Steps:
1. Make a GET request with item endpoint to a Data Base for non-authorization
2. Checking that status code like response is 401

**Testing GET request for Item witch doesn't exist**
### Steps:
1. Make a GET request with Authorization
2. Checking that status code like response is 404

**Testing a GET request with existing Item**
### Steps:
1. Create a Store with name "test" and save it into Data Base
2. Create an Item with name "test" and price "19.99" and save it into Data Base
3. Make a GET request with Authorization
4. Checking that there is 200 status code (OK)

**Testing delete an Item**
### Step:
1. Create a Store with name "test" and save it into Data Base
2. Create an Item with name "test" and price "19.99" ID is 1, and save it into Data Base
3. Make a DELETE request to a Data Base
4. Checking that there is 200 status code (OK)
5. Checking that JSON has a correct format with message 'Item deleted'

**Testing create an Item and POST**
### Steps:
1. Create a Store with name "test" and save it into Data Base
2. Make a POST request with price 17.99, store id is 1, and header "Authorization"
3. Checking that there is 200 status code (OK)
4. Checking that JSON has a correct format with name of Store 'test' and price 17.99

**Testing creating a duplicate Item**
### Steps:
1. Create a Store with name "test" and save it into Data Base
2. Create an Item with name "test" and price "17.99", ID is 1, and save it into Data Base
3. Make a POST request with price 17.99, store id is 1, and header "Authorization"
4. Checking that there is 400 status code
5. Checking that JSON has a correct format there is message is "An item with name 'test' already exists."

**Testing the PUT Item**
### Steps:
1. Create a Store with name "test" and save it into Data Base
2. Make a PUT request with price 17.99, store id is 1, and header "Authorization"
3. Checking that there is 200 status code (OK)
4. Checking that name of Item is "test" and price is 17.99
5. Checking that JSON has a correct format have a name 'test' and price 17.99

**Testing the PUT update Item**
### Steps:
1. Create a Store with name "test" and save it into Data Base
2. Make a PUT request with price 5.99, store id is 1, and header "Authorization"
3. Checking that Iem have a name "test" and price 5.99
4. Checking that there is 200 status code (OK)
5. Checking that name of Item is "test" and price is 17.99
6. Checking that JSON has a correct format have a name 'test' and price 17.99

**Testing Item List**
### Steps:
1. Create a Store with name "test" and save it into Data Base
2. Make a PUT request with price 5.99, store id is 1, and header "Authorization"
3. Make a GET to Data Base request
4. Checking that JSON format has a List with Item: name is 'test' and price 5.99

**Test creating a Store**
### Steps:
1. Make a POST request
2. Checking that there is 200 status code (OK)
3. Checking that in Data Base Store with name 'test' Exist
4. Checking that JSON have an Empty list of Items

**Testing create a Duplicate Store**
### Steps:
1. Make a POST request to Data Base twice
2. Checking that there is 400 status code

**Testing Delete the Store**
### Steps:
1. Create a Store with name 'test' and save in into Data Base
2. Make a DELETE request to Data Base
3. Checking that there is 200 status code (OK)
4. Checking that JSON has a correct format there is message 'Store deleted'

**Test finding a Store**
### Steps:
1. Create a Store with name 'test' and save in into Data Base
2. Make a GET request to Data Base
3. Checking that there is 200 status code (OK)
4. Checking that in Data Base Store with name 'test' Exist
5. Checking that JSON have an Empty list of Items

**Testing the Store witch not Found**
### Steps:
1. Make a GET request to Data Base
2. Checking that there is 404 status code
3. Checking that JSON has a correct format there is message 'Store not found'

**Test finding the Store with Items**
### Steps:
1. Create a Store with name "test" and save it into Data Base
2. Create an Item with name "test" and price "19.99", ID is 1, and save it into Data Base
3. Make a GET request to Data Base
4. Checking that there is 201 status code
5. Checking that JSON format has a List with Item: name is 'test' and price 19.99

**Checking that Store have an Empty List**
### Steps:
1. Create a Store with name "test" and save it into Data Base
2. Make a GET request to Data Base
3. Checking that JSON have an Empty list of Items

**Testing that Store have List with Items**
### Steps:
1. Create a Store with name "test" and save it into Data Base
2. Create an Item with name "test" and price "19.99", ID is 1, and save it into Data Base
3. Make a GET request to Data Base
4. Checking that JSON format has a List with Item: name is 'test' and price 19.99

**Test register user**
### Steps:
1. Make a POST request with register user with 'username' is 'test', 'password' is '1234'
2. Checking that there is 201 status code
3. Checking that user with username of 'test' is Exist in a Data Base
4. Checking that JSON has a correct format there is message 'User created successfully.'

**Test Registration and Login**
### Steps:
1. Make a POST request with register user with 'username' is 'test', 'password' is '1234'
2. Mke a POST request with authenticate user with 'username' is 'test', 'password' is '1234'
3. Checking there is access token

**Test Registration duplicate user**
### Steps:
1. Make a POST request with register user with 'username' is 'test', 'password' is '1234'
2. Mke a POST request with authenticate user with 'username' is 'test', 'password' is '1234'
3. Checking that there is 400 status code
4. Checking that JSON has a correct format there is message 'User already exist'


<a name="Unit"></a>
## Unit

**Test creating an Item**
### Steps:
1. Create an Item with name "test" and price "19.99", ID is 1, and save it into Data Base
2. Checking that the Item have a name 'test' 
3. Checking that the Item have a price 19.99
4. Checking that the Item have an ID "1"

**Testing an Item have a correct JSON format**
### Steps:
1. Create an Item with name "test" and price "19.99", ID is 1, and save it into Data Base
2. Checking that the JSON format haven't "The JSON export of the item is incorrect. Received {item.json()}, expected {expected}."

**Testing create a Store**
### Steps:
1. Create a Store with name "test" and save it into Data Base
2. Checking that the Store have name - 'test'

**Testing create a User**
### Steps:
1. Create a User with name 'test' and password 'abcd'
2. Checking that the User have name - 'test' 
3. Checking that the Store have password - 'abcd'


<a name="Tools Used"></a>
### Tools Used

- Asus VivoBook 14, core i5 - 10 gen.
- Python 3 - Popular programming language
- PyCharm 2023 1.4 - IDE
- Flask - Microframework

<a name="Risks"></a>
### Possible Risks in Automation

- Lack of documentation and clear technical specifications, which can lead to an error in the operation of a real application
- The total time spent on automation can exceed the total time of manual testing, and be very labor-intensive

<a name="Interval time assessment"></a>
### Interval time assessment (in hours)

- Writing an automation plan: 1 hour;
- Test environment setup: 10 min;
- Writing and debugging autotests: 11 hours;
- Witting the Documentation 2 hors;

**Total: 13 hours 10 min**