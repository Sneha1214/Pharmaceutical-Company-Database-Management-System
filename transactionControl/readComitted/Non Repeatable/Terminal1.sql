\c pharmacompany
begin transaction isolation level read committed;
show transaction_isolation;
update drug
set price=45
where dname='Crocin 500 mg';
update drug
set price=50
where dname='Crocin 500 mg';
update drug
set price=55
where dname='Crocin 500 mg';
update drug
set price=60
where dname='Crocin 500 mg';
update drug
set price=65
where dname='Crocin 500 mg';
commit;