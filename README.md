# chatter.Inc
chatter.Inc A simple Chat application with rooms with members joined in rooms



Prerequisites

   1.Install Python

    Install python-3.7.2 and python-pip. Follow the steps from the below reference document based on your Operating System. Reference: https://docs.python-guide.org/starting/installation/

   2. Setup virtual environment

   #install virtualenv

     sudo pip install virtualenv

   #make directory for virtualenv

     mkdir envs

   #Create virtual environment

     virtualenv envs

   #Activate virtual environment

     . envs/bin/activate

   3. Clone git repository

     git clone https://github.com/Dhuvaraggn/chatter.Inc.git

   4. Install requirements

     cd chatter.Inc/
     pip install -r requirements.txt

   5.Migrate Database to create DB in local machine
      
     python manage.py makemigrations db  
     python manage.py migrate
     
   6. Run the server
     
     python manage.py runserver
     
   #your server is up on port 8000

   #Try opening http://localhost:8000/ in the browser. Now you are good to go. plz at first create a account my clicking sign up first time. then its fun....
   FunPandrooo!!!!!!!!!
   
  7.create a superuser to access the DB from http:/localhost:8000/admin/
  
      python manage.py createsuperuser
   enter name of user and password and kudos your running a chatter.Inc messenger.
   

URLS start page : http://localhost:8000/
