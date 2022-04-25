CREATE TABLE media (
    id int,
    media_type varchar(10),
    name varchar(255),
    short_name varchar(255),
    long_description text,
    short_description text,
    created_at timestamp,
    updated_at timestamp,
    review_url varchar(255),
    review_score float,
    slug varchar(255),
    genres text[],
    created_by text[],
    published_by text[],
    franchises text[],
    regions text[]
);