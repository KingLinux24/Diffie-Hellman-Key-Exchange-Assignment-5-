# Diffie-Hellman Key Exchange (Assignment 5)

## 📘 Assignment
**Task:** Implement Diffie-Hellman Key Exchange using socket communication  
**Goal:** Generate a common secret key between two console apps named `alice` and `bob`.

---

## ✅ Requirements / Instructions
1. Generate a random private key for both users with **6-bit length** (i.e., values up to 64).  
2. The user supplies:
   - A **prime number** `p`
   - A **primitive root / generator** `g` (modulo `p`)
3. Both parties (Alice and Bob) exchange their public values (R1 and R2) using socket communication and then compute the **shared secret key** on each side.

---

## 🔧 How it should work (overview)
1. **Alice** generates a private key `a` (6-bit), computes `A = g^a mod p`, and sends `A` to Bob.
2. **Bob** generates a private key `b` (6-bit), computes `B = g^b mod p`, and sends `B` to Alice.
3. **Alice** computes shared secret `s = B^a mod p`.
4. **Bob** computes shared secret `s = A^b mod p`.
5. Both `s` values should be equal — this is the common secret.

---

## 📁 Suggested Folder Structure
diffie-hellman-assignment5/
│
├── alice.py # Alice client: generates private key, sends A, receives B, computes secret
├── bob.py # Bob client: generates private key, sends B, receives A, computes secret
├── README.md
└── LICENSE

---

<img width="1619" height="911" alt="image" src="https://github.com/user-attachments/assets/0a6b7ac9-84aa-440c-9ee3-673d9c293116" />

---

## ▶️ Usage (example)
1. Start one side as a **server** (or have a small relay). Example approach:
   - Run `alice.py` to listen for a connection from Bob (or vice-versa).
   - Run `bob.py` and connect to Alice.

2. Typical flow in two terminals (example):
```bash
# Terminal 1 — Alice (server)
python3 alice.py

# Terminal 2 — Bob (client)
python3 bob.py
