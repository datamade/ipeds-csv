# Variables
PG_DB=ipeds
GENERATED_FILES = schools_raw.csv

# Non-file targets
.PHONY: all clean

clean:
	rm -Rf build/*

all: $(GENERATED_FILES)

schools_raw.csv:
		psql -d $(PG_DB) -c \
		'COPY (SELECT DISTINCT "HD2014"."UNITID", \
					"INSTNM", "ADDR", "CITY", "STABBR", "LOCALE", "WEBADDR", "INSTSIZE", "EFUGFT", "ICLEVEL", "HBCU", \
					"ALLONCAM", "ROOM", "BOARD", "RELAFFIL", \
					"GRTOTLT", "GRBKAAT", "GRHISPT", \
					"DVADM01", \
					"EFBKAAT", "EFHISPT", "EFWHITT", \
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
					LIMIT 30 \
					) \
		TO STDOUT WITH CSV HEADER' > build/$@
		touch build/$@

# Create the main csv file with human readble data from IPEDS
# schools_processed.csv : schools_raw.csv
# Code goes here.