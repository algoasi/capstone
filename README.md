# WGU C964 Capstone
### Diabetes Prediction

This readme will guide you through how to run the application.

##### Initial Setup
To run this program, you will need to have Python 3 installed. You can follow [these instructions](https://docs.python-guide.org/starting/install3/osx/) to install via Homebrew if using MacOs or download the executable for Windows [here](https://www.python.org/downloads/).

##### Running the program
Clone this repo and open it in your editor.
From your terminal, make sure you are in the directory of this repo.
cd into the server directory
&nbsp;&nbsp;&nbsp;&nbsp;`cd server`
Install the requirements
&nbsp;&nbsp;&nbsp;&nbsp;`pip install -r requirements.txt`
Run the app
&nbsp;&nbsp;&nbsp;&nbsp;`python server.py`
Navigate to https://localhost:8080

##### App Usage
The application has a form with several labeled input fields that are all numerical. Each one is required and you cannot submit the form if they are not all filled in. Once all the inputs are filled in, click the "Submit" button. This will send the data to the API endpoint which will return a value that classifies said data as being indicative of a risk of diabetes or not.