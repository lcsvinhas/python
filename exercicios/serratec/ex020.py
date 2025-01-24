from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///exemplo.db"
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', age={self.age}, email='{self.email}')"


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_user(name, age, email):
    existing_user = session.query(User).filter_by(email=email).first()
    if existing_user:
        print(f"User with email {email} already exists: {existing_user}")
        return
    new_user = User(name=name, age=age, email=email)
    session.add(new_user)
    session.commit()
    print(f"Added {new_user}")


def get_users():
    users = session.query(User).all()
    for user in users:
        print(user)


def update_user(user_id, new_name=None, new_age=None, new_email=None):
    user = session.query(User).get(user_id)
    if user:
        if new_name:
            user.name = new_name
        if new_age:
            user.age = new_age
        if new_email:
            user.email = new_email
        session.commit()
        print(f"Updated {user}")
    else:
        print("User not found!")


def delete_user(user_id):
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        print(f"Deleted {user}")
    else:
        print("User not found!")


if __name__ == "__main__":
    # Adicionar usuários
    add_user("Alice", 25, "alice@example.com")
    add_user("Bob", 30, "bob@example.com")

    # Listar usuários
    print("\nLista de usuários:")
    get_users()

    # Atualizar usuário
    update_user(1, new_name="Alicia", new_age=26)

    # Listar usuários após atualização
    print("\nLista de usuários após atualização:")
    get_users()

    # Deletar um usuário
    delete_user(2)

    # Listar usuários após exclusão
    print("\nLista de usuários após exclusão:")
    get_users()
