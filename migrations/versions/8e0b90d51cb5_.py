"""empty message

Revision ID: 8e0b90d51cb5
Revises: c663b78fbaad
Create Date: 2022-07-20 13:44:05.077251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e0b90d51cb5'
down_revision = 'c663b78fbaad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('players', sa.Column('ties', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('players', 'ties')
    # ### end Alembic commands ###