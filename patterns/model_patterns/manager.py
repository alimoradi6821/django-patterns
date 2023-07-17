from django.db.models.query import QuerySet
#############################
from django.db.models import Q
# for union or integration or differance two query-set
#############################
class PostQuerySet(QuerySet):

    def public_posts(self):
        return self.filter(privacy="public")

PostManager = PostQuerySet.as_manager