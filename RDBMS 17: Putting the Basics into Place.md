![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Krishan,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

This video assumes that you are using our recommended development environment, and have
already created your new repository.

The very first thing that we need to do is install two Python packages.
`pip3 install Flask-SQLAlchemy psycopg2`

Previously, we've learned how t  o use Flask to build the Thorin project, and SQLAlchemy to work with Postgres databases.

By installing Flask-SQLAlchemy, this actually comes with both Flask and the SQLAlchemy requirements together in one download.
In order to work with the Postgres database, as you may recall, we need to have psycopg2 installed as well.

------

Next, we will be storing some sensitive data, and we need to hide them using environment
variables hidden within a new file called `'env.py'`.

Make sure to have a `.gitignore` file that contains any files and folders which should be ignored by GitHub, such as an env.py file.

`env.py = Since these variables should be available system-wide on our application, we need to import the operating system itself.`
To set up default environment variables, it takes two arguments, the key and the value,
both within quotes, and for this project we need six different variables, so copy that line six times.

Those six variables are: IP, PORT, SECRET_KEY, DEBUG, DEVELOPMENT, and DB_URL.
`IP` is 0.0.0.0
`PORT` is 5000 for Flask applications.
`SECRET_KEY` can be any random string you'd like.
*************************
`DEBUG` will be set to True for now, but `make sure you set DEBUG to False prior to your actual project submissions.`
**************************
`DEVELOPMENT` will also be set to True for now, and this is what we'll use to distinguish
between our local environment, and our deployed application later.
`DB_URL` will point to our database, which we don't currently have, but when working locally,
we'll use the local Postgres environment.
The `three slashes represent the fact that our database is local within our workspace`,
and we'll be creating a new database called `'taskmanager'`.

------

Next, `the entire application will need to be its own Python package`, so to make this
a package, we need a new folder which we will simply call taskmanager/.

Inside of taskmanager, a new file called `__init__.py` `(use double underscore)`
This will make sure to `initialize our taskmanager application as a package`, allowing us to use
our own imports, as well as any standard imports.

We will start by importing the following:
import os from flask import Flask
from flask_sqlalchemy import SQLAlchemy

In order to actually use any of our hidden environment variables, we need to import the `'env'` package.
However, since we are not pushing the env.py file to GitHub, this file will not be visible
once deployed to Heroku, and will throw an error.
`This is why we need to only import 'env'` if the OS can find an existing file path for the env.py file itself.

Now we can create an instance of the imported Flask() class, and that will be stored in
a variable called 'app', which takes the default Flask __name__ module.

Then, we need to `specify two app configuration variables`, and these will both come from our environment variables.
app.config SECRET_KEY and app.config SQLALCHEMY_DATABASE_URI, both wrapped in square brackets and quotes.

Each of these will be set to get their `respective environment variable`, which is `SECRET_KEY`,
and the short and sweet `DB_URL` for the database location which we'll set up later.

Then, we need to `create an instance of the imported SQLAlchemy() class`, which will be
assigned to a variable of 'db', and set to the instance of our Flask 'app'.

Finally, `from our taskmanager package`, we will be `importing a file called 'routes'` which we'll create momentarily.

These linting warnings are technically not accurate, so to stop the warnings, we can
add a comment at the end of each line, `# noqa for 'No Quality Assurance'`.

------

`routes.py - To render html templates`

We're going to start using some Flask functionality, `so we can import render_template from flask` to start with.

------

`run.py`

Now it's time to `create the main Python file that will actually run the entire application`.
This will be `at the root level` of our workspace,` not part of the taskmanager package` itself.
Since it will run the whole application, let's just `call it run.py` in that case.

We need to `import os` once again, in order to utilize environment variables within this file.

We also `need to import the 'app' variable` that we've created within our taskmanager
package, defined in the init file.

The last step to run our application is to tell our app how and where to run the application.

This is the same process we've seen before, `checking that the 'name' class is equal to the default 'main' string, wrapped in double underscores.`
`If it's a match, then we need to have our app running`, which will take three arguments:
'host', 'port', and 'debug'.
Each of these, as you may recall, are `stored in the environment variables (env.py)`, so we need to
`use os.environ.get()`.

The `host` is the `IP`, 
the `port` is obviously `PORT`, but that `needs to be converted into an integer`, 
and then `debug` is of course `DEBUG`.

------

Finally, we need to render some sort of front-end template to verify that the application is running successfully.
Within our taskmanager package, let's create a new directory called 'templates', which
is where Flask looks for any HTML templates to be rendered.
Then, within this templates directory, we will create a new file called base.html, which
is what will be rendered from our routes.py file.