
\c pharmacompany

INSERT into EMPLOYEE values('James', 'Borg', 'FM01','AA01','Formulation engineer manager',243000,28,'450 Stone Houston TX', 'M','2015-11-10',1);
INSERT into EMPLOYEE values('John', 'Smith','CSM02','AA01','Clinical studies manager',232000,26,'731 Fondren Houston TX', 'M','2015-2-10',2);
INSERT into EMPLOYEE values('Franklin','Wong','MM03','AA01','Manufacturing manager',147000,27,'638 voss Houston TX', 'M','2016-6-12',3);
INSERT into EMPLOYEE values('Alicia', 'Zelaya','EM04','AA01','Exports manager',143000,24,'3321 Castle Spring Tx','F','2016-8-4',4);
INSERT into EMPLOYEE values('Jennifer', 'Wallace','M05','CSM02','Manufacturing',46000,25,'291 Berry Bellaire Tx', 'F','2017-11-10',3);
INSERT into EMPLOYEE values('Ramesh', 'Narayan','F06','FM01','Formulation engineer',62000,26,'975 Fire Oak Humble, TX','M','2017-4-14',1);
INSERT into EMPLOYEE values('Joyce', 'English','CS07','CSM02','Clinical studies',49000,27,'5631 Rice,Houston TX', 'F','2018-3-22',2);
INSERT into EMPLOYEE values('Ahmed', 'Jabbar','E08','EM04','Exports',40000,28,'980 Dallas Houston,TX', 'M','2019-5-6',4);
INSERT into EMPLOYEE values('Wennifer', 'Jallace','M09','CSM02','Manufacturing',45000,25,'299 Berry Bellaire Tx', 'F','2017-11-9',3);
INSERT into EMPLOYEE values('Paul', 'Geroge','M10','CSM02','Manufacturing',42000,32,'300 Berry Bellaire Tx','M','2017-11-9',3);
INSERT into EMPLOYEE values('Jimothy', 'jalame','E12','EM04','Exports',38000,33,'302 Berry Bellaire TX','M','2017-11-8',4);
INSERT into EMPLOYEE values('Admin', 'admin','AA01',NULL,'Admin Dept',10000,33,'Admin Dept,Pharma Company','M','2012-09-8',4);





INSERT into RAW_MATERIALS values(001,'acetaminophen',3);
INSERT into RAW_MATERIALS values(002,'Fexofenadine',4);
INSERT into RAW_MATERIALS values(003,'esomeprazole',2);
INSERT into RAW_MATERIALS values(004,'Lactobacillus acidophilus',3);
INSERT into RAW_MATERIALS values(005,'tramadol hydrochloride',1);
INSERT into RAW_MATERIALS values(006,'Ranitidine hydrochloride',1);
INSERT into RAW_MATERIALS values(007,'Ibuprofen',3);
INSERT into RAW_MATERIALS values(008,'Diclofenac',4);



INSERT into DRUG values(001,'Crocin 500 mg',30,'disaccharide gentiobiose,dicarboxylic acid crocetin,acetaminophen');
INSERT into DRUG values(002,'Alegra 180 mg',250,'Fexofenadine');
INSERT into DRUG values(003,'Sompraz-L',210,'esomeprazole');
INSERT into DRUG values(004,'Providac 1 mg',310,'Lactobacillus acidophilus');
INSERT into DRUG values(005,'Trambax 50 mg Tab',100,'tramadol hydrochloride');
INSERT into DRUG values(006,'Rantac 150 mg',30,'Ranitidine hydrochloride');
INSERT into DRUG values(007,'Brufen 400 mg',10,'Ibuprofen');
INSERT into DRUG values(008,'Voveran SR 100',130,'Diclofenac');



INSERT into DEPARTMENT values('Formulations',1,'FM01','James');
INSERT into DEPARTMENT values('Clinical Studies',2,'CSM02','John');
INSERT into DEPARTMENT values('Manufacturing',3,'MM03','Franklin');
INSERT into DEPARTMENT values('Exports',4,'EM04','Alicia');
INSERT into DEPARTMENT values('Research',5,'M05','Jennifer');
INSERT into DEPARTMENT values('RMC',7,'F06','Ramesh');
INSERT into DEPARTMENT values('Imports',6,'CS07','Joyce');
INSERT into Department values ('Admin Dept',8,'AA01','Admin');



