package hello

import (
	"fmt"
	"net/http"
)

func init() {
	http.HandleFunc("/", handler)
	http.HandleFunc("/quote", quoteHandler)
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Hello, world!")
}

func quoteHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Lets do it together - Said no one ever!")
}
