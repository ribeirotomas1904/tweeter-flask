"""empty message

Revision ID: e8dd3b5d4c1c
Revises: 22b618e8a1b7
Create Date: 2020-10-14 00:22:51.652269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8dd3b5d4c1c'
down_revision = '22b618e8a1b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('followers', 'followed_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('followers', 'follower_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('followers', 'follower_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('followers', 'followed_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
