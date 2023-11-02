"""step two

Revision ID: 1603840793cf
Revises: 99a503e8ac41
Create Date: 2023-11-01 20:26:02.460756

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1603840793cf'
down_revision: Union[str, None] = '99a503e8ac41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
