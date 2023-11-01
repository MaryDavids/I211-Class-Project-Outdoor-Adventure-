import pymysql
#uncomment the following line when you start project 3.2:
from app import app


# Make sure you have data in your tables. You should have used auto increment for 
# primary keys, so all primary keys should start with 1

#you will need this helper function for all of your functions
#Use the uncommented version to test and turn in your code.  
#Comment out this version and then uncomment and use the second version below when you are importing 
#this file into your app.py in your I211_project for Project 3.2


# def get_connection():
#     return pymysql.connect(host=app.config['DB_HOST'],
#                            user=app.config['DB_USER'],
#                            password=app.config['DB_PASS'],
#                            database=app.config['DB_DATABASE'],
#                            cursorclass=pymysql.cursors.DictCursor)

def get_connection():
    return pymysql.connect(host="db.luddy.indiana.edu",
                           user="i211s23_davidsma",
                           password="my+sql=i211s23_davidsma",
                           database="i211s23_davidsma",
                           cursorclass=pymysql.cursors.DictCursor)

def get_trips():
    '''Returns a list of dictionaries representing all of the trips data'''
    #add your code below, deleting the "pass"
    sql= "select * from trips;"
    conn= get_connection()
    with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()


# trip can be a dictionary with all course information or can represent multiple variables that contain all of the trip information.

def get_trip(trip_id):
    '''Takes a trip_id, returns a single dictionary containing the data for the trip with that id'''
    sql= "select * from trips where name = %s"
    conn= get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id))
            return cursor.fetchone()

    

def add_trip(name,location,length,level,start_date,cost,leader,description): # replace with name, location... ?
    '''Takes as input all of the data for a trip. Inserts a new trip into the trip table'''
    #for i in trip:
    sql= "insert into trips(name,location,length,level,start_date,cost,leader,description) values (%s, %s,%s,%s,%s, %s,%s,%s )"
    conn= get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name,location,length,level,start_date,cost,leader,description)) #or just trip?
        conn.commit()
    

def update_trip(trip_id, name,location,length,level,start_date,cost,leader,description):
    '''Takes a trip_id and data for a trip. Updates the trip table with new data for the trip with trip_id as it's primary key'''
    sql= 'update trips set name= %s, location=%s, length=%s,level=%s,start_date=%s,cost=%s,leader=%s,description=%s where id_trip= %s'
    conn= get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name,location,length,level,start_date,cost,leader,description, trip_id)) 
        conn.commit()

    

def add_member(name, date_of_birth, email, address, phone): #add name, dob, email ... as input?
    '''Takes as input all of the data for a member and adds a new member to the member table'''
    sql= "insert into members (name,date_of_birth,email,address,phone) values (%s, %s,%s,%s,%s)"
    conn= get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name, date_of_birth, email, address, phone)) # or just member 
        conn.commit()
    
def get_members():
    '''Returns a list of dictionaries representing all of the member data'''
    sql= "select * from members"
    conn= get_connection()
    with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
   

def edit_member(member_id, name, date_of_birth, email, address, phone ): #can i do this with the "member info"? 
    '''Given an member__id and member info, updates the data for the member with the given member_id in the member table'''
    #update table set name
    sql= "update members set name = %s, date_of_birth=%s,email=%s, address=%s, phone=%s where id_mem= %s"
    conn= get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, name, date_of_birth, email, address, phone, member_id) # or just member 
        conn.commit()
    

def delete_member(member_id): #is there a way to test this yet?
    '''Takes a member_id and deletes the member with that member_id from the member table'''
    # delete 
    sql= "delete from members where id_mem= %s" 
    conn= get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, member_id)
        conn.commit()

    
def add_member_trip(trip_id, member_id):
    '''Takes as input a trip_id and a member_id and inserts the appropriate data into the database that indicates the member with member_id as a primary key is attending the trip with the trip_id as a primary key'''
    sql= "insert into attendance (id_trip, id_mem) values (%s, %s)" 
    conn= get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, trip_id, member_id)
        conn.commit()
    
def remove_member_trip(trip_id, member_id):
    '''Takes as input a trip_id and a member_id and deletes the data in the database that indicates that the member with member_id as a primary key 
    is attending the trip with trip_id as a primary key.'''
    sql= "delete from attendance where id_trip= %s and id_mem= %s" 
    conn= get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, trip_id, member_id)
        conn.commit()
    
def get_attendees(trip_id):
    '''Takes a trip_id and returns a list of dictionaries representing all of the members attending the trip with trip_id as its primary key'''
    #grab members assocated with trip in attendance \
    sql="select * from members where id_mem in (select id_mem from attendance where id_trip= %s)"
    conn= get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id))
            #trips_dict[trip_id]= data
            return cursor.fetchall() 

    
# * subquery

# if __name__ == '__main__':
    #add more test code here to make sure all your functions are working correctly
    # try:
    #     print(f'All trips: {get_trips()}')
    #     print("#"*80)
    #     print(f'Trip info for trip_id 1: {get_trip(1)}')

    #     # delete_member(1)

    #     # add_trip("A Day in Yellowwood", "Yellowwood State Forest", 1, "beginner", "2023-04-22", "$10", "Sy Hikist", "A day of hiking in Yellowwood. Bring a water bottle" )
    #     # print(f'All Members: {get_members()}')
    #     # add_member("Tom Sawyer", "1970-04-01","tsawyer@twain.com", "101 E Sam Clemons Dr Bloomington, IN", "812-905-1865")
    #     # print(f"All members attending the trip with trip_id 1: {get_attendees(1)}")

    # except Exception as e:
    #     print(e)