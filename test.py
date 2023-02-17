from sqlalchemy.orm import Session

from applications.product.views import ProductView
from config.models import User, Category
from config.settings import engine

product_obj_ = ProductView()

with Session(engine) as session:
    a = session.get(Category, 1)
    print(a)
