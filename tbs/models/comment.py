"""
The Bestory Project
"""

from datetime import datetime

import pendulum
import sqlalchemy as sa
from tbs.lib import db

table = sa.Table(
    "comments",
    app.tbs.lib.db.meta.DATA,

    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("parent_id", sa.Integer, sa.ForeignKey("comments.id"), index=True,
              nullable=True),
    sa.Column("author_id", sa.Integer, sa.ForeignKey("users.id"), index=True,
              nullable=False),
    sa.Column("story_id", sa.Integer, sa.ForeignKey("stories.id"), index=True,
              nullable=False),

    sa.Column("content", sa.Text(4096), nullable=False),

    sa.Column("likes_count", sa.Integer, default=0, nullable=False),
    sa.Column("comments_count", sa.Integer, default=0, nullable=False),

    sa.Column("is_removed", sa.Boolean, default=False, nullable=False),

    sa.Column("submitted_date", db.types.DateTime,
              default=lambda: datetime.utcnow().replace(tzinfo=pendulum.UTC),
              nullable=False),
    sa.Column("edited_date", db.types.DateTime, nullable=True),
)