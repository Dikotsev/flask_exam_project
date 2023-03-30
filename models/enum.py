from enum import Enum


class UserRolesEnum(Enum):
   admin = "admin"
   user = "user"
   seller = "seller"


class PurchaseState(Enum):
   listed = "listed"
   pending = "pending"
   rejected = "rejected"
   completed = "completed"