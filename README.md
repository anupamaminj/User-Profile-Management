# User Profile Management

A web application for managing user profiles with mobile number-based authentication. Users can log in using their mobile number, view their profile details, and update their information.

---

##  Technologies Used 

•	Framework: Django
•	Frontend: HTML, CSS, JavaScript
•	Database: SQLite


## Usage
1.	Navigate to http://127.0.0.1:8000/login/ to log in using a registered mobile number.
2.	If the number exists, the user is redirected to their profile page.
3.	Users can view their details and update individual fields.
4.	Changes are saved to the database, and the last_updated timestamp is refreshed


##  Features

- **Login Page**:
    1. Mobile number input with validation (10 digits)
    2. Error handling for invalid numbers
    3. Display message if the number is not found
- **Profile Display**:
    1. Organized layout showing all user details
    2. Clear indication of empty/missing fields
    3. User-friendly timestamp formatting
- **Profile Update**:
    1. Edit individual fields with an update button
    2. Save updated data to the database
    3. Automatically update the last_updated timestamp
- **Data Validation**:
    1. PAN card format validation (ABCDE1234F)
    2. Email format validation
    3. Mobile number format validation
    4. Required field validation where applicable




