import sqlite3

def transfer_user_data(source_db_path, target_db_path):
    # Connect to the source database
    source_conn = sqlite3.connect(source_db_path)
    source_cursor = source_conn.cursor()

    # Connect to the target database
    target_conn = sqlite3.connect(target_db_path)
    target_cursor = target_conn.cursor()

    # Ensure the target 'user' table exists and has the same structure as the source
    target_cursor.execute("""
    CREATE TABLE IF NOT EXISTS auth_user (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        password VARCHAR(128) NOT NULL,
        last_login DATETIME NULL,
        is_superuser BOOLEAN NOT NULL,
        username VARCHAR(150) NOT NULL UNIQUE,
        last_name VARCHAR(150) NOT NULL,
        email VARCHAR(254) NOT NULL,
        is_staff BOOLEAN NOT NULL,
        is_active BOOLEAN NOT NULL,
        date_joined DATETIME NOT NULL,
        first_name VARCHAR(150) NOT NULL
    );
    """)

    # Fetch data from the source 'auth_user' table
    source_cursor.execute("SELECT * FROM auth_user")
    users = source_cursor.fetchall()

    # Insert data into the target 'auth_user' table
    target_cursor.executemany("""
    INSERT INTO auth_user (id, password, last_login, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, users)

    # Commit changes and close connections
    target_conn.commit()
    source_conn.close()
    target_conn.close()

# Paths to your databases
source_db_path = '.\\db2.sqlite3'  # Adjust path for Windows path conventions
target_db_path = '.\\db.sqlite3'  # Adjust path for Windows path conventions

# Call the function to transfer data
transfer_user_data(source_db_path, target_db_path)
