"""add tasks model

Revision ID: 70ea0d2e0784
Revises: bc2c2aa7c0b7
Create Date: 2018-09-26 17:24:29.245525

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '70ea0d2e0784'
down_revision = 'bc2c2aa7c0b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_created_date', table_name='users')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_updated_date', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_index('ix_users_updated_date', 'users', ['updated_date'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.create_index('ix_users_created_date', 'users', ['created_date'], unique=False)
    # ### end Alembic commands ###
