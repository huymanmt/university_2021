LOAD DATA LOCAL INFILE './output/diemthi2022.csv'
INTO TABLE mark_2022
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

