# Note Book

Link to Note Book:-
https://colab.research.google.com/drive/1iOZ2J3uEAR1b9YR7M8aIrckplZJ_rBvi#scrollTo=a_b38ApBJcDk

1. CSV file is taken and converted to panddas datframe.
2. Now we are checking if any data anomilies are there in the csv file or not.
3. Finally we are training the split data in three different models (RandomForestRegressor, LogisticRegression, SVC)
4. Last we are calculating precision, accuracy, f1 score and recall.




# Flask API

Run create_db.py file to create database for the APP.
To run the Flask APP just run the main.py file after installing packages in requirements.txt.


1. There are six APIs with proper validation of Authorization using jwt token for all the APIs with username and password.

2. First we have to login with the below API. Put valid username and password at the end point.
      http://127.0.0.1:5000/login/username/password
      
3. We can retrive data from database using the below API.
      http://127.0.0.1:5000/api/retrive

4. We can insert data to database using the below API.
      http://127.0.0.1:5000/api/insert/Id/23267/native_english_speaker/Soham/course_instructor/Rounak/course/Eng/semester/sem2/class_size/200/performance_score/300
      
5. We can delete record from database using Id use the below API.
      http://127.0.0.1:5000/api/delete/23267
      
6. We can update record in database using Id use the below API.
      http://127.0.0.1:5000/api/update/2316/native_english_speaker/rounak454
      
   
# Fast API

Run create_db.py file to create database for the APP.
To run the Fast APP just run the main.py file after installing packages in requirements.txt.

1. There are one API with proper validation of Authorization using jwt token for the APIs with username and password.

2. First we have to authenticate the API. Put valid username and password.
      http://127.0.0.1:8000/docs#
      
      
