-- @block analysis the topic
SELECT DISTINCT QUERY
FROM PAPER;
-- @block create a record for filter record
CREATE TABLE TOPIC_RECORD (
    QUERY CHAR(100) PRIMARY KEY,
    FIRST_FILTER_LOG CHAR(20)
);
-- @block insert now existing topic
INSERT INTO TOPIC_RECORD (QUERY)
SELECT DISTINCT QUERY
FROM PAPER;
-- @block show insert state
SELECT *
FROM TOPIC_RECORD;
-- @block create a first_filter table
CREATE TABLE FIRST_FILTER (
    TITLE CHAR(100),
    COMMENT CHAR(100),
    FOREIGN KEY (TITLE) REFERENCES PAPER(TITLE)
);
-- @block (repeated) select one specific topic and get one  
SELECT *
FROM PAPER
WHERE QUERY = "mountain+torrents+loss+assessment";
-- @block (repeated) insert one into first filter
-- INSERT INTO FIRST_FILTER (TITLE, COMMENT)
-- VALUES("", "");
-- @block test the json import: failed and need extension for sqlite to deal
-- Declare @JSON varchar(max)
-- SELECT @JSON = BulkColumn
-- FROM OPENROWSET (BULK '../data/未命名.JSON', SINGLE_CLOB) as j;
-- @block (repeated) set the filter topic
UPDATE TOPIC_RECORD
SET FIRST_FILTER_LOG = "important"
WHERE QUERY = "mountain+torrents+loss+assessment";