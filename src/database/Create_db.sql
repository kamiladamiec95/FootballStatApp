CREATE DATABASE [FootballStatistics]

GO

USE [FootballStatistics]
GO
/****** Object:  StoredProcedure [dbo].[AddLeague]    Script Date: 20.03.2024 17:23:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
    CREATE PROCEDURE [dbo].[AddLeague]
(
	@LeagueName nvarchar(255)
)
AS
BEGIN

declare @sql varchar(max)

set @sql = 'CREATE SCHEMA ' + @LeagueName

EXEC(@sql)

set @sql = 'CREATE TABLE [' + @LeagueName + '].[Matches](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[HomeTeamId] [int] NOT NULL,
	[HomeTeamScore] [int] NULL,
	[AwayTeamId] [int] NULL,
	[AwayTeamScore] [int] NULL,
	[MatchExternalId] [bigint] NULL,
	[IsFinished] [int] NULL,
	[HomeTeamFouls] [int] NULL,
	[AwayTeamFouls] [int] NULL,
	[HomeTeamYellowCards] [int] NULL,
	[AwayTeamYellowCards] [int] NULL,
	[HomeTeamRedCards] [int] NULL,
	[AwayTeamRedCards] [int] NULL,
	[HomeTeamCorners] [int] NULL,
	[AwayTeamCorners] [int] NULL,
	[BallPossesion] [int] NULL,
	[HomeTeamOffsides] [int] NULL,
	[AwayTeamOffsides] [int] NULL,
	[MatchTime] [decimal](3, 2) NULL,
 CONSTRAINT [PK_' + @LeagueName +'Matches] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]'

EXEC(@sql)


set @sql = 
'CREATE TABLE [' + @LeagueName + '].[RawData](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Event] [varchar](255) NULL,
	[Player] [nvarchar](100) NULL,
	[Team] [nvarchar](80) NULL,
	[MatchExternalId] bigint NULL
 CONSTRAINT [PK_' + @LeagueName + 'RawData] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]'

EXEC(@sql)


set @sql = 
'CREATE TABLE [' + @LeagueName + '].[Teams](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[ShortName] [nvarchar](80) NULL,
	[LongName] [nvarchar](255) NULL,
	[FoundingDate] [date] NULL,
	[Address] [nvarchar](300) NULL
 CONSTRAINT [PK_' + @LeagueName + 'Teams] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]'

EXEC(@sql)

SET @sql = 
'CREATE PROCEDURE [' + @LeagueName + '].[AddTeams]
(
	@ShortName varchar(80),
	@LongName varchar(255),
	@FoundingDate date,
	@Address nvarchar(30)
)
AS
BEGIN

	INSERT INTO ' + @LeagueName + '.Teams ([ShortName], [LongName], [FoundingDate], [Address])
	SELECT @ShortName, @LongName, @FoundingDate, @Address

END'


EXEC(@sql)

SET @sql = 
'CREATE PROCEDURE ' + @LeagueName + '.AddMatch
	@HomeTeamName nvarchar(255),
	@AwayTeamName nvarchar(255),
	@MatchExternalId bigint,
	@IsFinished int
AS
BEGIN

	INSERT INTO ' + @LeagueName + '.Matches (HomeTeamId, HomeTeamScore, AwayTeamId, AwayTeamScore, MatchExternalId, IsFinished)
	SELECT
	(SELECT TOP 1 Id
	FROM ' + @LeagueName + '.Teams
	WHERE ShortName = @HomeTeamName), 0,
	(SELECT TOP 1 Id
	FROM ' + @LeagueName + '.Teams
	WHERE ShortName = @AwayTeamName), 0
	,@MatchExternalId
	,@IsFinished
END'

EXEC(@sql)

END