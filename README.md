# Set up React  
0. `cd ~/environment && git clone https://github.com/NJIT-CS490/project3-agendasync && cd project3-agendasync`    
1. Install your stuff!    
  a) `npm install && npm install -g webpack && npm install --save-dev webpack && npm install socket.io-client --save`    
  b) `pip install flask-socketio`    
  c) `pip install eventlet`    
  d) `pip install twilio`    
  e) `pip install google_auth_oauthlib`
  f) `
:warning: :warning: :warning: If you see any error messages, make sure you use `sudo pip` or `sudo npm`. If it says "pip cannot be found", run `which pip` and use `sudo [path to pip from which pip] install`  :warning: :warning: :warning:  
</div>
  
# Getting PSQL to work with Python  
  
1. Update yum: `sudo yum update`, and enter yes to all prompts    
2. Upgrade pip: `sudo pip install --upgrade pip`  
3. Get psycopg2: `sudo pip install psycopg2-binary`    
4. Get SQLAlchemy: `sudo pip install Flask-SQLAlchemy==2.1`    
  
# Setting up PSQL  
  
1. Install PostGreSQL: `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`    
    Enter yes to all prompts.    
2. Initialize PSQL database: `sudo service postgresql initdb`    
3. Start PSQL: `sudo service postgresql start`    
4. Make a new superuser: `sudo -u postgres createuser --superuser $USER`    
    :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked!  
5. Make a new database: `sudo -u postgres createdb $USER`    
        :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked!  
6. Make sure your user shows up:    
    a) `psql`    
    b) `\du` look for ec2-user as a user    
    c) `\l` look for ec2-user as a database    
7. Make a new user:    
    a) `psql` (if you already quit out of psql)    
    ## REPLACE THE [VALUES] IN THIS COMMAND! Type this with a new (short) unique password.    
    b) I recommend 4-5 characters - it doesn't have to be very secure. Remember this password!   
        `create user [some_username_here] superuser password '[some_unique_new_password_here]';`   
        :warning: this should look like `create user sresht superuser password 'mypass';` :warning:   
    c) `\q` to quit out of sql    
8. `cd` into `project3-agendasync` and make a new file called `sql.env` and add `SQL_USER=` and `SQL_PASSWORD=` in it  
9. Fill in those values with the values you put in 7. b)  
  
  
# Enabling read/write from SQLAlchemy  
There's a special file that you need to enable your db admin password to work for:  
1. Open the file in vim: `sudo vim /var/lib/pgsql9/data/pg_hba.conf`  
:warning: :warning: :warning: If that doesn't work: `sudo vim $(psql -c "show hba_file;" | grep pg_hba.conf)`  :warning: :warning: :warning:  
2. Replace all values of `ident` with `md5` in Vim: `:%s/ident/md5/g`  
3. After changing those lines, run `sudo service postgresql restart`  
4. Ensure that `sql.env` has the username/password of the superuser you created!  
5. Run your code!    
  a) `npm run watch`. If prompted to install webpack-cli, type "yes"    
  b) In a new terminal, `python app.py`    
  c) Preview Running Application (might have to clear your cache by doing a hard refresh)    
6. You should just see the same random number as lect10's socket demo.

# Initializing Google API

The app uses Google to initialize and authenticate user interaction.
1. Create a Google API account at https://console.developers.google.com/apis/dashboard
2. On your developer console, search `Google Calendar API` in the top search bar and enable it for your account
3. Return to the console UI and click the APIs and Services Tab, click on `Credentials`
4. Click `Create OAuth client ID`
5. Create a web application as well as give it a name
6. Insert the a uri link from your AWS preview
7. Download a credentials file from your web application and rename it `credentials.json`, insert it into your directory

# Deploying to Heroku
Sign up for heroku at https://www.heroku.com/
1. heroku login -i
2. heroku create
3. git push heroku master
Navigate to your newly created Heroku site.
Add secret keys from development.env by going to https://dashboard.heroku.com/apps
Click into your app > Settings > Config Vars > Reveal Config Vars > Add key value pairs for each variable.
Configure requirements.txt with all requirements needed to run your app.
Configure Procfile with the command needed to run your app.
