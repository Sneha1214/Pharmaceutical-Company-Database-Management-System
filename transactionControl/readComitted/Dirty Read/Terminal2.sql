\c pharmacompany
begin transaction isolation level read committed;
show transaction_isolation;
select price
from drug
where dname='Crocin 500 mg';
commit;