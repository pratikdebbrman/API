from flask import Flask,jsonify,g
import pandas as pd
import sqlite3
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, create_access_token, decode_token
from datetime import timedelta,datetime


app = Flask(__name__)

DATABASE = 'database.db'

# Set the secret key for signing JWT tokens
app.config['JWT_SECRET_KEY'] = 'my-secret-key'

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=2)

# Initialize the JWT manager
jwt = JWTManager(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Define a login endpoint to generate JWT tokens
@app.route('/login/<string:username>/<string:password>')
def login(username,password):
    # Authenticate the user 
    # http://127.0.0.1:5000/login/pdeb/2433
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER_DETAIL WHERE UserID = ? and Pass = ?", (username,password))
    results = cursor.fetchall()
    conn.commit()
    cursor.close()

    # Check if any rows were returned
    if len(results) > 0:
        print('Query returned', len(results), 'rows')
        
        # Generate a JWT token
        access_token = create_access_token(identity=username)

        global store_access_token
        store_access_token=access_token

        return jsonify({'message': 'Access token created Sucessfully'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401


def decode():
    if len(store_access_token)!=0:
        decoded_token = decode_token(store_access_token)
        # Check if the token has expired
        exp_timestamp = decoded_token['exp']
        exp_datetime = datetime.fromtimestamp(exp_timestamp)
        is_expired = exp_datetime < datetime.now()
        print(exp_datetime)
        print(datetime.now())

        if is_expired:
            return 'Token has expired'
        else:
            return 'Token is valid'
    else:
        return 'No Token Found as not authenticated'



@app.route('/api/retrive')
def retrive():
    # http://127.0.0.1:5000/api/retrive

    decode()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TA;")
    data = cursor.fetchall()
    df=pd.DataFrame(data, columns=['id','native_english_speaker', 'course_instructor', 'course', 'semester', 'class_size','performance_score'])
    data_dict = df.to_dict(orient='records')
    response = jsonify(data_dict)

    conn.commit()
    cursor.close()
    return response

@app.route('/api/insert/Id/<int:Id>/native_english_speaker/<string:native_english_speaker>/course_instructor/<string:course_instructor>/course/<string:course>/semester/<string:semester>/class_size/<string:class_size>/performance_score/<int:performance_score>')
def insert(Id, native_english_speaker, course_instructor, course, semester, class_size,performance_score):

    # http://127.0.0.1:5000/api/insert/Id/23267/native_english_speaker/Soham/course_instructor/Rounak/course/Eng/semester/sem2/class_size/200/performance_score/300
    
    decode()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO TA (Id, native_english_speaker, course_instructor, course, semester, class_size,performance_score) VALUES (?, ?, ?, ?, ?, ?, ?)", (Id, native_english_speaker, course_instructor, course, semester, class_size,performance_score))
    conn.commit()
    cursor.close()
    return "ID {} has been added sucessfully".format(id)



@app.route('/api/delete/<int:id>')
def delete_customer(id):

    # http://127.0.0.1:5000/api/delete/23267

    decode()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TA WHERE Id = ?", (id,))
    conn.commit()
    cursor.close()
    return "ID {} has been deleted".format(id)

@app.route('/api/update/<int:Id>/native_english_speaker/<string:native_english_speaker>')
def update_customer(Id,native_english_speaker):

    #http://127.0.0.1:5000/api/update/2316/native_english_speaker/rounak454

    decode()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE TA SET native_english_speaker = ? WHERE Id = ?", (native_english_speaker, Id))
    conn.commit()
    cursor.close()
    return "ID {} has been updated".format(id)

if __name__ == '__main__':
    app.run()
