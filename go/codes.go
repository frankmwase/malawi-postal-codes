// GENERATED CODE - DO NOT EDIT MANUALLY
package mwpost

import "strings"

// Location represents a Malawian postal code and its associated metadata.
type Location struct {
    // Name of the city or town
    City   string `json:"city"`
    // The 4-digit postal code
    Code   string `json:"code"`
    // The geographic region (Northern, Central, or Southern)
    Region string `json:"region"`
}

// Codes is a complete list of all Malawian postal codes.
var Codes = []Location{
    {City: "Mzuzu", Code: "3020", Region: "Northern"},
    {City: "Karonga", Code: "3120", Region: "Northern"},
    {City: "Rumphi", Code: "3040", Region: "Northern"},
    {City: "Nkhata Bay", Code: "3050", Region: "Northern"},
    {City: "Chitipa", Code: "3110", Region: "Northern"},
    {City: "Lilongwe", Code: "1000", Region: "Central"},
    {City: "Salima", Code: "1050", Region: "Central"},
    {City: "Kasungu", Code: "1020", Region: "Central"},
    {City: "Ntcheu", Code: "1060", Region: "Central"},
    {City: "Mchinji", Code: "1040", Region: "Central"},
    {City: "Blantyre", Code: "2010", Region: "Southern"},
    {City: "Zomba", Code: "2060", Region: "Southern"},
    {City: "Thyolo", Code: "2110", Region: "Southern"},
    {City: "Mulanje", Code: "2120", Region: "Southern"},
    {City: "Mangochi", Code: "2080", Region: "Southern"},
}

// Lookup returns the postal code for a given city name (case-insensitive).
// Returns an empty string if the city is not found.
func Lookup(city string) string {
    for _, v := range Codes {
        if strings.EqualFold(v.City, city) {
            return v.Code
        }
    }
    return ""
}

// LookupByCode returns the city name for a given 4-digit postal code.
// Returns an empty string if the code is not found.
func LookupByCode(code string) string {
    for _, v := range Codes {
        if v.Code == code {
            return v.City
        }
    }
    return ""
}
