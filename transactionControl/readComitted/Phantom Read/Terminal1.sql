\c pharmacompany
begin transaction isolation level read committed;
show transaction_isolation;
update drug
set price=50
where dname='Crocin 500 mg';
commit;