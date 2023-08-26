"""alter tbl TipoAtivo nome coluna papel p/ nome

Revision ID: abf962063955
Revises: d5badf8c446f
Create Date: 2023-08-26 11:43:24.596210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abf962063955'
down_revision = 'd5badf8c446f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column("TiposAtivo", "papel")
    op.add_column("TiposAtivo", sa.Column("tipo", sa.String(100), nullable=False))


def downgrade() -> None:
    op.drop_column("TiposAtivo", "tipo")
    op.add_column("TiposAtivo", sa.Column("papel", sa.String(50), nullable=False))
