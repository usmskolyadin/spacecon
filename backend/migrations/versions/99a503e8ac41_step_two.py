"""step two

Revision ID: 99a503e8ac41
Revises: 067523070d3d
Create Date: 2023-11-01 20:13:25.855399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99a503e8ac41'
down_revision: Union[str, None] = '067523070d3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
