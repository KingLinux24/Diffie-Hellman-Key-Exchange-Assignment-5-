import socket
import random

def generate_private_key():
    # Generate a random 6-bit private key (1 to 64)
    return random.randint(1, 64)

def diffie_hellman_key_exchange():
    prime = int(input("Enter a prime number: "))
    generator = int(input("Enter a primitive root (generator): "))

    private_key = generate_private_key()
    print(f"Alice's private key: {private_key}")

    # Compute Alice's public value R1 = g^private_key mod prime
    R1 = pow(generator, private_key, prime)
    print(f"Alice's public value (R1): {R1}")

    # Set up client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

    # Send Alice's public value R1 to Bob
    client_socket.sendall(str(R1).encode())

    # Receive Bob's public value R2
    data = client_socket.recv(1024)
    R2 = int(data.decode())
    print(f"Received Bob's public value (R2): {R2}")

    # Compute the common secret key: (R2^private_key) mod prime
    secret_key = pow(R2, private_key, prime)
    print(f"Alice's computed secret key: {secret_key}")

    client_socket.close()

if __name__ == "__main__":
    diffie_hellman_key_exchange()
