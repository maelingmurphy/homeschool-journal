"""Add date-related fields with timezone=False

Revision ID: 1bc44823a291
Revises: b0825873d910
Create Date: 2021-07-13 21:20:58.822109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bc44823a291'
down_revision = 'b0825873d910'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activity_date', sa.DateTime(timezone=False), nullable=False))
        batch_op.create_index(batch_op.f('ix_activity_activity_date'), ['activity_date'], unique=False)

    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attendance_date', sa.DateTime(timezone=False), nullable=False))
        batch_op.create_index(batch_op.f('ix_attendance_attendance_date'), ['attendance_date'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_attendance_attendance_date'))
        batch_op.drop_column('attendance_date')

    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_activity_activity_date'))
        batch_op.drop_column('activity_date')

    # ### end Alembic commands ###