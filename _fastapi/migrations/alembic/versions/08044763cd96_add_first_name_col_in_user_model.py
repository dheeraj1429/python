"""add first name col in user model

Revision ID: 08044763cd96
Revises: 9cc26ab224a2
Create Date: 2026-10-03 20:28:38.407304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08044763cd96'
down_revision: Union[str, Sequence[str], None] = '9cc26ab224a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('first_name', sa.String(length=50), nullable=True))

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", "first_name")