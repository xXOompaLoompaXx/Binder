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
('user1', 'John Doe', '$2b$12$S4wQi7RWnrtQol0bOvv8keOz2nQ6Fub9AV2MEijyyRRNhYFpDu4hK', '1990-01-01', 'København', 'john.doe5@gmail.com'),
('user2', 'Jane Smith', '$2b$12$WEqlUfNCPvarT52jPapmx.KGkZ0lEMhNYAFpx/fx/Kbhwmcb70QSy', '1985-05-05', 'Slagelse', 'jane.smith7@gmail.com'),
('user3', 'Alice Johnson', '$2b$12$iRit8JqRCvZ06LIEFJUm2.zbRRopar55TiQaZ3nLiR2kxJzGgo9Y.', '1992-09-09', 'Roskilde', 'alice.johnson9@gmail.com'),
('user4', 'Bob Brown', '$2b$12$MpWGiL9BE9XYUhPosZgASOW7ZJ0VxJnNTctYfeLazLuNGVwPWzNtO', '1988-03-03', 'Odense', 'bob.brown3@gmail.com'),
('user5', 'Charlie Davis', '$2b$12$XsD44Jhil1FIdKlxfvhFTOlFNNObZHKJb8opUp7f5/zl0tXl.WB1e', '1995-12-12', 'Aarhus', 'charlie.davis12@gmail.com'),
('user6', 'Diana Miller', '$2b$12$T/yHhFrodKlHav4btYTXlOihA..IJdpkFYLzQy8h8auVuAf2QiJXC', '1991-04-04', 'København', 'diana.miller4@gmail.com'),
('user7', 'Ethan Wilson', '$2b$12$0zxkh5/EdGo2.syacQ.57.a/aC.Va72gz9pY0k/baNkrWBUIeXvty', '1989-07-07', 'Slagelse', 'ethan.wilson7@gmail.com'),
('user8', 'Fiona Thomas', '$2b$12$jB0dq/UrXy/QpyXFen05fu2DO3KKKdQ/1Dr7hdEf6sxY21Ze5l8cq', '1986-02-02', 'Roskilde', 'fiona.thomas2@gmail.com'),
('user9', 'George Clark', '$2b$12$Mx5w45GrTusSEKyAgci4/efV0tbTQ/3ANuSfnhJohC8tmZjKO/SXC', '1993-11-11', 'Odense', 'george.clark11@gmail.com'),
('user10', 'Hannah Lewis', '$2b$12$P6N2lKJNdQHmJEqebAHau.2lObC.SQ68/tsxsvS4DPh5iajW58tYC', '1994-08-08', 'Aarhus', 'hannah.lewis8@gmail.com'),
('user11', 'Isaac Turner', '$2b$12$gq26SOq7dTG9kaWhG/Bv6uB8MBk6Fe3qB6MfM0GZt7f6Dik5wVbA2', '1990-10-10', 'København', 'isaac.turner10@gmail.com'),
('user12', 'Julia Adams', '$2b$12$l4c.PCje0Gmtl.30v5uOiO5xYSs5US6JC9n6CwAEm4Z/OfuZnxo8C', '1987-01-01', 'Slagelse', 'julia.adams1@gmail.com'),
('user13', 'Kevin White', '$2b$12$7GZb272ZSkPjsIxP.jCDhuyZgbKm8S8HEqwjOJ1Pbt0WyD3he5NkW', '1991-06-06', 'Roskilde', 'kevin.white6@gmail.com'),
('user14', 'Laura Martinez', '$2b$12$CDiGWx6JkydzrBErtGJXhekz5xYMq21FpFRALCjszk9iYDOr7kb.2', '1989-04-04', 'Odense', 'laura.martinez4@gmail.com'),
('user15', 'Michael Scott', '$2b$12$/EDOPMK/QJEIzgznkqeKv.mN5aX1SwEnWnvkU8aOfYruR/2.D6OFq', '1992-08-08', 'Aarhus', 'michael.scott8@gmail.com'),
('user16', 'Oliver Hansen', '$2b$12$hyGKHAUgiddj1WWHk//orO6wlSxWoA.FgGB67Rsd4vRRoahLwkhzq', '1990-01-01', 'København', 'oliver.hansen1@gmail.com'),
('user17', 'Emma Jensen', '$2b$12$JqtgDyzm1GFWuBJM0pAp2utUDOi01jCm29Wu3FNLpQfSwODSdn1K.', '1985-05-05', 'Slagelse', 'emma.jensen5@gmail.com'),
('user18', 'Noah Pedersen', '$2b$12$IjM6gEqJb.CMA9SExJPgiu2cXiuUAccnHTJBryeeXyoOgU5SB8EWa', '1992-09-09', 'Roskilde', 'noah.pedersen9@gmail.com'),
('user19', 'William Larsen', '$2b$12$CVnhlRKo6yGDw3FFQPfBb.YTEUP/pJpDV9VfXusQ2ai3DeN6XxNim', '1988-03-03', 'Odense', 'william.larsen3@gmail.com'),
('user20', 'Sophia Nielsen', '$2b$12$l7MSOUScK5FRwZ4S6J9AbufG5nTb3rpIhpeaKANoCEEFekj4wmbC2', '1995-12-12', 'Aarhus', 'sophia.nielsen12@gmail.com'),
('user21', 'Isabella Christiansen', '$2b$12$cPcSvutvwlCrEC.uX/M81uq3M6YM/fx2qkNJZPH.QjVvGXfKwCDwe', '1991-04-04', 'København', 'isabella.christiansen4@gmail.com'),
('user22', 'Liam Andersen', '$2b$12$.0ML/sMlmsrPRu6lFSqI3edy3WWolKlWYCJ.ehXdJJpbuNLOg0Tri', '1989-07-07', 'Slagelse', 'liam.andersen7@gmail.com'),
('user23', 'Mia Thomsen', '$2b$12$hj0t49RgsNboIuNKyYZo9.rOQnINW2PZPmHEUr9TU9qrO9cOAEIxC', '1986-02-02', 'Roskilde', 'mia.thomsen2@gmail.com'),
('user24', 'Lucas Sørensen', '$2b$12$oJtS7pm4PCxtF.VLDjwlYOhPl3HEt5XCd5QSD6SotFdk5u49L.IXy', '1993-11-11', 'Odense', 'lucas.sorensen11@gmail.com'),
('user25', 'Ella Petersen', '$2b$12$6pRiODrp5UzT/mvNNtpQTOZtjh3scOPMCYLUPP.NLC0m6gxDN5lQi', '1994-08-08', 'Aarhus', 'ella.petersen8@gmail.com');



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
('Example Band 1', 'Rock', 0, '2024-06-08');

INSERT INTO band_contains VALUES 
(10, 1, TRUE),
(4, 1, TRUE),
(1, 1, NULL),
(7, 1, TRUE);

INSERT INTO bands (band_name, band_genre, band_state, creation_date) VALUES 
('Example Band 2', 'Rock', 0, '2024-06-08');

INSERT INTO band_contains VALUES 
(13, 2, TRUE),
(16, 2, TRUE),
(1, 2, NULL),
(18, 2, TRUE);

