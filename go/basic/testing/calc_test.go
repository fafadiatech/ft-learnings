package calc

import "testing"

func TestAdd(t *testing.T) {
	x := Add(1, 100)
	if x != 101 {
		t.Error("Expected 101, got", x)
	}
}
