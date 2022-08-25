
#! ./bin/bash

echo "Enable loading local data"

mysql -u huyman -p"Man@28081999" university < enable.sql

echo "Creating table"

mysql --local-infile=1 -u huyman -p"Man@28081999" university < createtable.sql

echo "Importing data"

mysql --local-infile=1 -u huyman -p"Man@28081999" university < mark_2019.sql

mysql --local-infile=1 -u huyman -p"Man@28081999" university < mark_2020.sql

mysql --local-infile=1 -u huyman -p"Man@28081999" university < mark_2021.sql

mysql --local-infile=1 -u huyman -p"Man@28081999" university < mark_2022.sql

echo "Verifying data"

mysql --local-infile=1 -u huyman -p"Man@28081999" university < verifydata.sql

echo "Successfully import data to MySQL Database"
