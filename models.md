
`Models > Tables`
create a new column variable of 'id'
These will be columns on our tables, and each will be Integers, with `primary_key set to True`, which will auto-increment each new record added to the database.

------

`import db - SQLAlchemy`
If you recall from the last few lessons, we had to specifically import each column type at the top of the file.
However, with Flask-SQLAlchemy, the 'db' variable contains each of those already, and we can
simply use dot-notation to specify the data-type for our columns.

------

`__repr__(self)`
For each model, we also need to create a function called __repr__ that takes itself as the argument,
similar to the 'this' keyword in JavaScript.
This is a standard Python function meaning 'represent’, which means to represent the class objects as a string.

------

`Tabel Column formatting`

`unique=True`
We also want to make sure each new Category being added to the database is unique, so we'll set that to True.


Then, we also need to make sure it's not empty or blank, so by setting `nullable=False` this
enforces that it's a required field.

`Delete` 
Later, we decide to delete 1 of those categories, so any of the 5 tasks that have this specific
category linked as a foreign key, will throw an error, since this ID is no longer available.
This is where the `ondelete="CASCADE"` comes into play, and essentially means that once
a category is deleted, it will perform a cascading effect and also delete any task linked to it.

------

`Relational connection`
Then, we need to use something called 'backref' which establishes a bidirectional relationship
in this one-to-many connection, meaning it sort of reverses and becomes many-to-one.
It needs to back-reference itself, but in quotes and lowercase, so `backref="category"`.

------

`lazy=True`

The last parameter here is `lazy=True`, which means that when we query the database for
categories, it can simultaneously identify any task linked to the categories.

------

`Return some sort of string for the Task class.`

The final thing that we need to do with our class-based models, is to return some sort of string for the Task class.
We could simply return self.task_name, but instead, let's utilize some of Python's formatting to include different columns.
We'll use placeholders of {0}, {1}, and {2}, and then the Python .format() method to specify
that these equate to self.id, self.task_name, and self.is_urgent.

------
`will need to also create this 'taskmanager' database.`

Let's navigate to the Terminal, and login to the Postgres CLI by `typing 'psql' and hitting enter.`
To create the database, we can simply type:
`CREATE DATABASE taskmanager;`

------

`Switch over to that connection by typing:`
\c taskmanager;

------

`Exit PostgresCLI`

Exit CLI by typing \q.

------

`Use Python to generate and migrate our models into this new database.`
This will take the models that we've created for Category and Task, and build the database
schema using the details we've provided.

It's important to note, that if you were to modify your models later, then you'll need
to migrate these changes each time the file is updated with new context.

For example, if you added a new column on the Task table for 'task_owner', once the
file is saved, you'll need to make your migrations once again, so the database knows about these changes.


------
`Access Python Intepreter`

Access the Python interpreter by typing "python3" and enter.

------

`Import our 'db' variable found within the taskmanager package.`

we need to import our 'db' variable found within the taskmanager package, so type:
`from taskmanager import db`

Now, using db, we need to perform the `db.create_all()` method.

That's it, pretty simple enough, our `Postgres database should be populated with these two tables and their respective columns and relationships.`

------
`Exit Python Interpreter`
Exit the Python interpreter by typing exit().

Congratulations, you now have your database models and schema migrated into the database.

------

`To confirm that these tables exist within your database:`

psql -d taskmanager
\dt

------


`OTHER`

`backref="category" >>>> ondelete="CASCADE"`

If you recall, we created a relationship between our Category and Task models, using a 'backref' and the 'ondelete' cascade.
Now that we have full CRUD functionality for both of these tables, let's see how that works together.
Once again for demonstration purposes, I'm going to create a new Category called "Test",
and two new tasks that use this new category.
As you can see, for the category, they both use the new "Test" category.
The reason we add the backref and delete cascade, has to do with the fact that if the "Test"
category gets deleted, then we will show an error on these two Tasks for having invalid categories.
However, once the backref and delete cascade are added, if we decide to delete the "Test"
category, then it will perform a cascade effect and delete any task utilizing this category.

------