"""Change activity_date and attendance_date column types to datetime

Revision ID: 3285660b7427
Revises: 5ad1dca7adf8
Create Date: 2021-07-05 11:59:30.787363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3285660b7427'
down_revision = '5ad1dca7adf8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.alter_column('attendance_date',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.alter_column('attendance_date',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)

    # ### end Alembic commands ###
