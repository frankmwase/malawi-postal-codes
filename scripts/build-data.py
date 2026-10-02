import json
import os

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
 * A complete list of all Malawian postal codes.
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

// Codes is a complete list of all Malawian postal codes.
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

def generate_go_structs(data):
    lines = []
    for item in data:
        line = f'    {{City: "{item["city"]}", Code: "{item["code"]}", Region: "{item["region"]}"}},'
        lines.append(line)
    return "\n".join(lines)

def main():
    # 1. Load the data
    with open('data/codes.json', 'r') as f:
        data = json.load(f)

    # 2. Generate for each language
    for lang, config in LANGUAGES.items():
        print(f"Generating {lang}...")
        
        # Prepare the data strings
        if lang == "go":
            formatted_content = config["template"].format(
                go_structs="\n" + generate_go_structs(data)
            )
        else:
            formatted_content = config["template"].format(
                data_json=json.dumps(data, indent=2)
            )

        # Ensure directory exists
        os.makedirs(os.path.dirname(config["path"]), exist_ok=True)
        
        # Write the file
        with open(config["path"], 'w') as f:
            f.write(formatted_content.strip())
            f.write("\n") # Ensure newline at end of file

if __name__ == "__main__":
    main()