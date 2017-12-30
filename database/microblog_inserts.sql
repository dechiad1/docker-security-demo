insert into users (username, passwd) values ('John', 'potato12');
insert into users (username, passwd) values ('Billy', 'starwars1');
insert into users (username, passwd) values ('Peter', 'yavin7');

insert into posts (body, timestamp, user_id) values ('Im really looking forward to christmas this year. I hope I get a new Lego set.',to_timestamp('21-12-2017 12:11:56','dd-mm-yyyy hh24:mi:ss'),1);
insert into posts (body, timestamp, user_id) values ('Best of luck to you sir. Let us know what you get!',to_timestamp('22-12-2017 02:00:02','dd-mm-yyyy hh24:mi:ss'),3);
insert into posts (body, timestamp, user_id) values ('I got the set I wanted! Its a Dinosaur adventure set.',to_timestamp('02-01-2018 08:10:00','dd-mm-yyyy hh24:mi:ss'),1);
insert into posts (body, timestamp, user_id) values ('Thats great John! You must have been a really good guy this year!',to_timestamp('04-01-2018 17:41:59','dd-mm-yyyy hh24:mi:ss'),2);
