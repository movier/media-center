"""empty message

Revision ID: 3d7f78765af2
Revises: f7d22c46bb91
Create Date: 2021-04-29 08:24:53.666734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d7f78765af2'
down_revision = 'f7d22c46bb91'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('media', sa.Column('filename', sa.String(), nullable=True))


def downgrade():
    with op.batch_alter_table('media') as batch_op:
        batch_op.drop_column('filename')
