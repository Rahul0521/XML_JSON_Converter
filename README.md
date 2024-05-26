# XML_JSON_Converter
This is a Django Application which allows users to convert XML File to JSON Format.
XML to JSON Converter Web App
This project is a full-stack web application that allows users to upload XML files, converts them to JSON format, and provides the option to download the converted JSON file. The application is built using Django and Bootstrap, ensuring a responsive and user-friendly interface.

Features
Upload XML files
Convert XML to JSON format
Download the converted JSON file
Progress bar during upload and conversion process
Error handling and user feedback
Responsive design for desktop, tablet, and mobile devices
Secure handling of data with CSRF tokens
Technologies Used
Django
Python
Bootstrap
HTML
CSS
JavaScript
jQuery
Docker
Getting Started
Prerequisites
Python 3.7+
Docker (for containerization)
pip (Python package installer)
Installation
Clone the repository:

bash
```git clone https://github.com/Rahul0521/XML_JSON_Converter.git```
```cd xml-to-json-converter```
Create a virtual environment and activate it:

bash

```python -m venv venv```
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash

```pip install -r requirements.txt```
Run database migrations:

bash

```python manage.py migrate```
Run the development server:

bash

```python manage.py runserver```
The application should now be running at http://127.0.0.1:8000.

Docker
Build the Docker image:

bash

```docker build -t xml_to_json_converter .```
Run the Docker container:

bash

```docker run -p 8000:8000 xml_to_json_converter```
The application should now be running at http://127.0.0.1:8000.

Usage
Upload XML File:

Navigate to the home page, upload your XML file, and click the "Upload" button.

Conversion Progress:

A progress bar will show the status of the upload and conversion process.

Download JSON File:

Once the conversion is complete, you will be redirected to a page displaying the JSON data. Click the "Download JSON" button to download the file.

Error Handling
If the uploaded file is not a valid XML file, you will be redirected to an error page with a message indicating the issue.

Responsive Design
The application uses Bootstrap for a responsive design, ensuring it works well on desktops, tablets, and mobile devices.

Security
CSRF protection is enabled to prevent cross-site request forgery attacks.
File handling is done securely in memory to protect user data.
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository
Create a new branch (git checkout -b feature-branch)
Make your changes
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature-branch)
Create a new Pull Request
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions or feedback, please contact me at yadav.rahul0521@gmail.com.

