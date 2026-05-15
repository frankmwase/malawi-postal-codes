# Malawi Postal Codes SDK

An SDK for Malawi postal codes, designed for consistency and ease of use in e-commerce and logistics applications.

## The "Source of Truth" Architecture

This project uses a monorepo structure where all postal code data is centralized in `data/codes.json`. All language-specific libraries (TypeScript, Go, etc.) are automatically generated from this single source of truth, ensuring 100% consistency across your stack.

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
│   └── codes.json           # The master list of all codes (Source of Truth)
├── typescript/              # The NPM package
│   ├── src/index.ts         # Generated TypeScript source
│   ├── package.json
│   └── README.md
├── go/                      # The Go Module
│   ├── codes.go             # Generated Go source
│   ├── go.mod
│   └── README.md
├── scripts/                 # Automation scripts
│   └── build-data.py        # Syncs JSON data to all libraries
└── README.md                # Main project overview
```

## How to Update Data

1.  Edit `data/codes.json` with the new or modified postal codes.
2.  Run the build script:
    ```bash
    python3 scripts/build-data.py
    ```
3.  Commit and push the changes.

## Recommended Address Format

When mailing within or to Malawi, the Malawian postal service recommends the following format to ensure efficient delivery:

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
*Feel free to contibute*
