"""Added employee and department models

Revision ID: 9548efbc8327
Revises: 
Create Date: 2021-06-06 19:41:09.761193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9548efbc8327'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=False),
    sa.Column('employee_name', sa.String(length=100), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=False),
    sa.Column('department', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('employee_name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_employee_date_of_birth'), 'employee', ['date_of_birth'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employee_date_of_birth'), table_name='employee')
    op.drop_table('employee')
    op.drop_table('department')
    # ### end Alembic commands ###
