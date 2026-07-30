CREATE TABLE IF NOT EXISTS accounts (
	userid integer NOT NULL,
	username varchar NOT NULL,
	password varchar NOT NULL,
	email varchar NOT NULL,
	PRIMARY KEY (userid)
);

CREATE TABLE IF NOT EXISTS reviews (
	reviewid integer NOT NULL,
	album_name varchar NOT NULL,
	artist_name varchar NOT NULL,
	rating integer NOT NULL,
	review_text varchar NOT NULL,
	PRIMARY KEY (reviewid)
);

INSERT INTO customers (reviewid, album_name, artist_name, rating, review_text) VALUES
	(1, 'I Against I', 'Bad Brains', 10, "Bad Brains at their best."),
	(2, 'RAT WARS', 'HEALTH', 7, "The best of their Neo-Industrial efforts.")
  ;
