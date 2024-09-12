package main

type PGNGameMeta struct {
	Event        string
	EventDate    string
	EventSponsor string
	Section      string // playing section possible enum: Open or Reserve
	Stage        string // possible enum e.g. Preliminary/SemiFinal
	Board        string // Board number in team event
	Site         string
	Date         string
	Time         string
	UTCTime      string
	UTCDate      string
	TimeControl  string
	Round        string
	White        string
	Black        string
	WhiteTitle   string
	BlackTitle   string
	WhiteElo     string
	BlackElo     string
	WhiteUSCF    string // US chess Fed
	BlackUSCF    string // US chess Fed
	WhiteNA      string // email/network addr
	BlackNA      string // email/network addr
	WhiteType    string // possible enum: human or program
	BlackType    string // possible enum: human or program
	Opening      string
	ECO          string // Encyclopedia of Chess Opening
	NIC          string // New In Chess database
	Variation    string
	SubVariation string
	SetUp        string
	FEN          string // dependent on SetUp Field
	Termination  string
	Annotator    string
	Mode         string
	PlyCount     string // number of moves
	Result       string
}

type Move struct {
	Piece       string
	Origin      string
	Destination string
}
type PGNGame struct {
	meta  PGNGameMeta
	moves []Move
}
