\c pharmacompany
begin transaction isolation level serializable;
show transaction_isolation;
update drug
set price=50
where dname='Crocin 500 mg';
commit;