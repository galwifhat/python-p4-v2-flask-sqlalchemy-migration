"""rename address

Revision ID: 727c4010430d
Revises: 0b56a6db5d8d
Create Date: 2025-06-14 04:07:34.607254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '727c4010430d'
down_revision = '0b56a6db5d8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('departments', sa.Column('location', sa.String(), nullable=False))
    # op.drop_column('departments', 'address')
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('departments', sa.Column('address', sa.VARCHAR(), nullable=True))
    # op.drop_column('departments', 'location')
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
