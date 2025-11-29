from pyscript import display, document

# CLUBS
varsity = {
    'name': 'Varsity Team',
    'desc': 'Basketball and volleyball athletes representing HHS.',
    'time': 'Mondays, 3:00 PM',
    'location': 'School Gym',
    'moderator': 'Coach Hopper',
    'members': 25
}

cocc = {
    'name': 'COCC',
    'desc': 'Cadet Officer Candidate Course focused on discipline and leadership.',
    'time': 'Thursdays, 3:30 PM',
    'location': 'Field Area',
    'moderator': 'Mr. Harrington',
    'members': 40
}

dance = {
    'name': 'Dance Club',
    'desc': 'For Students who enjoy dancing, choreography, and performing!',
    'time': 'Mondays & Fridays, 4:00 PM',
    'location': 'Dance Studio',
    'moderator': 'Ms. Mayfield',
    'members': 30
}

def clear_box():
    document.getElementById("output").innerHTML = ""


# DISPLAY
def show(club):
    clear_box()
    display(f"Name: {club['name']}", target="output")
    display(f"Description: {club['desc']}", target="output")
    display(f"Meeting Time: {club['time']}", target="output")
    display(f"Location: {club['location']}", target="output")
    display(f"Moderator: {club['moderator']}", target="output")
    display(f"Members: {club['members']}", target="output")


# BUTTON FUNCTIONS
def show_varsity(e):
    show(varsity)

def show_cocc(e):
    show(cocc)

def show_dance(e):
    show(dance)
