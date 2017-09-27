package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

type Page struct {
	url      string
	fileName string
}

type Crawler struct {
	frontier []Page
}

var done = make(chan bool)

func NewCrawler(seedlist []Page) *Crawler {
	c := Crawler{}
	c.frontier = seedlist
	return &c
}

func (c *Crawler) fetchPage(currentPage Page) {
	msg := fmt.Sprintf("Fetching page:%s", currentPage.url)
	fmt.Println(msg)

	resp, err := http.Get(currentPage.url)

	if err != nil {
		fmt.Println("Error fetching", currentPage)
	}

	bytes, _ := ioutil.ReadAll(resp.Body)
	fmt.Print("Fetched Bytes:")
	fmt.Print(len(bytes))
	fmt.Print("\n")

	saveError := ioutil.WriteFile(currentPage.fileName, bytes, 0644)

	if saveError != nil {
		fmt.Println("Issues saving file:", currentPage.fileName)
	}

	done <- true
}

func (c *Crawler) crawl() {
	for _, page := range c.frontier {
		go c.fetchPage(page)
	}

}

func main() {
	dealsCrawler := NewCrawler(
		[]Page{
			Page{"https://www.snapdeal.com/offers/deal-of-the-day", "sd"},
			Page{"https://www.flipkart.com/", "fk"},
			Page{"http://www.amazon.in/gp/goldbox/", "az"},
			Page{"http://www.jabong.com/deals/deal-of-the-day/", "jb"},
			Page{"http://www.myntra.com/deal-of-the-day", "my"},
			Page{"https://www.nykaa.com/offers.html", "ny"},
		},
	)
	dealsCrawler.crawl()
	for _, i := range dealsCrawler.frontier {
		<-done
		msg := fmt.Sprintf("Done Crawling:%s", i)
		fmt.Println(msg)
	}
}
