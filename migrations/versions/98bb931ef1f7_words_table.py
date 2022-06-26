"""words table

Revision ID: 98bb931ef1f7
Revises: ae51ec2bb41b
Create Date: 2022-06-26 16:35:14.977000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98bb931ef1f7'
down_revision = 'ae51ec2bb41b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word_en', sa.String(length=140), nullable=True),
    sa.Column('word_ru', sa.String(length=140), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('word')
    # ### end Alembic commands ###
