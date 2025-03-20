"""load options

Revision ID: 1378c605957c
Revises: bcfffcf7bad0
Create Date: 2025-03-16 20:43:34.740557

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1378c605957c"
down_revision: Union[str, None] = "bcfffcf7bad0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
