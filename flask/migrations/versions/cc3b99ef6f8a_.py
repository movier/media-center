"""empty message

Revision ID: cc3b99ef6f8a
Revises: 884ff021d61a
Create Date: 2021-04-21 05:32:06.358015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc3b99ef6f8a'
down_revision = '884ff021d61a'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('media', 'mtime', new_column_name='created_at')
    op.create_index(op.f('ix_media_created_at'), 'media', ['created_at'], unique=False)
    op.drop_index('ix_media_mtime', table_name='media')


def downgrade():
    op.alter_column('media', 'created_at', new_column_name='mtime')
    op.create_index('ix_media_mtime', 'media', ['mtime'], unique=False)
    op.drop_index(op.f('ix_media_created_at'), table_name='media')
