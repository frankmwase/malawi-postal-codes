# Malawi Postal Codes (TypeScript SDK)

A type-safe library for Malawi postal codes with full Intellisense support.

## Installation

```bash
npm install @frankmwase/malawi-postal-codes
```

## Usage

```typescript
import { codes, findByCity, findByCode } from '@frankmwase/malawi-postal-codes';

// 1. Get a city object by name
const blantyre = findByCity('Blantyre');
console.log(blantyre?.code); // "2010"
console.log(blantyre?.region); // "Southern"

// 2. Inverse lookup (Find city by code)
const city = findByCode('1000');
console.log(city?.city); // "Lilongwe"

// 3. Access all codes
console.log(codes.length); // 15
```

## Recommended Address Format

To ensure efficient delivery in Malawi, use the following address format:

```text
[Recipient’s Name]
[Street Address or P.O. Box Number]
[City/Town] [Postal Code]
Malawi
```
