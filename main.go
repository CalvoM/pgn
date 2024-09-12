package main

import (
	"errors"
	"flag"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
	"strings"
)

func downloadPGN(URL string) (string, error) {
	fileURL, err := url.ParseRequestURI(URL)
	segments := strings.Split(fileURL.Path, "/")
	fileName := segments[len(segments)-1]
	if err != nil {
		fmt.Println(fmt.Errorf("Invalid URL: %v", URL))
		return "", err
	}
	resp, err := http.Get(fileURL.String())
	if err != nil {
		fmt.Println(fmt.Errorf("Cannot fetch the URL: %s", err))
		return "", err
	}
	defer resp.Body.Close()
	file, err := os.CreateTemp("", fileName)
	if err != nil {
		fmt.Println(fmt.Errorf("Temp File creation error: %s", err))
		return "", err
	}
	_, err = io.Copy(file, resp.Body)
	file.Close()
	return file.Name(), nil
}

func main() {
	useURL := flag.Bool("url", false, "Get PGN from url link provided.")
	flag.Parse()
	var sourceFile string
	var err error
	if *useURL {
		sourceFile, err = downloadPGN(flag.Arg(0))
		if err != nil {
			os.Exit(1)
		}
	} else {
		sourceFile = flag.Arg(0)
		if _, err = os.Stat(sourceFile); errors.Is(err, os.ErrNotExist) {
			fmt.Println(err)
			os.Exit(1)
		}
	}
	b, err := os.ReadFile(sourceFile)
	if err != nil {
		fmt.Println(fmt.Errorf("File Opening error: %s", err))
		os.Exit(1)
	}
	l := NewLexer(strings.NewReader(string(b)))
	l.Lex()
	fmt.Printf("%v", l.Tokens())
	// var s PGNFileScanner
	// s.Scan(strings.NewReader(string(b)))
	// fmt.Println(s.Games())
}
