# PROJECT LOG FORMAT

## DATE, 2021 (Day  #100DaysofCode)

**Today's Progress**:

**Thoughts**: 

**Resources**

----------------------------------------------------------
## February 3, 2021 (Day 26 #100DaysofCode)

**Today's Progress**:
- Continued with Frontend Development Career Path: Started Module 2
    - HTML elements
    - Basic HTML file structure
    - Headings and paragraphs
    - Strong `<strong>` and emphasis `<em>` inline elements
- Worked on Homeschool Web App:
    - Add activity table to `index.html`
    - Wrote query to select activity data for current date (`today`) in `/index` route
    - Added select dropdown form that will eventually link to queries to show activities based on selection (Today, This Week, Next Week)

**Thoughts**: 
- I've started taking notes for my coding courses in Notion and it's been extremely helpful for organizing my notes and embedding code snippets. It is also a database system, so it's also great for organizing the various resources I've been collecting for future review.
- I ran into an issue where I was trying to test submission in one form and it would display errors in a different form on the same page even though the original form passed validation and I had not clicked the submit button on the different form. I then realized that I had to change the names of the variables attributed to the `SubmitField` so they would be different for both forms (they were previously both named `submit`). Then I updated the conditional statement in the `/index` route that checked for the the name of the submit button passed from the form(input name is passed from WTForms field name) & checked form validation before continuing with further actions. Now validation works correctly for both forms on the `index.html` page. 

```python
# In forms.py

class AddAttendanceForm(FlaskForm):
    """Add attendance form"""
    attendance_date = DateField('Date', format='%Y-%m-%d')
    student = SelectField(u'Student', choices=[])
    submit = SubmitField('Log Attendance')

class DisplayActivitiesForm(FlaskForm):
    """Display activites form"""
    display = SelectField(u'Display', choices=['Today','This Week','Next Week'])
    display_submit = SubmitField('Display')

# In routes.py

# Validation for form
if "submit" in request.form and form2.validate_on_submit():
    # Continue with further steps

# Validation for form
if "display_submit" in request.form and form3.display.validate(form3):
    # Continue with further steps
```

