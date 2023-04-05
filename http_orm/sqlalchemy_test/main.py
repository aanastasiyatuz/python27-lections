from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# driver://user:password@host:port/db_name
db_url = 'postgresql://nastya:1@127.0.0.1:5432/sqlalchemy_test'
engine = create_engine(db_url)
# подключение к бд

Base = declarative_base()
# базовый класс для таблиц

# создаем таблицу
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return f"<Product({self.id}) -> {self.title}>"

Base.metadata.create_all(bind=engine)
# записываем таблицу в бд

SessionLocal = sessionmaker(bind=engine)
# создаем класс для сессий (один обьект от данного класса - одна сессия)

session = SessionLocal()
# создаем сессию

new_product = Product(title='product1', price=120)
# создаем продукт (запись в таблицу)
# для орм создаем запрос на запись в таблицу

session.add(new_product)
# добавляем запрос в сессию

session.commit()
# отправляем набор запросов бд

products = session.query(Product).all()
# получаем все записи из таблицы product
print(products)

res = session.query(Product).filter(Product.price > 100).all()
# получаем все записи из таблицы product у которых цена больше 100
print(res)

product3 = session.query(Product).get(3)
# получаем продукт под id 3
print(product3)

product4 = session.query(Product).get(4)
# получаем продукт под id 4
session.delete(product4)
# удаляем продукт
session.commit()
# сохраняем изменения в бд

product3.title = 'new title'
product3.price = 100
# изменяем продукт
session.commit()
# сохраняем изменения в бд
