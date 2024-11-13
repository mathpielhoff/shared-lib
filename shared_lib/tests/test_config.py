from shared_lib.utils.config import Config

def test_config_values():
    assert Config.SECRET_KEY == "default-secret-key"
    assert Config.ALGORITHM == "HS256"
    assert Config.ACCESS_TOKEN_EXPIRE_MINUTES == 30