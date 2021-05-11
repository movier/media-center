"""empty message

Revision ID: 9bc1259c228b
Revises: c9f95e57df4b
Create Date: 2021-05-11 03:12:24.710797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bc1259c228b'
down_revision = 'c9f95e57df4b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('android_release', sa.Column('download_url', sa.String(), nullable=True))

def downgrade():
    with op.batch_alter_table('android_release') as batch_op:
        batch_op.drop_column('download_url')
