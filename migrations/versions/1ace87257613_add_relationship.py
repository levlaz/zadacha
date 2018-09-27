"""add relationship

Revision ID: 1ace87257613
Revises: 67784282f034
Create Date: 2018-09-26 17:31:44.384404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ace87257613'
down_revision = '67784282f034'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('creator_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'user', ['creator_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'creator_id')
    # ### end Alembic commands ###
