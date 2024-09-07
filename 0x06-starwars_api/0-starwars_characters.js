#!/usr/bin/node

const request = require('request');

// Check if movie ID is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api';

// Function to fetch character name from URL
function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

// Main function to fetch and print characters
function fetchAndPrintCharacters (movieId) {
  const filmUrl = `${baseUrl}/films/${movieId}/`;

  request(filmUrl, async (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const film = JSON.parse(body);
    const characterUrls = film.characters;

    for (const url of characterUrls) {
      try {
        const name = await getCharacterName(url);
        console.log(name);
      } catch (error) {
        console.error('Error fetching character:', error);
      }
    }
  });
}

// Execute the main function
fetchAndPrintCharacters(movieId);
