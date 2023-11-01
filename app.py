from flask import Flask, render_template, url_for, request, redirect  
from os.path import exists
app= Flask(__name__)

app.config.from_pyfile(app.root_path + '/config_defaults.py')
if exists(app.root_path + '/config.py'):
    app.config.from_pyfile(app.root_path +'/config.py')

# import csv
import html
from os.path import exists 
import database
import re

# database.get_trips()
mem_path= app.root_path + '/members.csv'
trip_path= app.root_path + '/trips.csv'

# app.config.from_pyfile(app.root_path + '/config_defaults.py')
# if exists(app.root_path + '/config.py'):
# app.config.from_pyfile(app.root_path + '/config.py')


# def get_members():
#     with open(mem_path, 'r') as csvfile:
#         data= csv.DictReader(csvfile)
#         memberss= {row['name']:
#                 {'name':row['name'],
#                     'date_of_birth':row['date_of_birth'], 
#                     'email':row['email'],
#                     'address':row['address'],
#                     'phone':row['phone']} for row in data}
#         return memberss


# def get_trips():
#     with open(trip_path, 'r')as csvfile:
#         data= csv.DictReader(csvfile)
#         trips= {row['name']:
#             {'name':row['name'],
#              'start_date':row['start_date'],
#              'length':row['length'],
#              'cost':row['cost'],
#              'location':row['location'],
#              'level':row['level'],
#              'leader':row['leader'],
#              'description':row['description']
#         }for row in data}
#     return trips 

   

# def set_members(memberss):
#     cat=['name','date_of_birth','email','address','phone']

#     try:
#         with open(mem_path, mode='w', newline='') as csv_file:
#             writer = csv.DictWriter(csv_file, fieldnames=cat)
#             writer.writeheader()
#             for mem in memberss.values():
#                 writer.writerow(mem)
#     except Exception as err:
#         print(err)

def set_trips(tripss):
    cat=['name', 'location', 'length', 'level', 'start_date', 'cost', 'leader', 'description'] 
    try:
        with open(trip_path, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cat)
            writer.writeheader()
            for tri in tripss.values():
                writer.writerow(tri)
    except Exception as err:
        print(err)

#unused database** 
# database.remove_member_trip(trip_id, member_id)
# database.add_member_trip(trip_id, member_id)
# database.get_attendees(trip_id)


def check_name(name):
    error=""
    msg=[]
    if not name:
        msg.append("Name is missing")
    if len(name)> 30:
        msg.append("Name is too long")
    if len(msg)>0:
        error= "\n".join(msg)
    return error 

def check_email(email):
    error=""
    msg=[]
    if not email:
        msg.append("Email is missing")
    if len(email)> 30:
        msg.append("Email is too long")
    if len(msg)>0:
        error= "\n".join(msg)
    return error 

def check_address(address):
    error=""
    msg=[]
    if not address:
        msg.append("Address is missing")
    if len(address) >70:
        msg.append("Address is too long")
    if len(msg)>0:
        error= "\n".join(msg)
    return error 
    
def check_phone(phone):  #what's the difference between validate and 
    msg=[]
    val= r"\(\d{3}\) \d{3}-\d{4}"
    if not phone:
        msg.append("Phone number is missing")
    match= re.match(r"\(\d{3}\) \d{3}-\d{4}", phone)
    if not match:
        msg.append("Bad phone number")
    if len(msg)>0:
        error= "\n".join(msg)
    return error 
    



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/members')
def members():
    #display in order of age 
    memberss= database.get_members()
    # print(memberss)
    return render_template('members.html',  memberss= memberss)

def member_form():
    return render_template('member_form.html')

# @app.route('/members/add')

