from datetime import datetime, timezone

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func


class IdPkMixin:
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)


class TimeMixin:
    create_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        server_default=func.now()
    )

    update_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        server_default=func.now(),
        onupdate=datetime.now(timezone.utc),
        server_onupdate=func.now()
    )
