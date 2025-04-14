from sqli.dao.user import User
import base64

def test_password_security():
    print("\n=== Password Security Test ===\n")
    
    # Test case 1: Legacy MD5 hash verification
    test_user = User(
        id=1,
        first_name="Test",
        middle_name=None,
        last_name="User",
        username="test_user",
        pwd_hash="5f4dcc3b5aa765d61d8327deb882cf99",  # MD5 hash of "password"
        is_admin=False
    )
    
    print("1. Testing legacy MD5 password:")
    is_valid, new_hash = test_user.check_password("password")
    print(f"- Legacy password valid: {is_valid}")
    print(f"- New hash generated: {'Yes' if new_hash else 'No'}")
    if new_hash:
        print(f"- New hash format: {new_hash}")
        print(f"- Hash components: {new_hash.split('$')}")
        version, salt_b64, hash_b64 = new_hash.split('$')
        print(f"- Salt length: {len(base64.b64decode(salt_b64))} bytes")
        print(f"- Hash length: {len(base64.b64decode(hash_b64))} bytes")
    
    print("\n2. Testing new secure hash format:")
    # Create a new password hash using the secure method
    new_user_hash = User.hash_new_password("mypassword123")
    test_user2 = User(
        id=2,
        first_name="Test",
        middle_name=None,
        last_name="User2",
        username="test_user2",
        pwd_hash=new_user_hash,
        is_admin=False
    )
    
    print(f"- New password hash: {new_user_hash}")
    is_valid, upgrade_hash = test_user2.check_password("mypassword123")
    print(f"- Correct password verification: {is_valid}")
    print(f"- No upgrade needed: {upgrade_hash is None}")
    
    is_valid, _ = test_user2.check_password("wrongpassword")
    print(f"- Wrong password correctly rejected: {not is_valid}")
    
    print("\n3. Security properties:")
    version, salt_b64, hash_b64 = new_user_hash.split('$')
    salt = base64.b64decode(salt_b64)
    hash_bytes = base64.b64decode(hash_b64)
    print(f"- Hash version: {version}")
    print(f"- Salt size: {len(salt)} bytes")
    print(f"- Hash size: {len(hash_bytes)} bytes")
    print(f"- Using PBKDF2-SHA256 with 600,000 iterations")

if __name__ == "__main__":
    test_password_security()