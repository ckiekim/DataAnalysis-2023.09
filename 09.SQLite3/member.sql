# SQLite3

create table member (
    mid integer primary key autoincrement,
    name text not null,
    age int default 20
);

insert into member(name, age) values
    ('james', 25), ('maria', 23), ('tommy', 19), ('emma', 27);
