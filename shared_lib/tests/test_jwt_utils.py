from shared_lib.utils.jwt_utils import create_access_token, decode_jwt
from datetime import timedelta

def test_create_and_decode_jwt():
    data = {"sub": "test_user", "role": "admin", "tenantId":1}
    token = create_access_token(data, expires_delta=timedelta(minutes=5))
    decoded = decode_jwt(token)
    assert decoded.username == "test_user"
    assert decoded.role == "admin"
    assert decoded.tenant_id == 1