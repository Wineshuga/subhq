from datetime import datetime
from sqlmodel import SQLModel
from models.models import (BillingCycle, Category, PaymentStatus, SubscriptionStatus)

# user schemas

class UserBase(SQLModel):
  email: str
  fullname: str

class UserPublic(UserBase):
  id: int
  created_at: datetime
  updated_at: datetime

class UserCreate(UserBase):
  email: str
  fullname: str
  password: str

class UserUpdate(SQLModel):
  fullname: str | None = None
  password: str | None = None

# subscription schemas

class SubscriptionBase(SQLModel):
  service_id: int
  amount: int
  currency: str
  billing_cycle: BillingCycle
  next_renewal: datetime

class SubscriptionCreate(SQLModel):
  service_id: int
  amount: int
  currency: str
  billing_cycle: BillingCycle
  next_renewal: datetime | None = None

class SubscriptionPublic(SubscriptionBase):
  id: int
  user_id: int
  subscription_status: SubscriptionStatus
  created_at: datetime
  updated_at: datetime


class SubscriptionUpdate(SQLModel):
  subscription_status: SubscriptionStatus | None = None
  amount: int | None = None
  currency: str | None = None
  billing_cycle: BillingCycle | None = None
  next_renewal: datetime | None = None

# service schemas

class ServiceCreate(SQLModel):
  name: str
  logo_url: str | None = None
  category: Category

class ServicePublic(SQLModel):
  id: int
  name: str
  logo_url: str | None = None
  category: Category
  created_at: datetime
  updated_at: datetime

# payment schemas

class PaymentCreate(SQLModel):
  subscription_id: int
  amount: int
  currency: str
  payment_provider: str | None = None

class PaymentPublic(SQLModel):
  id: int
  subscription_id: int
  user_id: int
  amount: int
  currency: str
  payment_status: PaymentStatus
  payment_provider: str | None
  transaction_reference: str | None
  paid_at: datetime | None
  created_at: datetime
  updated_at: datetime