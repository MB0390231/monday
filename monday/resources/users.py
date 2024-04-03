from monday.monday.query_joins import get_users_query
from monday.monday.resources.base import BaseResource


class UserResource(BaseResource):
    def fetch_users(self, **kwargs):
        query = get_users_query(**kwargs)
        return self.client.execute(query)
