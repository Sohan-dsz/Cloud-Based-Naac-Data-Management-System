-- Initialize additional databases for different services

-- Create Keycloak database
SELECT 'CREATE DATABASE keycloak_db OWNER keycloak_user'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'keycloak_db')\gexec

-- Create Metabase database  
SELECT 'CREATE DATABASE metabase_db OWNER metabase_user'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'metabase_db')\gexec

-- Create users
CREATE USER IF NOT EXISTS keycloak_user WITH PASSWORD 'keycloak_password';
CREATE USER IF NOT EXISTS metabase_user WITH PASSWORD 'metabase_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE keycloak_db TO keycloak_user;
GRANT ALL PRIVILEGES ON DATABASE metabase_db TO metabase_user;