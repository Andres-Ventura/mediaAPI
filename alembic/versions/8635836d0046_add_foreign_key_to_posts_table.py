"""add foreign-key to posts table

Revision ID: 8635836d0046
Revises: 5e4c8be86de3
Create Date: 2022-12-09 15:00:57.399703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8635836d0046'
down_revision = '5e4c8be86de3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", 
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
