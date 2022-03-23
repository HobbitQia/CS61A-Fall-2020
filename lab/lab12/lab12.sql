.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students 
      where color = "blue" and pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students 
      where color = "blue" and pet = "dog";


CREATE TABLE smallest_int AS
  SELECT time, smallest from students where smallest > 2 order by smallest limit 20;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color , b.color
      from students as a, students as b
          where a.song = b.song and a.pet = b.pet and a.time < b.time;


CREATE TABLE sevens AS
  SELECT a.seven
      from students as a, numbers as b
          where a.number = 7 and b.'7' = 'True' and a.time = b.time;

