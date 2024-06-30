"""add Department

Revision ID: 891558a2d35c
Revises: d46aae540c48
Create Date: 2024-06-30 11:25:12.219229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '891558a2d35c'
down_revision = 'd46aae540c48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
