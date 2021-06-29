CREATE TABLE user (
    id INTERGER PRIMARY KEY AUTOINCREMENT
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    hobbies TEXT,
    active BOOLEN DEFAULT 0);
