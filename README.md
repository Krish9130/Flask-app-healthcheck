#Create a Virtual Environment

    python3 -m venv flask-venv

#Activate the Virtual Environment

    source flask-venv/bin/activate

#Install Dependencies

    pip install -r requirements.txt

#Run the Flask Application

    python3 app.py runserver

# Background running 

    nohup python3 manage.py runserver 127.0.0.1:5000 > nohup_main.log 2>&1 	&


##Access the Application on internet

http://localhost:5000/
