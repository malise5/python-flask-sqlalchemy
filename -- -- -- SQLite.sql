-- -- -- SQLite
-- DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS pets;

-- -- CREATE TABLE owners 
-- CREATE TABLE owners (
--     id INTEGER PRIMARY KEY,
--     name TEXT,
--     address TEXT,
--     phone TEXT,
--     email TEXT
-- );

CREATE TABLE pets (
    id INTEGER PRIMARY KEY,
    name TEXT,
    owner_id INTEGER,
    age INTEGER,
    breed TEXT,
    favorite_food TEXT,
    last_fed_at DATETIME,
    last_walked_at DATETIME,
    FOREIGN KEY (owner_id) REFERENCES owners(id)
);


-- INSERT INTO owners (name, address, phone, email) VALUES
-- ('John Doe', '123 Elm St', '555-1234', 'joe@gmail.com'),
-- ('Jane Smith', '456 Oak St', '555-5678','jane@gmail.com'),
-- ('Alice Johnson', '789 Pine St', '555-8765','alice@gmail.com');

-- ALTER TABLE pets ADD COLUMN image_url TEXT;
-- INSERT INTO pets (name, owner_id, age, breed, favorite_food, last_fed_at, last_walked_at, image_url) VALUES
-- ('Buddy', 1, 3, 'Golden Retriever', 'Chicken', '2023-10-01 08:00:00', '2023-10-01 09:00:00', 'https://example.com/buddy.jpg'),
-- ('Mittens', 2, 2, 'Siamese', 'Fish', '2023-10-01 08:30:00', '2023-10-01 09:30:00', 'https://example.com/mittens.jpg'),
-- ('Charlie', 3, 5, 'Beagle', 'Beef', '2023-10-01 09:00:00', '2023-10-01 10:00:00', 'https://example.com/charlie.jpg');

-- INSERT INTO pets (name, owner_id, age, breed, favorite_food, last_fed_at, last_walked_at, image_url) VALUES
-- ('Max', 1, 4, 'Labrador', 'Chicken', '2023-10-01 08:00:00', '2023-10-01 09:00:00', 'https://example.com/max.jpg'),
-- ('Bella', 2, 1, 'Bulldog', 'Beef', '2023-10-01 08:30:00', '2023-10-01 09:30:00', 'https://example.com/bella.jpg'),
-- ('Lucy', 3, 6, 'Poodle', 'Fish', '2023-10-01 09:00:00', '2023-10-01 10:00:00', 'https://example.com/lucy.jpg');


-- CRUD operations
-- SELECT * FROM pets;
-- SELECT * FROM pets WHERE owner_id = 1;
-- SELECT * FROM pets WHERE age > 2;
-- SELECT * FROM pets WHERE favorite_food = 'Chicken';
-- SELECT * FROM pets WHERE last_fed_at > '2023-10-01 08:00:00';

-- one to many
SELECT owners.name, pets.name as 'pet name' FROM owners
JOIN pets ON owners.id = pets.owner_id;

-- many to many
-- CREATE TABLE handlers (
--     id INTEGER PRIMARY KEY,
--     name TEXT,
--     phone TEXT,
--     email TEXT
-- );

-- CREATE TABLE appointments (
--     id INTEGER PRIMARY KEY,
--     pet_id INTEGER,
--     handler_id INTEGER,
--     appointment_time DATETIME,
--     FOREIGN KEY (pet_id) REFERENCES pets(id),
--     FOREIGN KEY (handler_id) REFERENCES handlers(id)
-- );

-- INSERT INTO handlers (name, phone, email) VALUES
-- ('Dr. Smith', '555-1111', 'smith@gmail.com'),
-- ('Dr. Brown', '555-2222', 'Brown@gmail.com'),
-- ('Dr. Green', '555-3333', 'Green@gmail.com');


-- INSERT INTO appointments (pet_id, handler_id, appointment_time) VALUES
-- (1, 1, '2023-10-01 10:00:00'),
-- (2, 2, '2023-10-01 11:00:00'),
-- (3, 3, '2023-10-01 12:00:00');

-- SELECT pets.name, handlers.name as 'handler name' FROM pets
-- JOIN appointments ON pets.id = appointments.pet_id
-- JOIN handlers ON appointments.handler_id = handlers.id;

SELECT 
    pets.name AS pet_name,
    handlers.name AS handler_name,
    appointments.appointment_time
FROM appointments
JOIN pets  
    ON appointments.pet_id = pets.id
JOIN handlers 
    ON appointments.handler_id = handlers.id

