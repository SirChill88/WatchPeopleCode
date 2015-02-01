"""empty message

Revision ID: 34d183116728
Revises: 2f8bfdb8907a
Create Date: 2015-02-01 16:05:30.385282

"""

# revision identifiers, used by Alembic.
revision = '34d183116728'
down_revision = '2f8bfdb8907a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'stream_channel_key', 'stream', type_='unique')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(u'stream_channel_key', 'stream', ['channel'])
    ### end Alembic commands ###