from marshmallow.fields import Nested, missing_


class NestedCustom(Nested):
    def __init__(self, nested, default=missing_, exclude=tuple(), only=None, **kwargs):
        if 'model' in kwargs:
            self.model = kwargs['model']
        super(NestedCustom, self).__init__(nested, default=default, exclude=exclude, only=only, **kwargs)

    def _serialize(self, nested_obj, attr, obj):
        if type(nested_obj) == int:
            object = self.model.query.filter_by(id=int(nested_obj)).first()
            return super(NestedCustom, self)._serialize(object, attr, obj)

        return super(NestedCustom, self)._serialize(nested_obj, attr, obj)
