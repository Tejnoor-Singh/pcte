import datetime
from bson import *
from flask import *
from mongodb import MongoDBHelper
web_app = Flask("dinee app")
app = Flask(__name__, template_folder="templates")


@web_app.route("/")
def index():
    return render_template('index.html')


@web_app.route("/about")
def about_us():
    return render_template('about.html')


@web_app.route("/contact")
def contact_us():
    return render_template('contact.html')


@web_app.route("/home")
def home():
    return render_template('index.html')


@web_app.route("/dashboard")
def dashboard():
    return render_template('goto.html')


@web_app.route("/auth-manager")
def auth_manager():
    return render_template('auth.html')


@web_app.route("/auth-client")
def auth_client():
    return render_template('client.html')


@web_app.route("/auth-labour")
def auth_labour():
    return render_template('labour.html')


@web_app.route("/submission-date", methods=['POST'])
def submission_date():
    submission_date = {
        # 'identity': request.form['identity'],
        'project-name': request.form['project-name'],
        'updation': request.form['updation'],
        'submit-by': request.form['submit'],
        'createdOn': datetime.datetime.today()
    }

    print(submission_date)
    db = MongoDBHelper(collection="project-submission")
    result = db.insert(submission_date)
    customer_id = result.inserted_id
    # session['phone'] = manager_data['phone']
    return render_template('auth.html')


@web_app.route("/register-manager", methods=['POST'])
def register_manager():
    manager_data = {
        # 'identity': request.form['identity'],
        'username': request.form['username'],
        'email': request.form['email'],
        'phone-number': request.form['phone'],
        # 'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest(),
        'password': request.form['password'],
        'createdOn': datetime.datetime.today()
    }

    print(manager_data)
    db = MongoDBHelper(collection="manager-signup")
    result = db.insert(manager_data)
    customer_id = result.inserted_id
    # session['phone'] = manager_data['phone']
    return render_template('auth.html')


@web_app.route("/login-manager", methods=['POST'])
def login_manager():
    manager_login_data = {
        'username': request.form['username'],
        'email': request.form['email'],
        'password': request.form['password'],

    }
    print(manager_login_data)
    db = MongoDBHelper(collection="manager-signup")
    documents = list(db.fetch(manager_login_data))
    print(documents, type(documents))
    if len(documents) == 1:

        session['email'] = documents[0]['email']
        session['password'] = documents[0]['password']
        print(vars(session))
        session['email'] = manager_login_data['email']
        session['username'] = manager_login_data['username']

        return render_template('managerdashboard.html')

    else:
        return render_template('h.html')


@web_app.route("/register-client", methods=['POST'])
def register_client():
    client_data = {
        # 'identity': request.form['identity'],
        'username': request.form['username'],
        'email': request.form['email'],
        'phone-number': request.form['phone'],
        # 'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest(),
        'password': request.form['password'],
        'createdOn': datetime.datetime.today()
    }

    print(client_data)
    db = MongoDBHelper(collection="client-signup")
    result = db.insert(client_data)
    customer_id = result.inserted_id
    # session['phone'] = manager_data['phone']
    return render_template('auth.html')


@web_app.route("/login-client", methods=['POST'])
def login_client():
    client_login_data = {
        'username': request.form['username'],
        'email': request.form['email'],
        'password': request.form['password'],

    }
    print(client_login_data)
    db = MongoDBHelper(collection="manager-signup")
    documents = list(db.fetch(client_login_data))
    print(documents, type(documents))
    if len(documents) == 1:
        session['username'] = documents[0]['username']
        session['email'] = documents[0]['email']
        session['password'] = documents[0]['password']
        print(vars(session))
        session['email'] = client_login_data['email']

        return render_template('client_login_data.html')
    else:
        return render_template('h.html')


