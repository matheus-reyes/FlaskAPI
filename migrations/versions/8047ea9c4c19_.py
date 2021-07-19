"""empty message

Revision ID: 8047ea9c4c19
Revises: 9b6b297a7d88
Create Date: 2021-07-19 10:38:09.920151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8047ea9c4c19'
down_revision = '9b6b297a7d88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('game_name_key', 'game', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('game_name_key', 'game', ['name'])
    # ### end Alembic commands ###