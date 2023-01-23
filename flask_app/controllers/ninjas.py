from flask_app import app, render_template, request, redirect, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo 

@app.route('/ninja')
def ninjas():
    return render_template("new_ninja.html", dojos=Dojo.display_dojo())

@app.route('/ninja/form', methods=['post'])
def create_ninja():
    print(request.form)
    Ninja.create_ninja_dojo(request.form)
    return redirect('/')


