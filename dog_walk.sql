-- Create a table named 'dog_walks'
CREATE TABLE dog_walks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dog_name TEXT NOT NULL,
    walk_date DATE NOT NULL,
    duration_minutes INTEGER NOT NULL
);

-- Insert sample data into the 'dog_walks' table
INSERT INTO dog_walks (dog_name, walk_date, duration_minutes) VALUES
('Buddy', '2023-10-01', 30),
('Max', '2023-10-02', 45),
('Bella', '2023-10-03', 60);