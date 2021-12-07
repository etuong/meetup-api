    
DROP TABLE IF EXISTS event;

CREATE TABLE event
(
    event_id VARCHAR(100) NOT NULL,
    status VARCHAR(100) NULL,
    event_date VARCHAR(100) NULL,
    rsvp_count INTEGER NULL,
    venue_lat REAL NULL,
    venue_lon REAL NULL,
    venue_city VARCHAR(100) NULL,
    link VARCHAR(300) NULL,
    PRIMARY KEY (event_id)
);
