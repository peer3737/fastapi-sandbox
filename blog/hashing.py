from passlib.context import CryptContext

# Define the password hashing context
# 'schemes' specifies the algorithms to use, in order of preference.
pwd_context = CryptContext(
    schemes=["bcrypt"], # Argon2 is generally preferred, but bcrypt is also strong.
    deprecated="auto" # Allows passlib to re-hash old algorithms if encountered.
)

class Hash:
    @staticmethod
    def bcrypt(password: str) -> str:
        """Hashes a plain-text password using the configured context."""
        return pwd_context.hash(password)

    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        """Verifies a plain-text password against a hashed password."""
        return pwd_context.verify(plain_password, hashed_password)