INSERT into MANUFACTURING values('Automated / Integrated Workcell','In-Production','2021-10-12',null,001,'M05');
INSERT into MANUFACTURING values('Automated Biomolecular Interaction Analyzer','In-Production','2021-10-12',null,002,'M09');
INSERT into MANUFACTURING values('Cell Counters','In-Production','2021-10-12',null,004,'M10');
INSERT into MANUFACTURING values('Cell Disruptor','In-Production','2021-10-12',null,003,'MM03');
INSERT into MANUFACTURING values('Cell Harvesting System','Complete','2021-5-9','2021-6-11',005,'F06');
INSERT into MANUFACTURING values('Chemical Synthesizer','Complete','2021-5-9','2021-6-11',006,'CS07');
INSERT into MANUFACTURING values('Carbon Dioxide Transmitter','Complete','2021-5-9','2021-6-11',007,'FM01');
INSERT into MANUFACTURING values('Cell Disruptor','Complete','2021-5-9','2021-6-11',008,'EM04');




INSERT into EXPORTS values(001,'State-Wide','Crocin 500 mg','Karnataka',10,'EM04');
INSERT into EXPORTS values(008,'Nation-Wide','Voveran SR 100','Karnataka,Kerala,UP',870000,'E12');
INSERT into EXPORTS values(002,'State-Wide','Brufen 400 mg','Karnataka',800,'E12');
INSERT into EXPORTS values(006,'State-Wide','Alegra 180 mg','Karnataka',1230,'E08');
INSERT into EXPORTS values(001,'State-Wide','Crocin 500 mg','Kerala',900,'E08');
INSERT into EXPORTS values(005,'Nation-Wide','Trambax 50 mg Tab','Karnataka,Bihar,Punjab',10,'E12');
INSERT into EXPORTS values(001,'State-Wide','Crocin 500 mg','Odisha',1000,'E12');


INSERT into LICENSE values('CDSO','Ramesh',002);
INSERT into LICENSE values('SDSCO','Suresh',008);
INSERT into LICENSE values('SDSCO','Veena',003);
INSERT into LICENSE values('CDSO','Ramesh',001);
INSERT into LICENSE values('CDSO','Seema',005);
INSERT into LICENSE values('SDSCO','Raghav',006);
INSERT into LICENSE values('CDSO','Shriram',007);
INSERT into LICENSE values('SDSCO','Sneha',004);


INSERT into CLINICAL_STUDY values(11,'Crocin 500 mg',1,'Gathering test subjects done, injected with drug',001,'CSM02');
INSERT into CLINICAL_STUDY values(122,'Trambax 50 mg Tab',3,'Tested on 20 individuals,no symptoms',005,'CS07');
INSERT into CLINICAL_STUDY values(123,'Alegra 180 mg',3,'Tested on 600 individuals,high symptoms',002,'CSM02');
INSERT into CLINICAL_STUDY values(124,'Sompraz-L',4,'Tests done',003,'CS07');
INSERT into CLINICAL_STUDY values(101,'Voveran SR 100',3,'Tested on 20 individuals,no symptoms',008,'CSM02');
INSERT into CLINICAL_STUDY values(165,'Brufen 400 mg',1,'Gathering test subjects done, injected with drug',007,'CS07');
INSERT into CLINICAL_STUDY values(189,'Providac 1 mg',3,'Tested on 20 individuals,no symptoms',004,'CSM02');



INSERT into FORMULATION values(101,'Petri dish testing on bacillus','No change',001,001);
INSERT into FORMULATION values(100,'Petri dish testing on Lactobacillus','High porosity',002,008);
INSERT into FORMULATION values(156,'Petri dish testing on algae','No change',003,003);
INSERT into FORMULATION values(108,'Petri dish testing on virusoid','Color change ',004,007);
INSERT into FORMULATION values(111,'Petri dish testing on Stem-cell','fast multiplication',005,006);
INSERT into FORMULATION values(190,'Petri dish testing on baci','No change',006,004);
INSERT into FORMULATION values(160,'Petri dish testing on fungi','No change',007,002);
INSERT into FORMULATION values(132,'Petri dish testing on Saliva','sudden multiplication',008,005);


INSERT into LOGININFO values('FM01',123);
INSERT into LOGININFO values('CSM02',124);
INSERT into LOGININFO values('MM03',125);
INSERT into LOGININFO values('EM04',126);
INSERT into LOGININFO values('M05',127);
INSERT into LOGININFO values('F06',128);
INSERT into LOGININFO values('CS07',129);
INSERT into LOGININFO values('E08',130);
INSERT into LOGININFO values('M09',131);
INSERT into LOGININFO values('M10',132);
INSERT into LOGININFO values('E12',133);
INSERT into LOGININFO values('AA01',111);