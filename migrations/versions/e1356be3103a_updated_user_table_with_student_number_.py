"""Updated user table with student_number field

Revision ID: e1356be3103a
Revises: d95be32ae2af
Create Date: 2021-01-16 15:31:21.987961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1356be3103a'
down_revision = 'd95be32ae2af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_index('ix_student_attendance')
        batch_op.drop_column('attendance')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student_number', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_user_student_number'), ['student_number'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_student_number'))
        batch_op.drop_column('student_number')

    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attendance', sa.VARCHAR(length=64), nullable=True))
        batch_op.create_index('ix_student_attendance', ['attendance'], unique=False)

    # ### end Alembic commands ###
