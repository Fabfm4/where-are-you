from flask_rest_jsonapi.exceptions import ObjectNotFound
from flask_rest_jsonapi import ResourceDetail


class ResourceDetailMixin(ResourceDetail):

    def __init__(self):
        super(ResourceDetailMixin, self).__init__()

    def before_get_object(self, view_kwargs):
        print(self)
