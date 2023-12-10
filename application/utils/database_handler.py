from application.database_operations import DatabaseOperations

DATABASE_HANDLE = DatabaseOperations()


def get_handle():
    return DATABASE_HANDLE
