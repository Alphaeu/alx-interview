
##Log Parsing Script

#Overview

This Python script is designed to parse log data from stdin, compute metrics, and generate statistics based on the specified input format. It reads input line by line, processes the data, and provides output according to the defined requirements.

#Requirements

Python 3.4.3 or later
Linux environment (Ubuntu 20.04 LTS recommended)
PEP 8 style compliance (version 1.7.x)
Supported editors: vi, vim, emacs

#Installation

Clone the repository:
bash
Copy code
git clone https://github.com/your_username/your_repository.git
Navigate to the project directory:
bash
Copy code
cd log-parsing-script
Make sure the script is executable:
bash
Copy code
chmod +x 0-stats.py
Usage
Execute the script by piping log data into it:
bash
Copy code
cat your_log_file.log | ./0-stats.py
The script will process the log data and print statistics as specified in the task requirements.
Input Format
The script expects log data in the following format:
php
Copy code
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Lines that do not adhere to this format will be skipped.
Output
The script generates statistics after every 10 lines of input or upon a keyboard interruption (CTRL + C). The statistics include:
Total file size: Sum of all previous file sizes.
Number of lines by status code: Counts of different HTTP status codes (200, 301, 400, 401, 403, 404, 405, and 500) encountered in the input.
Example
bash
Copy code
cat example_log.log | ./0-stats.py
Sample output:
yaml
Copy code
Total file size: 5213 200: 2 401: 1 403: 2 404: 1 405: 1 500: 3
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.


