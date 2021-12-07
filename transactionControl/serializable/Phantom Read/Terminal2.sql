\c pharmacompany
begin transaction isolation level serializable;
show transaction_isolation;
select price
from drug
where price>=50;
select price
from drug
where price>=50;
commit;