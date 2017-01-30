# Variables
PG_DB=ipeds

# Non-file targets
.PHONY: all clean

clean:
	rm -Rf build/*

all: schools_raw.csv build/schools_processed.csv

schools_raw.csv:
		psql -d $(PG_DB) -c \
		'COPY (SELECT "HD2014"."UNITID", \
					"INSTNM", "ADDR", "CITY", "STABBR", "ZIP", "LOCALE", "WEBADDR", "INSTSIZE", "ICLEVEL", "HBCU", \
					"ALLONCAM", "ROOM", "BOARD", "RELAFFIL", \
					"BAGR150", \
					"GRRTBK", "GRRTHS", \
					"DVADM01", \
					"ENRFT", "RMINSTTP", "RMOUSTTP", "PCTENRW", "PCTENRBK", "PCTENRHS", "PCTENRWH", \
					"PGRNT_P", "FGRNT_P" \
					FROM "HD2014" \
					LEFT JOIN "IC2014" \
					ON "HD2014"."UNITID"="IC2014"."UNITID" \
					LEFT JOIN "GR200_14" \
					ON "HD2014"."UNITID"="GR200_14"."UNITID" \
					LEFT JOIN "DRVGR2014" \
					ON "HD2014"."UNITID"="DRVGR2014"."UNITID" \
					LEFT JOIN "DRVADM2014" \
					ON "HD2014"."UNITID"="DRVADM2014"."UNITID" \
					LEFT JOIN "DRVEF2014" \
					ON "HD2014"."UNITID"="DRVEF2014"."UNITID" \
					LEFT JOIN "SFA1314_P1" \
					ON "HD2014"."UNITID"="SFA1314_P1"."UNITID" \
					) \
		TO STDOUT WITH CSV HEADER' > build/$@
		touch build/$@

# Create the main csv file with human readble data from IPEDS
build/schools_processed.csv: build/schools_raw.csv
		cat $< | python decoder.py > $@


