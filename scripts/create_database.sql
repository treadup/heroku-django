CREATE DATABASE herokudjango;
CREATE USER herokudj WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE herokudjango TO herokudj;
ALTER ROLE herokudj SET client_encoding TO 'utf8';
ALTER ROLE herokudj SET default_transaction_isolation TO 'read committed';
ALTER ROLE herokudj SET TIMEZONE TO 'UTC';
