CREATE TABLE Client_Info (
    ClientID VARCHAR(10) PRIMARY KEY, 
    Name VARCHAR(50),
    PhoneNum VARCHAR(20),
    Gender CHAR(1),
    Age INT,
    OPProcedure VARCHAR(100),
    Amount DECIMAL(10,2)
);