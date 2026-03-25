CREATE DATABASE IF NOT EXISTS audio_emailer;

USE audio_emailer;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(200) UNIQUE NOT NULL,
    password VARCHAR(500) NOT NULL,
    provider VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS preferences (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    voice VARCHAR(100),
    speed FLOAT,
    pause FLOAT,
    theme VARCHAR(20),

    CONSTRAINT fk_user_pref
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);
