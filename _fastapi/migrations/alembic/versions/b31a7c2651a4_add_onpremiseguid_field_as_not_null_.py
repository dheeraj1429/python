"""add onPremiseGuid field as not-null into the user table

Revision ID: b31a7c2651a4
Revises: 08044763cd96
Create Date: 2026-10-03 20:43:47.935068

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b31a7c2651a4'
down_revision: Union[str, Sequence[str], None] = '08044763cd96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("users", sa.Column("on_premise_guid", sa.String(100), nullable=True))
    op.execute('UPDATE users SET on_premise_guid = UUID() WHERE on_premise_guid IS NULL')
    op.alter_column("users", "on_premise_guid", existing_type=sa.String(length=100), nullable=False)

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", "on_premise_guid")