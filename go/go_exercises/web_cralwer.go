package main

import (
    "fmt"
    "sync"
)

type Fetcher interface {
    // Fetch returns the body of URL and
    // a slice of URLs found on that page.
    Fetch(url string) (body string, urls []string, err error)
}

type SafeCounter struct {
    v   map[string]bool
    mux sync.Mutex
}

var c SafeCounter = SafeCounter{v: make(map[string]bool)}

func (s SafeCounter) check_visited(url string) bool {
    s.mux.Lock()
    defer s.mux.Unlock()
    _, ok := s.v[url]
    if ok == false {
        s.v[url] = true
        return false
    }
    return true

}

// Crawl uses fetcher to recursively crawl
// pages starting with url, to a maximum of depth.
func Crawl(url string, depth int, fetcher Fetcher) {
    // TODO: Fetch URLs in parallel.
    // TODO: Don't fetch the same URL twice.
    // This implementation doesn't do either:
    var wg sync.WaitGroup
    var crawl func(url string, depth int, fetch Fetcher)
    crawl = func(url string, depth int, fetch Fetcher) {
        defer wg.Done()
        if depth <= 0 {
            return
        }
        if c.check_visited(url) {
            return
        }
        body, urls, err := fetcher.Fetch(url)
        if err != nil {
            fmt.Println(err)
            return
        }
        fmt.Printf("found: %s %q\n", url, body)
        for _, u := range urls {
            wg.Add(1)
            go crawl(u, depth-1, fetcher)
        }
        return
    }
    wg.Add(1)

    crawl(url, depth, fetcher)
    wg.Wait()
}

func main() {
    Crawl("https://golang.org/", 4, fetcher)
}

// fakeFetcher is Fetcher that returns canned results.
type fakeFetcher map[string]*fakeResult

type fakeResult struct {
    body string
    urls []string
}

func (f fakeFetcher) Fetch(url string) (string, []string, error) {
    if res, ok := f[url]; ok {
        return res.body, res.urls, nil
    }
    return "", nil, fmt.Errorf("not found: %s", url)
}

// fetcher is a populated fakeFetcher.
var fetcher = fakeFetcher{
    "https://golang.org/": &fakeResult{
        "The Go Programming Language",
        []string{
            "https://golang.org/pkg/",
            "https://golang.org/cmd/",
        },
    },
    "https://golang.org/pkg/": &fakeResult{
        "Packages",
        []string{
            "https://golang.org/",
            "https://golang.org/cmd/",
            "https://golang.org/pkg/fmt/",
            "https://golang.org/pkg/os/",
        },
    },
    "https://golang.org/pkg/fmt/": &fakeResult{
        "Package fmt",
        []string{
            "https://golang.org/",
            "https://golang.org/pkg/",
        },
    },
    "https://golang.org/pkg/os/": &fakeResult{
        "Package os",
        []string{
            "https://golang.org/",
            "https://golang.org/pkg/",
        },
    },
}

