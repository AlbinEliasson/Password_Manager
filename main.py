# This is a sample Python script.
import database


def main():
    connection = database.get_db_connection()

    with connection:
        cursor = database.get_cursor(connection)
        # database.drop_table(connection, cursor)
        database.create_table(connection, cursor)
        # database.insert_app_name_password(connection, cursor, "test", "password")
        # database.update_password(connection, cursor, "test", "notAPassword")
        # database.remove_app_name_password(connection, cursor, "test")
        database.show_table(cursor)


if __name__ == '__main__':
    main()
