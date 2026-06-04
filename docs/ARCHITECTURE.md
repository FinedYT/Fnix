Client
 ↓
TCP Listener
 ↓
Connection Handler
 ↓
HTTP Parser
 ↓
Router
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