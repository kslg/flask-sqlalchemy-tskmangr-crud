from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)


# READ from the DB
@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


# CREATE - Two methods "GET" and "POST", since we will be submitting a form to the database.
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


# UPDATE the DB
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


# DELETE category from the DB
@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


# DELETE task from the DB
@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))

    
# Whenever you use the url_for() method on your links, it's important to note that these are
# calling the actual Python functions (def home, etc), not the app.route, eventhough these are often the same name.
# Check the imports at the top of the page are correct.

# CREATE - Two methods "GET" and "POST", since we will be submitting a form to the database.
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", categories=categories)

# UPDATE the DB
@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.category_id = request.form.get("category_id")
        db.session.commit()
    return render_template("edit_task.html", task=task, categories=categories)