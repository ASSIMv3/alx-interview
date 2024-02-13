#!/usr/bin/node
const axios = require('axios');

const fetchCharacterNames = async (movieId) => {
    try {
        const response = await axios.get(`https://swapi-api.alx-tools.com/api/films/${movieId}/`);
        const characters = response.data.characters;
        for (const characterUrl of characters) {
            const characterResponse = await axios.get(characterUrl);
            console.log(characterResponse.data.name);
        }
    } catch (error) {
        console.error('Error fetching data:', error.message);
    }
};

const movieId = process.argv[2];
if (!movieId) {
    console.log("Please provide a movie ID as argument.");
    process.exit(1);
}

fetchCharacterNames(movieId);
