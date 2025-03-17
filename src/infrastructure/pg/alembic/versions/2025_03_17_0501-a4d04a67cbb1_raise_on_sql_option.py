"""raise on sql option

Revision ID: a4d04a67cbb1
Revises: acae3b58b67d
Create Date: 2025-03-17 05:01:17.929563

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4d04a67cbb1'
down_revision: Union[str, None] = 'acae3b58b67d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
