-- creates the database hbtn_0d_2 and the user user_0d_2

-- If the database hbtn_0d_2 already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;i

-- If the user user_0d_2 already exists, your script should not fail
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- The user_0d_2 password should be set to user_0d_2_pwd
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
