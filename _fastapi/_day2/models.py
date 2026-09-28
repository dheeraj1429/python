from datetime import datetime
from typing import Optional
from sqlalchemy import String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

# Model
class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

  username: Mapped[str] = mapped_column(
    String(60), unique=True, nullable=False, index=True
  )

  email: Mapped[str] = mapped_column(
    String(100), unique=True, nullable=False, index=True
  )

  bio: Mapped[Optional[str]] = mapped_column(Text)

  created_at: Mapped[datetime] = mapped_column(
    DateTime, server_default=func.now()
  )

