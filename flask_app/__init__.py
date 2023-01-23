from flask import render_template, request, redirect, session
from flask import Flask
app = Flask(__name__)
app.secret_key = "Anything you want"