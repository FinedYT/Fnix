Core Request Flow:
TCP Listener
 ↓
Connection Handler
 ↓
HTTP Parser
 ↓
Router
 ↓
Handler(Error handler if route not found)
 ↓
Response Builder
 ↓
Client

Request Lifecycle:
1. Client connects to Fnix
2. TCP listener accepts connection
3. Connection handler receives data
4. HTTP parser extracts request information
5. Router selects target handler
6. Response is generated
7. Response is sent back to client

Networking Layer Responsibilities:
- Listener listens for incoming connections
- Connection performs the connection
- Connection Manager manages incoming connections
Networking Layer does not:
- parse HTTP
- route requests
- generate responses