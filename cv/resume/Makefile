SRC_TEX := $(wildcard *.tex) 
SHARED_TEX := $(wildcard shared/*.tex) 
PDF = $(foreach src,$(SRC_TEX),$(subst .tex,.pdf,$(src)))

UNAME := $(shell uname)

PDFLATEX_ARGS = -shell-escape -interaction nonstopmode

.PHONY : default

default : $(PDF)

$(PDF) : $(SRC_TEX) $(SHARED_TEX)
	$(foreach tex,$(SRC_TEX), \
	pdflatex $(PDFLATEX_ARGS) $(tex);)

clean:
	rm -f $(PS) $(PDF) *.dvi *.log *.aux *.bbl *.blg *.ent *.synctex.gz *.fdb_latexmk *.out *.fls
