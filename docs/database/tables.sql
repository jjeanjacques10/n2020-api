-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2020-06-10 01:43:09.707

-- foreign keys
ALTER TABLE Dialog
    DROP CONSTRAINT Bot_messages_association_1;

ALTER TABLE Segments
    DROP CONSTRAINT Segments_Bot;

ALTER TABLE Suggestions
    DROP CONSTRAINT Suggestions_Types;

ALTER TABLE Dialog
    DROP CONSTRAINT User_messages_association_1;

ALTER TABLE Bot_messages
    DROP CONSTRAINT bot_message_bot;

ALTER TABLE User_messages
    DROP CONSTRAINT message_users;

-- tables
DROP TABLE Bot;

DROP TABLE Bot_messages;

DROP TABLE Categories;

DROP TABLE Dialog;

DROP TABLE Segments;

DROP TABLE Suggestions;

DROP TABLE User_messages;

DROP TABLE Users;

-- sequences
CALL DropSequence('Bot_messages_seq');

CALL DropSequence('Bot_seq');

CALL DropSequence('Categories_seq');

CALL  DropSequence('Segments_seq');

CALL DropSequence('Suggestions_seq');

CALL DropSequence('User_messages_seq');

CALL DropSequence('Users_seq');

-- End of file.


-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2020-06-10 01:43:09.707

-- tables
-- Table: Bot
CREATE TABLE Bot (
    id integer  NOT NULL,
    name varchar(255)  NOT NULL,
    welcome_message varchar(255)  NOT NULL,
    farewell_message varchar(255)  NOT NULL,
    downtime integer  NOT NULL,
    default_answer varchar(255)  NOT NULL,
    CONSTRAINT Bot_pk PRIMARY KEY (id)
);

-- Table: Bot_messages
CREATE TABLE Bot_messages (
    id integer  NOT NULL,
    content varchar(255)  NOT NULL,
    time datetime(6)  NOT NULL,
    Bot_id integer  NOT NULL,
    CONSTRAINT Bot_messages_pk PRIMARY KEY (id)
);

-- Table: Categories
CREATE TABLE Categories (
    id integer  NOT NULL,
    title varchar(255)  NOT NULL,
    CONSTRAINT Categories_pk PRIMARY KEY (id)
);

-- Table: Dialog
CREATE TABLE Dialog (
    User_messages_id integer  NOT NULL,
    Bot_messages_id integer  NOT NULL
);

-- Table: Segments
CREATE TABLE Segments (
    id integer  NOT NULL,
    name varchar(255)  NOT NULL,
    Bot_id integer  NOT NULL,
    CONSTRAINT Segments_pk PRIMARY KEY (id)
);

-- Table: Suggestions
CREATE TABLE Suggestions (
    id integer  NOT NULL,
    title varchar(255)  NOT NULL,
    type integer  NOT NULL,
    description varchar(1000)  NOT NULL,
    url Varchar(500)  NOT NULL,
    image_url varchar(500)  NOT NULL,
    Categories_id integer  NOT NULL,
    CONSTRAINT Suggestions_pk PRIMARY KEY (id)
);

-- Table: User_messages
CREATE TABLE User_messages (
    id integer  NOT NULL,
    content varchar(255)  NOT NULL,
    time datetime(6)  NOT NULL,
    Users_id integer  NOT NULL,
    CONSTRAINT User_messages_pk PRIMARY KEY (id)
);

-- Table: Users
CREATE TABLE Users (
    id integer  NOT NULL,
    photo_url varchar(1000)  NOT NULL,
    name varchar(255)  NOT NULL,
    phone varchar(15)  NOT NULL,
    email varchar(320)  NOT NULL,
    password varchar(20)  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: Bot_messages_association_1 (table: Dialog)
ALTER TABLE Dialog ADD CONSTRAINT Bot_messages_association_1
    FOREIGN KEY (Bot_messages_id)
    REFERENCES Bot_messages (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Segments_Bot (table: Segments)
ALTER TABLE Segments ADD CONSTRAINT Segments_Bot
    FOREIGN KEY (Bot_id)
    REFERENCES Bot (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Suggestions_Types (table: Suggestions)
ALTER TABLE Suggestions ADD CONSTRAINT Suggestions_Types
    FOREIGN KEY (Categories_id)
    REFERENCES Categories (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: User_messages_association_1 (table: Dialog)
ALTER TABLE Dialog ADD CONSTRAINT User_messages_association_1
    FOREIGN KEY (User_messages_id)
    REFERENCES User_messages (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: bot_message_bot (table: Bot_messages)
ALTER TABLE Bot_messages ADD CONSTRAINT bot_message_bot
    FOREIGN KEY (Bot_id)
    REFERENCES Bot (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: message_users (table: User_messages)
ALTER TABLE User_messages ADD CONSTRAINT message_users
    FOREIGN KEY (Users_id)
    REFERENCES Users (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- sequences
-- Sequence: Bot_messages_seq
CALL CreateSequence('Bot_messages_seq', 1, 1)
      NOMINVALUE
      NOMAXVALUE
      START WITH 1
      NOCYCLE
;

-- Sequence: Bot_seq
CALL CreateSequence('Bot_seq', 1, 1)
      NOMINVALUE
      NOMAXVALUE
      START WITH 1
      NOCYCLE
;

-- Sequence: Categories_seq
CALL CreateSequence('Categories_seq', 1, 1)
      NOMINVALUE
      NOMAXVALUE
      START WITH 1
      NOCYCLE
;

-- Sequence: Segments_seq
CALL CreateSequence('Segments_seq', 1, 1)
      NOMINVALUE
      NOMAXVALUE
      START WITH 1
      NOCYCLE
;

-- Sequence: Suggestions_seq
CALL CreateSequence('Suggestions_seq', 1, 1)
      NOMINVALUE
      NOMAXVALUE
      START WITH 1
      NOCYCLE
;

-- Sequence: User_messages_seq
CALL CreateSequence('User_messages_seq', 1, 1)
      NOMINVALUE
      NOMAXVALUE
      START WITH 1
      NOCYCLE
;

-- Sequence: Users_seq
CALL CreateSequence('Users_seq', 1, 1)
      NOMINVALUE
      NOMAXVALUE
      START WITH 1
      NOCYCLE
;

-- End of file.

