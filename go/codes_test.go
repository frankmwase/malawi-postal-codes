package mwpost

import (
	"strings"
	"testing"
)

func TestLookups(t *testing.T) {
	if len(Codes) == 0 {
		t.Fatal("expected postal codes")
	}

	cities := make(map[string]bool)
	codes := make(map[string]bool)
	for _, location := range Codes {
		if got := Lookup(strings.ToUpper(location.City)); got != location.Code {
			t.Errorf("Lookup(%q) = %q, want %q", location.City, got, location.Code)
		}
		if got := LookupByCode(location.Code); got != location.City {
			t.Errorf("LookupByCode(%q) = %q, want %q", location.Code, got, location.City)
		}
		city := strings.ToLower(location.City)
		if cities[city] || codes[location.Code] {
			t.Fatalf("duplicate city or code: %+v", location)
		}
		cities[city], codes[location.Code] = true, true
	}
}

func TestMissingEntries(t *testing.T) {
	if got := Lookup("unknown town"); got != "" {
		t.Errorf("Lookup(unknown town) = %q, want empty string", got)
	}
	if got := LookupByCode("9999"); got != "" {
		t.Errorf("LookupByCode(9999) = %q, want empty string", got)
	}
}
