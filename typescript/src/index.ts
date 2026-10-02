// GENERATED CODE - DO NOT EDIT MANUALLY

/**
 * Represents a Malawian postal code and its associated metadata.
 */
export interface PostalCode {
  /** Name of the city or town */
  city: string;
  /** The 4-digit postal code */
  code: string;
  /** The geographic region (Northern, Central, or Southern) */
  region: 'Northern' | 'Central' | 'Southern';
}

/**
 * A complete list of all Malawian postal codes.
 */
export const codes: PostalCode[] = [
  {
    "city": "Mzuzu",
    "code": "3020",
    "region": "Northern"
  },
  {
    "city": "Karonga",
    "code": "3120",
    "region": "Northern"
  },
  {
    "city": "Rumphi",
    "code": "3040",
    "region": "Northern"
  },
  {
    "city": "Nkhata Bay",
    "code": "3050",
    "region": "Northern"
  },
  {
    "city": "Chitipa",
    "code": "3110",
    "region": "Northern"
  },
  {
    "city": "Lilongwe",
    "code": "1000",
    "region": "Central"
  },
  {
    "city": "Salima",
    "code": "1050",
    "region": "Central"
  },
  {
    "city": "Kasungu",
    "code": "1020",
    "region": "Central"
  },
  {
    "city": "Ntcheu",
    "code": "1060",
    "region": "Central"
  },
  {
    "city": "Mchinji",
    "code": "1040",
    "region": "Central"
  },
  {
    "city": "Blantyre",
    "code": "2010",
    "region": "Southern"
  },
  {
    "city": "Zomba",
    "code": "2060",
    "region": "Southern"
  },
  {
    "city": "Thyolo",
    "code": "2110",
    "region": "Southern"
  },
  {
    "city": "Mulanje",
    "code": "2120",
    "region": "Southern"
  },
  {
    "city": "Mangochi",
    "code": "2080",
    "region": "Southern"
  }
];

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
