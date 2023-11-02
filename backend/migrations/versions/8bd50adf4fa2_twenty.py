"""twenty

Revision ID: 8bd50adf4fa2
Revises: 283bffbc2022
Create Date: 2023-11-02 14:05:48.704484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bd50adf4fa2'
down_revision: Union[str, None] = '283bffbc2022'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
