package main

import (
	"bufio"
	"fmt"
	"io"
	"strings"
)

type TokenType int

const (
	TokenString TokenType = iota
	TokenNewline
	TokenNumber
	TokenPeriod
	TokenStar
	TokenLSQB
	TokenRSQB
	TokenLPar
	TokenRPar
	TokenTagName
	TokenTagValue
	TokenMoveNumber
	TokenFile
	TokenRank
	TokenPiece
	TokenCastleKingSide
	TokenCastleQueenSide
	TokenDraw
	TokenCheck
	TokenCheckMate
	PROMOTIONINDICATOR
	PROMOTIONPIECE
	TokenCapture
)

func (ttype TokenType) String() string {
	switch ttype {
	case TokenNewline:
		return "TokenNewLine"
	case TokenLSQB:
		return "TokenLSQB"
	case TokenRSQB:
		return "TokenRSQB"
	case TokenTagName:
		return "TokenTagName"
	case TokenTagValue:
		return "TokenTagValue"
	default:
		return fmt.Sprintf("%d", int(ttype))
	}
}

type (
	Pos struct {
		line   int
		column int
	}
	Token struct {
		tpos   Pos
		ttype  TokenType
		tvalue string
	}
	Lexer struct {
		reader *bufio.Reader
		pos    Pos
		atEOF  bool
		tokens []Token
	}
)

func NewLexer(r io.Reader) *Lexer {
	return &Lexer{pos: Pos{line: 1, column: 0}, reader: bufio.NewReader(r), atEOF: false}
}

func (l *Lexer) Lex() {
	for {
		r, _, err := l.reader.ReadRune()
		if err != nil {
			if err == io.EOF {
				return
			}
			panic(err)
		}
		l.pos.column++
		switch r {
		case '[': // Tag Pair
			l.tokens = append(l.tokens, Token{tpos: l.pos, ttype: TokenLSQB, tvalue: string(r)})
			l.pos.column++
			l.lexTagPair()
			l.tokens = append(l.tokens, Token{tpos: l.pos, ttype: TokenRSQB, tvalue: string(']')})
			l.pos.column++
			l.tokens = append(l.tokens, Token{tpos: l.pos, ttype: TokenNewline, tvalue: string('\n')})
			l.pos.line++
			l.pos.column = 0
		default:
			return
		}
	}
}

func (l *Lexer) lexMoves() {}

func (l *Lexer) lexTagPair() {
	l.readTagName()
	l.readTagValue()
}

func (l *Lexer) readTagName() {
	tagName, err := l.reader.ReadString(byte(' '))
	if err != nil {
		panic(err)
	}
	l.tokens = append(l.tokens, Token{tpos: l.pos, ttype: TokenTagName, tvalue: strings.TrimSpace(tagName)})
	l.pos.column += len(tagName)
}

func (l *Lexer) readTagValue() {
	tillEnd, err := l.reader.ReadString('\n')
	tillEnd = strings.TrimSpace(tillEnd)
	if err != nil {
		panic(err)
	}
	if tillEnd[len(tillEnd)-1] != ']' {
		fmt.Println(fmt.Errorf("Poorly delimited tagpair"))
		return
	}
	if tillEnd[0] != '"' {
		fmt.Println(fmt.Errorf("Poorly structured tag value"))
		return
	}
	if tillEnd[len(tillEnd)-2] != '"' {
		fmt.Println(fmt.Errorf("Poorly structured tag value"))
		return
	}
	tagValue := tillEnd[1 : len(tillEnd)-2]
	l.tokens = append(l.tokens, Token{tpos: l.pos, ttype: TokenTagValue, tvalue: strings.TrimSpace(tagValue)})
	l.pos.column += len(tagValue) + 2 // Add 2 apostrophes
}

func (l Lexer) Tokens() []Token {
	return l.tokens
}
