"""select option

Revision ID: acae3b58b67d
Revises: 1378c605957c
Create Date: 2025-03-17 04:52:15.398528

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "acae3b58b67d"
down_revision: Union[str, None] = "1378c605957c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
