# User data models and indexes
class BaseIndex:
    pass

class UserIndex(BaseIndex):
    index_name = 'idx_user_email'
    fields = ['email', 'status']
