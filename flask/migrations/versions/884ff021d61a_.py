"""empty message

Revision ID: 884ff021d61a
Revises: 75c05af6efc3
Create Date: 2021-04-19 04:14:26.018275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '884ff021d61a'
down_revision = '75c05af6efc3'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('videos', 'media')
    op.rename_table('cast', 'people')
    op.rename_table('video_cast', 'media_people')
    op.alter_column('media_people', 'video_id', new_column_name='media_id')
    op.alter_column('media_people', 'cast_id', new_column_name='people_id')
    op.execute('CREATE INDEX ix_people_id ON people(id)')
    op.execute('CREATE UNIQUE INDEX ix_people_name ON people(name)')
    op.execute('CREATE INDEX ix_media_id ON media(id)')
    op.execute('CREATE INDEX ix_media_mtime ON media(mtime)')
    op.execute('CREATE INDEX ix_media_title ON media(title)')
    op.execute('DROP INDEX ix_cast_id')
    op.execute('DROP INDEX ix_cast_name')
    op.execute('DROP INDEX ix_videos_id')
    op.execute('DROP INDEX ix_videos_mtime')
    op.execute('DROP INDEX ix_videos_title')



def downgrade():
    op.rename_table('media', 'videos')
    op.rename_table('people', 'cast')
    op.rename_table('media_people', 'video_cast')
    op.alter_column('video_cast', 'media_id', new_column_name='video_id')
    op.alter_column('video_cast', 'people_id', new_column_name='cast_id')
    op.execute('CREATE INDEX ix_cast_id ON cast(id)')
    op.execute('CREATE UNIQUE INDEX ix_cast_name ON cast(name)')
    op.execute('CREATE INDEX ix_videos_id ON videos(id)')
    op.execute('CREATE INDEX ix_videos_mtime ON videos(mtime)')
    op.execute('CREATE INDEX ix_videos_title ON videos(title)')
    op.execute('DROP INDEX ix_people_id')
    op.execute('DROP INDEX ix_people_name')
    op.execute('DROP INDEX ix_media_id')
    op.execute('DROP INDEX ix_media_mtime')
    op.execute('DROP INDEX ix_media_title')
