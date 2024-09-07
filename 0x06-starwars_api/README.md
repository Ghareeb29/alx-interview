# 0x06. Star Wars API

This script fulfills all the requirements specified:

1. It uses the first positional argument as the Movie ID.
2. It displays one character name per line in the same order as the "characters" list in the `/films/` endpoint.
3. It uses the Star Wars API (<https://swapi-api.alx-tools.com/api>).
4. It uses the `request` module for making HTTP requests.

Here's a breakdown of how the script works:

1. We first check if the correct number of arguments is provided.
2. We define a function `getCharacterName` that fetches a character's name from a given URL.
3. The main function `fetchAndPrintCharacters` does the following:
   - Fetches the film data using the provided movie ID.
   - Extracts the list of character URLs from the film data.
   - Iterates through each character URL, fetches the character's name, and prints it.
4. We use async/await to ensure that the characters are printed in the correct order.

To use this script:

1. Save it as `0-starwars_characters.js` in your `0x06-starwars_api` directory.
2. Make sure to install the `request` module by running `npm install request` in your project directory.
3. Make the script executable with `chmod +x 0-starwars_characters.js`.
4. Run it with a movie ID, for example: `./0-starwars_characters.js 3`.

This script should meet all the requirements, including using semistandard style and not using `var`. It's also set up to be run on Ubuntu 20.04 LTS with Node.js version 10.14.x.
