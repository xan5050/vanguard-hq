/*
create database Vangaurd;
use Vangaurd;
*/
drop table if exists CardAssignment;
drop table if exists deck;
drop table if exists card;

-- Start of creating tables
create table deck(
deckid int primary key auto_increment,
Name varchar(60),
Des varchar(200)
);

create table card(
cardid int primary key auto_increment,
cardName varchar(60),
cardText varchar(200)
);

create table CardAssignment(
CardAssignmentID int primary key auto_increment,
deckid int,
cardid int,
foreign key(deckid) references deck(deckid),
foreign key(cardid) references card(cardid)
);
-- End of create all tables 

insert into deck(deckid, Name, Des)
values(1,'prison','control');

-- select * from deck;

-- select * from card;

insert into card(cardName, cardText) 
values('Muna','draw');


insert into CardAssignment(deckid, cardid)
values(1,1);
select * from CardAssignment;


