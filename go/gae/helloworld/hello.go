package hello

import (
	"fmt"
	"net/http"
)

func init() {
	http.HandleFunc("/", handler)
	http.HandleFunc("/quote", quote_handler)
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Hello, world!")
}

func quote_handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Lets do it together - Said no one ever!")
}
