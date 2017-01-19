# Variables
PG_DB=ipeds
GENERATED_FILES = HD2014.csv GR2014.csv

# Non-file targets
.PHONY: all clean

clean:
	rm -Rf finished/*

all: $(GENERATED_FILES)

# Targets to create csv files with encoded data from IPEDS; make this file with SQL.
# HD2014.csv:
# 		psql -d $(PG_DB) -c \
# 		'COPY (SELECT "INSTNM", "ADDR", "CITY", "STABBR", "LOCALE", "WEBADDR" \
# 		FROM "HD2014") TO STDOUT WITH CSV HEADER' > finished/$@
# 		touch finished/$@

# GR2014.csv:
# 		psql -d $(PG_DB) -c \
# 		'COPY (SELECT "GRTOTLT", "GRBKAAT", "GRHISPT" \
# 		FROM "GR2014") TO STDOUT WITH CSV HEADER' > finished/$@
# 		touch finished/$@

# Create the main csv file with human readble data from IPEDS
# schools_processed.csv : schools_raw.csv
# Code goes here.

HD2014.csv:
		psql -d $(PG_DB) -c \
		'COPY (SELECT "GR2014"."UNITID", "INSTNM", "ADDR", "CITY", "STABBR", "LOCALE", "WEBADDR", \
		"GRTOTLT", "GRBKAAT", "GRHISPT" \
		FROM "HD2014" \
		INNER JOIN "GR2014" \
		ON "GR2014"."UNITID"="HD2014"."UNITID" \
		) TO STDOUT WITH CSV HEADER' > finished/$@
		touch finished/$@

GR2014.csv:
		psql -d $(PG_DB) -c \
		'COPY (SELECT "GRTOTLT", "GRBKAAT", "GRHISPT" \
		FROM "GR2014") TO STDOUT WITH CSV HEADER' > finished/$@
		touch finished/$@
