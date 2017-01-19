# Variables
PG_DB=ipeds
GENERATED_FILES = HD2014.csv GR2014.csv

# Non-file targets
.PHONY: all clean

clean:
	rm -Rf build/*

all: schools_raw.csv

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

schools_raw.csv:
		psql -d $(PG_DB) -c \
		'COPY (SELECT "HD2014"."UNITID", \
					"INSTNM", "ADDR", "CITY", "STABBR", "LOCALE", "WEBADDR", "INSTSIZE", "EFUGFT", "ICLEVEL", "HBCU", \
					"ALLONCAM", "ROOM", "BOARD", "RELAFFIL", \
					"GRTOTLT", "GRBKAAT", "GRHISPT", \
					"DVADM01", \
					"EFBKAAT", "EFHISPT", "EFWHITT" \
					"RMINSTTP", "RMOUSTTN", "PCTENRW", \
					"PGRNT_N", "FGRNT_N" \
					FROM "HD2014" \
					INNER JOIN "IC2014" \
					ON "HD2014"."UNITID"="IC2014"."UNITID" \
					INNER JOIN "GR2014" \
					ON "HD2014"."UNITID"="GR2014"."UNITID" \
					INNER JOIN "DRVADM2014" \
					ON "HD2014"."UNITID"="DRVADM2014"."UNITID" \
					INNER JOIN "EF2014A" \
					ON "HD2014"."UNITID"="EF2014A"."UNITID" \
					INNER JOIN "DRVEF2014" \
					ON "HD2014"."UNITID"="DRVEF2014"."UNITID" \
					INNER JOIN "SFA1314_P1" \
					ON "HD2014"."UNITID"="SFA1314_P1"."UNITID" \
					) \
		TO STDOUT WITH CSV HEADER' > build/$@
		touch build/$@

