from sqlalchemy import create_engine, String, Column, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError, OperationalError
import bcrypt

db = create_engine("sqlite:///meubanco.db")
Seção = sessionmaker(bind=db)
session = Seção()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    chave = Column("chave", String, primary_key=True)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, chave, senha, ativo=True):
        self.chave = chave
        self.senha = senha
        self.ativo = ativo

def hash_senha(senha):
    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return senha_hash

def create_usuario(chave, senha):
    try:
        senha_criptografada = hash_senha(senha)
        usuario = Usuario(chave=chave, senha=senha_criptografada.decode('utf-8'))
        session.add(usuario)
        session.commit()
        print("Usuário inserido com sucesso.")
        return True
    except IntegrityError:
        session.rollback()
        print("Erro: Já existe um usuário com essa chave.")
    except OperationalError as e:
        session.rollback()
        print(f"Erro no banco de dados: {e}")
    except Exception as e:
        platform_specific_module = None
        session.rollback()
        print(f"Erro inesperado: {e}")
    finally:
        print("Operação de criação de usuário concluída.")

def verificar_usuario(chave, senha):
    try:
        usuario = session.query(Usuario).filter_by(chave=chave).first()
        if usuario:
            if senha:
                senha_hash_bd = usuario.senha.encode('utf-8')
                if bcrypt.checkpw(senha.encode('utf-8'), senha_hash_bd):
                    print("Senha correta.")
                    return True
                else:
                    print("Senha incorreta.")
                    return False
            else:
                print("Senha não fornecida.")
                return False
        else:
            print("Usuário não encontrado.")
            return False
    except OperationalError as e:
        print(f"Erro no banco de dados: {e}")
        return False
    except Exception as e:
        print(f"Erro ao verificar usuário: {e}")
        return False

try:
    Base.metadata.create_all(bind=db)
    print("Banco de dados criado com sucesso.")
except OperationalError as e:
    print(f"Erro ao criar banco de dados: {e}")
except Exception as e:
    print(f"Erro inesperado ao criar banco de dados: {e}")