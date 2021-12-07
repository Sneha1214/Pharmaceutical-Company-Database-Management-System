\c pharmacompany
begin transaction isolation level serializable;
show transaction_isolation;
select price
from drug
where dname='Crocin 500 mg';
commit;