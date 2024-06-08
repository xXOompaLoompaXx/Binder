-- database_init.sql

-- Drop relationships first due to foreign key constraints
DROP TABLE IF EXISTS Band_contains;
DROP TABLE IF EXISTS Prefers_Genre;
DROP TABLE IF EXISTS Typical_Instruments;
DROP TABLE IF EXISTS Plays;

-- Drop entities next
DROP TABLE IF EXISTS Bands;
DROP TABLE IF EXISTS Users;

-- Drop types last
DROP TABLE IF EXISTS Cities;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Instruments;

-- types
CREATE TABLE IF NOT EXISTS Instruments(
    instrument varchar(50) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Genre(
    genre varchar(50) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Cities(
    city varchar(50) PRIMARY KEY,
    coordinates varchar(50)
);

-- entities
CREATE TABLE IF NOT EXISTS Users(
    pk serial not null PRIMARY KEY,
    email varchar(100) UNIQUE,
    user_name varchar(50) UNIQUE,
    full_name varchar(50),
    password varchar(120),
    birth_date DATE,
    located_in varchar(50) NOT NULL,
    FOREIGN KEY (located_in) REFERENCES Cities(city)
);

CREATE TABLE IF NOT EXISTS Bands(
    band_id serial not null PRIMARY KEY,
    band_name varchar(50),
    band_genre varchar(50),
    band_state INTEGER,
    creation_date DATE,
    FOREIGN KEY (band_genre) REFERENCES Genre(genre)
);

-- relationships
CREATE TABLE IF NOT EXISTS Plays 
    (pk INTEGER,
    instrument varchar(50),
    proficiency INTEGER,
    PRIMARY KEY (pk, instrument),
    FOREIGN KEY (pk) REFERENCES Users(pk),
    FOREIGN KEY (instrument) REFERENCES Instruments(instrument)
);

CREATE TABLE IF NOT EXISTS Typical_Instruments 
    (instrument varchar(50),
    genre varchar(50),
    PRIMARY KEY (genre, instrument),
    FOREIGN KEY (instrument) REFERENCES Instruments(instrument),
    FOREIGN KEY (genre) REFERENCES Genre(genre)
);

CREATE TABLE IF NOT EXISTS Prefers_Genre 
    (pk INTEGER,
    genre varchar(50),
    PRIMARY KEY (genre, pk),
    FOREIGN KEY (pk) REFERENCES Users(pk),
    FOREIGN KEY (genre) REFERENCES Genre(genre)
);

CREATE TABLE IF NOT EXISTS Band_contains 
    (pk INTEGER,
    band_id INTEGER,
    interested BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (band_id, pk),
    FOREIGN KEY (pk) REFERENCES Users(pk),
    FOREIGN KEY (band_id) REFERENCES Bands(band_id)
);

-- Reset sequences
ALTER SEQUENCE users_pk_seq RESTART WITH 1;
ALTER SEQUENCE bands_band_id_seq RESTART WITH 1;



--ADD DATA



-- add_data.sql

-- Insert data into Instruments
INSERT INTO Instruments (instrument) VALUES
('Guitar'),
('El-Guitar'),
('Drums'),
('Bass'),
('E-Piano'),
('Vocals'),
('Saxophone'),
('Piano'),
('Contra-Bass');

-- Insert data into Genre
INSERT INTO Genre (genre) VALUES
('Rock'),
('Jazz'),
('Pop');

-- Insert data into Typical_Instruments
INSERT INTO Typical_Instruments (instrument, genre) VALUES
('Drums', 'Rock'),
('El-Guitar', 'Rock'),
('Vocals', 'Rock'),
('Bass', 'Rock'),
('E-Piano', 'Jazz'),
('Contra-Bass', 'Jazz'),
('Saxophone', 'Jazz'),
('Drums', 'Jazz'),
('Guitar', 'Pop'),
('Piano', 'Pop'),
('Vocals', 'Pop'),
('Drums', 'Pop'),
('Bass', 'Pop');

-- Insert data into Cities
INSERT INTO Cities (city, coordinates) VALUES
('København', '40.7128,-74.0060'),
('Slagelse', '34.0522,-118.2437'),
('Roskilde', '41.8781,-87.6298'),
('Odense', '29.7604,-95.3698'),
('Aarhus', '25.7617,-80.1918');


-- Insert data into Users
INSERT INTO Users (user_name, full_name, password, birth_date, located_in, email) VALUES
('user1', 'John Doe', 'password1', '1990-01-01', 'København', 'john.doe5@gmail.com'),
('user2', 'Jane Smith', 'password2', '1985-05-05', 'Slagelse', 'jane.smith7@gmail.com'),
('user3', 'Alice Johnson', 'password3', '1992-09-09', 'Roskilde', 'alice.johnson9@gmail.com'),
('user4', 'Bob Brown', 'password4', '1988-03-03', 'Odense', 'bob.brown3@gmail.com'),
('user5', 'Charlie Davis', 'password5', '1995-12-12', 'Aarhus', 'charlie.davis12@gmail.com'),
('user6', 'Diana Miller', 'password6', '1991-04-04', 'København', 'diana.miller4@gmail.com'),
('user7', 'Ethan Wilson', 'password7', '1989-07-07', 'Slagelse', 'ethan.wilson7@gmail.com'),
('user8', 'Fiona Thomas', 'password8', '1986-02-02', 'Roskilde', 'fiona.thomas2@gmail.com'),
('user9', 'George Clark', 'password9', '1993-11-11', 'Odense', 'george.clark11@gmail.com'),
('user10', 'Hannah Lewis', 'password10', '1994-08-08', 'Aarhus', 'hannah.lewis8@gmail.com'),
('user11', 'Isaac Turner', 'password11', '1990-10-10', 'København', 'isaac.turner10@gmail.com'),
('user12', 'Julia Adams', 'password12', '1987-01-01', 'Slagelse', 'julia.adams1@gmail.com'),
('user13', 'Kevin White', 'password13', '1991-06-06', 'Roskilde', 'kevin.white6@gmail.com'),
('user14', 'Laura Martinez', 'password14', '1989-04-04', 'Odense', 'laura.martinez4@gmail.com'),
('user15', 'Michael Scott', 'password15', '1992-08-08', 'Aarhus', 'michael.scott8@gmail.com'),
--More Rock Users
('user16', 'Oliver Hansen', 'password16', '1990-01-01', 'København', 'oliver.hansen1@gmail.com'),
('user17', 'Emma Jensen', 'password17', '1985-05-05', 'Slagelse', 'emma.jensen5@gmail.com'),
('user18', 'Noah Pedersen', 'password18', '1992-09-09', 'Roskilde', 'noah.pedersen9@gmail.com'),
('user19', 'William Larsen', 'password19', '1988-03-03', 'Odense', 'william.larsen3@gmail.com'),
('user20', 'Sophia Nielsen', 'password20', '1995-12-12', 'Aarhus', 'sophia.nielsen12@gmail.com'),
('user21', 'Isabella Christiansen', 'password21', '1991-04-04', 'København', 'isabella.christiansen4@gmail.com'),
('user22', 'Liam Andersen', 'password22', '1989-07-07', 'Slagelse', 'liam.andersen7@gmail.com'),
('user23', 'Mia Thomsen', 'password23', '1986-02-02', 'Roskilde', 'mia.thomsen2@gmail.com'),
('user24', 'Lucas Sørensen', 'password24', '1993-11-11', 'Odense', 'lucas.sorensen11@gmail.com'),
('user25', 'Ella Petersen', 'password25', '1994-08-08', 'Aarhus', 'ella.petersen8@gmail.com');



-- Insert data into Prefers_Genre
INSERT INTO Prefers_Genre (pk, genre) VALUES
(1, 'Rock'),
(2, 'Jazz'),
(3, 'Pop'),
(4, 'Rock'),
(5, 'Jazz'),
(6, 'Pop'),
(7, 'Rock'),
(8, 'Jazz'),
(9, 'Pop'),
(10, 'Rock'),
(11, 'Jazz'),
(12, 'Pop'),
(13, 'Rock'),
(14, 'Jazz'),
(15, 'Pop'),
-- More Rock Users
(16, 'Rock'),
(17, 'Rock'),
(18, 'Rock'),
(19, 'Rock'),
(20, 'Rock'),
(21, 'Rock'),
(22, 'Rock'),
(23, 'Rock'),
(24, 'Rock'),
(25, 'Rock');



-- Insert data into Plays
INSERT INTO Plays (pk, instrument, proficiency) VALUES
(1, 'Bass', 8),
(2, 'E-Piano', 7),
(3, 'Piano', 6),
(4, 'Drums', 9),
(5, 'Saxophone', 7),
(6, 'Bass', 8),
(7, 'Vocals', 6),
(8, 'Contra-Bass', 7),
(9, 'Guitar', 5),
(10, 'El-Guitar', 8),
(11, 'Drums', 7),
(12, 'Vocals', 8),
(13, 'El-Guitar', 7),
(14, 'Saxophone', 6),
(15, 'Drums', 9),
-- More Rock Users
(16, 'Drums', 4),
(17, 'El-Guitar', 7),
(18, 'Vocals', 8),
(19, 'Bass', 2),
(20, 'Drums', 5),
(21, 'El-Guitar', 8),
(22, 'Vocals', 3),
(23, 'Bass', 4),
(24, 'Drums', 10),
(25, 'El-Guitar', 8);


-- Example Band

INSERT INTO bands (band_name, band_genre, band_state, creation_date) VALUES 
('example-band 1', 'Rock', 0, '2024-06-08');

INSERT INTO band_contains VALUES 
(10, 1, TRUE),
(4, 1, TRUE),
(1, 1, NULL),
(7, 1, TRUE);

INSERT INTO bands (band_name, band_genre, band_state, creation_date) VALUES 
('example-band 2', 'Rock', 0, '2024-06-08');

INSERT INTO band_contains VALUES 
(13, 2, TRUE),
(4, 2, TRUE),
(1, 2, NULL),
(7, 2, TRUE);

