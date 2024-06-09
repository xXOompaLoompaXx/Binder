# Binder
## About Binder
Binder is a social platform where musicians and music enthusiasts can meet each other by forming bands in a way that is fun and interactive, inspired by how Tinder works. 

First the user creates a profile on the register page, where the user can specify what genre, instrument and proficiency they have. They can then login in and start exploring the app. 

The most important page is the discover page. Here the user can say "Yes" and "No" to band suggestions and show interest that way. For each suggestion the user can see what users are in the band. The user can click on the other users and see their profile. Our system automatically makes band suggestions based on genre preference. 

When all users have said yes to a band suggestion, there is a maatch and a band is formed. The bands can be seen on the 'My Bands' page. Here the user can click on profiles to see the others profile-pages too.


## Setup
### Step 1: Setup python
1. Navigate to root
2.  Make sure to have python 3.10 (which is what the project is testet on). For this, you can easily create a virtuel environment by using conda: 
```
conda create -n binder python=3.10
```

3. Install required modules:
```
pip install -r requirements.txt
```
### Step 2: Setup database
1. Inside pgadmin create a new database, preferably called "binder".
2. In the root, there is a '.env' file, where you should fill in the needed details to connect to your database.
3. To setup the schema and add data, navigate to the 'Database Init' folder and run:
```
python db_init.py
```
Alternatively, you can execute the 'full_init.sql' however you like.

### Step 3: Run the flask application:
1. Navigate to the 'Binder' folder and run:
```
flask run
```
Then open the link (most often at 'localhost:5000') and you are now ready to use the application



## Simple guide to try the project
### Step 1: Login to Example Account
Login into the example account 'John Doe' using the following credentials:
- username: user1
- password: password1

For this profile, we have created two example bands, 'Example Band 1' and 'Example Band 2', where all users—except user1 (you)—are set to be already interested. Thus, when user1 says 'YES' to one of these example bands, a band is automatically formed.

### Step 2: View Profile
Optionally, view you profile information by opening the 'John Doe' profile page to see:
- N

### Step 2: Discover Bands
Open the 'Discover' page from the navigation bar. From here you should see the candidate 'Example Band 1' along with the candidate members.
- View each user's profile by clicking on their respective names.

Proceed to click "YES" to accept the band.

'Example Band 2' will now appear in its place.

Proceed again by clicking "YES" to accept the band.

### Step 3: View Your New Bands
You can now view both your new bands under the 'My Bands' page along all the members of each band.



