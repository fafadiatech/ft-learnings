package main

//Based on tutorial: http://thenewstack.io/building-a-web-server-in-go/

import (
       "io"
       "net/http"
)

func hello(w http.ResponseWriter, r *http.Request){
     io.WriteString(w, "Hello World\n")
}

func main(){
     http.HandleFunc("/", hello)
     http.ListenAndServe(":8000", nil)
}