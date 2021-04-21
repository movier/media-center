"""empty message

Revision ID: 7c7185fe1b1d
Revises: cc3b99ef6f8a
Create Date: 2021-04-21 08:16:45.159541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c7185fe1b1d'
down_revision = 'cc3b99ef6f8a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('media', sa.Column('media_type', sa.Enum('video', 'photo', 'live_photo', name='mediatypeenum'), nullable=True))
    op.add_column('media', sa.Column('size', sa.Integer(), nullable=True))


def downgrade():
    with op.batch_alter_table('media') as batch_op:
      batch_op.drop_column('size')
      batch_op.drop_column('media_type')
