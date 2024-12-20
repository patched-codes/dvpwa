from sqli.dao.user import User

def test_new_hash_implementation():
    # Test the new PBKDF2 implementation
    password = "mypassword123"
    
    # Generate first hash
    hash1, salt1 = User.hash_password(password)
    print(f"\nNew PBKDF2 Implementation:")
    print(f"Password: {password}")
    print(f"Hash: {hash1}")
    print(f"Salt: {salt1}")
    print(f"Hash length: {len(hash1)} characters")
    print(f"Salt length: {len(salt1)} characters")
    
    # Generate second hash of same password (should be different due to different salt)
    hash2, salt2 = User.hash_password(password)
    print(f"\nSecurity Improvements Demo:")
    print(f"Second hash of same password: {hash2}")
    print(f"Second salt: {salt2}")
    print(f"Hashes different (due to different salts): {hash1 != hash2}")
    
    # Verify password verification works
    user = User(id=1, first_name="Test", middle_name=None, last_name="User", 
                username="test", pwd_hash=hash1, pwd_salt=salt1, is_admin=False)
    
    print(f"\nPassword Verification Tests:")
    print(f"Correct password verifies: {user.check_password(password)}")
    print(f"Wrong password fails: {user.check_password('wrongpass')}")

if __name__ == "__main__":
    test_new_hash_implementation()