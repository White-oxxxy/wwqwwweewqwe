"""joined option

Revision ID: b7a8eaf232f5
Revises: 9b84531dc683
Create Date: 2025-03-17 05:35:32.395739

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b7a8eaf232f5"
down_revision: Union[str, None] = "9b84531dc683"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
