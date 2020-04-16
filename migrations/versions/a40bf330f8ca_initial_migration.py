"""Initial migration.

Revision ID: a40bf330f8ca
Revises: 
Create Date: 2020-04-16 21:00:36.175316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a40bf330f8ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('role', sa.Enum('ADMIN', name='userrole'), nullable=False),
    sa.Column('accuracy', sa.Float(), nullable=False),
    sa.Column('wiet_points', sa.Integer(), nullable=False),
    sa.Column('creation_time', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('question_set',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('details', sa.Text(), nullable=False),
    sa.Column('category', sa.Enum('PHOTO', 'TEXT', name='category'), nullable=False),
    sa.Column('creation_date', sa.TIMESTAMP(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('close_date', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user_profile.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('promotion_action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_set_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('BASIC', 'PREMIUM', name='promotiontype'), nullable=False),
    sa.Column('start_time', sa.TIMESTAMP(), nullable=False),
    sa.Column('end_time', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['question_set_id'], ['question_set.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_set_id', sa.Integer(), nullable=False),
    sa.Column('payload', sa.JSON(), nullable=False),
    sa.ForeignKeyConstraint(['question_set_id'], ['question_set.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question_set_report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('question_set_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('INAPPROPRIATE_CONTENT', name='reporttype'), nullable=True),
    sa.Column('details', sa.String(length=255), nullable=False),
    sa.Column('creation_time', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['question_set_id'], ['question_set.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question_answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('payload', sa.JSON(), nullable=False),
    sa.Column('creation_time', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_answer')
    op.drop_table('question_set_report')
    op.drop_table('question')
    op.drop_table('promotion_action')
    op.drop_table('question_set')
    op.drop_table('user_profile')
    # ### end Alembic commands ###
