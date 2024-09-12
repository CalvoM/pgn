package main

import (
	"fmt"
	"io"
	"strings"
)

var PGNGamesSeparator = []byte{0xa, 0xa, 0xa}

type PGNFileScanner struct {
	data  string
	items []string
}

func (pgnscanner *PGNFileScanner) splitGames() {
	for _, item := range strings.Split(pgnscanner.data, string(PGNGamesSeparator)) {
		if len(item) > 0 {
			pgnscanner.items = append(pgnscanner.items, item)
		}
	}
}

func (pgnscanner *PGNFileScanner) Scan(r io.Reader) {
	if b, err := io.ReadAll(r); err == nil {
		pgnscanner.data = string(b)
	} else {
		fmt.Println(fmt.Errorf("%s", err))
		return
	}
	pgnscanner.splitGames()
}

func (pgnscanner *PGNFileScanner) gameScan() {
}

func (pgnscanner PGNFileScanner) Games() []string {
	return pgnscanner.items
}
