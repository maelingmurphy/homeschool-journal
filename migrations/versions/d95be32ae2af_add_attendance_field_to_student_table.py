"""Add attendance field to student table

Revision ID: d95be32ae2af
Revises: 405f80aefc31
Create Date: 2021-01-12 19:40:55.280206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd95be32ae2af'
down_revision = '405f80aefc31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attendance', sa.String(length=64), nullable=True))
        batch_op.create_index(batch_op.f('ix_student_attendance'), ['attendance'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_student_attendance'))
        batch_op.drop_column('attendance')

    # ### end Alembic commands ###
