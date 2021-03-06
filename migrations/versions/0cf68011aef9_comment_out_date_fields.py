"""Comment out date fields

Revision ID: 0cf68011aef9
Revises: 9505ca147803
Create Date: 2021-07-13 21:48:25.956822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cf68011aef9'
down_revision = '9505ca147803'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('resources', sa.Text(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], name=op.f('fk_activity_student_id_student')),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name=op.f('fk_activity_subject_id_subject')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_activity_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_activity'))
    )
    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_activity_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_activity_notes'), ['notes'], unique=False)
        batch_op.create_index(batch_op.f('ix_activity_resources'), ['resources'], unique=False)
        batch_op.create_index(batch_op.f('ix_activity_status'), ['status'], unique=False)
        batch_op.create_index(batch_op.f('ix_activity_student_id'), ['student_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_activity_subject_id'), ['subject_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_activity_title'), ['title'], unique=False)
        batch_op.create_index(batch_op.f('ix_activity_user_id'), ['user_id'], unique=False)

    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.drop_index('ix_attendance_attendance_date')
        batch_op.drop_column('attendance_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attendance_date', sa.VARCHAR(length=64), autoincrement=False, nullable=False))
        batch_op.create_index('ix_attendance_attendance_date', ['attendance_date'], unique=False)

    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_activity_user_id'))
        batch_op.drop_index(batch_op.f('ix_activity_title'))
        batch_op.drop_index(batch_op.f('ix_activity_subject_id'))
        batch_op.drop_index(batch_op.f('ix_activity_student_id'))
        batch_op.drop_index(batch_op.f('ix_activity_status'))
        batch_op.drop_index(batch_op.f('ix_activity_resources'))
        batch_op.drop_index(batch_op.f('ix_activity_notes'))
        batch_op.drop_index(batch_op.f('ix_activity_description'))

    op.drop_table('activity')
    # ### end Alembic commands ###
