PDF = extended_abs.pdf
BLOATED = extended_abs_bloated.pdf
TEX = $(shell find ./ -type f -name '*.tex')
BIB = $(shell find ./ -type f -name '*.bib')
STY = $(shell find ./ -type f -name '*.sty')
CLS = $(shell find ./ -type f -name '*.cls')

UNAME := $(shell uname)

PDFLATEX_ARGS = -shell-escape -interaction nonstopmode

.PHONY : default

default : $(PDF)

$(PDF) : $(TEX) $(BIB) $(STY) $(CLS)
	-pdflatex $(PDFLATEX_ARGS) extended_abs
	-pdflatex $(PDFLATEX_ARGS) extended_abs
	-bibtex extended_abs
	-pdflatex $(PDFLATEX_ARGS) extended_abs
	-pdflatex $(PDFLATEX_ARGS) extended_abs
	-cp $(PDF) $(BLOATED)
	-gs -q -dBATCH -sOutputFile=$(PDF) -dNOPAUSE -sDEVICE=pdfwrite -dSubsetFonts=true -dCompressFonts=true -f $(BLOATED)
	-rm $(BLOATED)

clean:
	rm -f $(PS) $(BLOATED) $(PDF) *.dvi *.log *.aux *.bbl *.blg *.ent *.synctex.gz *.fls *.fdb_latexmk *.lof *.out *.toc *.lot
