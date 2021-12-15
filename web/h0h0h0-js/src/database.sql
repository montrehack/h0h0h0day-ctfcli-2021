DROP TABLE list;

CREATE TABLE list (
	full_name TEXT NOT NULL,
    attitude TEXT NOT NULL,
	gift TEXT NOT NULL
);

INSERT INTO list (full_name, attitude, gift) VALUES ('Apache log4j', 'Naughty', 'A metric ton of ${jndi:ldap://santa/coal}');
INSERT INTO list (full_name, attitude, gift) VALUES ('Apache HTTP Server', 'Naughty', '/gift/.%2e/.%2e/.%2e/.%2e/tmp/coal');
INSERT INTO list (full_name, attitude, gift) VALUES ('GhostScript', 'Naughty', 'Coal + a book : "Learning Policy.xml for Noobs!"');
INSERT INTO list (full_name, attitude, gift) VALUES ('Microsoft Exchange', 'Naughty', '1kg of coal per CVE in 2021 => 31kg of coal so far!');
INSERT INTO list (full_name, attitude, gift) VALUES ('PrintNightmare', 'Naughty', 'A tasty coal running as SYSTEM');
INSERT INTO list (full_name, attitude, gift) VALUES ('PetitPotam', 'Naughty', 'Another NTLM Relayed batch of coal! ');
INSERT INTO list (full_name, attitude, gift) VALUES ('YOU, the only nice person on this list', 'Nice', 'A flag! FLAG-44B24BCE6FA092743101F29F59594329');


