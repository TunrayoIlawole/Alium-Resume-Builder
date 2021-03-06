"""empty message

Revision ID: 64f19339c2c2
Revises: a14582cc8951
Create Date: 2020-09-25 22:39:38.386388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64f19339c2c2'
down_revision = 'a14582cc8951'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('education', sa.Column('location', sa.String(), nullable=True))
    op.add_column('user', sa.Column('city', sa.String(), nullable=True))
    op.add_column('user', sa.Column('country', sa.String(), nullable=True))
    op.add_column('user', sa.Column('current_occupation', sa.String(), nullable=True))
    op.add_column('user', sa.Column('state', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'state')
    op.drop_column('user', 'current_occupation')
    op.drop_column('user', 'country')
    op.drop_column('user', 'city')
    op.drop_column('education', 'location')
    # ### end Alembic commands ###
