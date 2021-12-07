
\c pharmacompany
drop trigger if exists t on manufacturing;
drop function if exists quantity();


CREATE FUNCTION quantity() 
RETURNS trigger AS $$
BEGIN	
IF (new.status = 'Complete' and old.status='In-Production') THEN
	UPDATE exports 
	SET quantity = quantity + 10
	WHERE exports.drug_identification =new.d_id;
	return new;
END IF;
return null;    
END;
$$ LANGUAGE plpgsql;


create TRIGGER t AFTER update on manufacturing for each row execute procedure quantity();
