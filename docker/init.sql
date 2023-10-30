DROP TABLE IF EXISTS item,
user;

CREATE TABLE IF NOT EXISTS user(
    user_id int UNSIGNED NOT NULL AUTO_INCREMENT,
    email varchar(20) DEFAULT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE IF NOT EXISTS item(
    item_id int UNSIGNED NOT NULL AUTO_INCREMENT,
    title varchar(20) DEFAULT NULL,
    description varchar(20) DEFAULT NULL,
    user_id int UNSIGNED NOT NULL,
    PRIMARY KEY(item_id),
    FOREIGN KEY user_id(user_id) REFERENCES user(user_id)
);