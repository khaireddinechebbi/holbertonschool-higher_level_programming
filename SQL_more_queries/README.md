# SQL - More Queries

## Description
This project focuses on mastering advanced SQL queries. It includes tasks related to user management, table creation, privileges management, and query operations such as joins, subqueries, and union operations.

The tasks will help you understand how to interact with databases, create and manage users, enforce constraints, and perform complex queries across multiple tables.

## Files

| Filename | Description |
|----------|------------|
| `0-privileges.sql` | Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the server. |
| `1-create_user.sql` | Creates the MySQL server user user_0d_1 with all privileges and sets the password to user_0d_1_pwd. |
| `2-create_read_user.sql` | Creates the database hbtn_0d_2 and user user_0d_2, with only SELECT privilege on the database. Sets the password to user_0d_2_pwd. |
| `3-force_name.sql` | Creates a table force_name with columns id (INT) and name (VARCHAR(256), NOT NULL). If the table already exists, the script will not fail. |
| `4-never_empty.sql` | Creates a table id_not_null with columns id (default value 1) and name (VARCHAR(256)). |
| `5-unique_id.sql` | Creates a table unique_id with a unique id (default value 1) and name (VARCHAR(256)). |
| `6-states.sql` | Creates a database hbtn_0d_usa and a states table with id (unique, primary key) and name. |
| `7-cities.sql` | Creates a database hbtn_0d_usa and a cities table with id (unique, primary key), state_id (foreign key), and name. |
| `8-cities_of_california_subquery.sql` | Lists cities in California from the hbtn_0d_usa database without using JOIN. |
| `9-cities_by_state_join.sql` | Lists all cities in hbtn_0d_usa with the corresponding state name using a JOIN. |
| `10-genre_id_by_show.sql` | Lists shows from hbtn_0d_tvshows that have at least one genre linked, sorted by title and genre ID. |
| `11-genre_id_all_shows.sql` | Lists all shows from hbtn_0d_tvshows, including NULL for shows without genres, sorted by title and genre ID. |
| `12-no_genre.sql` | Lists all shows in hbtn_0d_tvshows without a genre linked, sorted by title and genre_id. |
| `13-count_shows_by_genre.sql` | Lists all genres in hbtn_0d_tvshows and displays the number of shows linked to each genre, sorted by the number of shows. |
| `14-my_genres.sql` | Lists all genres of the show Dexter from the hbtn_0d_tvshows database, sorted by genre name. |
| `15-comedy_only.sql` | Lists all Comedy shows in the hbtn_0d_tvshows database, sorted by show title. |
| `16-shows_by_genre.sql` | Lists all shows and their linked genres from the hbtn_0d_tvshows database, sorted by show title and genre name. |