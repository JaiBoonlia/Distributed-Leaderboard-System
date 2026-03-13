# Distributed Leaderboard System

## Overview
This project implements a secure distributed leaderboard system using TCP socket programming. Multiple clients can submit scores and retrieve rankings from a central server.

The system supports concurrent client connections and uses SSL/TLS encryption for secure communication.

## Architecture
The system follows a client-server architecture.

Clients send commands to the server:
- SUBMIT <username> <score>
- GET
- QUIT

The server maintains the leaderboard and responds to client requests.

## Technologies Used
- Python
- TCP sockets
- SSL/TLS
- Multithreading

## How to Run

Start the server:

python server.py

Then open another terminal and run the client:

python client.py

Multiple clients can be run simultaneously.

## Example Commands

SUBMIT Alice 500  
SUBMIT Bob 450  
GET  

Example Output:

LEADERBOARD
1 Alice 500
2 Bob 450
