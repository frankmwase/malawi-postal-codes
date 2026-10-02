# Malawi Postal Codes (Go SDK)

A Go module for Malawi postal codes with GoDoc support for IDE intellisense.

## Installation

```bash
go get github.com/frankmwase/malawi-postal-codes/go
```

## Usage

```go
package main

import (
    "fmt"
    mwpost "github.com/frankmwase/malawi-postal-codes/go"
)

func main() {
    // 1. Lookup a code by city name
    code := mwpost.Lookup("Blantyre")
    fmt.Println(code) // "2010"

    // 2. Inverse lookup: Find city name by code
    city := mwpost.LookupByCode("1000")
    fmt.Println(city) // "Lilongwe"

    // 3. Loop through all locations
    for _, location := range mwpost.Codes {
        fmt.Printf("%s: %s (%s)\n", location.City, location.Code, location.Region)
    }
}
```

## Example Address Format

Confirm addressing requirements with the carrier before mailing. For illustration:

```text
[Recipient’s Name]
[Street Address or P.O. Box Number]
[City/Town] [Postal Code]
Malawi
```
