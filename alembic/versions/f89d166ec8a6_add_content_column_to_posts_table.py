"""add content column to posts table

Revision ID: f89d166ec8a6
Revises: a6905ab70e82
Create Date: 2022-12-09 14:36:32.776539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f89d166ec8a6'
down_revision = 'a6905ab70e82'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
