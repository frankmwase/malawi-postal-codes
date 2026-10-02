import argparse
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGIONS = {"Northern", "Central", "Southern"}

# Configuration for different languages
LANGUAGES = {
    "typescript": {
        "path": "typescript/src/index.ts",
        "template": """
// GENERATED CODE - DO NOT EDIT MANUALLY

/**
 * Represents a Malawian postal code and its associated metadata.
 */
export interface PostalCode {{
  /** Name of the city or town */
  city: string;
  /** The 4-digit postal code */
  code: string;
  /** The geographic region (Northern, Central, or Southern) */
  region: 'Northern' | 'Central' | 'Southern';
}}

/**
 * A curated list of Malawian postal codes.
 */
export const codes: PostalCode[] = {data_json};

/**
 * Finds a postal code entry by city name (case-insensitive).
 * @param city The name of the city to search for.
 * @returns The matching PostalCode object, or undefined if not found.
 */
export const findByCity = (city: string): PostalCode | undefined => 
  codes.find(c => c.city.toLowerCase() === city.toLowerCase());

/**
 * Finds a postal code entry by the postal code itself.
 * @param code The 4-digit postal code to search for.
 * @returns The matching PostalCode object, or undefined if not found.
 */
export const findByCode = (code: string): PostalCode | undefined =>
  codes.find(c => c.code === code);
"""
    },
    "go": {
        "path": "go/codes.go",
        "template": """
// GENERATED CODE - DO NOT EDIT MANUALLY
package mwpost

import "strings"

// Location represents a Malawian postal code and its associated metadata.
type Location struct {{
    // Name of the city or town
    City   string `json:"city"`
    // The 4-digit postal code
    Code   string `json:"code"`
    // The geographic region (Northern, Central, or Southern)
    Region string `json:"region"`
}}

// Codes is a curated list of Malawian postal codes.
var Codes = []Location{{{go_structs}
}}

// Lookup returns the postal code for a given city name (case-insensitive).
// Returns an empty string if the city is not found.
func Lookup(city string) string {{
    for _, v := range Codes {{
        if strings.EqualFold(v.City, city) {{
            return v.Code
        }}
    }}
    return ""
}}

// LookupByCode returns the city name for a given 4-digit postal code.
// Returns an empty string if the code is not found.
func LookupByCode(code string) string {{
    for _, v := range Codes {{
        if v.Code == code {{
            return v.City
        }}
    }}
    return ""
}}
"""
    }
}

def validate_data(data):
    if not isinstance(data, list) or not data:
        raise ValueError("codes.json must contain a non-empty array")

    cities = set()
    codes = set()
    for index, item in enumerate(data):
        if not isinstance(item, dict) or set(item) != {"city", "code", "region"}:
            raise ValueError(f"entry {index}: expected city, code, and region")
        city, code, region = item["city"], item["code"], item["region"]
        if not isinstance(city, str) or not city.strip() or city != city.strip():
            raise ValueError(f"entry {index}: city must be a non-empty trimmed string")
        if not isinstance(code, str) or not re.fullmatch(r"[0-9]{4}", code):
            raise ValueError(f"entry {index}: code must be a four-digit string")
        if not isinstance(region, str) or region not in REGIONS:
            raise ValueError(f"entry {index}: invalid region")
        if city.casefold() in cities or code in codes:
            raise ValueError(f"entry {index}: duplicate city or code")
        cities.add(city.casefold())
        codes.add(code)


def generate_go_structs(data):
    return "\n".join(
        f'    {{City: {json.dumps(item["city"], ensure_ascii=False)}, '
        f'Code: {json.dumps(item["code"])}, '
        f'Region: {json.dumps(item["region"])} }},'
        for item in data
    )


def render_sources(data):
    validate_data(data)
    sources = {}
    for lang, config in LANGUAGES.items():
        if lang == "go":
            source = config["template"].format(
                go_structs="\n" + generate_go_structs(data)
            ).strip() + "\n"
            source = subprocess.run(
                ["gofmt"], input=source, text=True, capture_output=True, check=True
            ).stdout
        else:
            source = config["template"].format(
                data_json=json.dumps(data, indent=2, ensure_ascii=False)
            ).strip() + "\n"
        sources[ROOT / config["path"]] = source
    return sources


def main():
    parser = argparse.ArgumentParser(description="Generate SDKs from data/codes.json")
    parser.add_argument("--check", action="store_true", help="check generated files without writing")
    args = parser.parse_args()

    with (ROOT / "data/codes.json").open(encoding="utf-8") as source:
        sources = render_sources(json.load(source))

    stale = []
    for path, content in sources.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"Generated {path.relative_to(ROOT)}")

    if stale:
        parser.exit(1, f"Outdated generated files: {', '.join(map(str, stale))}\n")


if __name__ == "__main__":
    main()