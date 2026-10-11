"""update user email col to non index

Revision ID: 9cc26ab224a2
Revises: 
Create Date: 2026-10-03 17:40:33.219024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9cc26ab224a2'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_index(index_name="ix_users_email", table_name="users")


def downgrade() -> None:
    """Downgrade schema."""
    op.create_index("ix_users_email", "users", ["email"], unique=True)
