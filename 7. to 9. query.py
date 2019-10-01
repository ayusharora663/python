#7.select count(version),version from tbl_users group by version sort by version;
#8. select * from tbl_accounts where tbl_accounts.userid=tbl_users.userid and tbl_users.deleted=1;
#9. create table tbl_student(id int(3) primary key,name varchar(15), gender varchar(10),age int(2),date_of_birth date,religion varchar(15) DEFAULT 'None');
    #insert into tbl_student values(1,'amit','male',24,1990-07-12);
    #insert into tbl_student values(2,'ganesh','male',34,1980-03-21,'christian');
