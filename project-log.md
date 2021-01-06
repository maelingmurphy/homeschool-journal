# PROJECT LOG

## DATE, 2021

**Today's Progress**:

**Thoughts**: 

**Resources**

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
