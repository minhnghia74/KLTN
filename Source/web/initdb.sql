/* Table thiết bị */
CREATE TABLE Device (
	DeviceID varchar(16) PRIMARY KEY,
	Description TEXT
);
/* Table nhân viên */
CREATE TABLE Employee (
	EmployeeName nvarchar(1024),
	CardID varchar(16) PRIMARY KEY,
	EmployeeBirthDate DATE
);

CREATE TABLE Work (
	CardID varchar(16) references Employee(CardID),
	DeviceID varchar(16) references Devices(DeviceID),
	EntryTime DATETIME, /* Thời gian quét thẻ */
	EntryTimeStamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (CardID, EntryTimeStamp)
);

/* Thẻ chưa đăng ký */
CREATE TABLE UnRegistered (
	CardID varchar(16) PRIMARY KEY
);

/* Table quản trị */
CREATE TABLE Administrator (
	username nvarchar(1024) PRIMARY KEY,
	password nvarchar(1024)
);

/* username/password dùng để test */
INSERT INTO Administrator VALUES ('admin', 'admin');