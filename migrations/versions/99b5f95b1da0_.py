"""empty message

Revision ID: 99b5f95b1da0
Revises: 509b61661f86
Create Date: 2022-12-16 13:28:54.453051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99b5f95b1da0'
down_revision = '509b61661f86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
