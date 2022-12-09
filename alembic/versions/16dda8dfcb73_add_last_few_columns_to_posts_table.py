"""add_last_few_columns_to_posts_table

Revision ID: 16dda8dfcb73
Revises: 8635836d0046
Create Date: 2022-12-09 15:05:29.735762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16dda8dfcb73'
down_revision = '8635836d0046'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
