# Binder
## About Binder
Binder is a social platform where musicians and music enthusiasts can meet each other by forming bands in a way that is fun and interactive, inspired by how Tinder works. 

First, the user creates a profile on the register page, where they can specify their genre, instrument, and proficiency. They can then log in and start exploring the app. 

The most important page is the discover page. Here, the user can say "Yes" or "No" to band suggestions and show interest that way. For each suggestion, the user can see which users are in the band. The user can click on the other users and see their profiles. Our system automatically makes band suggestions based on genre preferences. 

When all users have said yes to a band suggestion, there is a match, and a band is formed. The bands can be seen on the 'My Bands' page. Here, the user can click on profiles to see the other users' profile pages too.

## Setup
### Step 1: Setup Python
1. Navigate to the root.
2. Make sure to have Python 3.10 (which is what the project is tested on). For this, you can easily create a virtual environment by using conda: 
```
conda create binder -n python=3.10
```

3. Install required modules:
```
pip install -r requirements.txt
```
### Step 2: Setup Database
1. Inside pgAdmin, create a new database, preferably called "binder".
2. In the root, there is a '.env' file where you should fill in the needed details to connect to your database.
    - DB_HOST: The host-adress, often just: "localhost"
    - DB_NAME: The name of the database, for example: "binder"
    - DB_USER: psql username, often just: "postgres"
    - psqlPass: Your password for the user
3. To set up the schema and add data, navigate to the 'Database Init' folder and run:
```
python db_init.py
```
Alternatively, you can execute the 'full_init.sql' however you like.

### Step 3: Run the Flask Application:
1. Navigate to the 'Binder' folder and run:
```
flask run
```
Then open the link (most often at 'localhost:5000') and you are now ready to use the application.

## Simple Guide to Try the Project
### Step 1: Login to Example Account
Log in to the example account 'John Doe' using the following credentials:
- Username: user1
- Password: password1

For this profile, we have created two example bands, 'Example Band 1' and 'Example Band 2', where all users—except user1 (you)—are set to be already interested. Thus, when user1 says 'YES' to one of these example bands, a band is automatically formed.

### Step 2: View Profile
Optionally, view your profile information by opening the 'John Doe' profile page to see:
- Name and username
- Location
- Email
- Birth date
- Bands

### Step 3: Discover Bands
Open the 'Discover' page from the navigation bar. From here, you should see the candidate 'Example Band 1' along with the candidate members.
- View each user's profile by clicking on their respective names.

Proceed to click "YES" to accept the band.

'Example Band 2' will now appear in its place.

Proceed again by clicking "YES" to accept the band.

### Step 4: View Your New Bands
You can now view both your new bands under the 'My Bands' page along with all the members of each band.

## SQL
We have used INSERT, UPDATE, and SELECT statements in our project.

## Regex
We have used regex for validating email and full name syntax.

## Future Roadmap
We did not reach all the features that we would like, and some future features we would like to implement are listed below:
### Multiple Instruments/Genres
Having the option to choose multiple genres and instruments to widen the user's options and enrich the experience to accommodate real-life scenarios.

### More Complex Band Suggestions 
Proficiency and location should be taken into account when the system creates band suggestions.

### Browsing Others' Profiles/Bands
Expanding on the profile network and adding functionality towards this.

## Contributors
- Hetianyu Huang (csk355)
- Kevin Mark Lock (zqw671)
- Lau Safin (fns992)