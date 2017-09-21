package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

type Page struct {
	url       string
	file_name string
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

func (c *Crawler) fetch_page(current_page Page) {
	msg := fmt.Sprintf("Fetching page:%s", current_page.url)
	fmt.Println(msg)

	resp, err := http.Get(current_page.url)

	if err != nil {
		fmt.Println("Error fetching", current_page)
	}

	bytes, _ := ioutil.ReadAll(resp.Body)
	fmt.Print("Fetched Bytes:")
	fmt.Print(len(bytes))
	fmt.Print("\n")

	save_err := ioutil.WriteFile(current_page.file_name, bytes, 0644)

	if save_err != nil {
		fmt.Println("Issues saving file:", current_page.file_name)
	}

	done <- true
}

func (c *Crawler) crawl() {
	for _, page := range c.frontier {
		go c.fetch_page(page)
	}

}

func main() {
	deals_crawler := NewCrawler(
		[]Page{
			Page{"https://www.snapdeal.com/offers/deal-of-the-day", "sd"},
			Page{"https://www.flipkart.com/", "fk"},
			Page{"http://www.amazon.in/gp/goldbox/", "az"},
			Page{"http://www.jabong.com/deals/deal-of-the-day/", "jb"},
			Page{"http://www.myntra.com/deal-of-the-day", "my"},
			Page{"https://www.nykaa.com/offers.html", "ny"},
		},
	)
	deals_crawler.crawl()
	for _, i := range deals_crawler.frontier {
		<-done
		msg := fmt.Sprintf("Done Crawling:%s", i)
		fmt.Println(msg)
	}
}
