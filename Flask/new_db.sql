
/*******************************************************************************
   Chinook Database - Version 1.4
   Script: Chinook_Sqlite.sql
   Description: Creates and populates the Chinook database.
   DB Server: Sqlite
   Author: Luis Rocha
   License: http://www.codeplex.com/ChinookDatabase/license
********************************************************************************/

/*******************************************************************************
   Drop Foreign Keys Constraints
********************************************************************************/

/*******************************************************************************
   Drop Tables
********************************************************************************/

DROP TABLE IF EXISTS [USER_DETAIL];

DROP TABLE IF EXISTS [Album];

DROP TABLE IF EXISTS [TA];

/*******************************************************************************
   Create Tables
********************************************************************************/

CREATE TABLE [USER_DETAIL]
(
    [UserID] TEXT  NOT NULL,
    [Pass] TEXT,
    CONSTRAINT [PK_User] PRIMARY KEY  ([UserID])
);

CREATE TABLE [Album]
(
    [AlbumId] INTEGER  NOT NULL,
    [Title] NVARCHAR(160)  NOT NULL,
    [ArtistId] INTEGER  NOT NULL,
    CONSTRAINT [PK_Album] PRIMARY KEY  ([AlbumId]),
    FOREIGN KEY ([ArtistId]) REFERENCES [Artist] ([ArtistId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE [TA]
(
    [Id] INTEGER  NOT NULL,
    [native_english_speaker] NVARCHAR(200)  NOT NULL,
    [course_instructor] NVARCHAR(220),
    [course] NVARCHAR(220),
    [semester] NVARCHAR(220),
    [class_size] NVARCHAR(220),
    [performance_score] INTEGER,
    CONSTRAINT [PK_Id] PRIMARY KEY  ([Id])
);



/*******************************************************************************
   Populate Tables
********************************************************************************/
INSERT INTO [USER_DETAIL] ([UserID], [Pass]) VALUES ('pdeb','2433');
INSERT INTO [USER_DETAIL] ([UserID], [Pass]) VALUES ('deba','123');

INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (1, 'For Those About To Rock We Salute You', 1);
INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (2, 'Balls to the Wall', 2);
INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (3, 'Restless and Wild', 2);
INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (4, 'Let There Be Rock', 1);
INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (5, 'Big Ones', 3);
INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (6, 'Jagged Little Pill', 4);
INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (7, 'Facelift', 5);
INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (8, 'Warner 25 Anos', 6);
INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (9, 'Plays Metallica By Four Cellos', 7);
INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (10, 'Audioslave', 8);
INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (11, 'Out Of Exile', 8);
INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (12, 'BackBeat Soundtrack', 9);
INSERT INTO [Album] ([AlbumId], [Title], [ArtistId]) VALUES (13, 'The Best Of Billy Cobham', 10);

INSERT INTO [TA] ([Id], [native_english_speaker], [course_instructor],[course], [semester], [class_size],[performance_score]) VALUES (1123, 'Varun Sontake', 'Aman Singh','Physics', 'Sem1','200',120);