**Resources**
1. [Combining multiple forms in WTForms](https://dev.to/sampart/combining-multiple-forms-in-flask-wtforms-but-validating-independently-cbm)
2. [Flask multiple forms on the same page](https://stackoverflow.com/questions/58122969/flask-multiple-forms-on-the-same-page)
3. [Notion](https://www.notion.so/)
4. [Scrimba's Frontend Development Career Path](https://scrimba.com/learn/frontend)

----------------------------------------------------------
## February 2, 2021 (Day 25 #100DaysofCode)

**Today's Progress**:
- Started Scrimba's Frontend Development Career Path and completed Module 1.

**Thoughts**: 
- In one of the introductory projects in the Frontend Development Career Path, I was introduced to using CSS custom properties(variables). This is something I need to incorporate in this project's design! CSS custom properties allow you to define a value in one place and then reference it multiple times in other places. 

**Resources**
1. Emojis: [getemoji.com](https://getemoji.com/), [emojipedia.com](https://emojipedia.org/) 
2. [CSS custom properties(variables)](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
3. [Scrimba's Frontend Development Career Path](https://scrimba.com/learn/frontend)
----------------------------------------------------------

## January 31, 2021 (Day 24 #100DaysofCode)

**Today's Progress**: 
- Studied `onclick` event handlers and created a CodePen that shows/hides a box based via onclick event
- Added ability to dismiss Flask flash messages with button `onclick` event

**Link to Work**:
1. [Show/Hide a box based on button onclick event](https://codepen.io/maelingcodes/pen/eYBmMQa)

**Resources**
1. [How to - Alerts](https://www.w3schools.com/howto/howto_js_alert.asp)
----------------------------------------------------------
## January 30, 2021 (Day 23 #100DaysofCode)

**Today's Progress**:
- Completed Scrimba's Learn UI Design Fundamentals course
- Added logic to `/attendance` and `/index` routes that checks if attendance record already exists for a student before adding it to the database 

**Links to Work**:
1. [Learn UI Design Fundamentals - The Final Challenge](https://scrimba.com/scrim/co1674fe78bf180844353256c)
2. [Learn UI Design Fundamentals - Design Challenge 4: Visual Hierarchy](https://scrimba.com/scrim/co2c0433387188c01ecbd9341)
3. [Learn UI Design Fundamentals - Design Challenge 3: Color](https://scrimba.com/scrim/co8ec4c2a9b9b25989a37081c)

**Resources**
1. [StyleStage.dev - View how multiple people style one HTML page](https://stylestage.dev/styles/)

----------------------------------------------------------
## January 29, 2021 (Day 22 #100DaysofCode)

**Today's Progress**:
- Started Scrimba's Learn UI Design Fundamentals course to help me with the design aspect of my web app project

**Thoughts**: 
- Some of the fundamentals to consider for great design:
    - White Space
    - Color
    - Contrast
    - Scale
    - Alignment
    - Typography
    - Visual Hierarchy 
- WCAG has issued contrast guidelines for the visual representation of text and images of text. You can use contrast checking tools to help your projects adhere to these guidelines when designing (e.g. browser plugins, websites, UI design application plugins)

**Resources**
1. [WAVE - Web Accessibility Evaluation Tool](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh/related?hl=en-US)
2. [Contrast Checker - WebAim](https://webaim.org/resources/contrastchecker/) and their [API](https://webaim.org/resources/contrastchecker/?fcolor=EBE6EB&bcolor=1F76C7&api)
3. [Learn UI Design Fundamentals - Free course on Scrimba taught by Gary Simon](https://www.freecodecamp.org/news/learn-ui-design-fundamentals-with-this-free-one-hour-course/)

----------------------------------------------------------
## January 28, 2021 (Day 21 #100DaysofCode)

**Today's Progress**:
- Added ability for user to remove students and subjects (and their associated activities) from their Profile Edit pag (`profile-edit`)
- Learned how to use datetime module to create variable that holds current date. I had to pass the `today` variable to `index.html` and set it to the value attribute for the `{{ form2.attendance_date }}` field. 
```python
import datetime

today = datetime.date.today()
```
**Thoughts**: 
- I received errors when I removed a student from the database. Since I still had activities trying to show on `log.html` that were associated with that particular student id, the errors I received were SQL-related dealing with a NOT NULL constraint. I then realized I needed to also delete all associated student activities when deleting a student by accessing `student.activities`.
- I was able to get a static data HTML table working with Bootstrap Table with a filter extension that allows me to filter by the data in each column. However, I have not been able to get it to work with the dynamic data inserted via the Jinja template variables that are linked to my database queries. If I do end up getting this to work with my data, I will need to change my activity.status 'Not Completed' variable to 'Incomplete' so it will sort properly in the bootstrap-table. I may come back to trying to add this feature later but I did want to note what external dependencies I had to include to get the static TEST table on `log.html` working for Bootstrap Table - Filter Control:
    - CSS (place in <head> of `base.html`): 
        - `<link rel="stylesheet" href="https://unpkg.com/bootstrap-table@1.18.2/dist/bootstrap-table.min.css">`
    - JS (place right before `</body>` in `base.html`):
        -  `<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.10.0/bootstrap-table.js"></script>`
        - `<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.9.1/extensions/filter-control/bootstrap-table-filter-control.js"></script>`
**Resources**
1. [The Figma 2021 Crash Course by Example - Gary Simon](https://www.youtube.com/watch?v=Gu1so3pz4bA)
2. [Bootstrap Table Filter Control & Export Example](https://codepen.io/AurelieT/pen/JGxMgo)
3. [Bootstrap Table Options](https://bootstrap-table.com/docs/api/table-options/)
4. [Bootstrap Table - Getting Started](https://bootstrap-table.com/docs/getting-started/introduction/)
5. [datetime - Python docs](https://docs.python.org/3/library/datetime.html)
----------------------------------------------------------
## January 27, 2021 (Day 20 #100DaysofCode)

**Today's Progress**:
- Updated `/delete` route so activity records can be removed from the db via the delete button on the `log.html` page
- Added flash messaging to `update` route 
- Created user profile page (`profile.html`) that displays user's current list of students and subjects 
- Started working on an edit profile page (`profile-edit.html`) where user can add/remove students and subjects from their account.
    - Added functionality for user to add students and subjects to their account

**Thoughts**: 
- Glad to find out I can display two different FlaskForm classes on one html page. I did this so a user can add a student or a subject on the `profile-edit.html` page. When instantiating the forms in the route (`/profile-edit`), I made sure to have two different variable names for the forms and pass those two names through the render_template function to display the form fields via Jinja template variable names in `profile-edit.html`. 

**Resources**
1. [Bootstrap Filter Control Table](https://examples.bootstrap-table.com/#extensions/filter-control.html)

----------------------------------------------------------
## January 26, 2021 (Day 19 #100DaysofCode)

**Today's Progress**:
- Changed submit button label text to 'Update Activity' on `update.html`: `form.submit.label.text = "Update Activity"`
- Added `/details` route and `details.html` to template files in order to display activity record details 

----------------------------------------------------------
## January 25, 2021 (Day 18 #100DaysofCode)

**Today's Progress**:
- Added column for a delete button in attendance log table on `attend.html`. Linked to database in `/delete/attendance` route to commit the deletion changes. 
- Linked form data to database in`/update` route so user can update an activity record. User selects activity record on `log.html`, which takes them to `update.html`. They are then presented with a form with the current activity data populating the form. The user can then make changes in the form and upon submission, the changes are updated and committed in the database.
- Added some CSS styling (`display:flex`) to the attendance log form. Will need to add media queries to display as block for smaller viewports

----------------------------------------------------------
## January 24, 2021 (Day 17 #100DaysofCode)

**Today's Progress**:
- Learned how to pass an object into a WTForms form to be able to autofill certain form fields 
- Learned how to pass URL arguments to Flask routes
- Added `/update` route which takes the activity title as an argument (passed from 'Update' button in table on `log.html`) and displays a form to edit activity details (need to populate with user's data for the specific activity record and link to database in order to commit changes)
- Figured out how to prepopulate data for all fields in the form shown when a user clicks to update their activity record. Form details are populated via the `/update` route and shown on `update.html`.

**Thoughts**: 
- The code below, which links to a WTForms TextAreaField, does NOT show the user's description that was saved to the db. Setting the value in this case does not prepopulate the form with this data from `activity.description`. 
```html
 <div class="form-group">
        {{ form.description.label }}
        {{ form.description(size=500, class_='form-control', value=activity.description) }}
</div>
```
but the code blocks for other WTForm fields (StringField, DateField) work at populating the user data from the db using the following code:
```html
<div class="form-group">
    {{ form.title.label }}
    {{ form.title(size=100, class_='form-control', value=activity.title) }} 
    {% for error in form.title.errors %}
    <span style="color:red;">[{{ error }}]</span>
    {% endfor %}
</div>

<div class="form-group float-item">
    {{ form.activity_date.label }}
    {{ form.activity_date(class_='datepicker form-control', value=activity.activity_date) }}
    {% for error in form.activity_date.errors %}
    <span style="color:red;">[{{ error }}]</span>
    {% endfor %}
</div>
```
- I'm having issues prepopulating my Update Activity form with user data because I cannot get the modal links to pass the activity id to the `/log` route. I think I may be able to avoid some issues by creating a separate `/update` route and view function and remove the modal windows from `log.html`.


**Resources**
1. [Populating WTForms form fields with data](https://stackoverflow.com/questions/42984453/wtforms-populate-form-with-data-if-data-exists)
2. [Passing URL Arguments in Flask Using URL Converter](https://www.youtube.com/watch?v=qYeWemghBxI)
3. [Passing variables into url_for](https://stackoverflow.com/questions/48265877/how-to-access-variables-within-html-template-url-for)
4. [FontAwesome Icon Gallery - Latest Version](https://fontawesome.com/icons?d=gallery)

----------------------------------------------------------
## January 23, 2021 (Day 16 #100DaysofCode)

**Today's Progress**:
- Displayed attendance records in table in descending order: `attendance_records = current_user.attendance.order_by(Attendance.attendance_date.desc()).all()`
- Diplayed activity records in table in ascending order: `activities = current_user.activities.order_by(Activity.activity_date).all()`
- Worked on 'Update Activity' modal on log.html. Modal window now shows field data associated with the specific activity record, to allow user to update an activity. Still working on how to prepopulate the checkbox if activity has already been completed (linked to WTForms BooleanField object). Still need to pass data to '/update' route to actually add any changes from form data to the database. Also need to learn how to prepopulate the student and subject dropdown fields in the modal window. 

**Resources**
1. [Build a CRUD web app with Python & Flask - Part Two](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-two)
2. [Jinja, Flask and WTForms - how to pass parameters in field?](https://stackoverflow.com/questions/35768370/jinja-flask-and-wtforms-how-to-pass-parameters-in-field)
3. [Template Designer Documentation - Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/#assignments)
4. [How to change the default width of Bootstrap modal box](https://www.tutorialrepublic.com/faq/how-to-change-the-default-width-of-bootstrap-modal-box.php)
----------------------------------------------------------
## January 22, 2021 (Day 15 #100DaysofCode)

**Today's Progress**:
- Learned about how to undo changes in my repository with `git checkout`, `git revert` and `git reset`
- Reverted project to its state on 1/20/21
- Added student_id to Activity model and changed student-activity relationship to one-to-many in `models.py`
- Correctly passed student_id and subject_id to activity table when adding a new activity in `/add` route 
- Added `user_id` to `Subject` model. Changed user-subject relationship to one-to-many and removed user_subject helper table
- Used conditional logic to convert Boolean status data from Activity Form to "Completed"(True=1) or "Not Completed"(False=0), which was passed to the activity object in the database for the status field. 
- Learned how to implement FontAwesome icons within buttons and read about best practices for accessibility when using icons 
- Added ability to add attendance data for user's students on `attendance.html`
- Created a table to display all the attendance records associated with a user 

**Thoughts**: 
- I'm not sure what happened, but my `venv` folder disappeared from my project. Had to redo the following to setup my virtual environment:
    - Create a virtual environment: `python3 -m venv venv`
    - Activate virtual environment: source venv/bin/activate
    - Install flask: `pip install flask`
    - Set FLASK_APP environment variable: `export FLASK_APP=journal.py`
    - Install the python-dotenv package: `pip install python-dotenv`
    - Create .flaskenv file with environment variables for flask command (e.g. FLASK_APP=journal.py)
    - Upgrade pip version: `pip install --upgrade pip`
    - Install Flask-WTF: `pip install flask-wtf`
    - Install Flask-SQLAlchemy: `pip install flask-sqlalchemy`
    - Install Flask-Migrate: `pip install flask-migrate`
    - Install Flask-Login: `pip install flask-login`
    - Install Email() validator from WTForms: `pip install email-validator`
- To display headers when you're retrieving results from queries in sqlite terminal: `.headers on`. If you'd like to also display in column format: `.mode column`

**Resources**
1. [Undoing things with Git & GitHub](https://www.youtube.com/watch?v=RIYrfkZjWmA)
2. [Font Awesome Examples](https://fontawesome.com/v3.2.1/examples/)
3. [Accessibility with Icons - FontAwesome](https://fontawesome.com/how-to-use/on-the-web/other-topics/accessibility)
----------------------------------------------------------
## January 21, 2021 (Day 14 #100DaysofCode)

**Today's Progress**:
- I am now able to display the current user's list of activities in `/log` view, although all of the associated data is not populated (see 'Thoughts' below)

**Thoughts**: 
- I feel like I've gone in loops today trying to understand how to write queries in Flask-SQLAlchemy. I am trying to understand why my subject and student name data don't show up in my Activity Log table. Now I'm not sure if I should save the subject and student names directly as fields in the Activity model OR if I should try to query the database to save the student and subject ids to the Activity model and then run another query when it's time to display the student and subject names in the Activity log (on `/log` view). I've made changes to my files tonight but I'm not pushing anything (except for my project log) because I probably should start with a clean slate for tomorrow since I'm in such a state of confusion. 
- Activity status type is a a Boolean where (0 = not completed (FALSE), 1 = completed (TRUE))

**Resources**
1. [Debugging Queries in Flask-SQLAlchemy](https://www.youtube.com/watch?v=5puPZ3n06EE)
2. [Query API - SQLAlchemy Docs](https://docs.sqlalchemy.org/en/13/orm/query.html)
3. [Flask-SQLAlchemy with examples](https://pythonbasics.org/flask-sqlalchemy/)
4. [Get list of column names in SQLite](https://stackoverflow.com/questions/685206/how-to-get-a-list-of-column-names/685212)
5. [Nested queries with Sqlalchemy](https://blog.miguelgrinberg.com/post/nested-queries-with-sqlalchemy-orm)

----------------------------------------------------------
# PROJECT LOG
## January 20, 2021 (Day 13 #100DaysofCode)

**Today's Progress**:
- Added string representations of the Student and Subject objects so the names could appear as choices in the the 'Add Activity' form in the `/add` route. 
- Passed 'Add Activity' form data to database. Removed mock objects for Subject and Student choices and replaced with user's student and subject data from their User object in the database.

**Thoughts**: 
- If terminal closes and need to run app, make sure to: Change into correct directory; Activate virtual environment `source venv/bin/activate` ; Export Flask environment variables `export FLASK_APP=journal.py`, `export FLASK_DEBUG=True`; Run the app `flask run`

**Resources**
1. [Python __str__() and __repr__() methods](https://www.journaldev.com/22460/python-str-repr-functions)

----------------------------------------------------------
## January 19, 2021 (Day 12 #100DaysofCode)

**Today's Progress**:
- Passed 'Add Subject' form data from `index.html` to '/index` route.
- Linked 'Add Subject' form data to database in `/index` route and learned how to insert data into table using a backref from a many-to-many relationship 

**Thoughts**: 
- (Referencing the code in the `\index` route in `routes.py`. I kept getting this error (`TypeError: 'int' object is not iterable`) when I was trying to link the student object with the backref ('admin'). I then realized I needed to append the  `current_user.id` to the admin property of the student object I created. I needed to use the 'admin' backref in this manner because I am dealing with a many-to-many relationship betweent the user and subject tables. 
```python
# The code that gave me the TypeError: 'int' object is not iterable
for name in subject_names:
            subject = Subject(subject_name=name, admins=current_user.id)
            db.session.add(subject)
            db.session.commit()

# The correct way to link the current_user to the student object, via the backref
# 'admin' that was created via the many-to-many relationship between user and subject
# tables
for name in subject_names:
            subject = Subject(subject_name=name)
            subject.admins.append(current_user) # Using backref to associate subject with current user
            db.session.add(subject)
            db.session.commit()
```

**Resources**

----------------------------------------------------------
## January 18, 2021 (Day 11 #100DaysofCode)

**Today's Progress**:
- Studied the differences between declaring models for one-to-many and many-to-many relationships
- Added 2 helper/association tables (user_subject, student_activity) (required for many-to-many relationships) to `models.py` and updated the models that required the `db.relationship()` function to relate properly to each other. 
- Updated form structure on `index.html` so user can add students and subjects to their profile. 

**Thoughts**: -
- I ran into errors when adding my helper tables and updating my models. I was able to create the migration script, but received an error (`raise ValueError("Constraint must have a name")`) when trying to run `flask db upgrade`. I was able to implement [this solution](https://stackoverflow.com/questions/45527323/flask-sqlalchemy-upgrade-failing-after-updating-models-need-an-explanation-on-h) which required adding a `naming_convention` to my __init__.py file. The solution worked after I deleted my existing database - `app.db`, `migrations/` folder and then ran `flask db init`, `flask db migrate` and finally `flask db upgrade `.
- To turn on debugger when running app,  run `export FLASK_DEBUG=True` in the terminal before running `flask run`

**Resources**
1. [Declaring models - Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)
2. [Creating One-To-Many Relationships in Flask-SQLAlchemy](https://www.youtube.com/watch?v=juPQ04_twtA)
3. [Creating Many-To-Many Relationships in Flask-SQLAlchemy](https://www.youtube.com/watch?v=OvhoYbjtiKc)
----------------------------------------------------------

## January 17, 2021 (Day 10 #100DaysofCode)

**Today's Progress**:
- Added `Student` and `Subject` database models to `models.py`

**Thoughts**: 
- Realized today that the relationship between my students and activities table is many-to-many. A student can have many activities and an activity can have many students. I need to create an association table to be able to join those two tables together for queries.

**Resources**
1. [Creating Many-To-Many Relationships in Flask-SQLAlchemy](https://www.youtube.com/watch?v=OvhoYbjtiKc)
2.  [Many to Many - SQLAlchemy Docs](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many)
3. [Many to many relationships in SQLAlchemy models (Flask)](https://www.michaelcho.me/article/many-to-many-relationships-in-sqlalchemy-models-flask)

----------------------------------------------------------
## January 16, 2021 (Day 9 #100DaysofCode)

**Today's Progress**:
- Added student number to User database model
- Removed 'Add Student' fields from registration form
- Added 'Add Student(s)' form to index.html and updated the `/index` route so information passed from the form gets added to the database (names added to `student` table associated with user_id, student_number field in `user` table)
- Added conditional statment to index.html so the 'Add Student' section only shows if a user doesn't have a student number saved in the `user` table (e.g. `{% if not current_user.student_number %}`)
- Added CSS styling to Flash messaging by category

**Thoughts**: 
```sqlite
Open a database file in sqlite
sqlite> sqlite3 app.db

View all the tables in app.db
sqlite> .tables

View the schema for all tables in app.db
sqlite> .schema

Delete all rows from a table
sqlite> DELETE FROM <table>;

View all content in a table
sqlite> SELECT * FROM <table>;
```
- Flask `flash()` for flash messaging takes an optional second argument, categories. 

**Resources**
1. [Flashing messages with Flask](https://blog.tecladocode.com/flashing-messages-with-flask/)
2. [Message Flashing](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/)
----------------------------------------------------------
## January 15, 2021 (Day 8 #100DaysOfCode)

**Today's Progress**:
- Figured out how to dynamically add input fields to a form based on a user's select input. I was able to remove and add fields so the field number matched the user's select number. I learned more about how to interact with the DOM using JavaScript.
- Added an app.js file to my project and linked it on `base.html`


**Thoughts**: 
- Ran into issues today trying to figure out how to pass data from dynamically generated fields to the route using WTForms. I had to use a specific naming sequence for my input fields and `request.form.get("<name>")` to be able to access the data in those fields that populated based on the user's input. This is my workaround till I learn something better! 

**Resources**
1. [Dynamically adding HTML form fields based on user's input](https://stackoverflow.com/questions/31988183/dynamically-adding-html-form-fields-based-on-a-number-specified-by-the-user)
2. [Event Listeners on <select> elements - 1 choice example](https://stackoverflow.com/questions/24875414/addeventlistener-change-and-option-selection)
3. [Event Listeners - change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
4. [Adding input elements dynamically to form](https://stackoverflow.com/questions/14853779/adding-input-elements-dynamically-to-form#:~:text=If%20you%20want%20to%20dynamically,of%20them%20to%20the%20container.)
5. [Input text object properties](https://www.w3schools.com/jsref/dom_obj_text.asp)
6. [Dynamic Fields WTForms](https://www.rmedgar.com/blog/dynamic-fields-flask-wtf/)
----------------------------------------------------------
## January 14, 2021 (Day 7 #100DaysOfCode)

**Today's Progress**:
- Added `RegistrationForm` class to `forms.py`
- Installed `Email()` validator external dependency from WTForms: `$ pip install email-validator`
- Added registration form structure to `register.html`
- Added link to registration page below login form on `login.html`
- Added `/register` view on `routes.py` 
- Added custom messages for WTForms validation errors on `forms.py`

**Thoughts**: 
- When you define a class in Python, you can create class variables and instance variables. A class variable will be shared by all instances and an instance variable is unique to each instance. A good example of this in my project is my `RegistrationForm` class in `forms.py`. 

**Resources**
1. [Python Class and Instance Variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)
2. [Understanding Class and Instance Variables in Python3](https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3)
-  [Chapter 5: User Logins - Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)
3. [Form Validation with WTForms](https://flask.palletsprojects.com/en/1.1.x/patterns/wtforms/)

----------------------------------------------------------
## January 13, 2021 (Day 6 #100DaysOfCode)

**Today's Progress**:
- Added password hashing and verification (added to `app/models.py` via Werkzeug package)
- Added user loader function to `app/models.py`
- Added login functionality via flask-login
- Added logout view
- Added conditional logic for displaying login or logout link in nav bar
- Added login requirement for certain views with login decorators
- Added redirect to 'next' page in login view

**Resources**
-  [Chapter 5: User Logins - Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)

----------------------------------------------------------

## January 12, 2021 (Day 5 #100DaysOfCode)

**Today's Progress**:
- Added email field to 'user' database model
- Added 'login' view to `routes.py`
- Added LoginForm class to `forms.py`
- Created login.html to display login form 
- Added Activity class in `models.py`
- Fixed Alter table errors due to SQLite, followed [these instructions](https://blog.miguelgrinberg.com/post/). Had to make adjustments to database instance in `app/__init__.py`

**Thoughts**: 
 - Learned about the concept of multiple inheritance in Python and how it leads to the ability to use mixins to add different features to a class.
 - You can use a `pass` statement when writing a loop or function in python to serve as a placeholder, since you can't have an empty body. If you left it with an empty body, the interpreter would give an error. 
 - You can apply `index=True` as an attribute to a database model field in order to speed up queries on this column
 ```python
 # Example for the user table in models.py

 class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    students = db.relationship('Student', backref='admin', lazy='dynamic')
 ```
 - To view tables you created in sqlite, type `sqlite3 app.db` in the terminal. Then at the `sqlite>` command line, type `.tables`. To see schema for a specific table, type `.schema table`. To see all data in a specific table, type 

**Resources**
1. [Mixins and Python](https://www.ianlewis.org/en/mixins-and-python)
2. [Multiple inheritance in Python](https://www.geeksforgeeks.org/multiple-inheritance-in-python/)
3. [Python Multiple Inheritance](https://www.programiz.com/python-programming/multiple-inheritance)
4. [Making Python classes more modular using mixins](https://www.residentmar.io/2019/07/07/python-mixins.html)
5. [SQLAlchemy Column & Data Types](https://docs.sqlalchemy.org/en/14/core/type_basics.html)
6. [How to Connect to SQLite from Command Line](https://www.a2hosting.com/kb/developer-corner/sqlite/connect-to-sqlite-from-the-command-line)
----------------------------------------------------------

## January 11, 2021 (Day 4 #100DaysOfCode)

**Today's Progress**:
- Learned how to view previews of my markdown (.md) files in VSCode. Right-click on code editor tab for file and select 'Open Preview'.
- Completed Chapter 4: Databases in the Flask Mega-Tutorial
- Integrated Flask-SQLAlchemy with my web app! Added User and Student database models in models.py  
- Learned how to create a shell context so you can open up a Python interpreter with the relevant elements from your project, pre-imported. Added `make_shell_context()` function to journal.py

**Thoughts**: 
- When saving datetime information in your database, it is recommended to work with UTC dates and times. This will ensure uniform timestamps regardless of where the users are located. The timestamps will then be converted to the user's local time when they are displayed. - (miguelgrinberg.com)
- Working with Flask-Migrate (Alembic):
    -  `flask db init`: initializes the migration repository 
    - `flask db migrate -m "<optional message>"`: generates the migration script
    - `flask db upgrade`: applies the changes to the database
    - `flask db downgrade`: undoes the last migration 
- Changes to the database are made within the context of a session, which is accessed through `db.session`. Changes that have been added (`db.session.add()`) are not actually committed to the database until `db.session.commit()` is called. `db.session.rollback()` aborts the session and removes any changes stored in it. 
- Database queries:
    - All models have a query attribute which allows you to run database queries
    - Query to return all elements of a specific class called User: User.query.all())
    - Query to return a user whose id = 1: User.query.get(1)
    ```python
    # Query to get all posts written by a user
    u = User.query.get(1)
    posts = u.posts.all()

    # Query to print post author and body for all posts
    posts = Post.query.all()
    for p in posts:
        print(p.id, p.author.username, p.body)

    # Query to get all users in reverse alphabetical order
    User.query.order_by(User.username.desc()).all()
    ```
- SQLAlchemy provides the use of `db.relationship`, which gives you a high-level view of the relationships between tables without having to deal explicitly with foreign keys
- The `flask shell` command helps to set up a Python interpreter with the imports relevant to your application. You can create a "shell context" that names which symbols you want to pre-import. You can write this "shell context" function in the main file used to run the app with an `app.shell_context_processor` decorator. When ready to use, run `flask shell` in terminal BEFORE opening up a Python interpreter. 

**Resources**
1. [Case Styles](https://medium.com/better-programming/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841)
2. [Flask-SQLAlchemy documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
3. [Declaring models in Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)
4. [Chapter 4: Databases - Flask Mega-Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
----------------------------------------------------------
## January 10, 2021 (Day 3 #100DaysOfCode)

**Today's Progress**:
- Created mock objects and control statements to display activity information in table on log.html page until I can start pulling in info from the database. 
- Added new view function for displaying attendance history ('/attendance')
- Worked through Flask Mega-Tutorial (Chapter 2: Templates, Chapter 3: Web Forms)
- Made a dynamic WTForms SelectField with mock `students` and `subjects` object
- Added field validation with error displays and flash messaging 

**Thoughts**: 
- Creating mock objects can be useful when you're working on one part of the application but the other aspects of the system haven't been created yet. 
- Jinja2 is a template engine that comes with the Flask framework. The `render_template()` function takes a template filename and template arguments and then converts the placeholders, indicated by `{{ ... }}` blocks, to actual values. Control statements are given inside `{% ... %}` blocks.
- `GET` requests typically return information to the client(e.g. web browser). `POST` requests typically used when browser submits form data to the server. 
- Using the "with" construct in Flask template: From Miguel Grinberg -  " "with" in this situation is that this is more or less similar to using "with" in regular Python code. Basically what you get is that the variable defined as part of the with declaration can be used anywhere between the "with" and the "endwidth"."
- The `url_for()` function generates URLS, where the argument to url_for() is the endpoint name, which is the name of the view function. 
- You can use `os.urandom(24).hex()` to generate a random key, after importing the `os` library in Python 

**Resources**
1. [Form Validation with WTForms](https://flask.palletsprojects.com/en/1.1.x/patterns/wtforms/?highlight=form)
2. [Using CSRF with FlaskForm](https://flask-wtf.readthedocs.io/en/stable/csrf.html)
3. [The 'with' construct in Flask templates](https://www.reddit.com/r/flask/comments/8rc3oi/what_does_with_construct_do/)
4. [Flask Mega-Tutorial Chapter 2: Templates](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
5. [Flask Mega-Tutorial Chapter 3: Web Forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
6. [Dynamic WTForms SelectField](https://stackoverflow.com/questions/12850605/how-do-i-generate-dynamic-fields-in-wtforms)
7. [Message Flashing in Flask](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/)
----------------------------------------------------------
## January 9, 2021 (Day 2 #100DaysOfCode)

**Today's Progress**:
- Added modal windows for editing an activity and viewing activity details on log.html page 
- Installed Flask-SQLAlchemy via terminal: `pip install flask-sqlalchemy`
- Installed Flask-Migrate via terminal to use with database migration framework, Alembic: `pip install flask-migrate`
- Added Config class to configuration file (config.py) and added if else logic to app.py for choosing which configuration attributes to apply to the Config class. 
- Added SQLALCHEMY configuration variables to config.py file 
- Changed file structure of app. Made the application a package instead of a module. Added routes.py and __init__.py to app/ folder.
- Created a migration repository using Flask-Migrate. Got STUCK because Flask-Migrate was not detecting the table that I created in models.py. Going to walk through the Flask Mega-Tutorial to see if I detect what the problem is. 
    - Completed Chapter 1: Hello World!

**Thoughts**: 
- The 'OS' module in Python provides functions for interacting with the operating system. OS is included in Python's standard utility modules (no need to install externally). `os.path` is a sub-module of OS module and is commonly used for path name manipulation. `os.path.dirname(path)` is a method that gets the directory name from a specified path. `os.path.abspath(path)` is a method that returns the pathname to the path that is passed in as a parameter to this function. 
- It's important to consider the principle of 'separation of concerns' when deciding the location for your app's configuration variables. Instead of putting them in the same file where you create your application, you can create a configuration class in a separate Python module. For my project, I'm creating a configuration class in config.py in the top-level directory. 
- Routes are the different URLS that the app serves to the user. Handlers for the app routes are called view functions. These view functions are mapped to one or more route URLs and serves a specific URL depending on the logic defined in the function. The @app.route decorator creates a relationship between the URL given as an argument and the function (miguelgrinberg.com)
- If your application is a module (e.g. app.py), then the templates folder should be next to that module. If your application is a package (e.g. app/), the templates folder is inside your package
- Flask-Migrate: The `flask db` sub-command is used to manage various database migration scenarios. `flask db init` creates the migration repository. `flask db migrate` creates a migration automatically. 
- Make sure to type `python3` in the terminal BEFORE I try to run Python code in the terminal! Forgetting to do so results in a `...can't read /var/mail/...` error 

**Resources**
1. [Using the aria-labelledby attribute](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques/Using_the_aria-labelledby_attribute)
2. [The Flask Mega-Tutorial - Databases](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
3. [Python classes](https://docs.python.org/3/tutorial/classes.html)
4. [os.path.dirname() method](https://www.geeksforgeeks.org/python-os-path-dirname-method/)
5. [os.path.abspath() method](https://www.geeksforgeeks.org/python-os-path-abspath-method-with-example/)
6. [App Configuration & Web Forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
7. [Flask configuration files - the best explanation I've come across so far for setting up config.py](https://pythonise.com/series/learning-flask/flask-configuration-files)
8. [How to set up folder structure for rendering templates](https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates)
9. [How to add Flask-Migrate to project](https://blog.miguelgrinberg.com/post/how-to-add-flask-migrate-to-an-existing-project)


----------------------------------------------------------
## January 8, 2021 (Day 1 #100DaysOfCode)

**Today's Progress**:
- Started the #100DaysOfCode challenge
- Learned how to create a GIF from a screen capture on my laptop using licecap software
- Started building '/log' route and linked to log.html
- Used flexbox to change layout of form fields on 'Add An Activity' page
- Added a 'notes' field to the form on 'Add An Activity' page 
- Added modal window for adding a new activity from the log.html page 

**Thoughts**:
- This [tutorial](https://www.youtube.com/watch?v=XTpLbBJTOM4) was extremely helpful in learning how to use modals with Bootstrap.


**Resources**
1. [GIF Creation Tools](https://webflow.com/blog/5-tools-to-help-you-give-the-gift-of-gifs)
2. [The table HTML element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table) 
3. [Tables - Bootstrap](https://getbootstrap.com/docs/4.0/content/tables/)
4. [Modal - Bootstrap](https://getbootstrap.com/docs/4.0/components/modal/)

----------------------------------------------------------
## January 6, 2021

**Today's Progress**:
- Added rest of fields to 'Add an Activity' form on add.html file. Added Bootstrap CSS styling so form is responsive.

**Thoughts**: 
- To run app in development mode, run this in terminal: `export FLASK_ENV=development`
- You can inject HTML in the Jinja-templated form (e.g. to add a class to a field: `{{ form.title(size=100, class_='form-control') }}`)

**Resources**
1. [DatePicker widget with WTForms](https://stackoverflow.com/questions/26057710/datepickerwidget-with-flask-flask-admin-and-wtforms)
2. [Use calendars with DatePicker in Flask WTForms](https://www.youtube.com/watch?v=jAdFZa6KZNE)
3. [WTForms Fields](https://wtforms.readthedocs.io/en/2.3.x/fields/?highlight=html%20attributes)
4. [Passing HTML attributes to Flask form]((https://john.soban.ski/pass-bootstrap-html-attributes-to-flask-wtforms.html))

----------------------------------------------------------
## January 5, 2021

**Today's Progress**:
- Installed Flask-WTF to use with creating forms whose input can be validated: `$ pip install flask flask-WTF`
- Installed python-dotenv in order to use .env file to store SECRET_KEY variable: `pip install python-dotenv`
- Started creating form on 'add.html' using FlaskForm 
- Added config files with SECRET_KEY info to enable CSRF protection 

**Thoughts**: 
- WTForms is a Python library used for handling forms. It can be used via the Flask plugin, Flask-WTF
- Routes give instructions on what should be served to the user based on the URL they visit within the app. My routes for this app are defined in my app.py file
- Form classes are Python models that are used to validate the data submitted in forms.
- Jinja templates are used to render the HTML forms that are displayed to the user
- It's common to use CapitazliedWords when naming Python classes (e.g. AddActivity)
- You have to set up a secret key in order to use features like flask-login and CSRF protection. I encountered this error (RuntimeError: A secret key is required to use CSRF.)  when trying to view my form I created using WTForms. 
- It's best to use a separate configuration file for storing the configuration variables that will be applied to the Flask app. 
- Environment variables are stored in the system memory of the device running the app and can be temporarily created via the terminal: (e.g. `$ export SECRET_KEY='o9uaglkiDjro')`. The variable exists as long as you keep the terminal open. To check the variable value, `echo $SECRET_KEY`

**Resources**
1. [Handling Forms in Flask with Flask-WTF](https://hackersandslackers.com/flask-wtforms-forms/)
2. [WTForms Documentation](https://wtforms.readthedocs.io/en/2.3.x/#)
3. [FieldList with SelectField](https://stackoverflow.com/questions/24296834/wtform-fieldlist-with-selectfield-how-do-i-render)
4. [Secret key required to use CSRF](https://stackoverflow.com/questions/47687307/how-do-you-solve-the-error-keyerror-a-secret-key-is-required-to-use-csrf-whe)
5. [Generating SECRET KEY for Flask](https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask)
6. [Setting up .env file for use with Flask project](https://itnext.io/start-using-env-for-your-flask-project-and-stop-using-environment-variables-for-development-247dc12468be)
7. [Python with Flask Fundamentals](https://www.rithmschool.com/courses/flask-fundamentals/forms-with-wtforms)
8.[Flask Configuration](https://explore-flask.readthedocs.io/en/latest/configuration.html) - helped me set up my 2 config files to provide my SECRET_KEY: one in the root, other in instance folder

----------------------------------------------------------
## January 4, 2020
**Today's Progress**:
- Created private repo for project (homeschool-journal)
- Cloned into repo to be able to work on project locally 
- Activate virtual environment: In 'Environments' folder, run `source my_env/bin/activate` in the Terminal. To deactivate the virtual environment, run `deactivate` in the Terminal. 
- Created file main.py in order to run Flask (to run script in Terminal: python3 main.py)
- Created templates folder to store the html files for this project
- Incorporated Bootstrap for navbar structure and styling 
- Added a static folder to house style.css file 
- Started building input form on add.html page for adding an activity 

**Thoughts**: 
- When using `url_for` to link to another template HTML file, it must match the name of the view that renders the specific template file. Essentially, `url_for` links to views. 

**Resources**
1. [SSH Keys for GitHub](https://jdblischak.github.io/2014-09-18-chicago/novice/git/05-sshkeys.html)
2. [Cloning private GitHub repo](https://github.community/t/clone-private-repo/1371/2)
3. [freeCodeCamp - Build a web applicat using Flask](https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/)
4. [Building a URL to a specific function using url_for()](https://flask.palletsprojects.com/en/0.12.x/quickstart/#url-building)
5. [Flask series](https://dev.to/brunooliveira/flask-series-part-i-4do8)
6. [HTML input type="checkbox"](https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox)
7. [HTML input type="date"](https://www.w3schools.com/tags/att_input_type_date.asp)

----------------------------------------------------------
