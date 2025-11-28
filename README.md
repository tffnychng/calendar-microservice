# Calendar Microservice

## Request parameter
A json object that specifies how the date should be formatted, if no format is provided is not a supported format, the program will default to YYYY-MM-DD. Allowed format types include
- "MM-DD-YYYY"
- "MM/DD/YYYY"
- "DD-MM-YYYY"
- "DD/MM/YYYY"
- "YYYY-MM-DD"
- "YYYY/MM/DD"

## Response
Returns a formatted string containing the date
