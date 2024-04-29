# Saifertek Backend Task

## Screenshots

![Code Screenshot](/1.png)
*Code screenshot*

![Table Relations Screenshot](/2.png)
*Postgresql table relations*

![Output Terminal Screenshot](/3.png)
*Output terminal in VS Code*

## Description

This project connects to a PostgreSQL database using Python's psycopg2 library and performs two queries: one with JOIN and one without JOIN.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/your_project.git
    ```

2. Install psycopg2:

    ```bash
    pip install psycopg2
    ```

3. Update the database connection details in the script (`main.py`).

## Usage

Run the script `main.py` to execute the queries against the PostgreSQL database.

```bash
python q1.py
```

## Query with JOIN

```SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name
FROM locations l
JOIN countries c ON l.country_id = c.country_id
WHERE c.country_name = 'Canada'
```

## Query without JOIN

```
SELECT location_id, street_address, city, state_province, 
    (SELECT country_name FROM countries WHERE countries.country_id = locations.country_id) AS country_name
FROM locations
WHERE country_id = 'CA'
```

## Created By

![RAJGOPAL HOTA](https://rajgopal.in/static/media/about-img.d52ae63dfacf96e6cb6b.jpg)

Created by RAJGOPAL HOTA
