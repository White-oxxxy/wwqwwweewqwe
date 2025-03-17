"""selectin option

Revision ID: 9b84531dc683
Revises: a4d04a67cbb1
Create Date: 2025-03-17 05:30:01.720611

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b84531dc683'
down_revision: Union[str, None] = 'a4d04a67cbb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
