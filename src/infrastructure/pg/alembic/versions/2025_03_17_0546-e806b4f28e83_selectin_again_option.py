"""selectin again option

Revision ID: e806b4f28e83
Revises: b7a8eaf232f5
Create Date: 2025-03-17 05:46:25.243810

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e806b4f28e83"
down_revision: Union[str, None] = "b7a8eaf232f5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
