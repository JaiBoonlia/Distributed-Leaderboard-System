# Distributed Leaderboard System

## Overview
This project implements a secure distributed leaderboard system using TCP socket programming. Multiple clients can connect to a central server to submit scores and retrieve leaderboard rankings.

All communication between clients and the server is secured using SSL/TLS encryption. The server supports multiple concurrent clients and maintains a shared leaderboard that updates in real time.

---

## Architecture

The system follows a client–server architecture.

**Server**
- Maintains the leaderboard
- Accepts client connections
- Processes score submissions and leaderboard requests

**Clients**
- Connect to the server
- Submit scores
- Request leaderboard rankings

Communication occurs over TCP sockets secured with TLS.

---

## Technologies Used

- Python  
- TCP Socket Programming  
- SSL/TLS Encryption  
- Multithreading  

---

## Features

- Secure communication using SSL/TLS  
- Support for multiple concurrent clients  
- Real-time leaderboard updates  
- Custom command-based interaction  
- Basic error handling for invalid inputs and disconnections  

---

## How to Run the Project

### 1. Clone the Repository

```
git clone <repository-url>
cd secure-distributed-leaderboard
```

### 2. Generate TLS Certificates

Before running the server, generate a self-signed certificate:

```
python generate_cert.py
```

This will create:

```
server.crt
server.key
```

These files are not included in the repository for security reasons.

### 3. Start the Server

```
python server.py
```

The server will start listening for incoming client connections.

### 4. Start Clients

Open another terminal and run:

```
python client.py
```

Multiple clients can connect to the server simultaneously.

---

## Concurrency Handling

The server uses multithreading to handle multiple clients at the same time.  
Each client connection runs in a separate thread.

To prevent race conditions when updating the leaderboard, a thread lock is used to ensure consistent updates.

---

## Optimization and Fixes

During testing, several improvements were implemented:

- TLS certificate verification issues were resolved by configuring the client to accept the self-signed certificate.
- Input validation was added to handle invalid commands.
- Thread locks were implemented to avoid race conditions during concurrent score updates.
- Error handling was added to safely handle client disconnections.

---

## Conclusion

This project demonstrates a secure networked application using TCP sockets, TLS encryption, and concurrent client handling. The system maintains real-time leaderboard rankings while ensuring secure communication between distributed clients.