@app.route('/members/add', methods=['GET', 'POST'])
def add_members():
    # if POST request received (form submitted)
    if request.method == 'POST':
        # get dinosaurs.csv data
        members=database.get_members()
        # create new dict to hold new dino data from form
        # add form data to new dict
        name = html.escape(request.form['name'])
        address = html.escape(request.form['address'])
        # errorAd= check_address(address)
        # if errorAd:
        #     return render_template("member_form.html", errorAd=errorAd, address=address)
        email = html.escape(request.form['email'])
        # errorEM= check_email(email)
        # if errorEM:
        #     return render_template("member_form.html", errorEM=errorEM, email=email)
        phone = html.escape(request.form['phone'])
        # errorPH= check_phone(phone)
        # if errorPH:
        #     return render_template("member_form.html", errorAd=errorPH, address=email)
        date = html.escape(request.form['date'])
        # new_mem={"name":name, 'date_of_birth':date, 'email':email, 'address':address,  
        # 'phone':phone}
        # add new dict to csv data
        # print(members)
        # members[name]=new_mem
        database.add_member(name, date, email, address, phone)
        # write csv data back out to csv file
        # set_members(members) #to save new info from dict 
        # print(members)

        # since POST request, redirect to home after Submit
        return redirect(url_for('members'))
    
    # if GET request received (display form)
    else:
        return render_template('member_form.html')

@app.route('/members/edit', methods=['GET', 'POST']) #**fix 
def edit_members(mem_id):
    if request.method == 'POST':
            # get dinosaurs.csv data
            members=database.get_members()
            # create new dict to hold new dino data from form
            # add form data to new dict
            name = html.escape(request.form['name'])
            address = html.escape(request.form['address'])
            # error= check_address(address)
            email = html.escape(request.form['email'])
            phone = html.escape(request.form['phone'])
            date = html.escape(request.form['date'])
            database.edit_member(name, name, date, email, address, phone )

            # new_mem={"name":name, 'date_of_birth':date, 'email':email, 'address':address,  
            # 'phone':phone}
            # add new dict to csv data
            # print(members)
            # members[name]=new_mem

            # write csv data back out to csv file
            # set_members(members) #to save new info from dict 
            # print(members)

            # since POST request, redirect to home after Submit
            return redirect(url_for('members'))
    # database.edit_member(member_id, name, date_of_birth, email, address, phone )

@app.route('/members/delete', methods=['GET', 'POST']) #** fix 
def delete_members(mem_id):
    mems=database.get_members()
    database.delete_member(mem_id)

    return redirect(url_for('members'))

        
def trip_form():
    return render_template('trip_form.html')

@app.route('/')
@app.route('/trips')
@app.route('/trips/<trip_id>')

def trips(trip_id=None):
    # print(trip_list)
    if trip_id != None:
        # one_trip= tripss[trip_id]
        # print("trip_id is : ", trip_id)
        tripss= database.get_trip(trip_id)
        return render_template('trips-id.html', one_trip= tripss) # **fix 

        #trip names have to be unique because the trip_id--> Ex. trips/crazy... is dependednt on it 
        #get the name associated with the value 0 'name'
    else:
        tripss= database.get_trips()
        return render_template('trips.html', tripss= tripss)

    
@app.route('/trips/<trip_id>/edit', methods= ["GET","POST"] )
#edit trip withing add_trip function with if statement 
    #delete then re-add new 
    # update the values of a specific key 
    # trips[list]
