"""empty message

Revision ID: a49152c399b1
Revises: b66cfdcf56b1
Create Date: 2018-06-20 22:04:08.184262

"""
from alembic import op
from whereareyou.models.users import MatrixProfile, Permission, Profile
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a49152c399b1'
down_revision = 'b66cfdcf56b1'
branch_labels = None
depends_on = None


def upgrade():

    op.bulk_insert(
        Permission.__table__,
        [
            {
                'id': 1,
                'name': 'users',
                'description': 'User model',
                'is_active': True,
                'never_delete': True,
                'is_crud': True
            }
        ],
        multiinsert=False
    )
    op.bulk_insert(
        Profile.__table__,
        [
            {
                'id': 1,
                'name': 'admin',
                'is_active': True,
                'never_delete': True
            },
            {
                'id': 2,
                'name': 'app',
                'is_active': True,
                'never_delete': True
            }
        ],
        multiinsert=False
    )
    op.bulk_insert(
        MatrixProfile.__table__,
        [
            {
                'profile_id': 1,
                'permission_id': 1,
                'can_edit': True,
                'can_view': True,
                'can_create': True,
                'can_delete': True
            }
        ],
        multiinsert=False
    )


def downgrade():
    pass
