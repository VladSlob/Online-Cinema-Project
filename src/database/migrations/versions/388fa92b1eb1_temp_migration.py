"""temp_migration

Revision ID: 388fa92b1eb1
Revises: 9b8ddbae4c17
Create Date: 2025-03-25 15:50:11.336296

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "388fa92b1eb1"
down_revision: Union[str, None] = "9b8ddbae4c17"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "movies",
        "uuid",
        existing_type=sa.VARCHAR(),
        type_=sa.dialects.postgresql.UUID(),
        existing_nullable=False,
        postgresql_using="uuid::uuid",
    )


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "movies",
        "uuid",
        existing_type=sa.Uuid(),
        type_=sa.VARCHAR(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
