package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
)

func main() {
	xmlBody := `<?xml version="1.0" encoding="UTF-8"?><request><PageIndex>1</PageIndex><ReadCount>20</ReadCount><BoxType>1</BoxType><SortType>0</SortType><Ascending>0</Ascending><UnreadPreferred>0</UnreadPreferred></request>`

	form := url.Values{}
	form.Add("xml", xmlBody)

	resp, err := http.PostForm("http://192.168.8.1/html/smsinbox.html", form)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	body, _ := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(body[:len(body)]))
}
