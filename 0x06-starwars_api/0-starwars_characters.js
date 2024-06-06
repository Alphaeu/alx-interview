#!/usr/bin/env node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
    console.log('Please provide a Movie ID');
    process.exit(1);
}

// The URL for the Star Wars API film endpoint
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error('Error making request:', error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error('Failed to retrieve data. Status code:', response.statusCode);
        return;
    }

    // Parse the JSON response
    const filmData = JSON.parse(body);

    // Get the list of character URLs
    const characterUrls = filmData.characters;

    // For each character URL, make a request to get the character's name
    characterUrls.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
            if (error) {
                console.error('Error making request:', error);
                return;
            }

            if (response.statusCode !== 200) {
                console.error('Failed to retrieve data. Status code:', response.statusCode);
                return;
            }

            // Parse the JSON response
            const characterData = JSON.parse(body);

            // Print the character's name
            console.log(characterData.name);
        });
    });
});