def edit_trips(trip_id=None): # ** fix the edit 
    if request.method == 'POST':  
        #^ when user clicks "edit trip" buttongenerate "new form" but already filled in based on trip name 

        # print("TRIP ID 1ST CASE ", trip_id)

        select_trip= database.get_trip(trip_id) # trip_form(trip_id)

        # this_trip={'name':'hi'}
        #get trip name of the page it's on 
        # {{this_trip["name"]}}
        updName= html.escape(request.form.get('name'))
        # print("#"*20)
        # print("UPDATED NAME: ", updCost)
        updDate = html.escape(request.form.get('start_date'))
        updLength = html.escape(request.form.get('length'))
        updCost = html.escape(request.form.get('cost'))
        updLocation = html.escape(request.form.get('location'))
        updLevel = html.escape(request.form.get('level'))
        updLeader = html.escape(request.form.get('leader'))
        updDescription = html.escape(request.form.get('description'))

        database.update_trip(trip_id, updName,updLocation,updLength,updLevel,updDate,updCost,updLeader,updDescription)

        #overide existing dictionary using the id name 
        # dict_upd= {'name':updName, 'start_date':updDate, 'length':updLength, 'cost':updCost,  
        # 'location':updLocation, 'level':updLevel,'leader':updLeader, 'description': updDescription}
        
        # select_trip[trip_id]= dict_upd
        # # ** what function in database.py updates trip edits  for 

        # # set_trips() to update edits  
        # set_trips(select_trip)
        # to save edit

        #if submitted, return url for trips **
        # print(this_trip["length"])

        # return redirect(url_for('trips'))
        # print("TRIP ID", trip_id)
        return redirect(url_for('trips', trip_id= select_trip))

        #   
        #this_trip={'name':'hi'})
    else:
        select_trip= database.get_trip(trip_id)
        this_trip= select_trip
        return render_template('trip_form.html', this_trip= this_trip)



@app.route('/trips/<trip_id>/delete')# , methods= ["GET","POST"] )
def del_trips(trip_id):
    # if request.method == 'POST':

        trips=database.get_trips()

        # name = request.form['name']
        # location = request.form['location']
        # length = request.form['length']
        # level = request.form['level']
        # date = request.form['start_date']
        # cost = request.form['cost']
        # leader = request.form['leader']
        # description = request.form['description']

        # one_trip= trips[trip_id]
        #delet trip row from csv #delete item linked in dict 

        del trips[trip_id] #source: geeks for geeks 
        #OR trips[trip_id]= empt

        #set trips to save it
        set_trips(trips)
        return redirect(url_for('trips'))

    #     return render_template('delete_form.html', one_trip= one_trip)
    #     # url_for('trips')
    # else:
    #     return render_template('delete_form.html')
    
# def del_trips(trip_id):
#     trips=get_trips()
#     # id_trip= trips[trip_id]
#     del trips[trip_id] #source: geeks for geeks 
#     set_trips(trips)
#     return redirect(url_for('trips'))

 


@app.route('/trips/add', methods=['GET', 'POST'])
def add_trips():
    # if POST request received (form submitted)
    if request.method == 'POST':
        # get dinosaurs.csv data
        trips=database.get_trips()
        # create new dict to hold new dino data from form
        # add form data to new dict
        name = html.escape(request.form['name'])
        location = html.escape(request.form['location'])
        length = html.escape(request.form['length'])
        level = html.escape(request.form['level'])
        date = html.escape(request.form['start_date'])
        cost = html.escape(request.form['cost'])
        leader = html.escape(request.form['leader'])
        description = html.escape(request.form['description'])

        # new_trip={'name':name, 'start_date':date, 'length':length, 'cost':cost,  
        # 'location':location, 'level':level,'leader':leader, 'description': description}
        # # add new dict to csv data
        # trips[name]=new_trip
        
        # write csv data back out to csv file
        # set_trips(trips) 
        #to save new info from dict 
        database.add_trip(name,location,length,level,date,cost,leader,description)


        # since POST request, redirect to home after Submit
        return redirect(url_for('trips'))
    
    # if GET request received (display form)
    else:
        return render_template('trip_form.html')


# @app.route('/trips/<trip_id>/attendees/add')
# def get_attendees(member_id):
#      att= get_attendees()
#      return redirect(url_for('trips'))

#unused database** 
# database.remove_member_trip(trip_id, member_id)
# database.add_member_trip(trip_id, member_id)
# database.get_attendees(trip_id)

# mysql -h db.soic.indiana.edu -u i211s23_davidsma --password=my+sql=i211s23_davidsma -D i211s23_davidsma