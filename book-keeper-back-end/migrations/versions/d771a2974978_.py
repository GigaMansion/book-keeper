"""empty message

Revision ID: d771a2974978
Revises: 0ed9c5a4bcc2
Create Date: 2020-05-12 11:08:57.887191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd771a2974978'
down_revision = '0ed9c5a4bcc2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reimburse', sa.Column('status', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reimburse', 'status')
    # ### end Alembic commands ###
