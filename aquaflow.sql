CREATE DATABASE aquaflow_db;
USE aquaflow_db;

CREATE TABLE sensores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ph DECIMAL(4,2),
    turbidez DECIMAL(5,2)
);

USE aquaflow_db;
SHOW TABLES;

USE aquaflow_db;
SELECT * FROM sensores;

USE aquaflow_db;

SHOW TABLES;

SELECT * FROM sensores ORDER BY fecha DESC LIMIT 5;




