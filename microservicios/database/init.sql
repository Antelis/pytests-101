-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS equation_db;

-- Use the database
USE equation_db;

-- Create the results table if it doesn't exist
CREATE TABLE IF NOT EXISTS equation_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    a FLOAT NOT NULL,
    b FLOAT NOT NULL,
    c FLOAT NOT NULL,
    d FLOAT NOT NULL,
    result FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);