"""add user table

Revision ID: 5e4c8be86de3
Revises: f89d166ec8a6
Create Date: 2022-12-09 14:40:12.947745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e4c8be86de3'
down_revision = 'f89d166ec8a6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
    sa.Column('id', sa.Integer(), nullable=False), 
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False), 
    sa.PrimaryKeyConstraint('id'), 
    sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
