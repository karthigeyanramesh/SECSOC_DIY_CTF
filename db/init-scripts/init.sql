CREATE TABLE IF NOT EXISTS emails (
    email VARCHAR(50),
    date_joined VARCHAR(50),
    subscription_period VARCHAR(50),
    subscription_type VARCHAR(50),
    subscription_method VARCHAR(50)
);

USE mysql;

CREATE TABLE IF NOT EXISTS flag (
    flags VARCHAR(50)
);

INSERT INTO flag(flags) VALUES ("SECSOC{Th1s_1s_flAg}");

CREATE USER 'jig'@'%' IDENTIFIED BY 'noooo';

GRANT SELECT ON *.* TO 'jig'@'%' IDENTIFIED BY 'noooo';

FLUSH PRIVILEGES;
