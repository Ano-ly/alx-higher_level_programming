-- convert some databases, tables, fields to UTF8
-- convert some databases, tables, fields to UTF8
USE hbtn_0c_0;
-- convert database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert table
ALTER TABLE first_table COLLATE utf8mb4_unicode_ci;
-- convert field
ALTER TABLE first_table MODIFY COLUMN name COLLATE utf8mb4_unicode_ci;
