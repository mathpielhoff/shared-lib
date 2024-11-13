from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from shared_lib.utils.config import Config

# Récupération des variables d'environnement
DATABASE_URL = Config.AUTH_DB_URL

# Création de l'engine SQLAlchemy
engine = create_engine(DATABASE_URL)

# Création de la base déclarative pour les modèles
Base = declarative_base()

# Création du sessionmaker pour les interactions avec la base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Fonction pour obtenir une session de base de données.
    À utiliser avec le mot-clé `Depends` dans FastAPI.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Erreur lors de la création des tables : {e}")