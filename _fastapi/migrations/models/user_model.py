from typing import Optional
from datetime import datetime
from database import Base
from sqlalchemy import DateTime, func, String, Text
from sqlalchemy.orm import mapped_column, Mapped
import uuid

class UserModel(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

  user_name: Mapped[str] = mapped_column(
    String(60), unique=True, nullable=False, index=True
  )

  email: Mapped[str] = mapped_column(
    String(100), unique=True, nullable=False, index=True
  )

  place: Mapped[Optional[str]] = mapped_column(
    Text
  )

  create_at: Mapped[datetime] = mapped_column(
    DateTime, server_default=func.now()
  )

  first_name: Mapped[str] = mapped_column(
    String(50), nullable=True
  )

  on_premise_guid: Mapped[str] = mapped_column(
    String(100), nullable=False, default=uuid.uuid4()
  )
