"""empty message

Revision ID: fcde8b794202
Revises: 5b120c2fed07
Create Date: 2019-01-14 04:12:16.262896

"""
from alembic import op
from benandfrank.models.keys import KeyAccess
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcde8b794202'
down_revision = '5b120c2fed07'
branch_labels = None
depends_on = None


def upgrade():
    key_localhost = KeyAccess()
    key_localhost.host = "localhost"
    key_localhost.key = "localhost"
    op.bulk_insert(
        KeyAccess.__table__,
        [
            {
                "id": 1,
                "host": key_localhost.host,
                "created": "",
                "updated": "",
                "_key": key_localhost.key
            }
        ]
    )


def downgrade():
    pass
