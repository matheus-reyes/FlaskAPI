"""empty message

Revision ID: af6c58cca1dd
Revises: 8047ea9c4c19
Create Date: 2021-07-19 10:43:07.958652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af6c58cca1dd'
down_revision = '8047ea9c4c19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
