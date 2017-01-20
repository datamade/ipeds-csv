# ipeds-csv
Use this Makefile to generate a clean, decoded, sparkling CSV, which can be imported into the [College Matching site](https://github.com/datamade/college-matching-django).

## Dependencies
* posix operating system (linux or mac os, that sort of thing)
* python
* postgres
* make

#### On Ubuntu, install requirements like this:
```bash
sudo apt-get install postgres
```

#### On Mac OS X, install requirements like this:
```bash
brew install postgres python
```

## Getting Started

Before running this Makefile, you need a PostGres database with tables built from the [Integrated Postsecondary Education Data System (IPEDS)](https://nces.ed.gov/ipeds/). Use the Makefile in [ipeds-db](https://github.com/datamade/ipeds-db) to create your DB.

## Usage

Run the Makefile! It queries the IPEDS database, generates a CSV, and finally decodes that CSV into a human readable format. You can find the results in the `build` directory.

```bash
make all
```

Want something different? Clean out the `build` directory, and start over.

```bash
make clean
```

## Copyright

Copyright (c) 2017 DataMade. Released under the [MIT License](https://github.com/datamade/ipeds-csv/blob/master/LICENSE).
