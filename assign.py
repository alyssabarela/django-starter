import requests
from web.models import Officer, Incident
import math

def get_officers():
    headers = {"Accept": "application/json"}
    officers = requests.get(url='http://localhost:8000/officers/', headers=headers)
    return officers


officers = get_officers()
print(officers)


def assign(x, y, type):
    incidents = Incident.objects.filter(type=type, location_x=x, location_y=y, active=True)

    if incidents:
        incident = incidents[0]
        return incident.assigned_officer

    incident = Incident.objects.create(type=type, location_x=x, location_y=y, active=True)

    officers = Officer.objects.filter(available=True)
    smallest = -1
    responder = None
    for officer in officers:
        dist = get_distance(x, y, officer.location_x, officer.location_y)
        if dist < smallest:
            smallest = dist
            responder = officer
    responder.available = False
    responder.save()
    incident.assigned_officer = responder
    incident.save()
    if not responder:
        raise Exception("oh no!")
    return responder


def get_distance(x, y, officer_x, officer_y):
    x_distance = (x-officer_x)*(x-officer_x)
    y_distance = (y - officer_y)*(y - officer_y)
    return math.sqrt(x_distance+y_distance)


def clear_status(officer_id):
    officer = Officer.objects.get(id=officer_id)
    officer.available = True
    officer.save()


def update_location(officer_id, x, y):
    officer = Officer.objects.get(id=officer_id)
    officer.location_x = x
    officer.location_y = y
    officer.save()

# if incident type is in the same location with the same incident type, no need to dispatch