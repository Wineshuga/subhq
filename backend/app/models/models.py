from datetime import datetime
from sqlmodel import Field, SQLModel
from enum import Enum

class SubscriptionStatus(str, Enum):
  ACTIVE = "active"
  CANCELLED = "cancelled"
  EXPIRED = "expired"

class PaymentStatus(str, Enum):
  PENDING = "pending"
  SUCCESSFUL = "successful"
  FAILED = "failed"
  REFUNDED = "refunded"
  
class BillingCycle(str, Enum):
  MONTHLY = "monthly"
  QUARTERLY = "quarterly"
  ANNUALLY = "annually"

class Category(str, Enum):
  ENTERTAINMENT = "entertainment"
  PRODUCTIVITY = "productivity"
  AI_TOOLS = "ai tools"
  DESIGN = "design"
  EDUCATION = "education"
  COMMUNICATION = "communication"
  HEALTH_AND_FITNESS = "health and fitness"
  GAMING = "gaming"
  BUSINESS = "business"

class User(SQLModel, table=True):
  __tablename__ = "users"

  id: int = Field(default=None, primary_key=True)
  email: str = Field(index=True, nullable=False, unique=True)
  fullname: str = Field(default=None)
  hashed_password: str = Field(default=None)
  created_at: datetime = Field(default_factory=datetime.now)
  updated_at: datetime = Field(default_factory=datetime.now)

class Subscription(SQLModel, table=True):
  __tablename__ = "subscriptions"

  id: int = Field(default=None, primary_key=True)
  user_id: int = Field(foreign_key="users.id", nullable=False, index=True)
  service_id: int = Field(foreign_key="services.id", nullable=False, index=True)
  subscription_status: SubscriptionStatus = Field(default=None, index=True)
  amount: int = Field(default=None)
  currency: str = Field(default=None)
  billing_cycle: BillingCycle = Field(default=None, index=True)
  next_renewal: datetime = Field(default=None)
  created_at: datetime = Field(default_factory=datetime.now)
  updated_at: datetime = Field(default_factory=datetime.now)

class Service(SQLModel, table=True):
  __tablename__ = "services"

  id: int = Field(default=None, primary_key=True)
  name: str = Field(index=True, nullable=False, unique=True)
  logo_url: str = Field(default=None)
  category: Category = Field(default=None, index=True)
  created_at: datetime = Field(default_factory=datetime.now)
  updated_at: datetime = Field(default_factory=datetime.now)

class Payment(SQLModel, table=True):
  __tablename__ = "payments"

  id: int = Field(default=None, primary_key=True)
  subscription_id: int = Field(foreign_key="subscriptions.id", nullable=False, index=True)
  amount: int = Field(default=None)
  currency: str = Field(default=None)
  user_id: int = Field(foreign_key="users.id", nullable=False, index=True)
  payment_status: PaymentStatus = Field(default=None, index=True)
  payment_provider: str = Field(default=None)
  transaction_reference: str = Field(default=None, unique=True)
  paid_at: datetime = Field(default=None)
  created_at: datetime = Field(default_factory=datetime.now)
  updated_at: datetime = Field(default_factory=datetime.now)

