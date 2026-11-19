# Fnix
A lightweight HTTP server and reverse proxy framework for Python, designed for exploring networking and web server internals.

> [!NOTE]
> **Project Status: Early MVP**
> Fnix is currently under active development. Core synchronous HTTP server features are in progress, while asynchronous execution and reverse proxy capabilities are planned for upcoming releases.

## Project Structure
- `src/fnix/` — Core server implementation, routing, and request/response handling
- `docs/` — Architecture notes and documentation
- `tests/` — Unit and integration test suite

## Getting Started

### Prerequisites
- Python 3.10 or higher

### Installation
```bash
git clone https://github.com/FinedYT/Fnix.git
cd Fnix
```

## Roadmap
- [x] Basic HTTP request parsing and response serialization
- [x] Synchronous TCP socket server loop
- [ ] Routing and middleware pipeline
- [ ] Asynchronous I/O support (`asyncio`)
- [ ] Reverse proxy and upstream load balancing
- [ ] Configuration file support

## License
This project is licensed under the [MIT License](LICENSE).
