Get co_block.sql

1.  See on this table 

`co_block` (`rowid`, `time`, `user`, `rolled_back`,...)

2. Mysql magic<br/>
mysql -u jayse -p test < co_block.sql<br/>
mysql> use test<br/>
mysql> select time from co_block where rolled_back=1<br/>
+------------+<br/>
| time       |<br/>
+------------+<br/>
| 1581060905 |<br/>
+------------+<br/>

3.  Send flag<br/>

auctf{1581060905}
