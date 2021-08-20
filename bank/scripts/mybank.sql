create database  mybank;
use mybank;
show tables;
create table user(
SNo int NOT NULL AUTO_INCREMENT PRIMARY KEY ,
Mailid varchar(255),
CUSTOMER VARCHAR(50));
SELECT*FROM user;
insert into user(Mailid,CUSTOMER)values('abc123@gmail.com','Raja');
create table transaction(transfer_id int AUTO_INCREMENT PRIMARY KEY,
  Date_Time DATETIME);
SELECT * FROM transaction;