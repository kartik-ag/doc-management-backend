import secrets
import base64

# Generate Django Secret Key
django_secret_key = ''.join([secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

# Generate JWT Secret Key (using a longer key for JWT)
jwt_secret_key = base64.b64encode(secrets.token_bytes(64)).decode('utf-8')

print("\nDjango Secret Key:")
print(django_secret_key)
print("\nJWT Secret Key:")
print(jwt_secret_key) 