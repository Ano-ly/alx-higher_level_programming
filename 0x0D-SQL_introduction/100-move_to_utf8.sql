-- convert some databases, tables, fields to UTF8
-- convert some databases, tables, fields to UTF8
USE hbtn_0c_0;
-- convert database
ALTER DATABASE hbtn_0c_0 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY COLUMN name COLLATE utf8mb4_unicode_ci;
