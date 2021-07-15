"""Comment out date fields

Revision ID: af59a9fcb49b
Revises: 1bc44823a291
Create Date: 2021-07-13 21:30:01.091031

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'af59a9fcb49b'
down_revision = '1bc44823a291'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.drop_index('ix_activity_activity_date')
        batch_op.drop_column('activity_date')

    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.drop_index('ix_attendance_attendance_date')
        batch_op.drop_column('attendance_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attendance_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
        batch_op.create_index('ix_attendance_attendance_date', ['attendance_date'], unique=False)

    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activity_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
        batch_op.create_index('ix_activity_activity_date', ['activity_date'], unique=False)

    # ### end Alembic commands ###