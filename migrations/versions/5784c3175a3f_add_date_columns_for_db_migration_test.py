"""Add date columns for db migration test

Revision ID: 5784c3175a3f
Revises: f0eacc40564d
Create Date: 2021-07-13 21:12:59.351343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5784c3175a3f'
down_revision = 'f0eacc40564d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activity_date2', sa.DateTime(timezone=False), nullable=False))
        batch_op.create_index(batch_op.f('ix_activity_activity_date2'), ['activity_date2'], unique=False)
        batch_op.drop_index('ix_activity_notes2')
        batch_op.drop_column('notes2')

    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attendance_date2', sa.DateTime(timezone=False), nullable=False))
        batch_op.create_index(batch_op.f('ix_attendance_attendance_date2'), ['attendance_date2'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_attendance_attendance_date2'))
        batch_op.drop_column('attendance_date2')

    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.add_column(sa.Column('notes2', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.create_index('ix_activity_notes2', ['notes2'], unique=False)
        batch_op.drop_index(batch_op.f('ix_activity_activity_date2'))
        batch_op.drop_column('activity_date2')

    # ### end Alembic commands ###
