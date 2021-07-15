"""Add notes2 test for db migration

Revision ID: f0eacc40564d
Revises: acd6f57c7902
Create Date: 2021-07-13 21:09:48.785893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0eacc40564d'
down_revision = 'acd6f57c7902'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.add_column(sa.Column('notes2', sa.Text(), nullable=True))
        batch_op.create_index(batch_op.f('ix_activity_notes2'), ['notes2'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activity', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_activity_notes2'))
        batch_op.drop_column('notes2')

    # ### end Alembic commands ###