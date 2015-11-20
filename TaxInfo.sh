#usage: bash TaxInfo.sh
for line in $(cut RefSoilTax.txt -f 2);
 do wget -O $line.html "http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=$line";
done

grep "<dd><a ALT" *.html > TaxInfo.txt

rm *.html