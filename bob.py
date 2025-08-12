import socket
import random

def generate_private_key():
    # Generate a random 6-bit private key (1 to 64)
    return random.randint(1, 64)

def diffie_hellman_key_exchange():
    prime = int(input("Enter a prime number: "))
    generator = int(input("Enter a primitive root (generator): "))

    private_key = generate_private_key()
    print(f"Bob's private key: {private_key}")

    # Compute Bob's public value R2 = g^private_key mod prime
    R2 = pow(generator, private_key, prime)
    print(f"Bob's public value (R2): {R2}")

    # Set up server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    print("Bob is listening for connection...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")

        # Receive Alice's public value R1
        data = conn.recv(1024)
        R1 = int(data.decode())
        print(f"Received Alice's public value (R1): {R1}")

        # Send Bob's public value R2 to Alice
        conn.sendall(str(R2).encode())

        # Compute the common secret key: (R1^private_key) mod prime
        secret_key = pow(R1, private_key, prime)
        print(f"Bob's computed secret key: {secret_key}")

    server_socket.close()

if __name__ == "__main__":
    diffie_hellman_key_exchange()
