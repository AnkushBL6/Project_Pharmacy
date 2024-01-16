-- Bills table  
CREATE TABLE Bills (
  BillID int IDENTITY(1,1) PRIMARY KEY,
  BillDate date,
  BillNumber varchar(255), 
  MedicalAgency varchar(255),
  Company varchar(255),
  BillAmount decimal(10,2),
  Discount bit,
  StockistDiscount decimal (10,2),
  NetAmount decimal(10,2),
  IsFiled bit, 
  PaymentStatus varchar(255),
  PaymentMode varchar(255), 
  PaymentDate date,
  TransactionDetails varchar(max),
  Comments varchar(max),
  POC varchar(255)
);

-- Inventory table
CREATE TABLE Inventory (
  InventoryID int IDENTITY(1,1) PRIMARY KEY, 
  BillID int FOREIGN KEY REFERENCES Bills(BillID),
  ProductID varchar(255), 
  ProductName varchar(255),
  ProductType varchar(255),
  Quantity decimal(10,2),  
  PurchasePrice decimal(10,2),
  ExpiryDate date, 
  BatchNo varchar(255)
);

-- Stock_Entry table 
CREATE TABLE Stock_Entry (
  EntryID int IDENTITY(1,1) PRIMARY KEY,
  Date date, 
  ProductID varchar(255),
  ProductName varchar(255), 
  ProductType varchar(255),
  Quantity decimal(10,2),
  PurchasePrice decimal(10,2),
  SalePrice decimal(10,2),
  BatchNo varchar(255),
  BillNo varchar(255)  
);