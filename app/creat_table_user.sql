DROP TABLE IF EXISTS users;

CREATE TABLE users (
                Id integer PRIMARY KEY AUTOINCREMENT,
                username varchar(50),
                password varchar(50),
                `role` varchar(50)
                  )
