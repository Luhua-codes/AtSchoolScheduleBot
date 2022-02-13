# import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="at_school_schedule",
    ) as connection:
        # create_db_query = "CREATE DATABASE IF NOT EXISTS at_school_schedule"
        create_users_table_query = """
            CREATE TABLE user(
                id INT AUTO_INCREMENT PRIMARY KEY,
                discord_user_id BIGINT,
                monday BOOLEAN DEFAULT false,
                tuesday BOOLEAN DEFAULT false,
                wednesday BOOLEAN DEFAULT false,
                thursday BOOLEAN DEFAULT false,
                friday BOOLEAN DEFAULT false,
                mon_start_time_1 TIME DEFAULT NULL,
                mon_end_time_1 TIME DEFAULT NULL,
                mon_start_time_2 TIME DEFAULT NULL,
                mon_end_time_2 TIME DEFAULT NULL,
                mon_start_time_3 TIME DEFAULT NULL,
                mon_end_time_3 TIME DEFAULT NULL,
                tues_start_time_1 TIME DEFAULT NULL,
                tues_end_time_1 TIME DEFAULT NULL,
                tues_start_time_2 TIME DEFAULT NULL,
                tues_end_time_2 TIME DEFAULT NULL,
                tues_start_time_3 TIME DEFAULT NULL,
                tues_end_time_3 TIME DEFAULT NULL,
                wed_start_time_1 TIME DEFAULT NULL,
                wed_end_time_1 TIME DEFAULT NULL,
                wed_start_time_2 TIME DEFAULT NULL,
                wed_end_time_2 TIME DEFAULT NULL,
                wed_start_time_3 TIME DEFAULT NULL,
                wed_end_time_3 TIME DEFAULT NULL,
                thurs_start_time_1 TIME DEFAULT NULL,
                thurs_end_time_1 TIME DEFAULT NULL,
                thurs_start_time_2 TIME DEFAULT NULL,
                thurs_end_time_2 TIME DEFAULT NULL,
                thurs_start_time_3 TIME DEFAULT NULL,
                thurs_end_time_3 TIME DEFAULT NULL,
                fri_start_time_1 TIME DEFAULT NULL,
                fri_end_time_1 TIME DEFAULT NULL,
                fri_start_time_2 TIME DEFAULT NULL,
                fri_end_time_2 TIME DEFAULT NULL,
                fri_start_time_3 TIME DEFAULT NULL,
                fri_end_time_3 TIME DEFAULT NULL
            )
            """
        create_user_server_table_query = """
        CREATE TABLE user_servers(
            id INT AUTO_INCREMENT PRIMARY KEY,
            discord_user_id BIGINT,
            discord_server_id BIGINT
        )
        """
        with connection.cursor() as cursor:
            # cursor.execute(create_db_query)
            cursor.execute(create_users_table_query)
            cursor.execute(create_user_server_table_query)
            connection.commit()
except Error as e:
    print(e)
