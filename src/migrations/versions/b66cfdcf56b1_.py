"""empty message

Revision ID: b66cfdcf56b1
Revises: 79029ead276a
Create Date: 2018-06-20 22:03:54.038063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b66cfdcf56b1'
down_revision = '79029ead276a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('never_delete', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'never_delete')
    # ### end Alembic commands ###
