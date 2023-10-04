create table anniversary (
    aid integer primary key autoincrement,
    aname text not null,
    adate text not null,
    is_holiday int not null, 
    uid text not null
);
