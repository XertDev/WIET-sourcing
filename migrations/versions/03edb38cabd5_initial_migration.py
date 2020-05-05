"""Initial migration

Revision ID: 03edb38cabd5
Revises: a40bf330f8ca
Create Date: 2020-05-05 23:40:39.261750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03edb38cabd5'
down_revision = 'a40bf330f8ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_account',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('password_reset_tok', sa.String(length=128), nullable=True),
    sa.Column('password_reset_exp', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user_profile.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_account')
    # ### end Alembic commands ###
