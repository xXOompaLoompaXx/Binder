
--types

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


--entities

CREATE TABLE IF NOT EXISTS Users(
	pk serial not null PRIMARY KEY,
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


--relationships

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

CREATE TABLE IF NOT EXISTS Interested 
	(pk INTEGER,
	band_id INTEGER,
	PRIMARY KEY (band_id, pk),
	FOREIGN KEY (pk) REFERENCES Users(pk),
	FOREIGN KEY (band_id) REFERENCES Bands(band_id)
);


CREATE TABLE IF NOT EXISTS Contains 
	(pk INTEGER,
	band_id INTEGER,
	instrument varchar(50),
	PRIMARY KEY (band_id, pk),
	FOREIGN KEY (pk) REFERENCES Users(pk),
	FOREIGN KEY (band_id) REFERENCES Bands(band_id),
	FOREIGN KEY (instrument) REFERENCES Instruments(instrument)
);






