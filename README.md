Unified Portal For Hall Automation
==================================

This application was made as a course project of [CS253A](https://www.cse.iitk.ac.in/users/isaha/Courses/sdo22.shtml/): Software Development and Operations in spring 2022 under the guidance of [Dr. Indranil Saha](https://www.cse.iitk.ac.in/users/isaha/).

Unified Portal for Hall Automation is a merged platform designed for the residents of various halls at IITK to access day to day hall functionalities. This portal aims to digitalize various services provided by the hall that includes mess, canteen and various other services. Through this portal, you can book your mess extras, order your canteen food, request room cleaning, book various Hall facilities, and many more.

Broadly, the application will support the following:

* Students can pre-book extras in mess and order food in canteen.
* Students can book the hall's guest room, gym and sports courts online and also schedule cleaning services.
* Students can access their pending mess and canteen bills.
* Special permissions have been provided to the Hall Manager, Mess manager, Canteen Owner and the sports secretary to facilitate all these services.

## Group Details

| Name                | Roll no. | Email Id                |
| ------------------- | -------- | ----------------------- |
| Soham Amit Bharambe | 210264   | sohamb21@iitk.ac.in     |
| Divyansh            | 210355   | divyansh21@iitk.ac.in   |
| Divyansh Chhabria   | 210356   | divyanshc21@iitk.ac.in  |
| Jhalak Sharma       | 210474   | jhalak21@iitk.ac.in     |
| Kriti               | 210534   | kriti21@iitk.ac.in      |
| Kumar Harsh Mohan   | 210543   | harshmohan21@iitk.ac.in |
| Labajyoti Das       | 210552   | labajyoti21@iitk.ac.in  |
| Pranjal Singh       | 210744   | psingh21@iitk.ac.in     |
| Rajeev Kumar        | 210815   | rajeevks21@iitk.ac.in   |
| Sandeep Nitharwal   | 210921   | nsandeep21@iitk.ac.in   |

## Deployment

The web app is deployed at: https://upha.pythonanywhere.com/

## How to run the software locally?

* Make sure you have python and pip installed in your system.

Clone the repository-

```
git clone https://github.com/divc13/Unified-Portal-For-Hall-Automation
```

Run following commands to start the backend server-

```
cd Unified-Portal-For-Hall-Automation
```

```
pip install requirements.txt
```

```
python manage.py collectstatic
```

```
python manage.py makemigrations
```

```
python manage.py migrate
```

```
python manage.py runserver
```

Go on the localhost web address which must have been printed on the terminal.

## Demo run

![Screenshot](https://github.com/divc13/Unified-Portal-For-Hall-Automation/blob/e6049ef7f54690a1fa47d1bcfaf8d0656a4894a6/templates/static/demo_run_screenshot.jpg)

## Software Requirement Specification Document

A software requirements specification (SRS) is a document that describes what the software will do and how it will be expected to perform. It also describes the product's functionality to fulfill all stakeholders needs.

Link to SRS: [UPHA SRS v1.0 | The Tech Titans](https://github.com/divc13/Unified-Portal-For-Hall-Automation/blob/b440561306807d7626e09bd68bc8efed32ae3237/Documents/UPHA_Software_Requirement_Specification%20.pdf)

## Software Design Document

A software design document (SDD) describes software created to facilitate analysis, planning, implementation, and decision-making. This explains how a software product or a feature will be built to meet a set of technical requirements. If the requirements document describes the "what" of your project, the design document focuses on the "how".

Link to SDD: [UPHA SDD v1.0 | The Tech Titans](https://github.com/divc13/Unified-Portal-For-Hall-Automation/blob/b440561306807d7626e09bd68bc8efed32ae3237/Documents/UPHA_Software_Design_Document.pdf)

## Software Implementation Document

A software implementation document (SID) is a document that describes how a software product is built to meet a set of technical requirements. This document talks about implementation details like integration, CI/CD, hosting, VCS; it provides a surface-level overview of codebases and completeness of the application.

Link to SID: [UPHA SID v1.0 | The Tech Titans](https://github.com/divc13/Unified-Portal-For-Hall-Automation/blob/b440561306807d7626e09bd68bc8efed32ae3237/Documents/UPHA_Software_Implementation_Document.pdf)

## Testing Document

Test documentation includes all files that contain information on the testing team's strategy, progress, metrics, and achieved results. The combination of all available data serves to measure the testing effort, control test coverage, and track future project requirements.

Link to Test Doc: [UPHA SRS v1.0 | The Tech Titans](https://github.com/divc13/Unified-Portal-For-Hall-Automation/blob/6211934322394b97042cb2a2c798cd71dbd07766/Documents/UPHA_Test_Document.pdf)

## User Manual Document

A manual is a document that provides instructions or guidelines on how to perform an activity and serves as a reference book on the activity.

Link to User Manual: [UPHA SRS v1.0 | The Tech Titans](https://github.com/divc13/Unified-Portal-For-Hall-Automation/blob/b440561306807d7626e09bd68bc8efed32ae3237/Documents/UPHA_User_Manual.pdf)

## Code Structure

The project has been divided into following small apps-

- Mess -  It contains implementation of functionalities related to mess, i.e., student can view regular menu, book extras, view order history, and apply for rebate, and owner can modify regular menu and extras, react on rebate requests, view students’ bill, view extras orders, view feedback on regular menu, and modify BDMR.
- Canteen -  It contains implementation of functionalities related to canteen, i.e., students can place order, view pending order, and view order history, and owner can react to orders, modify menu, and view students’ bill.
- Booking -  It contains implementation of functionalities related to booking, i.e., guest room booking, sports equipment issue, and sports court booking.
- Cleaning -  It contains implementation of functionalities related to cleaning, i.e., lodge request and view past requests.
- Login -  It contains implementation of functionalities related to login, i.e., login old user, new user registration, and reset password.
- My_Account -  It contains implementation of accounts management of the students, i.e., mess bill, canteen bill, and electricity bill.
- Home -  It contains implementation of the homepage.

Three more folders and two more files are also present in the repository-

- templates -  It contains HTML files of base template.
- UPHA -  It contains files which are necessary to run the web app.
- manage.py -  A command-line utility that lets us interact with this Django project in various ways such as run server, create new app, etc.

Each app mentioned above contains following folders and files-

- migrations -  It propagates changes we make to our models (adding a field, deleting a model, etc.) into our database schema.
- templates -  It contains HTML files of web pages of the respective app.
- static (present only in Home and Login) -  It contains CSS files of web pages and also images related to them of the respective app.
- \_\_init\_\_.py -  It is an empty file that tells Python that this directory should be considered a Python package.
- admin.py -  It contains the administration interface for our app. The admin interface is a web-based interface that allows authorized users to manage the data in your app, including creating, editing, and deleting records.
- apps.py -  It contains the configuration for a specific Django app. It is used to customize various aspects of the app's behavior.
- models.py -  It contains the structure of our database tables using Python classes. Each class represents a database table, and the attributes of the class define the fields of the table.
- tests.py -  It is a module where we write test cases for our application. It should contain one or more classes that inherit from Django's TestCase class. Each class represents a group of related tests, and each method within the class represents a specific test.
- urls.py -  It contains the URL patterns for our application. Each URL pattern maps a URL to a specific view, which generates the HTTP response for that URL.
- views.py -  It contains the logic for handling requests and generating responses. Each view function takes a request object as its first argument and returns an HTTP response object.

## Directory Hierarchy

```
|—— .gitignore
|—— Booking
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— templates
|        |—— booking_error.html
|        |—— Booking_manager.html
|        |—— courts.html
|        |—— guestroom.html
|        |—— secy_add_equipments.html
|        |—— secy_validate_request.html
|        |—— secy_validate_return.html
|        |—— sports_equipments.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— Canteen
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— templates
|        |—— Owner_Modify_Menu.html
|        |—— Owner_New_Order.html
|        |—— Owner_Pending_Order.html
|        |—— Owner_Students_Bill.html
|        |—— Student_Cart.html
|        |—— Student_Orders_History.html
|        |—— Student_Pending_Order.html
|        |—— Student_Place_Order.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— Cleaning
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— templates
|        |—— Cleaning_hall.html
|        |—— Lodge_Request.html
|        |—— Past_Request.html
|        |—— Pending_Request.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— Home
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— static
|        |—— hall_image.jpg
|    |—— templates
|        |—— Home.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— Login
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— static
|        |—— Login
|            |—— upha.png
|            |—— vector.png
|    |—— templates
|        |—— Login.html
|        |—— OTP.html
|        |—— Reset_Password.html
|        |—— Set_Password.html
|        |—— SignUp.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— manage.py
|—— Mess
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— templates
|        |—— Manager_Extra_Items.html
|        |—— Manager_Modify_BDMR.html
|        |—— Manager_Modify_Menu.html
|        |—— Manager_Rebate_Requests.html
|        |—— Manager_Students_Pending_Bills.html
|        |—— Manager_View_Feedback.html
|        |—— Manager_View_Orders.html
|        |—— Student_Apply_For_Rebate.html
|        |—— Student_Booked_Extras.html
|        |—— Student_Book_Extras.html
|        |—— Student_Order_History.html
|        |—— Student_Regular_Menu.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— My_Account
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— templates
|        |—— Canteen.html
|        |—— Mess.html
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|    |—— __init__.py
|—— templates
|    |—— error.html
|    |—— staff_base.html
|    |—— static
|        |—— booking__1__1.png
|        |—— football.png
|        |—— home_1.png
|        |—— hostel.png
|        |—— household_1.png
|        |—— logo_black_1.png
|        |—— main_display.png
|        |—— power_1.png
|        |—— rectangle_5.png
|        |—— staff_base.css
|        |—— student_base.css
|        |—— styles.css
|        |—— wallet_1.png
|    |—— student_base.html
|—— UPHA
|    |—— asgi.py
|    |—— settings.py
|    |—— urls.py
|    |—— wsgi.py
|    |—— __init__.py
```
