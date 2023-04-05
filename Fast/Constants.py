records="records"

album_query="""
            SELECT * FROM Album limit 10;
            """

user_auth_query="""
    SELECT * FROM USER_DETAIL where "UserID"='{username}' and "Pass"='{password}';
    """