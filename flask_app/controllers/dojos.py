from flask_app import app, render_template, request, redirect, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def home_page():
    return redirect('/dojos')

@app.route('/dojos')
def display_dojo():
    all_dojos = Dojo.display_dojo()
    return render_template("home.html", dojos = all_dojos) # rendering are page where it shows the dojo 

@app.route('/dojo/form', methods=['POST'])
def add_dojo():
    print(request.form)
    Dojo.create_dojo(request.form) # It show you everything submitted in the form and displays it on screen
    return redirect('/dojos')


@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template("show.html", dojo=Dojo.get_one_with_ninja(data))

