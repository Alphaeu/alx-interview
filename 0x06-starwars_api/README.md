Here's a `README.md` file for your project:

```markdown
# Star Wars Characters

This project contains a script that prints all characters of a specified Star Wars movie using the Star Wars API.

## Requirements

- Node.js
- `request` module

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/alx-interview.git
    ```

2. **Navigate to the project directory:**
    ```sh
    cd alx-interview/0x06-starwars_api
    ```

3. **Install the `request` module:**
    ```sh
    npm install request
    ```

## Usage

To run the script, use the following command:

```sh
./0-starwars_characters.js <Movie ID>
```

Replace `<Movie ID>` with the ID of the Star Wars movie you want to query. For example, to get characters from "Return of the Jedi" (Movie ID 3):

```sh
./0-starwars_characters.js 3
```

## Example

```sh
alexa@ubuntu:~/0x06-starwars_api$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06-starwars_api$
```

## Files

- `0-starwars_characters.js`: The main script file.

## Notes

- Ensure you have Node.js installed before running the script.
- The script uses the `request` module to make HTTP requests to the Star Wars API.

## License

This project is licensed under the MIT License.
```

Replace `https://github.com/yourusername/alx-interview.git` with the actual URL of your GitHub repository. This `README.md` provides clear instructions on how to set up and use the script, including prerequisites, installation steps, usage, and an example.
