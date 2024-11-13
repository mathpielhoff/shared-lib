import pytest
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.ext.declarative import declarative_base

from shared_lib.utils.db_utils import engine, Base, init_db, get_db

@pytest.fixture(scope="module")
def setup_database():
    """
    Fixture pour initialiser la base de données avant les tests
    et la nettoyer après.
    """
    # Initialisation de la base de données
    init_db()
    yield
    # Nettoyage : suppression des tables après les tests
    Base.metadata.drop_all(bind=engine)

def test_database_connection(setup_database):
    """
    Test pour vérifier que la connexion à la base de données fonctionne.
    """
    # Tentative d'exécuter une simple requête SQL
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1

def test_create_tables(setup_database):
    """
    Test pour vérifier que les tables définies dans Base.metadata sont créées.
    """
    inspector = inspect(engine)  # Utilisez inspect pour obtenir l'inspecteur
    tables = inspector.get_table_names()
    expected_table_names = ["users"]  # Remplacez par vos tables
    assert set(expected_table_names) <= set(tables)

def test_get_db_session(setup_database):
    """
    Test pour vérifier que la fonction `get_db` fournit une session valide.
    """
    db = next(get_db())  # Get the first (and only) yielded session
    with db:
        result = db.execute(text("SELECT 1"))
        assert result.scalar() == 1