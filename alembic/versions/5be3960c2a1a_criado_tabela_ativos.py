"""criado tabela Ativos

Revision ID: 5be3960c2a1a
Revises: 
Create Date: 2023-01-22 16:53:55.023273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5be3960c2a1a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Ativos',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('valor', sa.Float(precision=2), nullable=False),
        sa.Column('papel', sa.String(10), nullable=False),
        sa.Column('tipo', sa.String(20), nullable=False),
    )


def downgrade():
    op.drop_table('Ativos')
