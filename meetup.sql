    
DROP TABLE IF EXISTS event;

CREATE TABLE event
(
    itemsID INTEGER NOT NULL,
    status VARCHAR(100) NULL,
    event_date VARCHAR(100) NULL,
    rsvp_count INTEGER NULL,
    PRIMARY KEY (itemsID)
);
