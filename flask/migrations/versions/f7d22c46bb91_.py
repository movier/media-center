"""empty message

Revision ID: f7d22c46bb91
Revises: cbae8101e30e
Create Date: 2021-04-22 04:24:48.898250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7d22c46bb91'
down_revision = 'cbae8101e30e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('media', sa.Column('datetime', sa.DateTime(), nullable=True))
    op.add_column('media', sa.Column('duration', sa.Float(), nullable=True))
    op.create_index(op.f('ix_media_datetime'), 'media', ['datetime'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_media_datetime'), table_name='media')
    with op.batch_alter_table('media') as batch_op:
      batch_op.drop_column('duration')
      batch_op.drop_column('datetime')
    
