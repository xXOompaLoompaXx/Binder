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
('Pop'),
('Classical'),
('Hip Hop');

-- Insert data into Cities
INSERT INTO Cities (city, coordinates) VALUES
('New York', '40.7128,-74.0060'),
('Los Angeles', '34.0522,-118.2437'),
('Chicago', '41.8781,-87.6298'),
('Houston', '29.7604,-95.3698'),
('Miami', '25.7617,-80.1918');

-- Insert data into Users
INSERT INTO Users (user_name, full_name, password, birth_date, located_in) VALUES
('user1', 'John Doe', 'password1', '1990-01-01', 'New York'),
('user2', 'Jane Smith', 'password2', '1985-05-05', 'Los Angeles'),
('user3', 'Alice Johnson', 'password3', '1992-09-09', 'Chicago'),
('user4', 'Bob Brown', 'password4', '1988-03-03', 'Houston'),
('user5', 'Charlie Davis', 'password5', '1995-12-12', 'Miami'),
('user6', 'Diana Miller', 'password6', '1991-04-04', 'New York'),
('user7', 'Ethan Wilson', 'password7', '1989-07-07', 'Los Angeles'),
('user8', 'Fiona Thomas', 'password8', '1986-02-02', 'Chicago'),
('user9', 'George Clark', 'password9', '1993-11-11', 'Houston'),
('user10', 'Hannah Lewis', 'password10', '1994-08-08', 'Miami'),
('user11', 'Isaac Turner', 'password11', '1990-10-10', 'New York'),
('user12', 'Julia Adams', 'password12', '1987-01-01', 'Los Angeles'),
('user13', 'Kevin White', 'password13', '1991-06-06', 'Chicago'),
('user14', 'Laura Martinez', 'password14', '1989-04-04', 'Houston'),
('user15', 'Michael Scott', 'password15', '1992-08-08', 'Miami');

-- Insert data into Bands
-- INSERT INTO Bands (band_id, band_name, band_genre, band_state, creation_date) VALUES
-- (1, 'The Rockers', 'Rock', 0, '2024-06-01'),
-- (2, 'Jazz Masters', 'Jazz', 0, '2024-06-02'),
-- (3, 'Pop Stars', 'Pop', 0, '2024-06-03'),
-- (4, 'Classical Ensemble', 'Classical', 1, '2024-06-04'),
-- (5, 'Hip Hop Crew', 'Hip Hop', 0, '2024-06-05'),
-- (6, 'Fusion Collective', 'Jazz', 0, '2024-06-06'),
-- (7, 'Symphony Strings', 'Classical', 1, '2024-06-07'),
-- (8, 'Electric Vibes', 'Pop', 0, '2024-06-08'),
-- (9, 'Rhythm Riders', 'Rock', 1, '2024-06-09'),
-- (10, 'Beats and Rhymes', 'Hip Hop', 2, '2024-06-10');

-- Insert data into Plays
INSERT INTO Plays (pk, instrument, proficiency) VALUES
(1, 'El-Guitar', 8),
(2, 'E-Piano', 7),
(3, 'Piano', 6),
(4, 'Drums', 9),
(5, 'Saxophone', 7),
(6, 'Bass', 8),
(7, 'Vocals', 6),
(8, 'Contra-Bass', 7),
(9, 'Guitar', 5),
(10, 'Bass', 8),
(11, 'Drums', 7),
(12, 'Vocals', 8),
(13, 'El-Guitar', 7),
(14, 'Saxophone', 6),
(15, 'Drums', 9);

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
(15, 'Pop');

-- Insert more data into Band_contains
-- INSERT INTO Band_contains (pk, band_id, instrument, interested) VALUES
-- (11, 1, 'Drums', false),
-- (14, 1, 'Drums', false),
-- (5, 1, 'Drums', false),
-- (2, 1, 'Drums', false),
-- (8, 1, 'Drums', false),


