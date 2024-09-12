package main

type (
	Pos   int
	lexer struct {
		input string
		pos   Pos
		start Pos
		atEOF bool
	}
)
