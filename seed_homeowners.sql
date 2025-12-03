CREATE DATABASE IF NOT EXISTS home_insurance;
USE home_insurance;

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS rate_tables (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    description TEXT
);

CREATE TABLE IF NOT EXISTS rate_table_entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rate_table_id INT,
    key_low INT,
    key_high INT,
    multiplier DECIMAL(5,3),
    FOREIGN KEY(rate_table_id) REFERENCES rate_tables(id)
);

CREATE TABLE IF NOT EXISTS quotes (
    quote_id VARCHAR(50) PRIMARY KEY,
    request_json JSON,
    response_json JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS policies (
    policy_id VARCHAR(50) PRIMARY KEY,
    quote_id VARCHAR(50),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(quote_id) REFERENCES quotes(quote_id)
);

CREATE TABLE IF NOT EXISTS claims (
    claim_id VARCHAR(50) PRIMARY KEY,
    policy_id VARCHAR(50),
    amount DECIMAL(10,2),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(policy_id) REFERENCES policies(policy_id)
);

-- Seed example rate table
INSERT INTO rate_tables (name, description) VALUES ('home_basic', 'Basic Homeowners rate table');
INSERT INTO rate_table_entries (rate_table_id, key_low, key_high, multiplier)
VALUES (1, 0, 50, 1.0), (1, 51, 100, 1.2), (1, 101, 200, 1.5);
