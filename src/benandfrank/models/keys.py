from ..models import db, TimeStampedMixin

from ..core.db.models.models import hybrid_property
from ..core.db.models import bcrypt


class KeyAccess(TimeStampedMixin, db.Model):

    host = db.Column(db.String(30))
    _key = db.Column(db.String(100))

    @hybrid_property
    def key(self):
        return self._key

    @key.setter
    def key(self, plaintext):
        self._key = bcrypt.generate_password_hash(plaintext)
