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
