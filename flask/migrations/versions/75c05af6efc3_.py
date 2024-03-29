"""empty message

Revision ID: 75c05af6efc3
Revises: e4a47fe24cfe
Create Date: 2020-01-22 07:56:52.999975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75c05af6efc3'
down_revision = 'e4a47fe24cfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cast',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cast_id'), 'cast', ['id'], unique=False)
    op.create_index(op.f('ix_cast_name'), 'cast', ['name'], unique=True)
    op.create_table('video_cast',
    sa.Column('video_id', sa.Integer(), nullable=True),
    sa.Column('cast_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cast_id'], ['cast.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['videos.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video_cast')
    op.drop_index(op.f('ix_cast_name'), table_name='cast')
    op.drop_index(op.f('ix_cast_id'), table_name='cast')
    op.drop_table('cast')
    # ### end Alembic commands ###
