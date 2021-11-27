CREATE DATABASE IF NOT EXISTS blogs;
 
 USE blogs;

 CREATE TABLE IF NOT EXISTS posts (
	id INT PRIMARY KEY AUTO_INCREMENT,
    post_title VARCHAR(255) NOT NULL,
    post_detail VARCHAR(255),
    post_time DATETIME
    ) Engine=InnoDB AUTO_INCREMENT= 1;

INSERT INTO blogs.posts (post_title,post_detail,post_time)
VALUES ('Hong beo','New content','');