@web_app.route("/register-labour", methods=['POST'])
def register_labour():
    labour_data = {
        # 'identity': request.form['identity'],
        'username': request.form['username'],
        'email': request.form['email'],
        'phone-number': request.form['phone'],
        # 'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest(),
        'password': request.form['password'],
        'createdOn': datetime.datetime.today()
    }

    print(labour_data)
    db = MongoDBHelper(collection="labour-signup")
    result = db.insert(labour_data)
    customer_id = result.inserted_id
    # session['phone'] = manager_data['phone']
    return render_template('auth.html')


@web_app.route("/login-labour", methods=['POST'])
def login_labour():
    client_login_data = {
        'username': request.form['username'],
        'email': request.form['email'],
        'password': request.form['password'],

    }
    print(client_login_data)
    db = MongoDBHelper(collection="manager-signup")
    documents = list(db.fetch(client_login_data))
    print(documents, type(documents))
    if len(documents) == 1:
        session['username'] = documents[0]['username']
        session['email'] = documents[0]['email']
        session['password'] = documents[0]['password']
        print(vars(session))
        session['email'] = client_login_data['email']

        return render_template('client_login_data.html')
    else:
        return render_template('h.html')


@web_app.route("/add-labour", methods=['POST'])
def add_labour():
    labour_data = {
        # 'identity': request.form['identity'],
        'name': request.form['name'],
        'skills': request.form['skills'],
        'phone-number': request.form['phone'],
        # 'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest(),
        'status': request.form['status'],
        'createdOn': datetime.datetime.today()
    }

    print(labour_data)
    db = MongoDBHelper(collection="labour")
    result = db.insert(labour_data)
    customer_id = result.inserted_id
    # session['phone'] = manager_data['phone']
    return render_template('managerdashboard.html')


db_helper = MongoDBHelper(collection="labour")  # Assuming your collection name is "labour"

from flask import Flask, render_template, request, session
from mongodb import MongoDBHelper

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management


# @app.route("/fetch-all-labourers")
# def fetch_all_labourer():
#     db = MongoDBHelper(collection="labour")
#
#     # Fetch all documents from 'labour' collection
#     documents = db.fetch()
#
#     # Print fetched documents for debugging
#     print("Fetched documents:", documents)
#     return render_template('managerdashboard.html', documents=documents)


# @web_app.route("/all-labourers", methods=['POST'])
# def fetch_all_labourers():
#     db_helper = MongoDBHelper(collection="labour")  # Initialize MongoDBHelper
#     documents = db_helper.fetch()  # Fetch documents from the "labour" collection
#     return render_template('managerdashboard.html', documents=documents)


@web_app.route("/fetch-submission", methods=['POST'])
def fetch_submission_date():
    db = MongoDBHelper(collection="project-submission")
    documents = list(db.fetch())
    print(documents, type(documents))
    # return "Customers Fetched for the Vet {}".format(session['vet_name'])
    return render_template('managerdashboard.html', documents=documents)

@web_app.route("/all-labourers", methods=['POST'])
def fetch_all_labourers():
    print("helloworld")
    db = MongoDBHelper(collection="labour")
    documents = list(db.fetch())
    print(documents, type(documents))
    # return "Customers Fetched for the Vet {}".format(session['vet_name'])
    return render_template('managerdashboard.html', documents=documents)


@web_app.route("/add_new_project", methods=['POST'])
def add_new_project():
    add_project_details = {

        'project-name': request.form['project-name'],
        'project-description': request.form['description'],
        'project-budget': request.form['budget'],
        'createdOn': datetime.datetime.today()
    }

    print(add_project_details)
    db = MongoDBHelper(collection="client-project")
    result = db.insert(add_project_details)
    customer_id = result.inserted_id
    # session['phone'] = manager_data['phone']
    return render_template('client-dashboard.html')


@web_app.route("/contact-us", methods=['POST'])
def contact__us():
    query_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'message': request.form['message']
    }
    print(query_data)
    db = MongoDBHelper(collection="contact-us")
    result = db.insert(query_data)
    return render_template('index.html')


def main():
    # In order to use session object in flask, we need to set some key as secret_key is aop
    web_app.secret_key = 'deni-key-1'
    web_app.run(port=5055)


if __name__ == "__main__":
    main()
