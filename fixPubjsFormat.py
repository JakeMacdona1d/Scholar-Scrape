import json

# Load JSON data from a file
with open('output/publications.json', 'r') as file:
    data = json.load(file)

# Convert to desired format, filtering by year
publications = []
for entry in data:
    # Ensure 'author' is a list of dictionaries with 'given' as the key
    authors = [{"given": name.strip()} for name in entry['author'].split(",")]

    # Extract year as a string
    issued_value = entry.get('issued')
    year = ""
    if isinstance(issued_value, str):
        year = issued_value.split("/")[0]  # Extract year as a string
    elif isinstance(issued_value, dict) and "date-parts" in issued_value:
        year = str(issued_value["date-parts"][0][0])  # Convert year to a string if it's not already
    else:
        year = ""  # Default to an empty string if format is not recognized

    # Only include entries for the years 2023 and 2024
    if year in ["2023", "2024"]:
        # Adjust the 'issued' format to always use string for the year
        issued = {"date-parts": [[year]]} if year else {"date-parts": [[""]]}
        
        # Create the new entry
        new_entry = {
            "title": entry['title'],
            "author": authors,
            "URL": entry['URL'],
            "abstract": entry['abstract'],
            "issued": issued
        }
        publications.append(new_entry)

# Print or save the result
with open('converted_publications.json', 'w') as outfile:
    json.dump(publications, outfile, indent=2)

# For demonstration, print the first entry if available
if publications:
    print(json.dumps(publications[0], indent=2))
else:
    print("No publications found for the years 2023 and 2024.")
