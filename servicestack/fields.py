from servicestack.utils import to_bytearray, from_bytearray
import marshmallow.fields as mf


class Bytes(mf.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return to_bytearray(value)

    def _deserialize(self, value, attr, data, **kwargs):
        return from_bytearray(value)
