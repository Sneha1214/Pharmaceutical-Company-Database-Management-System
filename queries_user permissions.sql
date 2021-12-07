\c pharmacompany

--creating users and granting privilages

CREATE USER FM01 WITH PASSWORD '123';
GRANT SELECT, INSERT, UPDATE, DELETE ON FORMULATION TO FM01;

CREATE USER CSM02 WITH PASSWORD '124';
GRANT SELECT, INSERT, UPDATE, DELETE ON CLINICAL_STUDY TO CSM02;

CREATE USER MM03 WITH PASSWORD '125';
GRANT SELECT, INSERT, UPDATE, DELETE ON MANUFACTURING TO MM03;

CREATE USER EM04 WITH PASSWORD '126';
GRANT SELECT, INSERT, UPDATE, DELETE ON EXPORTS TO EM04;

CREATE USER AA01 WITH PASSWORD '111';
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO AA01 WITH GRANT OPTION;

CREATE USER M05 WITH PASSWORD '127';
GRANT SELECT (STATUS) ON MANUFACTURING TO M05;

CREATE USER F06 WITH PASSWORD '128';
GRANT SELECT (TESTING) ON FORMULATION TO F06;

CREATE USER CS07 WITH PASSWORD '129';
GRANT SELECT (PHASE) ON CLINICAL_STUDY TO CS07;

CREATE USER E08 WITH PASSWORD '130';
GRANT SELECT (LOCATIONS) ON EXPORTS TO E08;

--Simple

select * from drug;
select * from drug where price>100;
select * from raw_materials where quantity<2;
select * from employee where dept_no=3;
select machinery from manufacturing where EMPID='EM04';
select composition from drug where DID=006;
select * from license where license_authority='CDSO';
select fname,lname from employee where gender='F';
select fname from employee where salary>40000;
select Testing,Conclusion from formulation where DrugID=004;

--Complex

--Count the number of employee department wise.
select count(EID), b.DNo,dept_name from employee a, department b  where a.dept_no=b.DNo  group by b.DNo,dept_name;

--Count the total salary department wise where more than 2 employees exist.
SELECT  dept_no, sum(salary) As totalsal
FROM employee
GROUP BY dept_no
HAVING COUNT(EID) > 2;


--Retrieve the employee details except of those who work in manufacturing.
(Select EID,Fname,Lname,Job_Position
From Employee)
EXCEPT
(Select EID,Fname,Lname,Job_Position
FROM Employee
Where Job_position='Manufacturing');

--Lists the drug and its export details grouped by type,drug name and quantity.
Select count(Drug_identification),D_name,Quantity,Type
From Exports
Group By Type,Quantity,D_name;

--Retrive emloyee id of all employees who work in dept=3 or are managers of employees who work in dept=3
(Select EID
FROM Employee
where Dept_no=3)
UNION
(Select Mgr_ID
from Department
where DNo=3);

-- Nested Queries

--Find 2nd highest salary of employee
Select distinct Salary from Employee e1 where 2=(Select count(distinct Salary) from Employee e2 where e1.salary<=e2.salary);

--Get 3rd highest salaries records from employee table
select distinct salary from employee as e1 where 3>=(select count(distinct salary) from employee as e2 where e1.salary<=e2.salary) order by e1.salary desc;

--Get the drug details with export quantity value greater than 500.
(Select * from Drug 
Where DID In (Select Distinct Drug_Identification from Exports 
Where Quantity>500));



