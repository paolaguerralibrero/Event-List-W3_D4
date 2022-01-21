from flask import render_template, request
from app import app
from models.event_info import events, add_new_event
from models.event import Event





@app.route('/events')
def index():
    return render_template('index.html', event_list=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['name']
    event_number_of_guests = request.form['number_of_guests']
    event_location = request.form['location']
    event_description = request.form['description']
    new_event = Event(event_date, event_name, event_number_of_guests, event_location, event_description )
    add_new_event(new_event)
    return render_template('index.html', event_list=events)