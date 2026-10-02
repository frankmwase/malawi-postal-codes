# Malawi Postal Codes SDK

An SDK for Malawi postal codes, designed for consistency and ease of use in e-commerce and logistics applications.

## The "Source of Truth" Architecture

This project uses a monorepo structure where its curated postal-code dataset is centralized in `data/codes.json`. The TypeScript and Go libraries are generated from that dataset; CI checks that generated files stay in sync. The current 15 entries are not a verified exhaustive registry. Confirm codes with the relevant postal provider before using them for delivery decisions. An authoritative source and last-verification date have not yet been documented.

| Language | Registry | Installation |
| :--- | :--- | :--- |
| **TypeScript** | NPM | `npm install @frankmwase/malawi-postal-codes` |
| **Go** | GitHub | `go get github.com/frankmwase/malawi-postal-codes/go` |

## Features

- **Lookup**: Find postal codes by city name (case-insensitive).
- **Inverse Lookup**: Find city names by postal code.
- **Type Safety**: Full TypeScript interfaces and Go structs.
- **Intellisense**: Complete documentation comments for IDE support.

## Project Structure

```text
malawi-postal-codes/
├── data/
│   └── codes.json           # Curated dataset (source for generated SDKs)
├── typescript/              # The NPM package
│   ├── src/index.ts         # Generated TypeScript source
│   ├── package.json
│   └── README.md
├── go/                      # The Go Module
│   ├── codes.go             # Generated Go source
│   ├── go.mod
│   └── README.md
├── scripts/                 # Automation scripts
│   └── build-data.py        # Validates data and syncs generated SDKs
└── README.md                # Main project overview
```

## How to Update Data

1. Edit `data/codes.json` with new or modified entries. Record the authoritative source and verification date when available.
2. Run `python3 scripts/build-data.py` from any directory (requires Python 3 and Go's `gofmt`). The script validates entries, rejects duplicates, and formats generated Go code.
3. Run `python3 scripts/build-data.py --check`, `python3 -m unittest discover -s scripts -p 'test_*.py'`, `cd go && go test ./...`, and `cd typescript && npm ci && npm test` before committing.

## Example Address Format

Confirm the required addressing format with the carrier before mailing. For illustration:

```text
[Recipient’s Name]
[Street Address or P.O. Box Number]
[City/Town] [Postal Code]
Malawi
```

**Example:**
```text
John Phiri
P.O. Box 456
Blantyre 2010
Malawi
```

## Postal Code Reference

These are the 15 entries currently included, not a complete registry.

| City/Town | Postal Code | Region |
| :--- | :--- | :--- |
| Lilongwe | 1000 | Central |
| Blantyre | 2010 | Southern |
| Zomba | 2060 | Southern |
| Mzuzu | 3020 | Northern |
| Karonga | 3120 | Northern |
| Salima | 1050 | Central |
| Kasungu | 1020 | Central |
| Ntcheu | 1060 | Central |
| Mulanje | 2120 | Southern |
| Mangochi | 2080 | Southern |
| Thyolo | 2110 | Southern |
| Rumphi | 3040 | Northern |
| Nkhata Bay | 3050 | Northern |
| Chitipa | 3110 | Northern |
| Mchinji | 1040 | Central |

---
*Feel free to contribute*
