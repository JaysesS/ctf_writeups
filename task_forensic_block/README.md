Get co_block.sql

1.  See on this table 

`co_block` (`rowid`, `time`, `user`, `rolled_back`,...)

2. Mysql magic
mysql -u jayse -p test < co_block.sql
mysql> use test
mysql> select time from co_block where rolled_back=1
+------------+
| time       |
+------------+
| 1581060905 |
+------------+

3.  Send flag

auctf{1581060905}
