CREATE TABLE athletes (
    id bigserial primary key,
    name varchar(200) not null,
    email varchar(100) not null,
    country varchar(200) null
);
