-- Creates the user user_0d_1 if it doesn't exist and grants specific privileges.
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';

-- Only grant the necessary privileges. Modify this list based on your actual requirements.
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ... -- Add other needed privileges here
   ON *.*
   TO 'user_0d_1'@'localhost'
   IDENTIFIED BY 'user_0d_1_pwd';

FLUSH PRIVILEGES;
