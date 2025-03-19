# Python - Object-Relational Mapping (ORM)

## Description
This project explores Object-Relational Mapping (ORM) using **MySQLdb** and **SQLAlchemy** in Python. It focuses on interacting with a MySQL database through Python scripts without directly writing SQL queries.

## Files

| File Name                  | Description |
|----------------------------|-------------|
| `0-select_states.py`       | Retrieves all states from the database and prints them. |
| `1-filter_states.py`       | Lists all states that start with 'N'. |
| `2-my_filter_states.py`    | Filters states based on user input (risk of SQL injection). |
| `3-my_safe_filter_states.py` | Secure version of `2-my_filter_states.py` using parameterized queries. |
| `4-cities_by_state.py`     | Lists all cities along with their state names. |
| `5-filter_cities.py`       | Filters cities based on state input. |
| `model_state.py`           | Defines the SQLAlchemy ORM model for the `states` table. |
| `7-model_state_fetch_all.py` | Lists all State objects using SQLAlchemy. |
| `8-model_state_fetch_first.py` | Retrieves the first State object using SQLAlchemy. |
| `9-model_state_filter_a.py` | Filters State objects that contain the letter 'a'. |
| `10-model_state_update_id_2.py` | Updates a specific State object in the database. |
| `11-model_state_insert.py` | Inserts a new State object into the database. |
| `12-model_state_delete.py` | Deletes State objects containing the letter 'a'. |
| `13-model_state_delete_a.py` | Deletes all State objects with a name containing 'a' using SQLAlchemy. |
| `model_city.py` | Defines the SQLAlchemy ORM model for the `cities` table. |
| `14-model_city_fetch_by_state.py` | Lists all City objects with their corresponding state names using SQLAlchemy. |
