"""make_filesystem_id_non_nullable

Revision ID: b7f98cfd6a70
Revises: d9d36b6f4d1e
Create Date: 2022-03-18 18:10:27.842201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7f98cfd6a70'
down_revision = 'd9d36b6f4d1e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('sources', schema=None) as batch_op:
        batch_op.alter_column(
            'filesystem_id',
            existing_type=sa.VARCHAR(length=96),
            nullable=False
        )


def downgrade() -> None:
    with op.batch_alter_table('sources', schema=None) as batch_op:
        batch_op.alter_column(
            'filesystem_id',
            existing_type=sa.VARCHAR(length=96),
            nullable=True
        )
