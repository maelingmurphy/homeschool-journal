# PROJECT LOG

## DATE, 2021

**Today's Progress**:

**Thoughts**: 

**Resources**

----------------------------------------------------------

## January 9, 2021

**Today's Progress**:
- Added modal windows for editing an activity and viewing activity details on log.html page 
- Installed Flask-SQLAlchemy via terminal: `pip install flask-sqlalchemy`
- Installed Flask-Migrate via terminal to use with database migration framework, Alembic: `pip install flask-migrate`
- Added Config class to configuration file (config.py) and added if else logic to app.py for choosing which configuration attributes to apply to the Config class. 
- Added SQLALCHEMY configuration variables to config.py file 

**Thoughts**: 
- The 'OS' module in Python provides functions for interacting with the operating system. OS is included in Python's standard utility modules (no need to install externally). `os.path` is a sub-module of OS module and is commonly used for path name manipulation. `os.path.dirname(path)` is a method that gets the directory name from a specified path. `os.path.abspath(path)` is a method that returns the pathname to the path that is passed in as a parameter to this function. 
- It's important to consider the principle of 'separation of concerns' when deciding the location for your app's configuration variables. Instead of putting them in the same file where you create your application, you can create a configuration class in a separate Python module. For my project, I'm creating a configuration class in config.py in the top-level directory. 
- Routes are the different URLS that the app serves to the user. Handlers for the app routes are called view functions. These view functions are mapped to one or more route URLs and serves a specific URL depending on the logic defined in the function. The @app.route decorator creates a relationship between the URL given as an argument and the function (miguelgrinberg.com)
- If your application is a module (e.g. app.py), then the templates folder should be next to that module. If your application is a package (e.g. app/), the templates folder is inside your package

**Resources**
1. [Using the aria-labelledby attribute](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques/Using_the_aria-labelledby_attribute)
2. [The Flask Mega-Tutorial - Databases](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
3. [Python classes](https://docs.python.org/3/tutorial/classes.html)
4. [os.path.dirname() method](https://www.geeksforgeeks.org/python-os-path-dirname-method/)
5. [os.path.abspath() method](https://www.geeksforgeeks.org/python-os-path-abspath-method-with-example/)
6. [App Configuration & Web Forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
7. [Flask configuration files - the best explanation I've come across so far for setting up config.py](https://pythonise.com/series/learning-flask/flask-configuration-files)
8. [How to set up folder structure for rendering templates](https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates)
----------------------------------------------------------
## January 8, 2021

**Today's Progress**:
- Started the #100DaysOfCode challenge
- Learned how to create a GIF from a screen capture on my laptop using licecap software
- Started building '/log' route and linked to log.html
- Used flexbox to change layout of form fields on 'Add An Activity' page
- Added a 'notes' field to the form on 'Add An Activity' page 
- Added modal window for adding a new activity from the log.html page 



**Thoughts**: 
This [tutorial](https://www.youtube.com/watch?v=XTpLbBJTOM4) was extremely helpful in learning how to use modals with Bootstrap. 

**Resources**
1. [GIF Creation Tools](https://webflow.com/blog/5-tools-to-help-you-give-the-gift-of-gifs)
2. [The <table> HTML element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
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
6. [HTML <input type="checkbox"](https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox)
7. [HTML <input type="date">](https://www.w3schools.com/tags/att_input_type_date.asp)
