-- Insert data into Instruments
INSERT INTO Instruments (instrument) VALUES
('Guitar'),
('Drums'),
('Bass'),
('Keyboard'),
('Vocals'),
('Violin'),
('Trumpet'),
('Saxophone'),
('Flute'),
('Cello'),
('Harp'),
('Clarinet'),
('Double Bass'),
('Trombone'),
('Synthesizer');

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
INSERT INTO Bands (band_id, band_name, band_genre, band_state, creation_date) VALUES
(1, 'The Rockers', 'Rock', 0, '2024-06-01'),
(2, 'Jazz Masters', 'Jazz', 1, '2024-06-02'),
(3, 'Pop Stars', 'Pop', 2, '2024-06-03'),
(4, 'Classical Ensemble', 'Classical', 1, '2024-06-04'),
(5, 'Hip Hop Crew', 'Hip Hop', 0, '2024-06-05'),
(6, 'Fusion Collective', 'Jazz', 0, '2024-06-06'),
(7, 'Symphony Strings', 'Classical', 1, '2024-06-07'),
(8, 'Electric Vibes', 'Pop', 0, '2024-06-08'),
(9, 'Rhythm Riders', 'Rock', 1, '2024-06-09'),
(10, 'Beats and Rhymes', 'Hip Hop', 2, '2024-06-10');

-- Insert data into Plays
INSERT INTO Plays (pk, instrument, proficiency) VALUES
(1, 'Guitar', 8),
(2, 'Drums', 7),
(3, 'Bass', 6),
(4, 'Keyboard', 9),
(5, 'Vocals', 7),
(6, 'Violin', 8),
(7, 'Trumpet', 6),
(8, 'Saxophone', 7),
(9, 'Flute', 5),
(10, 'Cello', 8),
(11, 'Guitar', 7),
(12, 'Drums', 8),
(13, 'Bass', 7),
(14, 'Keyboard', 6),
(15, 'Vocals', 9);

-- Insert data into Typical_Instruments
INSERT INTO Typical_Instruments (instrument, genre) VALUES
('Guitar', 'Rock'),
('Drums', 'Rock'),
('Bass', 'Rock'),
('Keyboard', 'Jazz'),
('Saxophone', 'Jazz'),
('Trumpet', 'Jazz'),
('Vocals', 'Pop'),
('Synthesizer', 'Pop'),
('Drums', 'Pop'),
('Violin', 'Classical'),
('Cello', 'Classical'),
('Flute', 'Classical'),
('Vocals', 'Hip Hop'),
('Synthesizer', 'Hip Hop'),
('Drums', 'Hip Hop');

-- Insert data into Prefers_Genre
INSERT INTO Prefers_Genre (pk, genre) VALUES
(1, 'Rock'),
(2, 'Jazz'),
(3, 'Pop'),
(4, 'Classical'),
(5, 'Hip Hop'),
(6, 'Classical'),
(7, 'Rock'),
(8, 'Jazz'),
(9, 'Hip Hop'),
(10, 'Pop'),
(11, 'Rock'),
(12, 'Jazz'),
(13, 'Pop'),
(14, 'Classical'),
(15, 'Hip Hop');

-- Insert more data into Band_contains
INSERT INTO Band_contains (pk, band_id, instrument, interested) VALUES
(1, 1, 'Guitar', false),
(2, 2, 'Drums', true),
(3, 3, 'Bass', false),
(4, 4, 'Keyboard', true),
(5, 5, 'Vocals', true),
(6, 1, 'Violin', false),
(7, 2, 'Trumpet', true),
(8, 3, 'Saxophone', false),
(9, 4, 'Flute', true),
(10, 5, 'Cello', true),
(11, 6, 'Guitar', true),
(12, 7, 'Drums', true),
(13, 8, 'Bass', false),
(14, 9, 'Keyboard', true),
(15, 10, 'Vocals', true),
(1, 6, 'Guitar', true),
(2, 7, 'Drums', true),
(3, 8, 'Bass', true),
(4, 9, 'Keyboard', true),
(5, 10, 'Vocals', false),
(2, 1, 'Drums', true),
(3, 1, 'Bass', true),
(11, 1, 'Synthesizer', true),
(4, 2, 'Keyboard', true),
(5, 2, 'Vocals', false),
(12, 2, 'Saxophone', true),
(6, 3, 'Violin', true),
(7, 3, 'Trumpet', true),
(14, 3, 'Synthesizer', true),
(8, 4, 'Saxophone', true),
(13, 4, 'Cello', true),
(12, 5, 'Clarinet', false),
(15, 5, 'Synthesizer', true),
(7, 6, 'Saxophone', true),
(9, 6, 'Flute', true),
(13, 6, 'Cello', true),
(8, 7, 'Drums', false),
(10, 7, 'Harp', true),
(14, 7, 'Synthesizer', true),
(11, 8, 'Guitar', true),
(12, 8, 'Drums', true),
(15, 8, 'Vocals', true),
(6, 9, 'Trumpet', false),
(13, 9, 'Bass', true),
(15, 9, 'Vocals', true),
(1, 10, 'Guitar', true),
(3, 10, 'Saxophone', true),
(4, 10, 'Keyboard', false);
