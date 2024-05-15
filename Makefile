PDF = dissertation.pdf
BLOATED = dissertation-bloated.pdf
TEX = $(shell find ./ -type f -name '*.tex')
BIB = $(shell find ./ -type f -name '*.bib')

UNAME := $(shell uname)

PDFLATEX_ARGS = -shell-escape -interaction nonstopmode

.PHONY : default

default : $(PDF)

$(PDF) : $(TEX) $(BIB)
	-pdflatex $(PDFLATEX_ARGS) dissertation
	-pdflatex $(PDFLATEX_ARGS) dissertation
	-bibtex dissertation
	-pdflatex $(PDFLATEX_ARGS) dissertation
	-pdflatex $(PDFLATEX_ARGS) dissertation
	-cp $(PDF) $(BLOATED)
	-gs -q -dBATCH -sOutputFile=$(PDF) -dNOPAUSE -sDEVICE=pdfwrite  -dSubsetFonts=true -dCompressFonts=true -f $(BLOATED)
# -cp dissertation.pdf dissertation-bloated.pdf

clean:
	rm -f $(PS) $(BLOATED) $(PDF) *.dvi *.log *.aux *.bbl *.blg *.ent *.synctex.gz *.fls *.fdb_latexmk *.lof *.out *.toc *.lot
