# -*- coding: utf-8 -*-
from flask_rest_jsonapi.exceptions import ObjectNotFound


class ResourceDetailMixin(object):

    def before_get_object(self, values_kwargs):
        pk = values_kwargs.get('id')
        object_model = self.model.query.filter_by(id=pk)
        if not object_model:
            raise ObjectNotFound('detail')

        return object_model
