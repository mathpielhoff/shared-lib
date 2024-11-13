from shared_lib.utils.config import Config

def test_config_values():
    assert Config.SECRET_KEY == "D88631E328913624FF564DD73798D-68CDE7567CE32A7DDB264246C7F74"
    assert Config.ALGORITHM == "HS256"
    assert Config.ACCESS_TOKEN_EXPIRE_MINUTES == 30
    assert Config.AUTH_DB_URL== "postgresql://auth-db-user:auth-db-user@localhost/mydb"