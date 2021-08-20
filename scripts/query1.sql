create database  bank;
use bank;
show tables;
create table users(
SNO INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
CUSTOMER VARCHAR(50));
select * from users;
insert into users (SNO,ID,CUSTOMER)values('Rani');
insert into users (SNO,ID,CUSTOMER)values('Raja');
insert into users (SNO,ID,CUSTOMER)values('Mani');

