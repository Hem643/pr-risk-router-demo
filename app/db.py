# User query service
def search_user(email: str):
    # DANGEROUS: Concatenation allows SQL injection
    query = "SELECT * FROM users WHERE email = '" + email + "'"
    return query
